from pydantic import BaseModel
from datetime import datetime, UTC

class PostsRequest(BaseModel):
  title: str
  content: str
  published_at: datetime = datetime.now(UTC)
  published: bool = False
  active: bool = True