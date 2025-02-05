from http import HTTPStatus
from uuid import UUID

import pytest

from api_tests.core.api_client import ApiClient
from api_tests.models.ozon_models.base import UuidRequest
from api_tests.tests.ozon_tests.endpoints import Endpoints


@pytest.fixture(scope="session")
def uuid_from_response(api_client: ApiClient) -> UUID:
    response = api_client.get(Endpoints.UUID)
    assert response.status_code == HTTPStatus.OK, "Failed to get UUID"

    uuid_data = UuidRequest.model_validate(response.json())
    return uuid_data.uuid
