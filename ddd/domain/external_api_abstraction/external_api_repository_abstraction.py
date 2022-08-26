from abc import ABC, ABCMeta, abstractmethod


class AbstractExternalApiRepository(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_university_using_requests(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_university_using_aiohttp(self) -> str:
        raise NotImplementedError
