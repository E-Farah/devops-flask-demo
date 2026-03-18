# **Python Flask DevOps Demo**

A **Python Flask app** showcasing **DevOps best practices**: CI/CD, Docker, testing, and linting.

---

# **Features**

- `GET /` → Returns a JSON message to confirm the app is running.  
- `GET /add?a=<num>&b=<num>` → Adds two numbers, returns JSON result.  
- **Automated Testing** with `pytest`.  
- **Code Quality** with `flake8`.  
- **Dockerized** for easy deployment.  
- **CI/CD Pipeline** with GitHub Actions, including automated tests, linting, and Docker image push.  

---

# **Tech Stack**

- Python 3.9  
- Flask  
- Pytest  
- Flake8  
- Docker  
- GitHub Actions

---

# **DevOps Notes**

- `.flake8` ensures only project files are checked.  
- Secrets (e.g., DockerHub credentials) are stored securely in GitHub Actions.  
- Fully automated pipeline runs on every push/pull request.

---

## How to Run

### Run Locally

1. **Clone the repo:**

- git clone https://github.com/E-Farah/devops-flask-demo.git
- cd devops-flask-demo


2. **Create and activate a virtual environment:**

- python -m venv venv
- venv\Scripts\activate (For Windows)
 **OR**
 source venv/bin/activate (For macOS / Linux)

3. **Install dependencies:**
- pip install -r requirements.txt

4. **Run the Flask app:**
- python app.py

5. **Open your browser and go to:**

- http://localhost:5000/

**Example: /add?a=2&b=3 → {"result": 5}**

### Run with Docker

1. **Build the Docker image:**
- docker build -t devops-flask-demo .

2. **Run the container:**
- docker run -p 5000:5000 devops-flask-demo

3. **Visit http://localhost:5000/ in your browser.**
