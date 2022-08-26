import json
from abc import ABC, ABCMeta, abstractmethod


class AuthenticationAbstraction(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def login(self, email: str, password: str) -> json:
        raise NotImplementedError

    @abstractmethod
    def refresh_token(self, uid: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def is_valid(self, access_token: str) -> bool:
        raise NotImplementedError
