import json

from ddd.domain.authentication_abstraction.abstract_authentication import AuthenticationAbstraction


class LoginWithGoogleFirebase:
    def __init__(self, authentication: AuthenticationAbstraction):
        self.authentication = authentication

    def login_with_google_firebase(self, email: str, password: str) -> json:
        return self.authentication.login(email=email, password=password)
