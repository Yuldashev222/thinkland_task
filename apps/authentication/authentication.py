from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication, AuthUser

from django.utils.translation import gettext_lazy as _

from apps.authentication.services import ENCODE_USER_FIELDS


class CustomJWTAuthentication(JWTAuthentication):
    """
    An authentication plugin that authenticates requests through a JSON web
    token provided in a request header.
    """

    def get_user(self, validated_token: Token) -> AuthUser:
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken(_("Token contained no recognizable user identification"))
        user = self.user_model(
            **{api_settings.USER_ID_FIELD: user_id},
            **{key: getattr(validated_token.payload, key, '') for key in ENCODE_USER_FIELDS}
        )

        return user
