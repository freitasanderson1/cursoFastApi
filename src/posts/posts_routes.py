from fastapi import APIRouter
from datetime import datetime, UTC
from posts.posts_model import PostsRequest

router = APIRouter(prefix='/posts')

@router.get("/")
def read_root():
  return {"msg": "Hello World!"}


@router.get("/{post_type}")
def read_post(post_type: int):
  return {"posts": [{'title':f'post {post_type}', 'date':datetime.now(UTC)}]}


@router.post("/{post_id}")
def create_post(post_id: int, post: PostsRequest):
  return {"post_name": PostsRequest.name, "post_id": post_id}