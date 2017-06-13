from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenAuthentication(TokenAuthentication):
    """
    Custom Token based authentication.

    Allows passing token via GET params
    """
    model = Token

    def authenticate(self, request):
        token = request.GET.get('token', None)
        if token:
            try:
                return self.authenticate_credentials(token)
            except ValueError:
                raise AuthenticationFailed("Invalid token")
        return super(CustomTokenAuthentication, self).authenticate(request)
