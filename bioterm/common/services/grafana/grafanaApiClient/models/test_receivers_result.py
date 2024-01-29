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
from pydantic import BaseModel
from grafanaApiClient.models.test_receiver_result import TestReceiverResult
from grafanaApiClient.models.test_receivers_config_alert_params import TestReceiversConfigAlertParams
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TestReceiversResult(BaseModel):
    """
    TestReceiversResult
    """ # noqa: E501
    alert: Optional[TestReceiversConfigAlertParams] = None
    notified_at: Optional[datetime] = None
    receivers: Optional[List[TestReceiverResult]] = None
    __properties: ClassVar[List[str]] = ["alert", "notified_at", "receivers"]

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
        """Create an instance of TestReceiversResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of alert
        if self.alert:
            _dict['alert'] = self.alert.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in receivers (list)
        _items = []
        if self.receivers:
            for _item in self.receivers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['receivers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TestReceiversResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alert": TestReceiversConfigAlertParams.from_dict(obj.get("alert")) if obj.get("alert") is not None else None,
            "notified_at": obj.get("notified_at"),
            "receivers": [TestReceiverResult.from_dict(_item) for _item in obj.get("receivers")] if obj.get("receivers") is not None else None
        })
        return _obj


