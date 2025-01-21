from fastapi import status
from httpx import AsyncClient

async def test_create_post_success(client: AsyncClient, access_token: str):
  headers = { "Authorization": f"Bearer {access_token}" }
  data = {"title": "Titulo Teste do Post", "content": "Esse Post é para conversarmos sobre calvície"}

  response = await client.post("/posts", json=data, headers=headers)

  assert response.status_code == status.HTTP_201_CREATED
  assert response.json().get("id") is not None