from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.banco_de_dados.usuario_repositorio import UsuarioRepositorio
from app.dependencias import obter_usuario_repositorio
from app.modelos.usuario import UsuarioCriarAtualizar

router = APIRouter(prefix="/registro")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@router.get("/", response_class=HTMLResponse)
async def pagina_registro(request: Request):
    return templates.TemplateResponse(
        request=request, name="registro.html", context={"error": None}
    )


@router.post("/")
async def registrar_usuario(
    usuario_repositorio: Annotated[
        UsuarioRepositorio, Depends(obter_usuario_repositorio)
    ],
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confirma_senha: str = Form(...),
):
    data = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "confirma_senha": confirma_senha,
    }

    if not all([email, senha, nome, confirma_senha]):
        return templates.TemplateResponse(
            request=request,
            name="registro.html",
            context={"error": "Campos obrigatórios faltantes", **data},
        )

    usuario_existente = await usuario_repositorio.buscar_usuario_por_email(email)
    if usuario_existente:
        return templates.TemplateResponse(
            request=request,
            name="registro.html",
            context={"error": "Usuário inválido!", **data},
        )

    # Criação da entidade usando o modelo Pydantic do professor
    usuario_criar = UsuarioCriarAtualizar(nome=nome, email=email, senha=senha)
    usuario = await usuario_repositorio.criar_usuario(usuario_criar)

    if usuario:
        response = RedirectResponse(url="/login", status_code=303)
        return response

    return templates.TemplateResponse("registro.html", {
            "request": request,
            "error": "Não foi possível criar o usuário, tente novamente mais tarde.",
            **data
        })