DeepSeek-R1 Chatbot

This project is an interactive chatbot powered by DeepSeek-R1 and built using Flask. It provides a simple web-based UI for users to engage in real-time conversations with the chatbot.

Features

Flask-based Web Interface: A lightweight and responsive UI for interacting with the chatbot.

DeepSeek-R1 Integration: Uses the DeepSeek-R1 model via the Ollama API.

Seamless Communication: Sends user queries to DeepSeek-R1 and retrieves intelligent responses.

AJAX-based Interaction: Ensures smooth communication between the frontend and backend.

Prerequisites

Python 3.8 or higher

Ollama installed and running locally

Installed dependencies (see below)

Installation

Clone the repository:

git clone https://github.com/your-username/deepseek-chatbot.git
cd deepseek-chatbot

Install dependencies:

pip install -r requirements.txt

Start the Ollama service:

ollama serve

Run the Flask application:

python app.py

Open your browser and go to:

http://127.0.0.1:5000

File Structure

app.py: Main Flask backend handling API calls.

templates/index.html: Frontend interface for chatting.

static/: Contains CSS, JavaScript, and other assets.

requirements.txt: List of required Python dependencies.

Dependencies

This project uses the following Python libraries:

flask

requests

ollama

Future Enhancements

Add support for multiple AI models.

Improve UI with real-time streaming responses.

Deploy on a cloud server (e.g., AWS, Azure, or Heroku).