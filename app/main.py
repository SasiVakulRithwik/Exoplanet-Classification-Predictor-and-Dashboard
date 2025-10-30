# FastAPI application entry point
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, HTMLResponse
import pandas as pd
import os
from .models import PredictionInput, PredictionResponse
from .ml_utils import load_ml_components, predict

app = FastAPI(title="Exoplanet Dashboard & Predictor")

# Mount static files and templates
# app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Load dataset for summary stats
dataset_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Exoplanet-Dataset.csv')
df = pd.read_csv(dataset_path)

@app.on_event("startup")
async def startup_event():
    """Load ML components when application starts"""
    load_ml_components()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main dashboard page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/analytics", response_class=HTMLResponse)
async def read_analytics(request: Request):
    """Serve the analytics page"""
    return templates.TemplateResponse("analytics.html", {"request": request})

@app.get("/dataset", response_class=HTMLResponse)
async def read_dataset(request: Request):
    """Serve the dataset info page"""
    return templates.TemplateResponse("dataset.html", {"request": request})

@app.get("/details", response_class=HTMLResponse)
async def read_details(request: Request):
    """Serve the documentation page"""
    return templates.TemplateResponse("details.html", {"request": request})

@app.get("/api/summary")
async def get_summary():
    """Provide dataset summary for dashboard"""
    summary = {
        "total_records": len(df),
        "class_distribution": df['label'].value_counts().to_dict(),
        "feature_means": df.mean().to_dict(),
        "feature_medians": df.median().to_dict()
    }
    return JSONResponse(content=summary)

@app.post("/api/predict", response_model=PredictionResponse)
async def make_prediction(input_data: PredictionInput):
    """Make prediction for exoplanet classification"""
    result = predict(input_data)
    return PredictionResponse(**result)