from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken


def test_get_message(client):
    refresh_token = RefreshToken()
    refresh_token[api_settings.USER_ID_CLAIM] = "testuser1@example.com"

    response = client.get(
        "/simplejwtdemo/api/message",
        HTTP_AUTHORIZATION="Bearer " + str(refresh_token.access_token),
    )
    assert response.json() == {"message": "Hello World"}


def test_get_message_without_authorization(client):
    response = client.get(
        "/simplejwtdemo/api/message",
    )
    assert response.status_code == 401
