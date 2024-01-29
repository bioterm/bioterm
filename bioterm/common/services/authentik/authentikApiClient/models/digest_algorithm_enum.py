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


class DigestAlgorithmEnum(str, Enum):
    """
    * `http://www.w3.org/2000/09/xmldsig#sha1` - SHA1 * `http://www.w3.org/2001/04/xmlenc#sha256` - SHA256 * `http://www.w3.org/2001/04/xmldsig-more#sha384` - SHA384 * `http://www.w3.org/2001/04/xmlenc#sha512` - SHA512
    """

    """
    allowed enum values
    """
    HTTP_COLON_SLASH_SLASH_WWW_DOT_W3_DOT_ORG_SLASH_2000_SLASH_09_SLASH_XMLDSIG_HASH_SHA1 = 'http://www.w3.org/2000/09/xmldsig#sha1'
    HTTP_COLON_SLASH_SLASH_WWW_DOT_W3_DOT_ORG_SLASH_2001_SLASH_04_SLASH_XMLENC_HASH_SHA256 = 'http://www.w3.org/2001/04/xmlenc#sha256'
    HTTP_COLON_SLASH_SLASH_WWW_DOT_W3_DOT_ORG_SLASH_2001_SLASH_04_SLASH_XMLDSIG_MINUS_MORE_HASH_SHA384 = 'http://www.w3.org/2001/04/xmldsig-more#sha384'
    HTTP_COLON_SLASH_SLASH_WWW_DOT_W3_DOT_ORG_SLASH_2001_SLASH_04_SLASH_XMLENC_HASH_SHA512 = 'http://www.w3.org/2001/04/xmlenc#sha512'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DigestAlgorithmEnum from a JSON string"""
        return cls(json.loads(json_str))

