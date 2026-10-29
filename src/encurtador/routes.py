from fastapi import APIRouter
from encurtador.schemas import UrlFormatada
from encurtador.repository import buscar_url
from fastapi import HTTPException
from fastapi.responses import RedirectResponse

router = APIRouter(tags=["Encurtador"], prefix="/encurtador")

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/shorten")
def receber_link(dados: UrlFormatada):
    return {"URL": "https://www.google.com/"}

