from fastapi import APIRouter, status
from posts.serializers import PostsRequest, PostsResponse, PostUpdate
from posts.services import PostService

service = PostService()

router = APIRouter(prefix='/posts', tags=["posts"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[PostsResponse])
async def read_post(limit:int = 0, skip:int = 0, published: bool = True, active: bool = True):
  return await service.read_all(published, limit, skip, active)

@router.get("/{post_id}", status_code=status.HTTP_200_OK, response_model=PostsResponse)
async def read_post(post_id: str):
  return await service.read(post_id)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostsResponse)
async def create_post(post: PostsRequest):
  return await service.create(post)

@router.patch("/{post_id}", status_code=status.HTTP_202_ACCEPTED, response_model=PostsResponse)
async def update_post(post_id:str, post: PostUpdate):
  return await service.update(post_id, post)

@router.delete("/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: str, fully: bool = False):
  return await service.delete(post_id) if not fully else await service.delete_fully(post_id)