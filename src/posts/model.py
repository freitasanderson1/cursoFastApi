import sqlalchemy as sa
from database import metadata

Post = sa.Table(
  'posts', 
  metadata, 
  sa.Column('id', sa.Integer, primary_key=True, nullable=False),
  sa.Column('title', sa.String(150), nullable=False),
  sa.Column('content', sa.String, nullable=False),
  sa.Column('published_at', sa.DateTime, nullable=True),
  sa.Column('published', sa.Boolean, default=False),
  sa.Column('active', sa.Boolean, default=True),
)