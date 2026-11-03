from fastapi import APIRouter
from encurtador.schemas import UrlFormatada
from encurtador.repository import buscar_url
from fastapi import HTTPException
from fastapi.responses import RedirectResponse
from database import get_db

router = APIRouter(tags=["Encurtador"], prefix="/encurtador")

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/health-db")
def health_check_db():
    if get_db():
        return {"status": "ok"}
    else:
        return {"status": "error"}

@router.post("/shorten")
def receber_link(dados: UrlFormatada):
    return {"URL": "https://www.google.com/"}

@router.get("/{codigo}")
def retornar_url_dicionario(codigo):
    url = buscar_url(codigo)

    if url:
        return RedirectResponse(url=url)
    else:
        raise HTTPException(status_code=404, detail="Código não encontrado")