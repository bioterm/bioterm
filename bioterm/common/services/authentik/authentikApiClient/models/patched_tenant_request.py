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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PatchedTenantRequest(BaseModel):
    """
    Tenant Serializer
    """ # noqa: E501
    domain: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Domain that activates this tenant. Can be a superset, i.e. `a.b` for `aa.b` and `ba.b`")
    default: Optional[StrictBool] = None
    branding_title: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    branding_logo: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    branding_favicon: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    flow_authentication: Optional[StrictStr] = None
    flow_invalidation: Optional[StrictStr] = None
    flow_recovery: Optional[StrictStr] = None
    flow_unenrollment: Optional[StrictStr] = None
    flow_user_settings: Optional[StrictStr] = None
    flow_device_code: Optional[StrictStr] = None
    event_retention: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Events will be deleted after this duration.(Format: weeks=3;days=2;hours=3,seconds=2).")
    web_certificate: Optional[StrictStr] = Field(default=None, description="Web Certificate used by the authentik Core webserver.")
    attributes: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["domain", "default", "branding_title", "branding_logo", "branding_favicon", "flow_authentication", "flow_invalidation", "flow_recovery", "flow_unenrollment", "flow_user_settings", "flow_device_code", "event_retention", "web_certificate", "attributes"]

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
        """Create an instance of PatchedTenantRequest from a JSON string"""
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
        # set to None if flow_authentication (nullable) is None
        # and model_fields_set contains the field
        if self.flow_authentication is None and "flow_authentication" in self.model_fields_set:
            _dict['flow_authentication'] = None

        # set to None if flow_invalidation (nullable) is None
        # and model_fields_set contains the field
        if self.flow_invalidation is None and "flow_invalidation" in self.model_fields_set:
            _dict['flow_invalidation'] = None

        # set to None if flow_recovery (nullable) is None
        # and model_fields_set contains the field
        if self.flow_recovery is None and "flow_recovery" in self.model_fields_set:
            _dict['flow_recovery'] = None

        # set to None if flow_unenrollment (nullable) is None
        # and model_fields_set contains the field
        if self.flow_unenrollment is None and "flow_unenrollment" in self.model_fields_set:
            _dict['flow_unenrollment'] = None

        # set to None if flow_user_settings (nullable) is None
        # and model_fields_set contains the field
        if self.flow_user_settings is None and "flow_user_settings" in self.model_fields_set:
            _dict['flow_user_settings'] = None

        # set to None if flow_device_code (nullable) is None
        # and model_fields_set contains the field
        if self.flow_device_code is None and "flow_device_code" in self.model_fields_set:
            _dict['flow_device_code'] = None

        # set to None if web_certificate (nullable) is None
        # and model_fields_set contains the field
        if self.web_certificate is None and "web_certificate" in self.model_fields_set:
            _dict['web_certificate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PatchedTenantRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domain": obj.get("domain"),
            "default": obj.get("default"),
            "branding_title": obj.get("branding_title"),
            "branding_logo": obj.get("branding_logo"),
            "branding_favicon": obj.get("branding_favicon"),
            "flow_authentication": obj.get("flow_authentication"),
            "flow_invalidation": obj.get("flow_invalidation"),
            "flow_recovery": obj.get("flow_recovery"),
            "flow_unenrollment": obj.get("flow_unenrollment"),
            "flow_user_settings": obj.get("flow_user_settings"),
            "flow_device_code": obj.get("flow_device_code"),
            "event_retention": obj.get("event_retention"),
            "web_certificate": obj.get("web_certificate"),
            "attributes": obj.get("attributes")
        })
        return _obj


