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
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from authentikApiClient.models.system_runtime import SystemRuntime
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class System(BaseModel):
    """
    Get system information.
    """ # noqa: E501
    http_headers: Dict[str, StrictStr] = Field(description="Get HTTP Request headers")
    http_host: StrictStr = Field(description="Get HTTP host")
    http_is_secure: StrictBool = Field(description="Get HTTP Secure flag")
    runtime: SystemRuntime
    tenant: StrictStr = Field(description="Currently active tenant")
    server_time: datetime = Field(description="Current server time")
    embedded_outpost_host: StrictStr = Field(description="Get the FQDN configured on the embedded outpost")
    __properties: ClassVar[List[str]] = ["http_headers", "http_host", "http_is_secure", "runtime", "tenant", "server_time", "embedded_outpost_host"]

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
        """Create an instance of System from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "http_headers",
                "http_host",
                "http_is_secure",
                "tenant",
                "server_time",
                "embedded_outpost_host",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of runtime
        if self.runtime:
            _dict['runtime'] = self.runtime.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of System from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "http_headers": obj.get("http_headers"),
            "http_host": obj.get("http_host"),
            "http_is_secure": obj.get("http_is_secure"),
            "runtime": SystemRuntime.from_dict(obj.get("runtime")) if obj.get("runtime") is not None else None,
            "tenant": obj.get("tenant"),
            "server_time": obj.get("server_time"),
            "embedded_outpost_host": obj.get("embedded_outpost_host")
        })
        return _obj


