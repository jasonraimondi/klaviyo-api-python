# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-02-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator

class CatalogItemCreateQueryResourceObjectAttributes(BaseModel):
    """
    CatalogItemCreateQueryResourceObjectAttributes
    """
    external_id: Optional[StrictStr] = Field(..., description="The ID of the catalog item in an external system.")
    integration_type: Optional[StrictStr] = Field('$custom', description="The integration type. Currently only \"$custom\" is supported.")
    title: Optional[StrictStr] = Field(..., description="The title of the catalog item.")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="This field can be used to set the price on the catalog item, which is what gets displayed for the item when included in emails. For most price-update use cases, you will also want to update the `price` on any child variants, using the [Update Catalog Variant Endpoint](https://developers.klaviyo.com/en/reference/update_catalog_variant).")
    catalog_type: Optional[StrictStr] = Field('$default', description="The type of catalog. Currently only \"$default\" is supported.")
    description: Optional[StrictStr] = Field(..., description="A description of the catalog item.")
    url: Optional[StrictStr] = Field(..., description="URL pointing to the location of the catalog item on your website.")
    image_full_url: Optional[StrictStr] = Field(None, description="URL pointing to the location of a full image of the catalog item.")
    image_thumbnail_url: Optional[StrictStr] = Field(None, description="URL pointing to the location of an image thumbnail of the catalog item")
    images: Optional[conlist(StrictStr)] = Field(None, description="List of URLs pointing to the locations of images of the catalog item.")
    custom_metadata: Optional[Dict[str, Any]] = Field(None, description="Flat JSON blob to provide custom metadata about the catalog item. May not exceed 100kb.")
    published: Optional[StrictBool] = Field(True, description="Boolean value indicating whether the catalog item is published.")
    __properties = ["external_id", "integration_type", "title", "price", "catalog_type", "description", "url", "image_full_url", "image_thumbnail_url", "images", "custom_metadata", "published"]

    @validator('integration_type')
    def integration_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('$custom'):
            raise ValueError("must be one of enum values ('$custom')")
        return value

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
    def from_json(cls, json_str: str) -> CatalogItemCreateQueryResourceObjectAttributes:
        """Create an instance of CatalogItemCreateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if external_id (nullable) is None
        # and __fields_set__ contains the field
        if self.external_id is None and "external_id" in self.__fields_set__:
            _dict['external_id'] = None

        # set to None if integration_type (nullable) is None
        # and __fields_set__ contains the field
        if self.integration_type is None and "integration_type" in self.__fields_set__:
            _dict['integration_type'] = None

        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        # set to None if catalog_type (nullable) is None
        # and __fields_set__ contains the field
        if self.catalog_type is None and "catalog_type" in self.__fields_set__:
            _dict['catalog_type'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if image_full_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_full_url is None and "image_full_url" in self.__fields_set__:
            _dict['image_full_url'] = None

        # set to None if image_thumbnail_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_thumbnail_url is None and "image_thumbnail_url" in self.__fields_set__:
            _dict['image_thumbnail_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CatalogItemCreateQueryResourceObjectAttributes:
        """Create an instance of CatalogItemCreateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CatalogItemCreateQueryResourceObjectAttributes.parse_obj(obj)

        _obj = CatalogItemCreateQueryResourceObjectAttributes.parse_obj({
            "external_id": obj.get("external_id"),
            "integration_type": obj.get("integration_type") if obj.get("integration_type") is not None else '$custom',
            "title": obj.get("title"),
            "price": obj.get("price"),
            "catalog_type": obj.get("catalog_type") if obj.get("catalog_type") is not None else '$default',
            "description": obj.get("description"),
            "url": obj.get("url"),
            "image_full_url": obj.get("image_full_url"),
            "image_thumbnail_url": obj.get("image_thumbnail_url"),
            "images": obj.get("images"),
            "custom_metadata": obj.get("custom_metadata"),
            "published": obj.get("published") if obj.get("published") is not None else True
        })
        return _obj

