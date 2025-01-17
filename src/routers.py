from posts import PostsRoutes
from auth import AuthRoutes

def IncludeRoutes(app):
  app.include_router(PostsRoutes)
  app.include_router(AuthRoutes)
