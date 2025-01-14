from pydantic import BaseModel
from datetime import datetime, UTC

class PostsRequest(BaseModel):
  title: str
  content: str
  published_at: datetime = datetime.now(UTC)
  published: bool = False


class PostsResponse(BaseModel):
  id: int
  title: str
  content: str
  published_at: datetime| None
  published: bool