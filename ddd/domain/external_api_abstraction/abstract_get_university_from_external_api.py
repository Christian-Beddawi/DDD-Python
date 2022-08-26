from abc import ABC, ABCMeta, abstractmethod


class AbstractGetUniversityFormExternalApi(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_university_using_requests(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def get_university_using_aiohttp(self) -> str:
        raise NotImplementedError
