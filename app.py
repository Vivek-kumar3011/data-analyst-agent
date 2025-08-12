from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import pandas as pd
import tempfile
import os
from utils.data_utils import load_data
from utils.analysis_utils import perform_analysis

app = FastAPI(title="Data Analyst Agent API")

@app.post("/")
async def analyze_data(questions: UploadFile = File(...), files: list[UploadFile] = File(None)):
    # Read questions.txt
    q_text = (await questions.read()).decode("utf-8")

    # Save any extra uploaded files temporarily
    temp_dir = tempfile.mkdtemp()
    file_paths = []
    if files:
        for f in files:
            file_path = os.path.join(temp_dir, f.filename)
            with open(file_path, "wb") as out_file:
                out_file.write(await f.read())
            file_paths.append(file_path)

    # Load and prepare data
    df = load_data(file_paths)

    # Run analysis
    result = perform_analysis(q_text, df)

    return JSONResponse(content=result)
