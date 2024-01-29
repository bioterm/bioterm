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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from grafanaApiClient.models.alert_rule_group_export import AlertRuleGroupExport
from grafanaApiClient.models.contact_point_export import ContactPointExport
from grafanaApiClient.models.notification_policy_export import NotificationPolicyExport
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AlertingFileExport(BaseModel):
    """
    AlertingFileExport
    """ # noqa: E501
    api_version: Optional[StrictInt] = Field(default=None, alias="apiVersion")
    contact_points: Optional[List[ContactPointExport]] = Field(default=None, alias="contactPoints")
    groups: Optional[List[AlertRuleGroupExport]] = None
    policies: Optional[List[NotificationPolicyExport]] = None
    __properties: ClassVar[List[str]] = ["apiVersion", "contactPoints", "groups", "policies"]

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
        """Create an instance of AlertingFileExport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contact_points (list)
        _items = []
        if self.contact_points:
            for _item in self.contact_points:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contactPoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item in self.groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in policies (list)
        _items = []
        if self.policies:
            for _item in self.policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AlertingFileExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiVersion": obj.get("apiVersion"),
            "contactPoints": [ContactPointExport.from_dict(_item) for _item in obj.get("contactPoints")] if obj.get("contactPoints") is not None else None,
            "groups": [AlertRuleGroupExport.from_dict(_item) for _item in obj.get("groups")] if obj.get("groups") is not None else None,
            "policies": [NotificationPolicyExport.from_dict(_item) for _item in obj.get("policies")] if obj.get("policies") is not None else None
        })
        return _obj

