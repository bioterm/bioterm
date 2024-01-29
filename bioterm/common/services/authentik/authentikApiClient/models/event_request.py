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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated
from authentikApiClient.models.event_actions import EventActions
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EventRequest(BaseModel):
    """
    Event Serializer
    """ # noqa: E501
    user: Optional[Dict[str, Any]] = None
    action: EventActions
    app: Annotated[str, Field(min_length=1, strict=True)]
    context: Optional[Dict[str, Any]] = None
    client_ip: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    expires: Optional[datetime] = None
    tenant: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["user", "action", "app", "context", "client_ip", "expires", "tenant"]

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
        """Create an instance of EventRequest from a JSON string"""
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
        # set to None if client_ip (nullable) is None
        # and model_fields_set contains the field
        if self.client_ip is None and "client_ip" in self.model_fields_set:
            _dict['client_ip'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EventRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "user": obj.get("user"),
            "action": obj.get("action"),
            "app": obj.get("app"),
            "context": obj.get("context"),
            "client_ip": obj.get("client_ip"),
            "expires": obj.get("expires"),
            "tenant": obj.get("tenant")
        })
        return _obj

