from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.banco_de_dados.local import BancoDeDadosLocal
from app.rotas import cliente, login, registro
from app.autenticacao_middleware import AuthenticationToken

# Caminho para a raiz (techlog-solutions)
BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = BancoDeDadosLocal()
    db.inicializar_banco()
    yield

app = FastAPI(
    title="Techlog Solution API",
    description="CRM para Techlog Solution",
    version="1.0.0",
    lifespan=lifespan,
)

app.mount(
    "/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static"
)
app.add_middleware(AuthenticationToken)

# Rotas de Clientes
app.include_router(cliente.router)
app.include_router(cliente.front_router)

# Rota de Login
app.include_router(login.router)
app.include_router(registro.router)


@app.get("/health")
async def health_check():
    return {"status": "OK"}


@app.get("/", response_class=HTMLResponse)
async def front_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"titulo": "Techlog Solutions CRM", "versao": "1.0.0"}
    )

@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("session_token")
    return response