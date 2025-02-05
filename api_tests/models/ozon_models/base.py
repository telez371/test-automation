from typing import Optional, Any, Dict
from uuid import UUID

from pydantic import Field, BaseModel


class UuidRequest(BaseModel):
    uuid: UUID


class UuidResponse(BaseModel):
    args: Dict[str, str]
    data: Optional[str] = None
    files: Optional[Dict[str, Any]] = None
    form: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None
    response_json: Optional[Dict[str, str]] = Field(default=None, alias="json")
    method: Optional[str] = None
    origin: Optional[str] = None
    url: Optional[str] = None


class GetAnythingResponse(BaseModel):
    args: Dict[str, str]
