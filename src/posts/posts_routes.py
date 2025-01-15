from fastapi import APIRouter, Response, status

from posts import PostsRequest, PostsResponse, PostModel

from database import database

router = APIRouter(prefix='/posts')

@router.get("/", response_model=list[PostsResponse])
async def read_post(response: Response, published: bool, limit:int, skip:int = 0):
  query = PostModel.select().where(PostModel.c.active==True)
  return await database.fetch_all(query)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostsResponse)
async def create_post(post: PostsRequest):
  command = PostModel.insert().values(
    title=post.title, 
    content=post.content, 
    published_at=post.published_at, 
    published=post.published,
    active=post.active,
  )

  last_id = await database.execute(command)
  return {**post.model_dump(), "id": last_id}

@router.patch("/{post_id}", status_code=status.HTTP_202_ACCEPTED, response_model=PostsResponse)
async def update_post(post_id:str, post: PostsRequest):
  command = PostModel.update().where(id=post_id).values(
    title=post.title, 
    content=post.content, 
    published_at=post.published_at, 
    published=post.published,  
    active=post.active,  
  )
  return await database.execute(command)  