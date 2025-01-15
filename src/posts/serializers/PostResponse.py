from pydantic import BaseModel
from datetime import datetime

class PostsResponse(BaseModel):
  id: int
  title: str
  content: str
  published_at: datetime| None
  published: bool
  active: bool