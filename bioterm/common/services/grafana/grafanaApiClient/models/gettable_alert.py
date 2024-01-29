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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from grafanaApiClient.models.alert_status import AlertStatus
from grafanaApiClient.models.receiver import Receiver
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GettableAlert(BaseModel):
    """
    GettableAlert gettable alert
    """ # noqa: E501
    annotations: Dict[str, StrictStr] = Field(description="LabelSet label set")
    ends_at: datetime = Field(description="ends at", alias="endsAt")
    fingerprint: StrictStr = Field(description="fingerprint")
    generator_url: Optional[StrictStr] = Field(default=None, description="generator URL Format: uri", alias="generatorURL")
    labels: Dict[str, StrictStr] = Field(description="LabelSet label set")
    receivers: List[Receiver] = Field(description="receivers")
    starts_at: datetime = Field(description="starts at", alias="startsAt")
    status: AlertStatus
    updated_at: datetime = Field(description="updated at", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["annotations", "endsAt", "fingerprint", "generatorURL", "labels", "receivers", "startsAt", "status", "updatedAt"]

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
        """Create an instance of GettableAlert from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in receivers (list)
        _items = []
        if self.receivers:
            for _item in self.receivers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['receivers'] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GettableAlert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "annotations": obj.get("annotations"),
            "endsAt": obj.get("endsAt"),
            "fingerprint": obj.get("fingerprint"),
            "generatorURL": obj.get("generatorURL"),
            "labels": obj.get("labels"),
            "receivers": [Receiver.from_dict(_item) for _item in obj.get("receivers")] if obj.get("receivers") is not None else None,
            "startsAt": obj.get("startsAt"),
            "status": AlertStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


