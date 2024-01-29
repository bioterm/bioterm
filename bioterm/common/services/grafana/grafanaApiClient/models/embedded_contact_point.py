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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EmbeddedContactPoint(BaseModel):
    """
    EmbeddedContactPoint is the contact point type that is used by grafanas embedded alertmanager implementation.
    """ # noqa: E501
    disable_resolve_message: Optional[StrictBool] = Field(default=None, alias="disableResolveMessage")
    name: Optional[StrictStr] = Field(default=None, description="Name is used as grouping key in the UI. Contact points with the same name will be grouped in the UI.")
    provenance: Optional[StrictStr] = None
    settings: Union[str, Any]
    type: StrictStr
    uid: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=40)]] = Field(default=None, description="UID is the unique identifier of the contact point. The UID can be set by the user.")
    __properties: ClassVar[List[str]] = ["disableResolveMessage", "name", "provenance", "settings", "type", "uid"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('alertmanager', ' dingding', ' discord', ' email', ' googlechat', ' kafka', ' line', ' opsgenie', ' pagerduty', ' pushover', ' sensugo', ' slack', ' teams', ' telegram', ' threema', ' victorops', ' webhook', ' wecom'):
            raise ValueError("must be one of enum values ('alertmanager', ' dingding', ' discord', ' email', ' googlechat', ' kafka', ' line', ' opsgenie', ' pagerduty', ' pushover', ' sensugo', ' slack', ' teams', ' telegram', ' threema', ' victorops', ' webhook', ' wecom')")
        return value

    @field_validator('uid')
    def uid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\-\_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-\_]+$/")
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
        """Create an instance of EmbeddedContactPoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "provenance",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EmbeddedContactPoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "disableResolveMessage": obj.get("disableResolveMessage"),
            "name": obj.get("name"),
            "provenance": obj.get("provenance"),
            "settings": obj.get("settings"),
            "type": obj.get("type"),
            "uid": obj.get("uid")
        })
        return _obj

