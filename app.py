from fastapi import FastAPI

app = FastAPI(title="AI Digital Footprint Risk Analyzer")


@app.get("/")
def home():
    return {"message": "AI Service is running"}


@app.get("/health")
def health():
    return {"status": "UP"}