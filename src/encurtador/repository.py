
urls: dict[str, str] = {
    "1": "https://github.com/Matheus-Reato/encurtador-url",
    "2": "https://www.google.com/",
}

def buscar_url(codigo):
    return urls.get(codigo)
