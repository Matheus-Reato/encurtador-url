from pydantic import BaseModel, HttpUrl

class UrlFormatada(BaseModel):
    url: HttpUrl