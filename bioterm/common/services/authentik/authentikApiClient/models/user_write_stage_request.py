# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2023.5.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from authentikApiClient.models.flow_set_request import FlowSetRequest
from authentikApiClient.models.user_creation_mode_enum import UserCreationModeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserWriteStageRequest(BaseModel):
    """
    UserWriteStage Serializer
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True)]
    flow_set: Optional[List[FlowSetRequest]] = None
    user_creation_mode: Optional[UserCreationModeEnum] = None
    create_users_as_inactive: Optional[StrictBool] = Field(default=None, description="When set, newly created users are inactive and cannot login.")
    create_users_group: Optional[StrictStr] = Field(default=None, description="Optionally add newly created users to this group.")
    user_path_template: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "flow_set", "user_creation_mode", "create_users_as_inactive", "create_users_group", "user_path_template"]

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
        """Create an instance of UserWriteStageRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item in self.flow_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flow_set'] = _items
        # set to None if create_users_group (nullable) is None
        # and model_fields_set contains the field
        if self.create_users_group is None and "create_users_group" in self.model_fields_set:
            _dict['create_users_group'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserWriteStageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "flow_set": [FlowSetRequest.from_dict(_item) for _item in obj.get("flow_set")] if obj.get("flow_set") is not None else None,
            "user_creation_mode": obj.get("user_creation_mode"),
            "create_users_as_inactive": obj.get("create_users_as_inactive"),
            "create_users_group": obj.get("create_users_group"),
            "user_path_template": obj.get("user_path_template")
        })
        return _obj


