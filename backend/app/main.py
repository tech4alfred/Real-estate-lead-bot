"""
Real Estate Lead Bot - FastAPI application entry point.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Real Estate Lead Bot API",
    description="PrimeHomes Realty - AI-powered lead management system",
    version="0.1.0",
)


@app.get("/api/v1/health")
def health_check():
    """Basic health check endpoint."""
    return {"status": "ok", "service": "real-estate-lead-bot"}
