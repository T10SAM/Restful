# Restful - API de Tarefas Colaborativas

## Descrição
API desenvolvida com FastAPI, SQLAlchemy e MySQL para gestão de tarefas colaborativas. Permite cadastro de usuários, autenticação JWT, criação e gerenciamento de tarefas, filtros avançados e exportação de dados em CSV.

## Funcionalidades
- Cadastro, listagem, atualização e deleção de usuários
- Autenticação JWT (login/logout)
- Cadastro, listagem, atualização, deleção e filtro de tarefas
- Exportação de tarefas em CSV
- Testes automatizados com pytest

## Instalação
1. Clone o repositório:
   ```bash
   git clone <url-do-repo>
   cd Restful
   ```
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração
1. Renomeie o arquivo `core/.env` e configure as variáveis de ambiente:
   ```env
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_HOST=127.0.0.1
   DB_NAME=nome_do_banco
   SECRET_KEY=sua_secret_key
   ```
2. Certifique-se de que o banco MySQL está rodando e o banco de dados existe.

## Execução
```bash
uvicorn main:app --reload
```
Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

## Testes
Execute os testes automatizados:
```bash
pytest
```

## Estrutura de Pastas
- `controller/` - Rotas e lógica de API
- `core/` - Configurações, autenticação, banco
- `models/` - Modelos ORM
- `repositories/` - Acesso a dados
- `schemas/` - Schemas Pydantic
- `tests/` - Testes automatizados

## Licença
MIT

