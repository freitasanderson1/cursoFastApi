from contextlib import asynccontextmanager
from posts import posts_routes
from fastapi import FastAPI
import sqlalchemy as sa
import databases


DATABASE_URL = 'sqlite:///./blog.db'

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

@asynccontextmanager
async def lifespan(app: FastAPI):
  from posts.posts_db import post
  
  await database.connect()
  metadata.create_all(engine)
  yield
  await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(posts_routes.router)
