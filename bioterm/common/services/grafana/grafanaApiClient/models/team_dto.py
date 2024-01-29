# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.

    The version of the OpenAPI document: 0.0.1
    Contact: hello@grafana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TeamDTO(BaseModel):
    """
    TeamDTO
    """ # noqa: E501
    access_control: Optional[Dict[str, StrictBool]] = Field(default=None, alias="accessControl")
    avatar_url: Optional[StrictStr] = Field(default=None, alias="avatarUrl")
    email: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    member_count: Optional[StrictInt] = Field(default=None, alias="memberCount")
    name: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = Field(default=None, alias="orgId")
    permission: Optional[StrictInt] = None
    uid: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["accessControl", "avatarUrl", "email", "id", "memberCount", "name", "orgId", "permission", "uid"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TeamDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TeamDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessControl": obj.get("accessControl"),
            "avatarUrl": obj.get("avatarUrl"),
            "email": obj.get("email"),
            "id": obj.get("id"),
            "memberCount": obj.get("memberCount"),
            "name": obj.get("name"),
            "orgId": obj.get("orgId"),
            "permission": obj.get("permission"),
            "uid": obj.get("uid")
        })
        return _obj


