from contextlib import asynccontextmanager
from controllers import post
from fastapi import FastAPI
import sqlalchemy as sa
import databases


DATABASE_URL = 'sqlite:///./blog.db'

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
  await database.connect()
  yield
  await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
