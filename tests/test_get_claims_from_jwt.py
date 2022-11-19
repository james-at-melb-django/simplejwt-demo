from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


def test_user_id_claim_recoverable_from_authorization_header(client):
    refresh_token = RefreshToken()
    refresh_token.payload = {
        api_settings.TOKEN_TYPE_CLAIM: "refresh",
        api_settings.USER_ID_CLAIM: "testuser1@example.com",
    }

    # Set "iat" (issued at) and "exp" (expiry) claims with default values:
    refresh_token.set_iat(at_time=refresh_token.current_time)
    refresh_token.set_exp(
        from_time=refresh_token.current_time, lifetime=refresh_token.lifetime
    )

    # Set "jti" (JSON Web Token Unique ID) claim:
    refresh_token.set_jti()

    # Encode the access token as a Base64 string, which is what appears in the
    # HTTP_AUTHORIZATION header, after the "Bearer " prefix:
    encoded_access_token = str(refresh_token.access_token)

    # Decode the access token:
    access_token = AccessToken(encoded_access_token)

    # Ensure that we can recover the User ID Claim from the access token:
    assert access_token[api_settings.USER_ID_CLAIM] == "testuser1@example.com"
