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
from pydantic import BaseModel, StrictBool

class RenderOptionsSubObject(BaseModel):
    """
    RenderOptionsSubObject
    """
    shorten_links: Optional[StrictBool] = True
    add_org_prefix: Optional[StrictBool] = True
    add_info_link: Optional[StrictBool] = True
    add_opt_out_language: Optional[StrictBool] = False
    __properties = ["shorten_links", "add_org_prefix", "add_info_link", "add_opt_out_language"]

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
    def from_json(cls, json_str: str) -> RenderOptionsSubObject:
        """Create an instance of RenderOptionsSubObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RenderOptionsSubObject:
        """Create an instance of RenderOptionsSubObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RenderOptionsSubObject.parse_obj(obj)

        _obj = RenderOptionsSubObject.parse_obj({
            "shorten_links": obj.get("shorten_links") if obj.get("shorten_links") is not None else True,
            "add_org_prefix": obj.get("add_org_prefix") if obj.get("add_org_prefix") is not None else True,
            "add_info_link": obj.get("add_info_link") if obj.get("add_info_link") is not None else True,
            "add_opt_out_language": obj.get("add_opt_out_language") if obj.get("add_opt_out_language") is not None else False
        })
        return _obj

