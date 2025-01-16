from pydantic import BaseModel
from datetime import datetime

class PostDelete(BaseModel):
  id: int
  title: str
  content: str
  published_at: datetime| None
  published: bool
  active: bool = False