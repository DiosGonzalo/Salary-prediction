# 🚀 Global Developer Salary Predictor API

> A Machine Learning-powered REST API that estimates developer salaries based on country, experience, and education level. Built with **FastAPI** and containerized with **Docker**.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)

## 📋 Overview

This project analyzes data from over **80,000 developers** (Stack Overflow Annual Survey) to predict market salaries. It exposes a trained **Random Forest** model through a high-performance REST API.

The goal is to provide real-time salary insights for developers looking to relocate or negotiate their compensation in different markets (USA, Germany, UK, etc.).

### 🛠️ Tech Stack
* **Language:** Python 3.9
* **API Framework:** FastAPI (Asynchronous & High Performance)
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Data Processing:** Pandas & NumPy
* **Containerization:** Docker

---

## 🐳 Quick Start (Run with Docker)

The easiest way to run this application is using Docker. No Python installation is required.

1.  **Build the Image:**
    ```bash
    docker build -t salary-api .
    ```

2.  **Run the Container:**
    ```bash
    docker run -p 8000:8000 salary-api
    ```

3.  **Access the API:**
    Open your browser and go to the automatic documentation:
    👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🐍 Manual Installation (Local Python)

If you prefer to run it without Docker:

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the server:**
    ```bash
    python -m uvicorn main:app --reload
    ```

---

## 📡 API Usage Example

Send a **POST** request to `/predict_salary` with the following JSON body:

**Request:**
```json
{
  "country": "Germany",
  "education": "Master",
  "experience": 5.0
}
