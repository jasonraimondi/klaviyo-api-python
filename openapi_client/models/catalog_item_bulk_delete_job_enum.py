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





class CatalogItemBulkDeleteJobEnum(str, Enum):
    """
    CatalogItemBulkDeleteJobEnum
    """

    """
    allowed enum values
    """
    CATALOG_MINUS_ITEM_MINUS_BULK_MINUS_DELETE_MINUS_JOB = 'catalog-item-bulk-delete-job'

    @classmethod
    def from_json(cls, json_str: str) -> CatalogItemBulkDeleteJobEnum:
        """Create an instance of CatalogItemBulkDeleteJobEnum from a JSON string"""
        return CatalogItemBulkDeleteJobEnum(json.loads(json_str))

