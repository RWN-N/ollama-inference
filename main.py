import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


HOST = "0.0.0.0"
PORT = 8000
OLLAMA_HOST = "http://localhost:11434"
DEBUG = True

client = ollama.Client(host=OLLAMA_HOST)
app = Flask(__name__)
CORS(app)


def get_existing_model_name():
    client_models = client.list().models
    if not client_models:
        raise Exception("Ollama Client doesn't have any model. \nPull model from ollama registry: \"ollama pull <model>\" e.g. \"ollama pull llama3.2\"")
    return client_models[0].model


@app.route("/inference", methods=['POST'])
@cross_origin()
def ollama_inference():
    data: dict = request.get_json()
    prompt: str | None = data.get("prompt")
    model_name: str | None = data.get("model")
    if prompt is None:
        return jsonify({'error': "Missing required payload: \"prompt\". Optional payload: \"model\""}), 400
    elif not isinstance(prompt, str):
        return jsonify({'error': "Invalid \"prompt\" type, required as string"}), 400
    
    if model_name is None:
        model_name = get_existing_model_name()

    try:
        resp = client.generate(model=model_name, prompt=prompt)
        return jsonify({"model": resp.model, "response": resp.response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)