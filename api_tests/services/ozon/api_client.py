from api_tests.core.base_client import BaseClient
from api_tests.services.ozon.config import Config


class ApiClient(BaseClient):
    def __init__(self, config: Config):
        super().__init__(config)
        self.base_url = config.BASE_URL
        self.default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }