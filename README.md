# Setup

## First time only

```
docker compose up -d               # starts the Postgres container in the background
python -m venv venv                # creates a local Python environment in ./venv
source venv/bin/activate           # activates it (Windows: venv\Scripts\activate)
pip install -r requirements.txt    # installs the project's Python packages into venv
```

`.env` should contain:
```
DATABASE_URL=postgresql://interview_user:interview_pass@localhost:5434/interview_db
```

If Docker fails with "Cannot connect to the Docker daemon", start it with `docker desktop start` (or open Docker Desktop), then retry.

## Every time you work

```
source venv/bin/activate    # activates the Python environment (needed every new terminal)
uvicorn main:app --reload   # starts the API server, restarts automatically on code changes
```

Open http://127.0.0.1:8000/docs to try the API (Swagger UI).

## Useful commands

- **Inspect the DB:** `docker compose exec db psql -U interview_user -d interview_db` — opens a SQL shell inside the Postgres container. Then `SELECT * FROM items;` or `\d items`
- **Stop Postgres:** `docker compose down` — stops and removes the container (data persists in the `db_data` volume)
