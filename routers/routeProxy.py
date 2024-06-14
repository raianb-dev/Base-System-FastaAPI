from fastapi import FastAPI, Request, HTTPException, APIRouter
from fastapi.responses import Response
import requests

router = APIRouter()

@router.get("/proxy")
async def proxy(url: str, request: Request):
    if not url.startswith(('http://', 'https://')):
        raise HTTPException(status_code=400, detail="URL inválida")

    try:
        headers = {'User-Agent': request.headers.get('User-Agent')}
        response = requests.get(url, headers=headers)

        return Response(
            content=response.content,
            media_type=response.headers.get('Content-Type', 'text/html'),
            status_code=response.status_code
        )
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar a URL: {str(e)}")


