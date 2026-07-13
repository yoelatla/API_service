# Setup

1. **First time only** — start Postgres (via Docker):
```
docker compose up -d
```
This runs Postgres with the user/password/db already set (`interview_user` / `interview_pass` / `interview_db`, port 5434). After the first time, it keeps running in the background — no need to redo this unless you rebooted or ran `docker compose down`.

2. **First time only** — create venv + install:
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Re-run `pip install -r requirements.txt` only if `requirements.txt` changes later.

3. **First time only** — `.env` should contain:
```
DATABASE_URL=postgresql://interview_user:interview_pass@localhost:5434/interview_db
```

4. **First time, and again any time the schema changes** — apply migrations (creates the `items` table):
```
alembic upgrade head
```

5. **Every time you start working** — activate the venv (if not already active) and run the server:
```
source venv/bin/activate
uvicorn main:app --reload
```
`--reload` means you don't need to restart this for code changes — only if the server crashes or you close the terminal.

6. Verify: open http://127.0.0.1:8000/docs — Swagger UI, test POST /items then GET /items.

7. **Any time you want to check nothing broke** — run tests (Postgres must be running):
```
python -m pytest -v
```

8. **Any time you want to inspect the DB directly** — open a psql shell into the running container:
```
docker compose exec db psql -U interview_user -d interview_db
```
Then e.g. `SELECT * FROM items;` or `\d items` to see the schema.
