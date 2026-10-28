from fastapi import APIRouter
from schemas import UrlFormatada

router = APIRouter(tags=["Encurtador"], prefix="/encurtador")

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/shorten")
def receber_link(dados: UrlFormatada):
    return {"status": "URL recebida"}
    