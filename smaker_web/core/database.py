from sqlmodel import SQLModel, Field, DateTime
from datetime import date, datetime
import importlib


class BaseModel(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime | None = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(
        default_factory=datetime.now,
        sa_column_kwargs={'onupdate': datetime.now}
    )
    deleted_at: datetime | None = Field(default=None)
