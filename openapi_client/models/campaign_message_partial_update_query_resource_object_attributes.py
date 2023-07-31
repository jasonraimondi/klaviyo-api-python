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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.render_options_sub_object import RenderOptionsSubObject

class CampaignMessagePartialUpdateQueryResourceObjectAttributes(BaseModel):
    """
    CampaignMessagePartialUpdateQueryResourceObjectAttributes
    """
    label: Optional[StrictStr] = Field(None, description="The label or name on the message")
    content: Optional[Dict[str, Any]] = Field(None, description="Additional attributes relating to the content of the message")
    render_options: Optional[RenderOptionsSubObject] = None
    __properties = ["label", "content", "render_options"]

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
    def from_json(cls, json_str: str) -> CampaignMessagePartialUpdateQueryResourceObjectAttributes:
        """Create an instance of CampaignMessagePartialUpdateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of render_options
        if self.render_options:
            _dict['render_options'] = self.render_options.to_dict()
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignMessagePartialUpdateQueryResourceObjectAttributes:
        """Create an instance of CampaignMessagePartialUpdateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignMessagePartialUpdateQueryResourceObjectAttributes.parse_obj(obj)

        _obj = CampaignMessagePartialUpdateQueryResourceObjectAttributes.parse_obj({
            "label": obj.get("label"),
            "content": obj.get("content"),
            "render_options": RenderOptionsSubObject.from_dict(obj.get("render_options")) if obj.get("render_options") is not None else None
        })
        return _obj

