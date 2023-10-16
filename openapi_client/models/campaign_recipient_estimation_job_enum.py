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





class CampaignRecipientEstimationJobEnum(str, Enum):
    """
    CampaignRecipientEstimationJobEnum
    """

    """
    allowed enum values
    """
    CAMPAIGN_MINUS_RECIPIENT_MINUS_ESTIMATION_MINUS_JOB = 'campaign-recipient-estimation-job'

    @classmethod
    def from_json(cls, json_str: str) -> CampaignRecipientEstimationJobEnum:
        """Create an instance of CampaignRecipientEstimationJobEnum from a JSON string"""
        return CampaignRecipientEstimationJobEnum(json.loads(json_str))


