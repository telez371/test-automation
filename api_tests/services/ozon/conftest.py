import pytest

from api_tests.services.ozon.api_client import ApiClient
from api_tests.services.ozon.config import Config

pytest_plugins = [
    "api_tests.fixtures.ozon_fixtures",
]


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    config = Config()
    return ApiClient(config)
