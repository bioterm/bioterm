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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from authentikApiClient.models.denied_action_enum import DeniedActionEnum
from authentikApiClient.models.flow_designation_enum import FlowDesignationEnum
from authentikApiClient.models.layout_enum import LayoutEnum
from authentikApiClient.models.policy_engine_mode import PolicyEngineMode
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FlowSet(BaseModel):
    """
    Stripped down flow serializer
    """ # noqa: E501
    pk: StrictStr
    policybindingmodel_ptr_id: StrictStr
    name: StrictStr
    slug: Annotated[str, Field(strict=True, max_length=50)] = Field(description="Visible in the URL.")
    title: StrictStr = Field(description="Shown as the Title in Flow pages.")
    designation: FlowDesignationEnum
    background: StrictStr = Field(description="Get the URL to the background image. If the name is /static or starts with http it is returned as-is")
    policy_engine_mode: Optional[PolicyEngineMode] = None
    compatibility_mode: Optional[StrictBool] = Field(default=None, description="Enable compatibility mode, increases compatibility with password managers on mobile devices.")
    export_url: StrictStr = Field(description="Get export URL for flow")
    layout: Optional[LayoutEnum] = None
    denied_action: Optional[DeniedActionEnum] = None
    __properties: ClassVar[List[str]] = ["pk", "policybindingmodel_ptr_id", "name", "slug", "title", "designation", "background", "policy_engine_mode", "compatibility_mode", "export_url", "layout", "denied_action"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
        return value

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
        """Create an instance of FlowSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "pk",
                "policybindingmodel_ptr_id",
                "background",
                "export_url",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FlowSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "policybindingmodel_ptr_id": obj.get("policybindingmodel_ptr_id"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "title": obj.get("title"),
            "designation": obj.get("designation"),
            "background": obj.get("background"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "compatibility_mode": obj.get("compatibility_mode"),
            "export_url": obj.get("export_url"),
            "layout": obj.get("layout"),
            "denied_action": obj.get("denied_action")
        })
        return _obj


