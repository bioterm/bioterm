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
from pydantic import BaseModel, StrictStr
from grafanaApiClient.models.slack_confirmation_field import SlackConfirmationField
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SlackAction(BaseModel):
    """
    See https://api.slack.com/docs/message-attachments#action_fields and https://api.slack.com/docs/message-buttons for more information.
    """ # noqa: E501
    confirm: Optional[SlackConfirmationField] = None
    name: Optional[StrictStr] = None
    style: Optional[StrictStr] = None
    text: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["confirm", "name", "style", "text", "type", "url", "value"]

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
        """Create an instance of SlackAction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of confirm
        if self.confirm:
            _dict['confirm'] = self.confirm.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SlackAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "confirm": SlackConfirmationField.from_dict(obj.get("confirm")) if obj.get("confirm") is not None else None,
            "name": obj.get("name"),
            "style": obj.get("style"),
            "text": obj.get("text"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "value": obj.get("value")
        })
        return _obj


