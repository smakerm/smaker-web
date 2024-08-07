from sqlmodel import Field, TEXT, Relationship, SQLModel
# from smaker_web.core import BaseModel
from ...core import BaseModel


class ArticleTagLink(SQLModel, table=True):
    tag_id: int | None = Field(
        default=None, foreign_key="tag.id", primary_key=True)
    article_id: int | None = Field(
        default=None, foreign_key="article.id", primary_key=True)


class Article(BaseModel, table=True):
    title: str = Field()
    abstract: str = Field(max_length=500)
    content: str = TEXT()
    tags: list["Tag"] = Relationship(
        back_populates="articles", link_model=ArticleTagLink)


class Tag(BaseModel, table=True):
    tag: str = Field(min_length=1, max_length=20)
    articles: list["Article"] = Relationship(
        back_populates="tags", link_model=ArticleTagLink)
