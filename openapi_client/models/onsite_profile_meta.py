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


from typing import Optional
from pydantic import BaseModel
from openapi_client.models.profile_meta_patch_properties import ProfileMetaPatchProperties

class OnsiteProfileMeta(BaseModel):
    """
    OnsiteProfileMeta
    """
    patch_properties: Optional[ProfileMetaPatchProperties] = None
    __properties = ["patch_properties"]

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
    def from_json(cls, json_str: str) -> OnsiteProfileMeta:
        """Create an instance of OnsiteProfileMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of patch_properties
        if self.patch_properties:
            _dict['patch_properties'] = self.patch_properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OnsiteProfileMeta:
        """Create an instance of OnsiteProfileMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OnsiteProfileMeta.parse_obj(obj)

        _obj = OnsiteProfileMeta.parse_obj({
            "patch_properties": ProfileMetaPatchProperties.from_dict(obj.get("patch_properties")) if obj.get("patch_properties") is not None else None
        })
        return _obj


