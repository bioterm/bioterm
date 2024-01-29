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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from grafanaApiClient.models.host_port import HostPort
from grafanaApiClient.models.tls_config import TLSConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmailConfig(BaseModel):
    """
    EmailConfig
    """ # noqa: E501
    auth_identity: Optional[StrictStr] = None
    auth_password: Optional[StrictStr] = None
    auth_password_file: Optional[StrictStr] = None
    auth_secret: Optional[StrictStr] = None
    auth_username: Optional[StrictStr] = None
    var_from: Optional[StrictStr] = Field(default=None, alias="from")
    headers: Optional[Dict[str, StrictStr]] = None
    hello: Optional[StrictStr] = None
    html: Optional[StrictStr] = None
    require_tls: Optional[StrictBool] = None
    send_resolved: Optional[StrictBool] = None
    smarthost: Optional[HostPort] = None
    text: Optional[StrictStr] = None
    tls_config: Optional[TLSConfig] = None
    to: Optional[StrictStr] = Field(default=None, description="Email address to notify.")
    __properties: ClassVar[List[str]] = ["auth_identity", "auth_password", "auth_password_file", "auth_secret", "auth_username", "from", "headers", "hello", "html", "require_tls", "send_resolved", "smarthost", "text", "tls_config", "to"]

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
        """Create an instance of EmailConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of smarthost
        if self.smarthost:
            _dict['smarthost'] = self.smarthost.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tls_config
        if self.tls_config:
            _dict['tls_config'] = self.tls_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EmailConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auth_identity": obj.get("auth_identity"),
            "auth_password": obj.get("auth_password"),
            "auth_password_file": obj.get("auth_password_file"),
            "auth_secret": obj.get("auth_secret"),
            "auth_username": obj.get("auth_username"),
            "from": obj.get("from"),
            "headers": obj.get("headers"),
            "hello": obj.get("hello"),
            "html": obj.get("html"),
            "require_tls": obj.get("require_tls"),
            "send_resolved": obj.get("send_resolved"),
            "smarthost": HostPort.from_dict(obj.get("smarthost")) if obj.get("smarthost") is not None else None,
            "text": obj.get("text"),
            "tls_config": TLSConfig.from_dict(obj.get("tls_config")) if obj.get("tls_config") is not None else None,
            "to": obj.get("to")
        })
        return _obj


