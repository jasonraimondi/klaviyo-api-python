# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-08-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TagEnum(str, Enum):
    """
    TagEnum
    """

    """
    allowed enum values
    """
    TAG = 'tag'

    @classmethod
    def from_json(cls, json_str: str) -> TagEnum:
        """Create an instance of TagEnum from a JSON string"""
        return TagEnum(json.loads(json_str))


