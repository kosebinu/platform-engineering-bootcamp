from fastapi import FastAPI

app = FastAPI(
    title="${{ values.name }}",
    description="${{ values.description }}",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    """Return basic service information."""
    return {
        "service": "${{ values.name }}",
        "status": "running",
    }


@app.get("/health")
def health() -> dict[str, str]:
    """Return the application health status."""
    return {
        "status": "healthy",
    }


@app.get("/ready")
def readiness() -> dict[str, str]:
    """Return the application readiness status."""
    return {
        "status": "ready",
    }