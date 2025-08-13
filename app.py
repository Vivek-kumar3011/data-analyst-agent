from fastapi import FastAPI, UploadFile, Form
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import duckdb
from bs4 import BeautifulSoup
import requests
from sklearn.linear_model import LinearRegression
import openai

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Data Analyst Agent API is running successfully!"}

@app.post("/analyze")
async def analyze_data(file: UploadFile, task: str = Form(...)):
    try:
        # Read uploaded CSV into pandas DataFrame
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # Example: Simple analysis
        summary = df.describe(include='all').to_dict()

        return {
            "status": "success",
            "task": task,
            "summary": summary
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
