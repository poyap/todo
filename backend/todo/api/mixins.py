from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .permissions import HasObjectPermission

class IsAuthorizedMixin:
    permission_classes = (IsAuthenticated, )


class AuthenticationMixin:
    authentication_classes = (SessionAuthentication, TokenAuthentication)