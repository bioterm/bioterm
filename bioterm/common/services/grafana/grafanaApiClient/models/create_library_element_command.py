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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateLibraryElementCommand(BaseModel):
    """
    CreateLibraryElementCommand is the command for adding a LibraryElement
    """ # noqa: E501
    folder_id: Optional[StrictInt] = Field(default=None, description="ID of the folder where the library element is stored.  Deprecated: use FolderUID instead", alias="folderId")
    folder_uid: Optional[StrictStr] = Field(default=None, description="UID of the folder where the library element is stored.", alias="folderUid")
    kind: Optional[StrictInt] = Field(default=None, description="Kind of element to create, Use 1 for library panels or 2 for c. Description: 1 - library panels 2 - library variables")
    model: Optional[Union[str, Any]] = Field(default=None, description="The JSON model for the library element.")
    name: Optional[StrictStr] = Field(default=None, description="Name of the library element.")
    uid: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["folderId", "folderUid", "kind", "model", "name", "uid"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (1, 2):
            raise ValueError("must be one of enum values (1, 2)")
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
        """Create an instance of CreateLibraryElementCommand from a JSON string"""
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
        """Create an instance of CreateLibraryElementCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "folderId": obj.get("folderId"),
            "folderUid": obj.get("folderUid"),
            "kind": obj.get("kind"),
            "model": obj.get("model"),
            "name": obj.get("name"),
            "uid": obj.get("uid")
        })
        return _obj


