from ddd.domain.external_api_abstraction.external_api_repository_abstraction import AbstractExternalApiRepository


class GetUniversityFormExternalApi:

    def __init__(self, external_api_repository: AbstractExternalApiRepository):
        self.external_api_repository = external_api_repository

    def get_university_using_requests(self) -> str:
        return self.external_api_repository.get_university_using_requests()

    async def get_university_using_aiohttp(self) -> str:
        return await self.external_api_repository.get_university_using_aiohttp()
