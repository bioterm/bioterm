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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PasswordPolicy(BaseModel):
    """
    Password Policy Serializer
    """ # noqa: E501
    pk: StrictStr
    name: StrictStr
    execution_logging: Optional[StrictBool] = Field(default=None, description="When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.")
    component: StrictStr = Field(description="Get object component so that we know how to edit the object")
    verbose_name: StrictStr = Field(description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(description="Return internal model name")
    bound_to: StrictInt = Field(description="Return objects policy is bound to")
    password_field: Optional[StrictStr] = Field(default=None, description="Field key to check, field keys defined in Prompt stages are available.")
    amount_digits: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    amount_uppercase: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    amount_lowercase: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    amount_symbols: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    length_min: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    symbol_charset: Optional[StrictStr] = None
    error_message: Optional[StrictStr] = None
    check_static_rules: Optional[StrictBool] = None
    check_have_i_been_pwned: Optional[StrictBool] = None
    check_zxcvbn: Optional[StrictBool] = None
    hibp_allowed_count: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(default=None, description="How many times the password hash is allowed to be on haveibeenpwned")
    zxcvbn_score_threshold: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(default=None, description="If the zxcvbn score is equal or less than this value, the policy will fail.")
    __properties: ClassVar[List[str]] = ["pk", "name", "execution_logging", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "bound_to", "password_field", "amount_digits", "amount_uppercase", "amount_lowercase", "amount_symbols", "length_min", "symbol_charset", "error_message", "check_static_rules", "check_have_i_been_pwned", "check_zxcvbn", "hibp_allowed_count", "zxcvbn_score_threshold"]

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
        """Create an instance of PasswordPolicy from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "pk",
                "component",
                "verbose_name",
                "verbose_name_plural",
                "meta_model_name",
                "bound_to",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PasswordPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "execution_logging": obj.get("execution_logging"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "bound_to": obj.get("bound_to"),
            "password_field": obj.get("password_field"),
            "amount_digits": obj.get("amount_digits"),
            "amount_uppercase": obj.get("amount_uppercase"),
            "amount_lowercase": obj.get("amount_lowercase"),
            "amount_symbols": obj.get("amount_symbols"),
            "length_min": obj.get("length_min"),
            "symbol_charset": obj.get("symbol_charset"),
            "error_message": obj.get("error_message"),
            "check_static_rules": obj.get("check_static_rules"),
            "check_have_i_been_pwned": obj.get("check_have_i_been_pwned"),
            "check_zxcvbn": obj.get("check_zxcvbn"),
            "hibp_allowed_count": obj.get("hibp_allowed_count"),
            "zxcvbn_score_threshold": obj.get("zxcvbn_score_threshold")
        })
        return _obj


