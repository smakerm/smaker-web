from fastapi import FastAPI
from .app import article_app

app = FastAPI()

app.mount('/article', article_app)


@app.get("/")
def hello():
    return "hello"
