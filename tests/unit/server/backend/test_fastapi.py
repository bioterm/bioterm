import pytest

from .....bioterm.server.backend.app.main import app

# from httpx import AsyncClient


@pytest.mark.asyncio
async def test_app_creation():
    # assert app.title == "YourProjectNameHere"  # Replace with your actual project name
    assert app.openapi_url == "/api/v0/openapi.json"
    assert app.redoc_url is None

    # If you're using OAuth in Swagger UI, assert its configuration:
    assert "clientId" in app.swagger_ui_init_oauth

    # Replace with your actual client id
    # assert app.swagger_ui_init_oauth["clientId"] == "YourAuthentikClientId"


# @pytest.mark.asyncio
# async def test_read_main():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/")
#     assert response.status_code == 200  # Assuming root endpoint responds with 200 OK
