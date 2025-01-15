from posts import PostsRoutes

def IncludeRoutes(app):
  app.include_router(PostsRoutes)
