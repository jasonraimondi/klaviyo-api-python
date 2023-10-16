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





class CatalogCategoryBulkUpdateJobEnum(str, Enum):
    """
    CatalogCategoryBulkUpdateJobEnum
    """

    """
    allowed enum values
    """
    CATALOG_MINUS_CATEGORY_MINUS_BULK_MINUS_UPDATE_MINUS_JOB = 'catalog-category-bulk-update-job'

    @classmethod
    def from_json(cls, json_str: str) -> CatalogCategoryBulkUpdateJobEnum:
        """Create an instance of CatalogCategoryBulkUpdateJobEnum from a JSON string"""
        return CatalogCategoryBulkUpdateJobEnum(json.loads(json_str))


