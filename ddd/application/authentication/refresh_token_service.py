from ddd.domain.authentication_abstraction.abstract_authentication import AuthenticationAbstraction


class RefreshJwtToken:
    def __init__(self, authentication: AuthenticationAbstraction):
        self.authentication = authentication

    def refresh_access_token(self, refresh_token: str) -> str:
        return self.authentication.refresh_token(refresh_token)
