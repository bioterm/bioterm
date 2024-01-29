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
from grafanaApiClient.models.http_client_config import HTTPClientConfig
from grafanaApiClient.models.slack_action import SlackAction
from grafanaApiClient.models.slack_field import SlackField
from grafanaApiClient.models.url import URL
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SlackConfig(BaseModel):
    """
    SlackConfig
    """ # noqa: E501
    actions: Optional[List[SlackAction]] = None
    api_url: Optional[URL] = None
    api_url_file: Optional[StrictStr] = None
    callback_id: Optional[StrictStr] = None
    channel: Optional[StrictStr] = Field(default=None, description="Slack channel override, (like #other-channel or @username).")
    color: Optional[StrictStr] = None
    fallback: Optional[StrictStr] = None
    fields: Optional[List[SlackField]] = None
    footer: Optional[StrictStr] = None
    http_config: Optional[HTTPClientConfig] = None
    icon_emoji: Optional[StrictStr] = None
    icon_url: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = None
    link_names: Optional[StrictBool] = None
    mrkdwn_in: Optional[List[StrictStr]] = None
    pretext: Optional[StrictStr] = None
    send_resolved: Optional[StrictBool] = None
    short_fields: Optional[StrictBool] = None
    text: Optional[StrictStr] = None
    thumb_url: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    title_link: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["actions", "api_url", "api_url_file", "callback_id", "channel", "color", "fallback", "fields", "footer", "http_config", "icon_emoji", "icon_url", "image_url", "link_names", "mrkdwn_in", "pretext", "send_resolved", "short_fields", "text", "thumb_url", "title", "title_link", "username"]

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
        """Create an instance of SlackConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of api_url
        if self.api_url:
            _dict['api_url'] = self.api_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of http_config
        if self.http_config:
            _dict['http_config'] = self.http_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SlackConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": [SlackAction.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None,
            "api_url": URL.from_dict(obj.get("api_url")) if obj.get("api_url") is not None else None,
            "api_url_file": obj.get("api_url_file"),
            "callback_id": obj.get("callback_id"),
            "channel": obj.get("channel"),
            "color": obj.get("color"),
            "fallback": obj.get("fallback"),
            "fields": [SlackField.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None,
            "footer": obj.get("footer"),
            "http_config": HTTPClientConfig.from_dict(obj.get("http_config")) if obj.get("http_config") is not None else None,
            "icon_emoji": obj.get("icon_emoji"),
            "icon_url": obj.get("icon_url"),
            "image_url": obj.get("image_url"),
            "link_names": obj.get("link_names"),
            "mrkdwn_in": obj.get("mrkdwn_in"),
            "pretext": obj.get("pretext"),
            "send_resolved": obj.get("send_resolved"),
            "short_fields": obj.get("short_fields"),
            "text": obj.get("text"),
            "thumb_url": obj.get("thumb_url"),
            "title": obj.get("title"),
            "title_link": obj.get("title_link"),
            "username": obj.get("username")
        })
        return _obj


