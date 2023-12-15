# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-12-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CatalogCategoryBulkCreateJobEnum(str, Enum):
    """
    CatalogCategoryBulkCreateJobEnum
    """

    """
    allowed enum values
    """
    CATALOG_MINUS_CATEGORY_MINUS_BULK_MINUS_CREATE_MINUS_JOB = 'catalog-category-bulk-create-job'

    @classmethod
    def from_json(cls, json_str: str) -> CatalogCategoryBulkCreateJobEnum:
        """Create an instance of CatalogCategoryBulkCreateJobEnum from a JSON string"""
        return CatalogCategoryBulkCreateJobEnum(json.loads(json_str))


