📌 Conteúdo e Evolução do Projeto
O projeto foi construído incrementalmente ao longo de 5 etapas modulares:

Módulo 1: Fundamentos Assíncronos e Ambiente:

Diferenciação entre I/O síncrono e assíncrono em Python com async/await e asyncio.

Isolamento de dependências com ambientes virtuais (venv).

Primeiros passos com conteinerização utilizando Docker.

Módulo 2: Estrutura Base e Rotas FastAPI:

Configuração inicial da aplicação FastAPI e servidor ASGI com Uvicorn.

Documentação interativa automática (Swagger UI em /docs).

Endpoints modulares com APIRouter e endpoint de verificação (/health-check).

Modelagem e validação de schemas de clientes com Pydantic.

Módulo 3: Persistência de Dados e Padrões de Projeto:

Banco de dados relacional SQLite com gerenciadores de contexto (contextmanager) para conexões seguras.

Padrão Repository para isolar a camada de acesso a dados (ClienteRepositorio).

Injeção de dependências do FastAPI através de Depends e padrão Singleton para gestão de instâncias de conexão.

Operações CRUD completas e tratamento de erros padronizado com HTTPException.

Módulo 4: Interface Web, Templates e Autenticação:

Renderização no servidor utilizando Jinja2 Templates e arquivos estáticos (CSS/JS).

Separação de fluxos entre rotas de API e páginas HTML (login, registro e listagem).

Persistência de usuários com tabela usuarios no SQLite.

Fluxo de autenticação: formulários POST, validação de credenciais, sessão mantida por cookies HTTP seguros (session_token), middlewares de proteção de rota e logout.

Módulo 5: Qualidade, Testes e Conteinerização:

Testes unitários com pytest e pytest-asyncio.

Injeção de fixtures e simulações com MagicMock e AsyncMock para testes de rotas sem acoplamento ao banco físico.

Middlewares de controle e autorização de requisições.

Preparação da aplicação para implantação com Dockerfile.

🚀 Tecnologias Utilizadas
Linguagem: Python 3.10+

Framework Web: FastAPI

Servidor ASGI: Uvicorn

Validação de Dados: Pydantic

Templates & Front-end: Jinja2, HTML5, CSS3

Banco de Dados: SQLite3

Testes: Pytest, unittest.mock (MagicMock, AsyncMock)

Conteinerização: Docker