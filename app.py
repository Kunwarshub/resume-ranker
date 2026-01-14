### app.py (Flask Backend)

from flask import Flask, render_template, request, jsonify, session
import PyPDF2
import requests
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app.html")
def render_app():
    return render_template("app.html")

@app.route("/upload_resume", methods=["POST"])
def upload_resume():
    try:
        resume_file = request.files['resume']
        reader = PyPDF2.PdfReader(resume_file)
        resume_text = "".join([page.extract_text() for page in reader.pages])
        session['resume_text'] = resume_text
        return jsonify({"success": True, "message": "Resume uploaded."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route("/ask", methods=["POST"])
def ask_question():
    user_question = request.json.get("question")
    resume_text = session.get("resume_text")

    if not resume_text:
        return jsonify({"success": False, "message": "No resume uploaded yet."})

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who analyzes resumes."},
            {"role": "user", "content": f"Resume:\n{resume_text}\n\nQuestion: {user_question}"}
        ]
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)
    try:
        answer = response.json()['choices'][0]['message']['content']
        return jsonify({"success": True, "answer": answer})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)