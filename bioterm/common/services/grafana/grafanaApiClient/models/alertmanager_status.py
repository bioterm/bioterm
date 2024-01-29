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
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from grafanaApiClient.models.alertmanager_config import AlertmanagerConfig
from grafanaApiClient.models.cluster_status import ClusterStatus
from grafanaApiClient.models.version_info import VersionInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AlertmanagerStatus(BaseModel):
    """
    AlertmanagerStatus alertmanager status
    """ # noqa: E501
    cluster: ClusterStatus
    config: AlertmanagerConfig
    uptime: datetime = Field(description="uptime")
    version_info: VersionInfo = Field(alias="versionInfo")
    __properties: ClassVar[List[str]] = ["cluster", "config", "uptime", "versionInfo"]

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
        """Create an instance of AlertmanagerStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cluster
        if self.cluster:
            _dict['cluster'] = self.cluster.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version_info
        if self.version_info:
            _dict['versionInfo'] = self.version_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AlertmanagerStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cluster": ClusterStatus.from_dict(obj.get("cluster")) if obj.get("cluster") is not None else None,
            "config": AlertmanagerConfig.from_dict(obj.get("config")) if obj.get("config") is not None else None,
            "uptime": obj.get("uptime"),
            "versionInfo": VersionInfo.from_dict(obj.get("versionInfo")) if obj.get("versionInfo") is not None else None
        })
        return _obj


