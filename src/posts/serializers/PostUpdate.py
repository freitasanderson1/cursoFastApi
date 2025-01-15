from pydantic import BaseModel
from datetime import datetime, UTC

class PostUpdate(BaseModel):
  title: str | None = None
  content: str | None = None
  published_at: datetime | None = None
  published: bool | None = None
  active: bool | None = None