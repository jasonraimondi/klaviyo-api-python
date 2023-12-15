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



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.catalog_item_enum import CatalogItemEnum

class CatalogItemDeleteQueryResourceObject(BaseModel):
    """
    CatalogItemDeleteQueryResourceObject
    """
    type: CatalogItemEnum = Field(...)
    id: StrictStr = Field(..., description="The catalog item ID is a compound ID (string), with format: `{integration}:::{catalog}:::{external_id}`. Currently, the only supported integration type is `$custom`, and the only supported catalog is `$default`.")
    __properties = ["type", "id"]

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
    def from_json(cls, json_str: str) -> CatalogItemDeleteQueryResourceObject:
        """Create an instance of CatalogItemDeleteQueryResourceObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CatalogItemDeleteQueryResourceObject:
        """Create an instance of CatalogItemDeleteQueryResourceObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CatalogItemDeleteQueryResourceObject.parse_obj(obj)

        _obj = CatalogItemDeleteQueryResourceObject.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id")
        })
        return _obj


