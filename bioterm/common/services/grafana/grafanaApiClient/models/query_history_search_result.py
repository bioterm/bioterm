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
from grafanaApiClient.models.query_history_dto import QueryHistoryDTO
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QueryHistorySearchResult(BaseModel):
    """
    QueryHistorySearchResult
    """ # noqa: E501
    page: Optional[StrictInt] = None
    per_page: Optional[StrictInt] = Field(default=None, alias="perPage")
    query_history: Optional[List[QueryHistoryDTO]] = Field(default=None, alias="queryHistory")
    total_count: Optional[StrictInt] = Field(default=None, alias="totalCount")
    __properties: ClassVar[List[str]] = ["page", "perPage", "queryHistory", "totalCount"]

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
        """Create an instance of QueryHistorySearchResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in query_history (list)
        _items = []
        if self.query_history:
            for _item in self.query_history:
                if _item:
                    _items.append(_item.to_dict())
            _dict['queryHistory'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of QueryHistorySearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page": obj.get("page"),
            "perPage": obj.get("perPage"),
            "queryHistory": [QueryHistoryDTO.from_dict(_item) for _item in obj.get("queryHistory")] if obj.get("queryHistory") is not None else None,
            "totalCount": obj.get("totalCount")
        })
        return _obj


