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
from authentikApiClient.models.binding_type_enum import BindingTypeEnum
from authentikApiClient.models.digest_algorithm_enum import DigestAlgorithmEnum
from authentikApiClient.models.name_id_policy_enum import NameIdPolicyEnum
from authentikApiClient.models.policy_engine_mode import PolicyEngineMode
from authentikApiClient.models.signature_algorithm_enum import SignatureAlgorithmEnum
from authentikApiClient.models.user_matching_mode_enum import UserMatchingModeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PatchedSAMLSourceRequest(BaseModel):
    """
    SAMLSource Serializer
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Source's display Name.")
    slug: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=50)]] = Field(default=None, description="Internal source name, used in URLs.")
    enabled: Optional[StrictBool] = None
    authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow to use when authenticating existing users.")
    enrollment_flow: Optional[StrictStr] = Field(default=None, description="Flow to use when enrolling new users.")
    policy_engine_mode: Optional[PolicyEngineMode] = None
    user_matching_mode: Optional[UserMatchingModeEnum] = None
    user_path_template: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    pre_authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow used before authentication.")
    issuer: Optional[StrictStr] = Field(default=None, description="Also known as Entity ID. Defaults the Metadata URL.")
    sso_url: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = Field(default=None, description="URL that the initial Login request is sent to.")
    slo_url: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="Optional URL if your IDP supports Single-Logout.")
    allow_idp_initiated: Optional[StrictBool] = Field(default=None, description="Allows authentication flows initiated by the IdP. This can be a security risk, as no validation of the request ID is done.")
    name_id_policy: Optional[NameIdPolicyEnum] = None
    binding_type: Optional[BindingTypeEnum] = None
    signing_kp: Optional[StrictStr] = Field(default=None, description="Keypair which is used to sign outgoing requests. Leave empty to disable signing.")
    digest_algorithm: Optional[DigestAlgorithmEnum] = None
    signature_algorithm: Optional[SignatureAlgorithmEnum] = None
    temporary_user_delete_after: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Time offset when temporary users should be deleted. This only applies if your IDP uses the NameID Format 'transient', and the user doesn't log out manually. (Format: hours=1;minutes=2;seconds=3).")
    __properties: ClassVar[List[str]] = ["name", "slug", "enabled", "authentication_flow", "enrollment_flow", "policy_engine_mode", "user_matching_mode", "user_path_template", "pre_authentication_flow", "issuer", "sso_url", "slo_url", "allow_idp_initiated", "name_id_policy", "binding_type", "signing_kp", "digest_algorithm", "signature_algorithm", "temporary_user_delete_after"]

    @field_validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of PatchedSAMLSourceRequest from a JSON string"""
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
        # set to None if authentication_flow (nullable) is None
        # and model_fields_set contains the field
        if self.authentication_flow is None and "authentication_flow" in self.model_fields_set:
            _dict['authentication_flow'] = None

        # set to None if enrollment_flow (nullable) is None
        # and model_fields_set contains the field
        if self.enrollment_flow is None and "enrollment_flow" in self.model_fields_set:
            _dict['enrollment_flow'] = None

        # set to None if slo_url (nullable) is None
        # and model_fields_set contains the field
        if self.slo_url is None and "slo_url" in self.model_fields_set:
            _dict['slo_url'] = None

        # set to None if signing_kp (nullable) is None
        # and model_fields_set contains the field
        if self.signing_kp is None and "signing_kp" in self.model_fields_set:
            _dict['signing_kp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PatchedSAMLSourceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "enabled": obj.get("enabled"),
            "authentication_flow": obj.get("authentication_flow"),
            "enrollment_flow": obj.get("enrollment_flow"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "user_matching_mode": obj.get("user_matching_mode"),
            "user_path_template": obj.get("user_path_template"),
            "pre_authentication_flow": obj.get("pre_authentication_flow"),
            "issuer": obj.get("issuer"),
            "sso_url": obj.get("sso_url"),
            "slo_url": obj.get("slo_url"),
            "allow_idp_initiated": obj.get("allow_idp_initiated"),
            "name_id_policy": obj.get("name_id_policy"),
            "binding_type": obj.get("binding_type"),
            "signing_kp": obj.get("signing_kp"),
            "digest_algorithm": obj.get("digest_algorithm"),
            "signature_algorithm": obj.get("signature_algorithm"),
            "temporary_user_delete_after": obj.get("temporary_user_delete_after")
        })
        return _obj


