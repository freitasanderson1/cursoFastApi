from database import database
from databases.interfaces import Record
from fastapi import HTTPException, status

from posts import PostModel
from posts.serializers import PostRequest, PostUpdate

class PostService:
  async def read_all(self, active:bool, published: bool, limit:int, skip:int) -> list[Record]:
    query = PostModel.select().where(
      PostModel.c.active==active,
      PostModel.c.published==published
    ).limit(limit if limit else None).offset(skip)
    
    return await database.fetch_all(query)
  
  async def read(self, post_id: str) -> Record:
    post = await self.__get_by_id(post_id)
    if isinstance(post, HTTPException):
        raise post
    return {**dict(post), "id": post_id}
  
  async def create(self, post: PostRequest) -> Record:
    command = PostModel.insert().values(**post.dict())
    last_id = await database.execute(command)
    return {**post.model_dump(), "id": last_id}
  
  async def update(self, post_id:str, post: PostUpdate) -> Record:
    data = post.model_dump(exclude_unset=True)
    command = PostModel.update().where(PostModel.c.id==post_id).values(**data)
    await database.execute(command)
    return {**post.model_dump(), "id": post_id}
  
  async def delete(self, post_id: str) -> dict:
    post = await self.__get_by_id(post_id)
    if isinstance(post, HTTPException):
      raise post
    command = PostModel.update().where(PostModel.c.id==post_id).values(active=False, published=False)
    await database.execute(command)
    return {"msg": "Post deletado com sucesso!", "post_id": post_id}
  
  async def delete_fully(self, post_id: str) -> dict:
    post = await self.__get_by_id(post_id)
    if isinstance(post, HTTPException):
      raise post
    command = PostModel.delete().where(PostModel.c.id==post_id)
    await database.execute(command)
    return {"msg": "Post deletado permanentemente com sucesso!", "post_id": post_id}
  
  async def __get_by_id(self, post_id: str) -> Record:
    query = PostModel.select().where(PostModel.c.id==post_id)
    post = await database.fetch_one(query)
    return post if post else HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post não encontrado!")