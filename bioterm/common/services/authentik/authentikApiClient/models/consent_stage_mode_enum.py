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
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ConsentStageModeEnum(str, Enum):
    """
    * `always_require` - Always Require * `permanent` - Permanent * `expiring` - Expiring
    """

    """
    allowed enum values
    """
    ALWAYS_REQUIRE = 'always_require'
    PERMANENT = 'permanent'
    EXPIRING = 'expiring'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConsentStageModeEnum from a JSON string"""
        return cls(json.loads(json_str))


