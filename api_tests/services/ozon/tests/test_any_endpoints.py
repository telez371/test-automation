from http import HTTPStatus
from uuid import UUID

from api_tests.core.base_client import BaseClient
from api_tests.models.ozon_models.base import UuidRequest, UuidResponse
from api_tests.services.ozon.endpoints import Endpoints


class TestRequests:

    def test_post_anything(self, api_client: BaseClient, uuid_from_response: UUID) -> None:
        payload = UuidRequest(uuid=uuid_from_response).model_dump(mode="json")

        response = api_client.post(Endpoints.ANYTHING, json=payload)
        assert response.status_code == HTTPStatus.OK

        response_data = UuidResponse.model_validate(response.json())
        assert response_data.response_json == payload

    def test_get_anything(self, api_client: BaseClient, uuid_from_response: UUID) -> None:
        payload = UuidRequest(uuid=uuid_from_response).model_dump(mode="json")

        response = api_client.get(Endpoints.ANYTHING, params=payload)
        assert response.status_code == HTTPStatus.OK

        response_data = UuidResponse.model_validate(response.json())
        assert response_data.args == payload
