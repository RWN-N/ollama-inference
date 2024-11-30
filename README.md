# Ollama Inference Flask API

This project provides a simple Flask-based REST API to interface with the Ollama model server. You can send prompts to the API for inference and receive responses from the model.

---

## Requirements

- Python 3.9+
- `ollama` installed and running locally
- Flask and other dependencies from `requirements.txt`

---

## Installation

### Step 1: Create and Activate a Virtual Environment (Optional)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     "venv\Scripts\activate"
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Step 2: Install Python Dependencies
Install dependencies:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up and Run Ollama

1. Download and install the Ollama runtime from their [official website](https://ollama.com/).

2. Pull the required model:
   ```bash
   ollama pull <model-name>
   ```
   Example:
   ```bash
   ollama pull llama3.2
   ```

3. Start the Ollama server:
   ```bash
   ollama serve
   ```
   This runs the server on `http://localhost:11434` by default.

---

## Running the Flask App

1. Start the Flask app:
   ```bash
   python main.py
   ```

2. The API will run on `http://0.0.0.0:8000` by default.

---

## Testing the API

### Endpoint: `/inference`

#### Request Method: `POST`

#### Payload:

| Field       | Type     | Description                                     |
|-------------|----------|-------------------------------------------------|
| `prompt`    | `string` | (Required) The prompt you want to send to Ollama |
| `model`     | `string` | (Optional) The model name (defaults to the first model available) |

#### Example cURL Request:

```bash
curl -X POST http://localhost:8000/inference \
-H "Content-Type: application/json" \
-d '{
    "prompt": "Tell me a fun fact about AI",
    "model": "llama3.2"
}'
```

#### Example Response:

```json
{
    "model": "llama3.2",
    "response": "AI can generate music, art, and even write books that are sometimes indistinguishable from those created by humans!"
}
```

### Error Handling

- **400 Bad Request**: Missing or invalid payload (e.g., `prompt` is missing or not a string).
- **500 Internal Server Error**: Errors during inference (e.g., model not loaded).

---

## Notes

1. Ensure the `ollama` server is running before starting the Flask app.
2. Use `ollama list` to check available models and pull any missing ones if needed. For example:
   ```bash
   ollama list
   ollama pull llama3.2
   ```
3. You can change the default settings (like the host and port) by modifying the `main.py` file.