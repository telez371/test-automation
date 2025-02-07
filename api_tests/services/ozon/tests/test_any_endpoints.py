from http import HTTPStatus
from uuid import UUID

import allure
import pytest

from api_tests.models.ozon_models.base import UuidRequest, UuidResponse
from api_tests.services.ozon.api_client import ApiClient
from api_tests.services.ozon.endpoints import Endpoints


@allure.epic("Ozon Service")
@allure.label("owner", "Aleksandr")
@allure.feature("Request Testing")
@allure.tag("api", "ozon", "smoke")
@pytest.mark.ozon
class TestRequests:

    @allure.story("POST Requests")
    @allure.title("Test POST anything endpoint")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("layer", "api")
    @allure.label("category", "Positive")
    @allure.issue("JIRA-123")
    @allure.testcase("https://testrail.com/case-123", "TestRail Case")
    def test_post_anything(self, api_client: ApiClient, uuid_from_response: UUID) -> None:
        with allure.step("Prepare request payload"):
            payload = UuidRequest(uuid=uuid_from_response).model_dump(mode="json")
            allure.attach(str(payload), "Request Payload", allure.attachment_type.JSON)

        with allure.step("Send POST request"):
            response = api_client.post(Endpoints.ANYTHING, json=payload)
            allure.attach(response.text, "Response", allure.attachment_type.JSON)

        with allure.step("Verify response status code"):
            assert response.status_code == HTTPStatus.OK, \
                f"API Response Error: Expected status_code {HTTPStatus.OK}, but got {response.status_code}"

        with allure.step("Validate response data"):
            response_data = UuidResponse.model_validate(response.json())
            assert response_data.response_json == payload, \
                f"Response data mismatch. Expected {payload}, got {response_data.response_json}"
            allure.attach(
                str(response_data.model_dump()),
                "Validated Response Data",
                allure.attachment_type.JSON
            )

    @allure.story("GET Requests")
    @allure.title("Test GET anything endpoint")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("layer", "api")
    @allure.label("category", "Positive")
    @allure.issue("JIRA-124")
    @allure.testcase("https://testrail.com/case-124", "TestRail Case")
    def test_get_anything(self, api_client: ApiClient, uuid_from_response: UUID) -> None:
        with allure.step("Prepare request parameters"):
            payload = UuidRequest(uuid=uuid_from_response).model_dump(mode="json")
            allure.attach(str(payload), "Request Parameters", allure.attachment_type.JSON)

        with allure.step("Send GET request"):
            response = api_client.get(Endpoints.ANYTHING, params=payload)
            allure.attach(response.text, "Response", allure.attachment_type.JSON)

        with allure.step("Verify response status code"):
            assert response.status_code == HTTPStatus.OK, \
                f"API Response Error: Expected status_code {HTTPStatus.OK}, but got {response.status_code}"

        with allure.step("Validate response data"):
            response_data = UuidResponse.model_validate(response.json())
            assert response_data.args == payload, \
                f"Response args mismatch. Expected {payload}, got {response_data.args}"
            allure.attach(
                str(response_data.model_dump()),
                "Validated Response Data",
                allure.attachment_type.JSON
            )
