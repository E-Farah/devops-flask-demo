# Python Flask DevOps Demo

A Python Flask application demonstrating **CI/CD with GitHub Actions, Docker, testing, linting, and Kubernetes deployment**.

---

## Features

- **Flask API**
  - `GET /` : Returns a message **Hello, the app is running.**.
  - `GET /add?a=<num>&b=<num>` : Adds two numbers and returns the result.
  - `GET /divide?x=<num>&y=<num>` : Divides two numbers, handles zero division safely
- **Automated Testing** with `pytest`.
- **Code Quality** enforced via `flake8`.
- **Dockerized** for easy deployment.
- **Environment-aware (APP_ENV)** : Automatically detects if the app is running locally or in Kubernetes, helping prevent accidental exposure of internal info.
- **CI/CD Pipeline**
  - Runs tests and linting on every push/pull request.
  - Builds and pushes Docker images to Docker Hub using GitHub Actions secrets.
- **Kubernetes Ready**
  - Deployment uses a public Docker image.
  - Includes NodePort service for local testing.

---

## **DevOps Notes**

- `.flake8` ensures only project files are checked.  
- Secrets (such as DockerHub credentials) are stored securely in GitHub Actions.  
- Fully automated pipeline runs on every push/pull request.

---

## How to Run on Kubernetes
 
**1. Clone the repository**

- git clone https://github.com/E-Farah/devops-flask-demo.git
- cd devops-flask-demo


**2. Make sure your cluster is running**

- minikube start

    **Reminder:** Make sure the Docker Desktop is open.


**3. Deploy the app**

- kubectl apply -f k8s/deployment.yaml
- kubectl apply -f k8s/service.yaml

**Kubernetes will automatically pull the public Docker image: efarah1/devops-flask-demo:latest**

**4. Verify the deployment**
- kubectl get pods
- kubectl get service

**5. Access the app**


- minikube service flask-service --url

    You will receive a URL like: http://minikube-ip:node-port
    Open the URL in your browser.

    Example API call:
    http://minikube-ip:node-port/add?a=2&b=3

    Expected result:
    {"result": 5}


---

## **Tech Stack**

- Python 3.9  
- Flask  
- Pytest  
- Flake8  
- Docker  
- GitHub Actions
- Kubernetes

---


# **System Design & Architecture Flow**

**1. Developer pushes code to GitHub**

**2. GitHub Actions automatically runs a CI pipeline:**

- Checks code quality with **flake8**

- Runs tests with **pytest**

**3. On main branch:**

- Docker image is built

- Image is pushed to Docker Hub

**4. Kubernetes pulls the image and deploys it**

### Kubernetes Features

- **Health checks:** Kubernetes automatically checks if the app is running and ready, and restarts it if something goes wrong  

- **Resource limits:** Limits the app from using too much CPU or memory

- **Environment variables:** Let the app know if it’s running locally (development) or in a deployed environment like Kubernetes (production) without changing the code (used for safety reasons like avoid leaking information)