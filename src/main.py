from contextlib import asynccontextmanager
from posts.posts_routes import router
from fastapi import FastAPI
from database import database, engine, metadata

@asynccontextmanager
async def lifespan(app: FastAPI):
  # from posts.posts_model import Post
  
  await database.connect()
  metadata.create_all(engine)
  yield
  await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(router)
