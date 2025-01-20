import sqlalchemy as sa
from database import metadata

User = sa.Table(
  'users', 
  metadata, 
  sa.Column('id', sa.Integer, primary_key=True, nullable=False),
  sa.Column('username', sa.String(100), unique=True, nullable=False),
  sa.Column('password', sa.String(64), nullable=False),
  sa.Column('is_admin', sa.Boolean, default=False, nullable=False),
  sa.Column('is_superuser', sa.Boolean, default=False, nullable=False),
  sa.Column('active', sa.Boolean, default=True, nullable=False),
)