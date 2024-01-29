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
from typing_extensions import Annotated
from authentikApiClient.models.digest_algorithm_enum import DigestAlgorithmEnum
from authentikApiClient.models.signature_algorithm_enum import SignatureAlgorithmEnum
from authentikApiClient.models.sp_binding_enum import SpBindingEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PatchedSAMLProviderRequest(BaseModel):
    """
    SAMLProvider Serializer
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow used for authentication when the associated application is accessed by an un-authenticated user.")
    authorization_flow: Optional[StrictStr] = Field(default=None, description="Flow used when authorizing this provider.")
    property_mappings: Optional[List[StrictStr]] = None
    acs_url: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=200)]] = None
    audience: Optional[StrictStr] = Field(default=None, description="Value of the audience restriction field of the assertion. When left empty, no audience restriction will be added.")
    issuer: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Also known as EntityID")
    assertion_valid_not_before: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Assertion valid not before current time + this value (Format: hours=-1;minutes=-2;seconds=-3).")
    assertion_valid_not_on_or_after: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Assertion not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    session_valid_not_on_or_after: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Session not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    name_id_mapping: Optional[StrictStr] = Field(default=None, description="Configure how the NameID value will be created. When left empty, the NameIDPolicy of the incoming request will be considered")
    digest_algorithm: Optional[DigestAlgorithmEnum] = None
    signature_algorithm: Optional[SignatureAlgorithmEnum] = None
    signing_kp: Optional[StrictStr] = Field(default=None, description="Keypair used to sign outgoing Responses going to the Service Provider.")
    verification_kp: Optional[StrictStr] = Field(default=None, description="When selected, incoming assertion's Signatures will be validated against this certificate. To allow unsigned Requests, leave on default.")
    sp_binding: Optional[SpBindingEnum] = None
    __properties: ClassVar[List[str]] = ["name", "authentication_flow", "authorization_flow", "property_mappings", "acs_url", "audience", "issuer", "assertion_valid_not_before", "assertion_valid_not_on_or_after", "session_valid_not_on_or_after", "name_id_mapping", "digest_algorithm", "signature_algorithm", "signing_kp", "verification_kp", "sp_binding"]

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
        """Create an instance of PatchedSAMLProviderRequest from a JSON string"""
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

        # set to None if name_id_mapping (nullable) is None
        # and model_fields_set contains the field
        if self.name_id_mapping is None and "name_id_mapping" in self.model_fields_set:
            _dict['name_id_mapping'] = None

        # set to None if signing_kp (nullable) is None
        # and model_fields_set contains the field
        if self.signing_kp is None and "signing_kp" in self.model_fields_set:
            _dict['signing_kp'] = None

        # set to None if verification_kp (nullable) is None
        # and model_fields_set contains the field
        if self.verification_kp is None and "verification_kp" in self.model_fields_set:
            _dict['verification_kp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PatchedSAMLProviderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "authentication_flow": obj.get("authentication_flow"),
            "authorization_flow": obj.get("authorization_flow"),
            "property_mappings": obj.get("property_mappings"),
            "acs_url": obj.get("acs_url"),
            "audience": obj.get("audience"),
            "issuer": obj.get("issuer"),
            "assertion_valid_not_before": obj.get("assertion_valid_not_before"),
            "assertion_valid_not_on_or_after": obj.get("assertion_valid_not_on_or_after"),
            "session_valid_not_on_or_after": obj.get("session_valid_not_on_or_after"),
            "name_id_mapping": obj.get("name_id_mapping"),
            "digest_algorithm": obj.get("digest_algorithm"),
            "signature_algorithm": obj.get("signature_algorithm"),
            "signing_kp": obj.get("signing_kp"),
            "verification_kp": obj.get("verification_kp"),
            "sp_binding": obj.get("sp_binding")
        })
        return _obj


