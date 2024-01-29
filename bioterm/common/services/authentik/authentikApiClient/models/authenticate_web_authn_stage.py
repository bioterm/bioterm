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
from pydantic import Field
from authentikApiClient.models.authenticator_attachment_enum import AuthenticatorAttachmentEnum
from authentikApiClient.models.flow_set import FlowSet
from authentikApiClient.models.resident_key_requirement_enum import ResidentKeyRequirementEnum
from authentikApiClient.models.user_verification_enum import UserVerificationEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AuthenticateWebAuthnStage(BaseModel):
    """
    AuthenticateWebAuthnStage Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr
    component: StrictStr = Field(description="Get object type so that we know how to edit the object")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    flow_set: Optional[List[FlowSet]] = None
    configure_flow: Optional[StrictStr] = Field(default=None, description="Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage.")
    friendly_name: Optional[StrictStr] = None
    user_verification: Optional[UserVerificationEnum] = None
    authenticator_attachment: Optional[AuthenticatorAttachmentEnum] = None
    resident_key_requirement: Optional[ResidentKeyRequirementEnum] = None
    __properties: ClassVar[List[str]] = ["pk", "name", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "flow_set", "configure_flow", "friendly_name", "user_verification", "authenticator_attachment", "resident_key_requirement"]

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
        """Create an instance of AuthenticateWebAuthnStage from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "pk",
                "component",
                "verbose_name",
                "verbose_name_plural",
                "meta_model_name",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item in self.flow_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flow_set'] = _items
        # set to None if configure_flow (nullable) is None
        # and model_fields_set contains the field
        if self.configure_flow is None and "configure_flow" in self.model_fields_set:
            _dict['configure_flow'] = None

        # set to None if friendly_name (nullable) is None
        # and model_fields_set contains the field
        if self.friendly_name is None and "friendly_name" in self.model_fields_set:
            _dict['friendly_name'] = None

        # set to None if authenticator_attachment (nullable) is None
        # and model_fields_set contains the field
        if self.authenticator_attachment is None and "authenticator_attachment" in self.model_fields_set:
            _dict['authenticator_attachment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AuthenticateWebAuthnStage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "flow_set": [FlowSet.from_dict(_item) for _item in obj.get("flow_set")] if obj.get("flow_set") is not None else None,
            "configure_flow": obj.get("configure_flow"),
            "friendly_name": obj.get("friendly_name"),
            "user_verification": obj.get("user_verification"),
            "authenticator_attachment": obj.get("authenticator_attachment"),
            "resident_key_requirement": obj.get("resident_key_requirement")
        })
        return _obj


