# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ProfileSubscriptionBulkCreateJobEnum(str, Enum):
    """
    ProfileSubscriptionBulkCreateJobEnum
    """

    """
    allowed enum values
    """
    PROFILE_MINUS_SUBSCRIPTION_MINUS_BULK_MINUS_CREATE_MINUS_JOB = 'profile-subscription-bulk-create-job'

    @classmethod
    def from_json(cls, json_str: str) -> ProfileSubscriptionBulkCreateJobEnum:
        """Create an instance of ProfileSubscriptionBulkCreateJobEnum from a JSON string"""
        return ProfileSubscriptionBulkCreateJobEnum(json.loads(json_str))


