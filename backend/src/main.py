from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from config.database import engine
from config.config import APP_NAME, VERSION

from routes.links import main, models # noqa
from routes import links


links.models.Base.metadata.create_all(bind=engine)
# ----------------------------------------

app = FastAPI(
    title=APP_NAME,
    version=VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# ---- Do this for all of your routes ----
app.include_router(links.main.router)
# ----------------------------------------


# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")
