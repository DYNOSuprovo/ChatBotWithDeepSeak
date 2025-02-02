from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama API URL

@app.route("/")
def index():
    return render_template("index.html")  # Loads the frontend

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    
    # Send request to DeepSeek-R1
    payload = {
        "model": "deepseek-r1",
        "prompt": user_input,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    
    if response.status_code == 200:
        reply = response.json().get("response", "Sorry, I couldn't process that.")
        return jsonify({"reply": reply})
    else:
        return jsonify({"reply": "Error connecting to DeepSeek-R1"}), 500

if __name__ == "__main__":
    app.run(debug=True)
