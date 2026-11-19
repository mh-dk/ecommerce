# E-Commerce Backend

A FastAPI e-commerce backend built with SQLAlchemy and PostgreSQL.

## Requirements

- Python 3.14 or later
- [uv](https://docs.astral.sh/uv/)
- PostgreSQL

## Setup

1. Install dependencies:

   ```powershell
   uv sync
   ```

2. Create the environment file:

   ```powershell
   Copy-Item env.example .env
   ```

   Update `SQLALCHEMY_URL` and `JWT_SECRET` in `.env`. For example:

   ```dotenv
   SQLALCHEMY_URL=postgresql+psycopg2://postgres:password@localhost:5432/ecommerce
   JWT_SECRET=replace-with-a-long-random-secret
   ```

   Generate a suitable JWT secret with:

   ```powershell
   python -c "import secrets; print(secrets.token_urlsafe(48))"
   ```

3. Create the PostgreSQL database referenced by `SQLALCHEMY_URL`.

   SQLAlchemy tables are generated automatically when the application starts. `Base.metadata.create_all(engine)` creates missing tables, but does not alter or migrate existing tables.

## Run

Development server with reload:

```powershell
uv run fastapi dev
```

Production server:

```powershell
uv run fastapi run
```

The API documentation is available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

The FastAPI entry point is `ecommerce:app`.

## Environment Variables

| Variable | Description |
| --- | --- |
| `SQLALCHEMY_URL` | PostgreSQL SQLAlchemy connection URL |
| `JWT_SECRET` | Secret key used to sign and verify HS256 bearer tokens |

## API Routes

| Area | Base path |
| --- | --- |
| Authentication | `/auth` |
| Users | `/users` |
| Vendors | `/vendors` |
| Products | `/products` |

Protected routes require an `Authorization: Bearer <token>` header.

> **Swagger limitation:** Swagger UI currently ignores `Authorization` headers for protected routes. Use a different API client, such as Postman or Insomnia, and set the `Authorization: Bearer <token>` header manually.