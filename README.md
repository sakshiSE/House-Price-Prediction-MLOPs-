#  House Price Prediction using Machine Learning & MLOps

An end-to-end Machine Learning project that predicts house prices based on property features. This project follows MLOps principles by incorporating data preprocessing, model training, experiment tracking with MLflow, a FastAPI-based prediction API, and Docker containerization for deployment.

---

##  Project Overview

The goal of this project is to build a reliable machine learning model that estimates house prices using various housing attributes. The project includes the complete machine learning workflow—from data preprocessing and model training to serving predictions through a  API.

---

##  Features

- Data preprocessing and feature engineering
- Machine Learning model for house price prediction
- Experiment tracking using MLflow
- FastAPI REST API for predictions
- Docker support for easy deployment
- Modular project structure following MLOps practices

---

##  Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- MLflow
- Docker
- Uvicorn

---

##  Project Structure

```text
House-Price-Prediction-MLOPs/
│
├── api/
│   └── main.py
│
├── data/
│
├── notebooks/
│
├── src/
│   ├── feature_pipeline.py
│   └── ...
│
├── best_model.pkl
├── requirements.txt
├── Dockerfile
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/sakshiSE/House-Price-Prediction-MLOPs.git
```

### 2. Navigate to the project directory

```bash
cd House-Price-Prediction-MLOPs
```

### 3. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Running the API

Start the FastAPI server:

```bash
uvicorn api.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

FastAPI automatically provides an interactive Swagger UI where you can test the prediction endpoint.

---

##  Running with Docker

Build the Docker image:

```bash
docker build -t house-price-prediction .
```

Run the container:

```bash
docker run -p 8000:8000 house-price-prediction
```

Then visit:

```
http://localhost:8000/docs
```


##  Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Preprocessing
5. Model Training
6. Model Evaluation
7. Experiment Tracking using MLflow
8. Model Serialization
9. FastAPI Deployment
10. Docker Containerization

---
