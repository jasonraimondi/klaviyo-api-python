# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-07-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ProfileSuppressionBulkCreateJobEnum(str, Enum):
    """
    ProfileSuppressionBulkCreateJobEnum
    """

    """
    allowed enum values
    """
    PROFILE_MINUS_SUPPRESSION_MINUS_BULK_MINUS_CREATE_MINUS_JOB = 'profile-suppression-bulk-create-job'

    @classmethod
    def from_json(cls, json_str: str) -> ProfileSuppressionBulkCreateJobEnum:
        """Create an instance of ProfileSuppressionBulkCreateJobEnum from a JSON string"""
        return ProfileSuppressionBulkCreateJobEnum(json.loads(json_str))


