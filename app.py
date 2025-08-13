from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import duckdb
import io
import openai
import os

# Load API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Data Analyst Agent",
    description="Upload CSV + ask data-related questions, get answers + visualizations.",
    version="1.0"
)

# Allow all CORS (for frontend use)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route
@app.get("/")
async def home():
    return {"status": "running", "message": "Data Analyst Agent API is live!"}

# Upload + process data
@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    question: str = Form(...)
):
    try:
        # Read uploaded CSV into DataFrame
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # Store dataframe in DuckDB for SQL queries
        con = duckdb.connect()
        con.register("data", df)

        # Generate SQL query based on natural language question (Optional)
        prompt = f"""
        You are a data analyst. Given the dataframe 'data', answer the question:
        Question: {question}
        Do not explain code, just give a short answer.
        """

        # Use OpenAI for answering
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a skilled data analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        answer = response.choices[0].message["content"]

        return JSONResponse(content={
            "columns": df.columns.tolist(),
            "rows": len(df),
            "sample_data": df.head(5).to_dict(orient="records"),
            "question": question,
            "answer": answer
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)