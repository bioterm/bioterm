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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TeamMemberDTO(BaseModel):
    """
    TeamMemberDTO
    """ # noqa: E501
    auth_module: Optional[StrictStr] = None
    avatar_url: Optional[StrictStr] = Field(default=None, alias="avatarUrl")
    email: Optional[StrictStr] = None
    labels: Optional[List[StrictStr]] = None
    login: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = Field(default=None, alias="orgId")
    permission: Optional[StrictInt] = None
    team_id: Optional[StrictInt] = Field(default=None, alias="teamId")
    team_uid: Optional[StrictStr] = Field(default=None, alias="teamUID")
    user_id: Optional[StrictInt] = Field(default=None, alias="userId")
    __properties: ClassVar[List[str]] = ["auth_module", "avatarUrl", "email", "labels", "login", "name", "orgId", "permission", "teamId", "teamUID", "userId"]

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
        """Create an instance of TeamMemberDTO from a JSON string"""
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
        """Create an instance of TeamMemberDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auth_module": obj.get("auth_module"),
            "avatarUrl": obj.get("avatarUrl"),
            "email": obj.get("email"),
            "labels": obj.get("labels"),
            "login": obj.get("login"),
            "name": obj.get("name"),
            "orgId": obj.get("orgId"),
            "permission": obj.get("permission"),
            "teamId": obj.get("teamId"),
            "teamUID": obj.get("teamUID"),
            "userId": obj.get("userId")
        })
        return _obj


