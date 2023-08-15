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



from pydantic import BaseModel, Field
from openapi_client.models.template_update_query_resource_object import TemplateUpdateQueryResourceObject

class TemplateUpdateQuery(BaseModel):
    """
    TemplateUpdateQuery
    """
    data: TemplateUpdateQueryResourceObject = Field(...)
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
    def from_json(cls, json_str: str) -> TemplateUpdateQuery:
        """Create an instance of TemplateUpdateQuery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TemplateUpdateQuery:
        """Create an instance of TemplateUpdateQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TemplateUpdateQuery.parse_obj(obj)

        _obj = TemplateUpdateQuery.parse_obj({
            "data": TemplateUpdateQueryResourceObject.from_dict(obj.get("data")) if obj.get("data") is not None else None
        })
        return _obj

