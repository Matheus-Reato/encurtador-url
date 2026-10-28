from fastapi import FastAPI
from encurtador import routes

app = FastAPI(title="Encurtador URLs")

app.include_router(routes.router)