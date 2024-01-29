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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PatchedEmailStageRequest(BaseModel):
    """
    EmailStage Serializer
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    flow_set: Optional[List[FlowSetRequest]] = None
    use_global_settings: Optional[StrictBool] = Field(default=None, description="When enabled, global Email connection settings will be used and connection settings below will be ignored.")
    host: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    port: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    username: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    use_tls: Optional[StrictBool] = None
    use_ssl: Optional[StrictBool] = None
    timeout: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    from_address: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=254)]] = None
    token_expiry: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = Field(default=None, description="Time in minutes the token sent is valid.")
    subject: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    template: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    activate_user_on_success: Optional[StrictBool] = Field(default=None, description="Activate users upon completion of stage.")
    __properties: ClassVar[List[str]] = ["name", "flow_set", "use_global_settings", "host", "port", "username", "password", "use_tls", "use_ssl", "timeout", "from_address", "token_expiry", "subject", "template", "activate_user_on_success"]

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
        """Create an instance of PatchedEmailStageRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PatchedEmailStageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "flow_set": [FlowSetRequest.from_dict(_item) for _item in obj.get("flow_set")] if obj.get("flow_set") is not None else None,
            "use_global_settings": obj.get("use_global_settings"),
            "host": obj.get("host"),
            "port": obj.get("port"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "use_tls": obj.get("use_tls"),
            "use_ssl": obj.get("use_ssl"),
            "timeout": obj.get("timeout"),
            "from_address": obj.get("from_address"),
            "token_expiry": obj.get("token_expiry"),
            "subject": obj.get("subject"),
            "template": obj.get("template"),
            "activate_user_on_success": obj.get("activate_user_on_success")
        })
        return _obj

