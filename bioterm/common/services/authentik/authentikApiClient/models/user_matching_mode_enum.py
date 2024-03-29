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


class UserMatchingModeEnum(str, Enum):
    """
    * `identifier` - Use the source-specific identifier * `email_link` - Link to a user with identical email address. Can have security implications when a source doesn't validate email addresses. * `email_deny` - Use the user's email address, but deny enrollment when the email address already exists. * `username_link` - Link to a user with identical username. Can have security implications when a username is used with another source. * `username_deny` - Use the user's username, but deny enrollment when the username already exists.
    """

    """
    allowed enum values
    """
    IDENTIFIER = 'identifier'
    EMAIL_LINK = 'email_link'
    EMAIL_DENY = 'email_deny'
    USERNAME_LINK = 'username_link'
    USERNAME_DENY = 'username_deny'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserMatchingModeEnum from a JSON string"""
        return cls(json.loads(json_str))


