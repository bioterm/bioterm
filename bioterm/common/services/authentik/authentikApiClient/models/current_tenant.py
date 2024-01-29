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
from pydantic import BaseModel, StrictStr
from authentikApiClient.models.footer_link import FooterLink
from authentikApiClient.models.ui_theme_enum import UiThemeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CurrentTenant(BaseModel):
    """
    Partial tenant information for styling
    """ # noqa: E501
    matched_domain: StrictStr
    branding_title: StrictStr
    branding_logo: StrictStr
    branding_favicon: StrictStr
    ui_footer_links: List[FooterLink]
    ui_theme: UiThemeEnum
    flow_authentication: Optional[StrictStr] = None
    flow_invalidation: Optional[StrictStr] = None
    flow_recovery: Optional[StrictStr] = None
    flow_unenrollment: Optional[StrictStr] = None
    flow_user_settings: Optional[StrictStr] = None
    flow_device_code: Optional[StrictStr] = None
    default_locale: StrictStr
    __properties: ClassVar[List[str]] = ["matched_domain", "branding_title", "branding_logo", "branding_favicon", "ui_footer_links", "ui_theme", "flow_authentication", "flow_invalidation", "flow_recovery", "flow_unenrollment", "flow_user_settings", "flow_device_code", "default_locale"]

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
        """Create an instance of CurrentTenant from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "ui_footer_links",
                "ui_theme",
                "default_locale",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in ui_footer_links (list)
        _items = []
        if self.ui_footer_links:
            for _item in self.ui_footer_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ui_footer_links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CurrentTenant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "matched_domain": obj.get("matched_domain"),
            "branding_title": obj.get("branding_title"),
            "branding_logo": obj.get("branding_logo"),
            "branding_favicon": obj.get("branding_favicon"),
            "ui_footer_links": [FooterLink.from_dict(_item) for _item in obj.get("ui_footer_links")] if obj.get("ui_footer_links") is not None else None,
            "ui_theme": obj.get("ui_theme"),
            "flow_authentication": obj.get("flow_authentication"),
            "flow_invalidation": obj.get("flow_invalidation"),
            "flow_recovery": obj.get("flow_recovery"),
            "flow_unenrollment": obj.get("flow_unenrollment"),
            "flow_user_settings": obj.get("flow_user_settings"),
            "flow_device_code": obj.get("flow_device_code"),
            "default_locale": obj.get("default_locale")
        })
        return _obj

