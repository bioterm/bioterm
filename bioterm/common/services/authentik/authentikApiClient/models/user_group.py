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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserGroup(BaseModel):
    """
    Simplified Group Serializer for user's groups
    """ # noqa: E501
    pk: StrictStr
    num_pk: StrictInt = Field(description="Get a numerical, int32 ID for the group")
    name: Annotated[str, Field(strict=True, max_length=80)]
    is_superuser: Optional[StrictBool] = Field(default=None, description="Users added to this group will be superusers.")
    parent: Optional[StrictStr] = None
    parent_name: StrictStr
    attributes: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["pk", "num_pk", "name", "is_superuser", "parent", "parent_name", "attributes"]

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
        """Create an instance of UserGroup from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "pk",
                "num_pk",
                "parent_name",
            },
            exclude_none=True,
        )
        # set to None if parent (nullable) is None
        # and model_fields_set contains the field
        if self.parent is None and "parent" in self.model_fields_set:
            _dict['parent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "num_pk": obj.get("num_pk"),
            "name": obj.get("name"),
            "is_superuser": obj.get("is_superuser"),
            "parent": obj.get("parent"),
            "parent_name": obj.get("parent_name"),
            "attributes": obj.get("attributes")
        })
        return _obj


