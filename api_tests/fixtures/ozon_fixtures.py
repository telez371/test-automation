from http import HTTPStatus
from uuid import UUID

import allure
import pytest

from api_tests.models.ozon_models.base import UuidRequest
from api_tests.services.ozon.api_client import ApiClient
from api_tests.services.ozon.endpoints import Endpoints


@pytest.fixture(scope="session")
@allure.title("Get UUID fixture")
@allure.label("layer", "api")
@allure.label("category", "Setup")
def uuid_from_response(api_client: ApiClient) -> UUID:
    with allure.step("Send GET request to UUID endpoint"):
        response = api_client.get(Endpoints.UUID)
        allure.attach(response.text, "Response", allure.attachment_type.JSON)

    with allure.step("Verify response status code"):
        assert response.status_code == HTTPStatus.OK, \
            f"API Response Error: Expected status_code {HTTPStatus.OK}, but got {response.status_code}"

    with allure.step("Parse and validate UUID from response"):
        uuid_data = UuidRequest.model_validate(response.json())
        allure.attach(str(uuid_data.model_dump()), "Parsed UUID Data", allure.attachment_type.JSON)

    return uuid_data.uuid
