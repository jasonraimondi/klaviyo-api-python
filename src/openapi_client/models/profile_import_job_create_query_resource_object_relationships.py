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


from typing import Optional
from pydantic import BaseModel
from openapi_client.models.profile_import_job_create_query_resource_object_relationships_lists import ProfileImportJobCreateQueryResourceObjectRelationshipsLists

class ProfileImportJobCreateQueryResourceObjectRelationships(BaseModel):
    """
    ProfileImportJobCreateQueryResourceObjectRelationships
    """
    lists: Optional[ProfileImportJobCreateQueryResourceObjectRelationshipsLists] = None
    __properties = ["lists"]

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
    def from_json(cls, json_str: str) -> ProfileImportJobCreateQueryResourceObjectRelationships:
        """Create an instance of ProfileImportJobCreateQueryResourceObjectRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of lists
        if self.lists:
            _dict['lists'] = self.lists.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProfileImportJobCreateQueryResourceObjectRelationships:
        """Create an instance of ProfileImportJobCreateQueryResourceObjectRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProfileImportJobCreateQueryResourceObjectRelationships.parse_obj(obj)

        _obj = ProfileImportJobCreateQueryResourceObjectRelationships.parse_obj({
            "lists": ProfileImportJobCreateQueryResourceObjectRelationshipsLists.from_dict(obj.get("lists")) if obj.get("lists") is not None else None
        })
        return _obj

