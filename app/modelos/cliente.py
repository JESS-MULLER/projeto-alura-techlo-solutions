from pydantic import BaseModel

class ClienteCriarAtualizar(BaseModel):
    nome: str
    email: str
    telefone: str

class Cliente(ClienteCriarAtualizar):
    id_: int
    nome: str
    email: str
    telefone: str