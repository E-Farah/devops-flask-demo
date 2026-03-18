# Python Flask DevOps Demo

This repository contains a **simple Python Flask application** demonstrating a modern DevOps workflow.  

The app provides a minimal Flask API with:

- `GET /` → Returns a JSON message confirming the app is running.  
- `GET /add?a=<num>&b=<num>` → Adds two numbers and returns the result in JSON.  

Key DevOps features included in this project:

- **Automated Testing**: Unit tests with `pytest` to ensure correct functionality.  
- **Code Quality**: `flake8` used for enforcing PEP8 standards.  
- **Dockerized**: The app can run in a Docker container for consistent deployment.  
- **CI/CD Pipeline**: GitHub Actions automatically runs tests, linting, and builds/pushes Docker images.  
- **Secure Secrets Management**: DockerHub credentials are stored safely as GitHub Actions secrets.

This project serves as a **demo for DevOps best practices** in Python applications, combining testing, linting, containerization, and automated deployment.