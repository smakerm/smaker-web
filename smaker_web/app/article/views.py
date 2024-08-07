from fastapi import FastAPI, Depends
from ..database import SessionDep
from sqlalchemy import select
from .models import Article, Tag

article_app = FastAPI()


@article_app.get("/")
async def article_list(db: SessionDep) -> list[Article]:
    articles = await db.execute(select(Article))
    print(articles)
    return articles
