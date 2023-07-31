# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-07-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.catalog_variant_enum import CatalogVariantEnum
from openapi_client.models.catalog_variant_update_query_resource_object_attributes import CatalogVariantUpdateQueryResourceObjectAttributes

class CatalogVariantUpdateQueryResourceObject(BaseModel):
    """
    CatalogVariantUpdateQueryResourceObject
    """
    type: CatalogVariantEnum = Field(...)
    id: StrictStr = Field(..., description="The catalog variant ID is a compound ID (string), with format: `{integration}:::{catalog}:::{external_id}`. Currently, the only supported integration type is `$custom`, and the only supported catalog is `$default`.")
    attributes: CatalogVariantUpdateQueryResourceObjectAttributes = Field(...)
    __properties = ["type", "id", "attributes"]

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
    def from_json(cls, json_str: str) -> CatalogVariantUpdateQueryResourceObject:
        """Create an instance of CatalogVariantUpdateQueryResourceObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CatalogVariantUpdateQueryResourceObject:
        """Create an instance of CatalogVariantUpdateQueryResourceObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CatalogVariantUpdateQueryResourceObject.parse_obj(obj)

        _obj = CatalogVariantUpdateQueryResourceObject.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "attributes": CatalogVariantUpdateQueryResourceObjectAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None
        })
        return _obj

