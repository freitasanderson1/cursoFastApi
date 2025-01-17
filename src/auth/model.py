import sqlalchemy as sa
from database import metadata

User = sa.Table(
  'users', 
  metadata, 
  sa.Column('id', sa.Integer, primary_key=True, nullable=False),
  sa.Column('login', sa.String(100), nullable=False),
  sa.Column('password', sa.String(64), nullable=False),
  sa.Column('active', sa.Boolean, default=True),
)