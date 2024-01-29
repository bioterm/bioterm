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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel
from pydantic import Field
from grafanaApiClient.models.dashboard_report_dto import DashboardReportDTO
from grafanaApiClient.models.time_range_dto import TimeRangeDTO
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DashboardDTO(BaseModel):
    """
    DashboardDTO
    """ # noqa: E501
    dashboard: Optional[DashboardReportDTO] = None
    report_variables: Optional[Union[str, Any]] = Field(default=None, alias="reportVariables")
    time_range: Optional[TimeRangeDTO] = Field(default=None, alias="timeRange")
    __properties: ClassVar[List[str]] = ["dashboard", "reportVariables", "timeRange"]

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
        """Create an instance of DashboardDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dashboard
        if self.dashboard:
            _dict['dashboard'] = self.dashboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_range
        if self.time_range:
            _dict['timeRange'] = self.time_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DashboardDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dashboard": DashboardReportDTO.from_dict(obj.get("dashboard")) if obj.get("dashboard") is not None else None,
            "reportVariables": obj.get("reportVariables"),
            "timeRange": TimeRangeDTO.from_dict(obj.get("timeRange")) if obj.get("timeRange") is not None else None
        })
        return _obj


