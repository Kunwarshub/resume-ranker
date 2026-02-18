# 📄 Resume Ranker

An AI-powered Resume Ranker that evaluates resumes against a job description and provides relevance scoring and feedback.  
The application helps candidates understand how well their resume matches a role and identify areas for improvement.

---

## 🚀 Features

- 📊 Resume–Job Description similarity scoring
- 🤖 AI-based evaluation and feedback
- 📄 PDF resume parsing
- 🧠 LLM-powered analysis
- 🌐 Web interface for uploading resumes
- 🐳 Dockerized for reproducible deployment

---

## 🛠️ Tech Stack

- **Python**
- **Flask / FastAPI** (update based on your framework)
- **LLM API** (Groq / OpenAI / etc.)
- **PyPDF2** for resume parsing
- **HTML Templates**
- **Docker** for containerization

---

## 📁 Project Structure

resume-ranker/
│
├── app.py # Main application
├── requirements.txt # Python dependencies
├── Dockerfile # Container configuration
├── templates/ # HTML templates
│ ├── index.html
│ └── app.html


---

## ⚙️ Setup (Local — without Docker)

### 1️⃣ Clone the repository

git clone https://github.com/Kunwarshub/resume-ranker.git
cd resume-ranker

2️⃣ Create virtual environment

python -m venv venv
venv/scripts/activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file:
GROQ_API_KEY=your_api_key

5️⃣ Run the application

python app.py
Open: http://localhost:8000

🐳 Running with Docker (Recommended)

Build image
docker build -t resume-ranker .

Run container
docker run --env-file .env -d -p 8000:8000 resume-ranker


Then open:

http://localhost:8000

📦 Deployment

The project is containerized using Docker, allowing consistent execution across environments:

Local development

Cloud VM deployments (AWS EC2 / Azure VM)

Container platforms

🎯 Future Improvements

Resume keyword optimization suggestions

Multiple resume comparison

ATS-style scoring metrics

Persistent database storage

Authentication system

👨‍💻 Author

Kunwar Malik

LinkedIn: https://www.linkedin.com/in/kunwar-abhey-pratap-malik/

GitHub: https://github.com/Kunwarshub

📄 License

This project is for educational and portfolio purposes.