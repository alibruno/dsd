# Ambiente de desenvolvimento

## Configurando o Ambiente Virtual (venv)

É uma boa prática utilizar um ambiente virtual para isolar as dependências do projeto.

1. Crie o ambiente virtual com o comando:

   ```bash
   python -m venv .venv
   ```

2. Ative o ambiente virtual:
   - **Linux/macOS:**

     ```bash
     source .venv/bin/activate
     ```

   - **Windows (PowerShell):**

     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

   - **Windows (CMD):**

     ```cmd
     .venv\Scripts\activate.bat
     ```

## Instalando as Dependências

Com o ambiente virtual ativado, instale as bibliotecas Python necessárias listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

As dependências principais incluem:

- `Django` (framework principal)
- `djangorestframework` (provê suporte à criação de
APIs RESTful)
- `drf-spectacular` (integra o Swagger para geração automática de documentação)
- `djangorestframework-simplejwt` (adiciona suporte à autenticação baseada em tokens JWT.)
