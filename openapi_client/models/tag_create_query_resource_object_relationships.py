# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-08-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field
from openapi_client.models.tag_create_query_resource_object_relationships_tag_group import TagCreateQueryResourceObjectRelationshipsTagGroup

class TagCreateQueryResourceObjectRelationships(BaseModel):
    """
    TagCreateQueryResourceObjectRelationships
    """
    tag_group: Optional[TagCreateQueryResourceObjectRelationshipsTagGroup] = Field(None, alias="tag-group")
    __properties = ["tag-group"]

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
    def from_json(cls, json_str: str) -> TagCreateQueryResourceObjectRelationships:
        """Create an instance of TagCreateQueryResourceObjectRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of tag_group
        if self.tag_group:
            _dict['tag-group'] = self.tag_group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TagCreateQueryResourceObjectRelationships:
        """Create an instance of TagCreateQueryResourceObjectRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TagCreateQueryResourceObjectRelationships.parse_obj(obj)

        _obj = TagCreateQueryResourceObjectRelationships.parse_obj({
            "tag_group": TagCreateQueryResourceObjectRelationshipsTagGroup.from_dict(obj.get("tag-group")) if obj.get("tag-group") is not None else None
        })
        return _obj

