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
from authentikApiClient.models.challenge_choices import ChallengeChoices
from authentikApiClient.models.contextual_flow_info import ContextualFlowInfo
from authentikApiClient.models.error_detail import ErrorDetail
from authentikApiClient.models.permission import Permission
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConsentChallenge(BaseModel):
    """
    Challenge info for consent screens
    """ # noqa: E501
    type: ChallengeChoices
    flow_info: Optional[ContextualFlowInfo] = None
    component: Optional[StrictStr] = 'ak-stage-consent'
    response_errors: Optional[Dict[str, List[ErrorDetail]]] = None
    pending_user: StrictStr
    pending_user_avatar: StrictStr
    header_text: Optional[StrictStr] = None
    permissions: List[Permission]
    additional_permissions: List[Permission]
    token: StrictStr
    __properties: ClassVar[List[str]] = ["type", "flow_info", "component", "response_errors", "pending_user", "pending_user_avatar", "header_text", "permissions", "additional_permissions", "token"]

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
        """Create an instance of ConsentChallenge from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of flow_info
        if self.flow_info:
            _dict['flow_info'] = self.flow_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in response_errors (dict of array)
        _field_dict_of_array = {}
        if self.response_errors:
            for _key in self.response_errors:
                if self.response_errors[_key] is not None:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.response_errors[_key]
                    ]
            _dict['response_errors'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item in self.permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_permissions (list)
        _items = []
        if self.additional_permissions:
            for _item in self.additional_permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additional_permissions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConsentChallenge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "flow_info": ContextualFlowInfo.from_dict(obj.get("flow_info")) if obj.get("flow_info") is not None else None,
            "component": obj.get("component") if obj.get("component") is not None else 'ak-stage-consent',
            "response_errors": dict(
                (_k,
                        [ErrorDetail.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("response_errors").items()
            ),
            "pending_user": obj.get("pending_user"),
            "pending_user_avatar": obj.get("pending_user_avatar"),
            "header_text": obj.get("header_text"),
            "permissions": [Permission.from_dict(_item) for _item in obj.get("permissions")] if obj.get("permissions") is not None else None,
            "additional_permissions": [Permission.from_dict(_item) for _item in obj.get("additional_permissions")] if obj.get("additional_permissions") is not None else None,
            "token": obj.get("token")
        })
        return _obj

