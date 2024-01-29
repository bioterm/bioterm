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
from pydantic import Field
from grafanaApiClient.models.link_transformation_config import LinkTransformationConfig
from grafanaApiClient.models.time_range import TimeRange
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InternalDataLink(BaseModel):
    """
    InternalDataLink definition to allow Explore links to be constructed in the backend
    """ # noqa: E501
    datasource_name: Optional[StrictStr] = Field(default=None, alias="datasourceName")
    datasource_uid: Optional[StrictStr] = Field(default=None, alias="datasourceUid")
    panels_state: Optional[Any] = Field(default=None, description="This is an object constructed with the keys as the values of the enum VisType and the value being a bag of properties", alias="panelsState")
    query: Optional[Any] = None
    time_range: Optional[TimeRange] = Field(default=None, alias="timeRange")
    transformations: Optional[List[LinkTransformationConfig]] = None
    __properties: ClassVar[List[str]] = ["datasourceName", "datasourceUid", "panelsState", "query", "timeRange", "transformations"]

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
        """Create an instance of InternalDataLink from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of time_range
        if self.time_range:
            _dict['timeRange'] = self.time_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in transformations (list)
        _items = []
        if self.transformations:
            for _item in self.transformations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transformations'] = _items
        # set to None if panels_state (nullable) is None
        # and model_fields_set contains the field
        if self.panels_state is None and "panels_state" in self.model_fields_set:
            _dict['panelsState'] = None

        # set to None if query (nullable) is None
        # and model_fields_set contains the field
        if self.query is None and "query" in self.model_fields_set:
            _dict['query'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of InternalDataLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "datasourceName": obj.get("datasourceName"),
            "datasourceUid": obj.get("datasourceUid"),
            "panelsState": obj.get("panelsState"),
            "query": obj.get("query"),
            "timeRange": TimeRange.from_dict(obj.get("timeRange")) if obj.get("timeRange") is not None else None,
            "transformations": [LinkTransformationConfig.from_dict(_item) for _item in obj.get("transformations")] if obj.get("transformations") is not None else None
        })
        return _obj


