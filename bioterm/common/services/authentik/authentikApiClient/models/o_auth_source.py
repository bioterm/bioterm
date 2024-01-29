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
from authentikApiClient.models.policy_engine_mode import PolicyEngineMode
from authentikApiClient.models.provider_type_enum import ProviderTypeEnum
from authentikApiClient.models.source_type import SourceType
from authentikApiClient.models.user_matching_mode_enum import UserMatchingModeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OAuthSource(BaseModel):
    """
    OAuth Source Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr = Field(description="Source's display Name.")
    slug: Annotated[str, Field(strict=True, max_length=50)] = Field(description="Internal source name, used in URLs.")
    enabled: Optional[StrictBool] = None
    authentication_flow: Optional[StrictStr] = Field(default=None, description="Flow to use when authenticating existing users.")
    enrollment_flow: Optional[StrictStr] = Field(default=None, description="Flow to use when enrolling new users.")
    component: StrictStr = Field(description="Get object component so that we know how to edit the object")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    policy_engine_mode: Optional[PolicyEngineMode] = None
    user_matching_mode: Optional[UserMatchingModeEnum] = None
    managed: Optional[StrictStr] = Field(description="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.")
    user_path_template: Optional[StrictStr] = None
    icon: Optional[StrictStr] = Field(description="Get the URL to the Icon. If the name is /static or starts with http it is returned as-is")
    provider_type: ProviderTypeEnum
    request_token_url: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="URL used to request the initial token. This URL is only required for OAuth 1.")
    authorization_url: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="URL the user is redirect to to conest the flow.")
    access_token_url: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="URL used by authentik to retrieve tokens.")
    profile_url: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="URL used by authentik to get user information.")
    consumer_key: StrictStr
    callback_url: StrictStr = Field(description="Get OAuth Callback URL")
    additional_scopes: Optional[StrictStr] = None
    type: SourceType
    oidc_well_known_url: Optional[StrictStr] = None
    oidc_jwks_url: Optional[StrictStr] = None
    oidc_jwks: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["pk", "name", "slug", "enabled", "authentication_flow", "enrollment_flow", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "policy_engine_mode", "user_matching_mode", "managed", "user_path_template", "icon", "provider_type", "request_token_url", "authorization_url", "access_token_url", "profile_url", "consumer_key", "callback_url", "additional_scopes", "type", "oidc_well_known_url", "oidc_jwks_url", "oidc_jwks"]

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
        """Create an instance of OAuthSource from a JSON string"""
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
                "managed",
                "icon",
                "callback_url",
                "type",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # set to None if authentication_flow (nullable) is None
        # and model_fields_set contains the field
        if self.authentication_flow is None and "authentication_flow" in self.model_fields_set:
            _dict['authentication_flow'] = None

        # set to None if enrollment_flow (nullable) is None
        # and model_fields_set contains the field
        if self.enrollment_flow is None and "enrollment_flow" in self.model_fields_set:
            _dict['enrollment_flow'] = None

        # set to None if managed (nullable) is None
        # and model_fields_set contains the field
        if self.managed is None and "managed" in self.model_fields_set:
            _dict['managed'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if request_token_url (nullable) is None
        # and model_fields_set contains the field
        if self.request_token_url is None and "request_token_url" in self.model_fields_set:
            _dict['request_token_url'] = None

        # set to None if authorization_url (nullable) is None
        # and model_fields_set contains the field
        if self.authorization_url is None and "authorization_url" in self.model_fields_set:
            _dict['authorization_url'] = None

        # set to None if access_token_url (nullable) is None
        # and model_fields_set contains the field
        if self.access_token_url is None and "access_token_url" in self.model_fields_set:
            _dict['access_token_url'] = None

        # set to None if profile_url (nullable) is None
        # and model_fields_set contains the field
        if self.profile_url is None and "profile_url" in self.model_fields_set:
            _dict['profile_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OAuthSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "enabled": obj.get("enabled"),
            "authentication_flow": obj.get("authentication_flow"),
            "enrollment_flow": obj.get("enrollment_flow"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "user_matching_mode": obj.get("user_matching_mode"),
            "managed": obj.get("managed"),
            "user_path_template": obj.get("user_path_template"),
            "icon": obj.get("icon"),
            "provider_type": obj.get("provider_type"),
            "request_token_url": obj.get("request_token_url"),
            "authorization_url": obj.get("authorization_url"),
            "access_token_url": obj.get("access_token_url"),
            "profile_url": obj.get("profile_url"),
            "consumer_key": obj.get("consumer_key"),
            "callback_url": obj.get("callback_url"),
            "additional_scopes": obj.get("additional_scopes"),
            "type": SourceType.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "oidc_well_known_url": obj.get("oidc_well_known_url"),
            "oidc_jwks_url": obj.get("oidc_jwks_url"),
            "oidc_jwks": obj.get("oidc_jwks")
        })
        return _obj

