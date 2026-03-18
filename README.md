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