# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-12-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from openapi_client.models.catalog_category_delete_query_resource_object import CatalogCategoryDeleteQueryResourceObject

class CatalogCategoryDeleteJobCreateQueryResourceObjectAttributesCategories(BaseModel):
    """
    Array of catalog categories to delete.  # noqa: E501
    """
    data: conlist(CatalogCategoryDeleteQueryResourceObject) = Field(...)
    __properties = ["data"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CatalogCategoryDeleteJobCreateQueryResourceObjectAttributesCategories:
        """Create an instance of CatalogCategoryDeleteJobCreateQueryResourceObjectAttributesCategories from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CatalogCategoryDeleteJobCreateQueryResourceObjectAttributesCategories:
        """Create an instance of CatalogCategoryDeleteJobCreateQueryResourceObjectAttributesCategories from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CatalogCategoryDeleteJobCreateQueryResourceObjectAttributesCategories.parse_obj(obj)

        _obj = CatalogCategoryDeleteJobCreateQueryResourceObjectAttributesCategories.parse_obj({
            "data": [CatalogCategoryDeleteQueryResourceObject.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None
        })
        return _obj


