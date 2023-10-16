# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.image_enum import ImageEnum
from openapi_client.models.image_partial_update_query_resource_object_attributes import ImagePartialUpdateQueryResourceObjectAttributes

class ImagePartialUpdateQueryResourceObject(BaseModel):
    """
    ImagePartialUpdateQueryResourceObject
    """
    type: ImageEnum = Field(...)
    id: StrictStr = Field(..., description="The ID of the image")
    attributes: ImagePartialUpdateQueryResourceObjectAttributes = Field(...)
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
    def from_json(cls, json_str: str) -> ImagePartialUpdateQueryResourceObject:
        """Create an instance of ImagePartialUpdateQueryResourceObject from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ImagePartialUpdateQueryResourceObject:
        """Create an instance of ImagePartialUpdateQueryResourceObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ImagePartialUpdateQueryResourceObject.parse_obj(obj)

        _obj = ImagePartialUpdateQueryResourceObject.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "attributes": ImagePartialUpdateQueryResourceObjectAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None
        })
        return _obj


