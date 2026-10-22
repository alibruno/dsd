# Aluga car

## Resumo do fluxo de dados no DRF

1. Uma requisição chega pela URL mapeada pelo Router (urls.py).
2. O Router direciona a requisição para o método apropriado dentro do ViewSet (views.py).
3. O ViewSet busca/salva dados no banco usando o Model (models.py).
4. O ViewSet passa os dados pelo Serializer (serializers.py) para validar as informações recebidas ou transformar o objeto do banco em JSON.
5. A resposta JSON é devolvida para o cliente (Navegador, Postman, App React, Mobile, etc.).

## Ambiente de desenvolvimento

### Configurando o Ambiente Virtual (venv)

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

### Instalando as Dependências

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
