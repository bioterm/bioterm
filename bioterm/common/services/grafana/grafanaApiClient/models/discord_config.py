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
from grafanaApiClient.models.http_client_config import HTTPClientConfig
from grafanaApiClient.models.url import URL
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DiscordConfig(BaseModel):
    """
    DiscordConfig
    """ # noqa: E501
    http_config: Optional[HTTPClientConfig] = None
    message: Optional[StrictStr] = None
    send_resolved: Optional[StrictBool] = None
    title: Optional[StrictStr] = None
    webhook_url: Optional[URL] = None
    __properties: ClassVar[List[str]] = ["http_config", "message", "send_resolved", "title", "webhook_url"]

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
        """Create an instance of DiscordConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of http_config
        if self.http_config:
            _dict['http_config'] = self.http_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhook_url
        if self.webhook_url:
            _dict['webhook_url'] = self.webhook_url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DiscordConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "http_config": HTTPClientConfig.from_dict(obj.get("http_config")) if obj.get("http_config") is not None else None,
            "message": obj.get("message"),
            "send_resolved": obj.get("send_resolved"),
            "title": obj.get("title"),
            "webhook_url": URL.from_dict(obj.get("webhook_url")) if obj.get("webhook_url") is not None else None
        })
        return _obj


