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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Token(BaseModel):
    """
    Token
    """ # noqa: E501
    account: Optional[StrictStr] = None
    company: Optional[StrictStr] = None
    details_url: Optional[StrictStr] = None
    exp: Optional[StrictInt] = None
    iat: Optional[StrictInt] = None
    included_users: Optional[StrictInt] = None
    iss: Optional[StrictStr] = None
    jti: Optional[StrictStr] = None
    lexp: Optional[StrictInt] = None
    lic_exp_warn_days: Optional[StrictInt] = None
    lid: Optional[StrictStr] = None
    limit_by: Optional[StrictStr] = None
    max_concurrent_user_sessions: Optional[StrictInt] = None
    nbf: Optional[StrictInt] = None
    prod: Optional[List[StrictStr]] = None
    slug: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    sub: Optional[StrictStr] = None
    tok_exp_warn_days: Optional[StrictInt] = None
    trial: Optional[StrictBool] = None
    trial_exp: Optional[StrictInt] = None
    update_days: Optional[StrictInt] = None
    usage_billing: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["account", "company", "details_url", "exp", "iat", "included_users", "iss", "jti", "lexp", "lic_exp_warn_days", "lid", "limit_by", "max_concurrent_user_sessions", "nbf", "prod", "slug", "status", "sub", "tok_exp_warn_days", "trial", "trial_exp", "update_days", "usage_billing"]

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
        """Create an instance of Token from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Token from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "company": obj.get("company"),
            "details_url": obj.get("details_url"),
            "exp": obj.get("exp"),
            "iat": obj.get("iat"),
            "included_users": obj.get("included_users"),
            "iss": obj.get("iss"),
            "jti": obj.get("jti"),
            "lexp": obj.get("lexp"),
            "lic_exp_warn_days": obj.get("lic_exp_warn_days"),
            "lid": obj.get("lid"),
            "limit_by": obj.get("limit_by"),
            "max_concurrent_user_sessions": obj.get("max_concurrent_user_sessions"),
            "nbf": obj.get("nbf"),
            "prod": obj.get("prod"),
            "slug": obj.get("slug"),
            "status": obj.get("status"),
            "sub": obj.get("sub"),
            "tok_exp_warn_days": obj.get("tok_exp_warn_days"),
            "trial": obj.get("trial"),
            "trial_exp": obj.get("trial_exp"),
            "update_days": obj.get("update_days"),
            "usage_billing": obj.get("usage_billing")
        })
        return _obj


