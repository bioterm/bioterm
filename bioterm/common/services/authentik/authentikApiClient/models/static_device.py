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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictInt
from pydantic import Field
from typing_extensions import Annotated
from authentikApiClient.models.static_device_token import StaticDeviceToken
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StaticDevice(BaseModel):
    """
    Serializer for static authenticator devices
    """ # noqa: E501
    name: Annotated[str, Field(strict=True, max_length=64)] = Field(description="The human-readable name of this device.")
    token_set: List[StaticDeviceToken]
    pk: StrictInt
    __properties: ClassVar[List[str]] = ["name", "token_set", "pk"]

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
        """Create an instance of StaticDevice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "token_set",
                "pk",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in token_set (list)
        _items = []
        if self.token_set:
            for _item in self.token_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['token_set'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of StaticDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "token_set": [StaticDeviceToken.from_dict(_item) for _item in obj.get("token_set")] if obj.get("token_set") is not None else None,
            "pk": obj.get("pk")
        })
        return _obj

