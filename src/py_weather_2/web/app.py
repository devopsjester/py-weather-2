"""FastAPI application factory."""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn
from .routes import location, weather

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="Weather App")
    
    # Set up templates and static files
    templates_dir = Path(__file__).parent / "templates"
    static_dir = Path(__file__).parent / "static"
    templates = Jinja2Templates(directory=str(templates_dir))
    
    # Mount static files if the directory exists
    if static_dir.exists():
        app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
    
    # Register routes
    app.include_router(location.router, prefix="/location", tags=["location"])
    app.include_router(weather.router, prefix="/weather", tags=["weather"])
    
    @app.get("/")
    async def index(request: Request):
        return templates.TemplateResponse(
            "index.html",
            {"request": request}
        )
    
    return app

# Create the application instance
app = create_app()

def run_server():
    """Run the web server."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run_server()