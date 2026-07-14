from fastapi import FastAPI

app = FastAPI(title="Interview API Skeleton")


@app.get("/")
def root():
    return {"status": "ok"}
