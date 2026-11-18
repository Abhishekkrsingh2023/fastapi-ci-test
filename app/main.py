from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI CI/CD Demo")


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

