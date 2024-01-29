# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2023.5.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from authentikApiClient.models.flow_inspector_plan import FlowInspectorPlan
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FlowInspection(BaseModel):
    """
    Serializer for inspect endpoint
    """ # noqa: E501
    plans: List[FlowInspectorPlan]
    current_plan: Optional[FlowInspectorPlan] = None
    is_completed: StrictBool
    __properties: ClassVar[List[str]] = ["plans", "current_plan", "is_completed"]

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
        """Create an instance of FlowInspection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in plans (list)
        _items = []
        if self.plans:
            for _item in self.plans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['plans'] = _items
        # override the default output from pydantic by calling `to_dict()` of current_plan
        if self.current_plan:
            _dict['current_plan'] = self.current_plan.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FlowInspection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plans": [FlowInspectorPlan.from_dict(_item) for _item in obj.get("plans")] if obj.get("plans") is not None else None,
            "current_plan": FlowInspectorPlan.from_dict(obj.get("current_plan")) if obj.get("current_plan") is not None else None,
            "is_completed": obj.get("is_completed")
        })
        return _obj

