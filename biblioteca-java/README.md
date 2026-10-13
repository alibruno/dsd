# Biblioteca API - Spring Boot

API REST para gerenciamento de autores, livros e usuarios. O projeto foi desenvolvido com Spring Boot e utiliza autenticacao stateless por JWT, controle de acesso por cargo e H2 como banco de dados em memoria.

## Tecnologias

- Java 25
- Spring Boot 3.5.6
- Spring Web, Spring Data JPA e Spring HATEOAS
- Spring Security com JWT
- H2 Database
- Springdoc OpenAPI / Swagger UI
- Gradle Wrapper

## Pre-requisitos

- JDK 25
- Git, opcionalmente

O projeto ja inclui o Gradle Wrapper, portanto nao e necessario instalar o Gradle separadamente.

## Executando localmente

Na pasta `biblioteca-java`, execute:

```bash
./gradlew bootRun
```

No Windows PowerShell:

```powershell
./gradlew.bat bootRun
```

A API sera iniciada em `http://localhost:8080`.

Para executar os testes:

```bash
./gradlew test
```

## Documentacao e banco

- Swagger UI: `http://localhost:8080/swagger-ui/index.html`
- OpenAPI JSON: `http://localhost:8080/v3/api-docs`
- Console H2: `http://localhost:8080/h2-console`

Dados de conexao do H2:

```text
JDBC URL: jdbc:h2:mem:biblioteca
Usuario: sa
Senha: deixe em branco
```

O banco e recriado em memoria quando a aplicacao e reiniciada.

## Autenticacao

As rotas de autenticacao sao publicas. As demais rotas exigem um token JWT no header:

```http
Authorization: Bearer <token>
```

### Cadastrar usuario

```http
POST /api/auth/cadastrar
Content-Type: application/json
```

```json
{
	"login": "admin",
	"senha": "senha-segura",
	"cargo": "ADMIN"
}
```

Os cargos disponiveis sao `USER` e `ADMIN`.

### Entrar

```http
POST /api/auth/entrar
Content-Type: application/json
```

```json
{
	"login": "admin",
	"senha": "senha-segura"
}
```

A resposta contem o token JWT para as requisicoes autenticadas.

## Endpoints principais

| Metodo | Rota | Permissao | Descricao |
| --- | --- | --- | --- |
| `POST` | `/api/auth/cadastrar` | Publica | Cadastra um usuario |
| `POST` | `/api/auth/entrar` | Publica | Autentica e retorna um JWT |
| `GET` | `/api/autores` | `USER` ou `ADMIN` | Lista autores |
| `GET` | `/api/autores/{id}` | `USER` ou `ADMIN` | Consulta um autor |
| `POST` | `/api/autores` | `ADMIN` | Cadastra um autor |
| `GET` | `/api/livros` | `USER` ou `ADMIN` | Lista livros |
| `GET` | `/api/livros/{id}` | `USER` ou `ADMIN` | Consulta um livro |
| `POST` | `/api/livros` | `ADMIN` | Cadastra um livro |

Exemplo de cadastro de autor:

```json
{
	"nome": "Machado de Assis"
}
```

Exemplo de cadastro de livro:

```json
{
	"titulo": "Dom Casmurro",
	"autor": {
		"id": 1
	}
}
```

As respostas de autores e livros incluem links HATEOAS para navegacao entre recursos.

## Estrutura resumida

```text
src/main/java/com/exemplo/biblioteca/
├── config/       # Seguranca e OpenAPI
├── controller/   # Endpoints REST
├── dto/          # Objetos de requisicao e resposta
├── model/        # Entidades e cargos
├── repository/   # Persistencia JPA
└── security/     # Filtro e servico JWT
```

## Observacao

As configuracoes atuais sao voltadas para desenvolvimento. Antes de publicar a API, altere a chave usada para assinar JWTs, desative o console H2 e revise as configuracoes de CORS, banco de dados e ambiente.
