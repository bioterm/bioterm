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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from grafanaApiClient.models.annotation_panel_filter import AnnotationPanelFilter
from grafanaApiClient.models.annotation_target import AnnotationTarget
from grafanaApiClient.models.data_source_ref import DataSourceRef
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AnnotationQuery(BaseModel):
    """
    TODO docs FROM: AnnotationQuery in grafana-data/src/types/annotations.ts
    """ # noqa: E501
    built_in: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Set to 1 for the standard annotation query all dashboards have by default.", alias="builtIn")
    datasource: Optional[DataSourceRef] = None
    enable: Optional[StrictBool] = Field(default=None, description="When enabled the annotation query is issued with every dashboard refresh")
    filter: Optional[AnnotationPanelFilter] = None
    hide: Optional[StrictBool] = Field(default=None, description="Annotation queries can be toggled on or off at the top of the dashboard. When hide is true, the toggle is not shown in the dashboard.")
    icon_color: Optional[StrictStr] = Field(default=None, description="Color to use for the annotation event markers", alias="iconColor")
    name: Optional[StrictStr] = Field(default=None, description="Name of annotation.")
    target: Optional[AnnotationTarget] = None
    type: Optional[StrictStr] = Field(default=None, description="TODO -- this should not exist here, it is based on the --grafana-- datasource")
    __properties: ClassVar[List[str]] = ["builtIn", "datasource", "enable", "filter", "hide", "iconColor", "name", "target", "type"]

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
        """Create an instance of AnnotationQuery from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of datasource
        if self.datasource:
            _dict['datasource'] = self.datasource.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AnnotationQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "builtIn": obj.get("builtIn"),
            "datasource": DataSourceRef.from_dict(obj.get("datasource")) if obj.get("datasource") is not None else None,
            "enable": obj.get("enable"),
            "filter": AnnotationPanelFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "hide": obj.get("hide"),
            "iconColor": obj.get("iconColor"),
            "name": obj.get("name"),
            "target": AnnotationTarget.from_dict(obj.get("target")) if obj.get("target") is not None else None,
            "type": obj.get("type")
        })
        return _obj

