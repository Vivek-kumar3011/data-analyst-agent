from fastapi import FastAPI, UploadFile, Form, HTTPException
import pandas as pd
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Data Analyst Agent API is running successfully!"}

@app.post("/analyze")
async def analyze_data(file: UploadFile, task: str = Form(...)):
    try:
        # Check file type
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Only CSV files are supported.")

        # Read uploaded CSV into pandas DataFrame
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # Simple example analysis
        summary = df.describe(include='all').to_dict()

        return {
            "status": "success",
            "task": task,
            "summary": summary
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}  # check this
