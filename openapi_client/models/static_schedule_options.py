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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool

class StaticScheduleOptions(BaseModel):
    """
    StaticScheduleOptions
    """
    datetime: datetime = Field(..., description="The time to send at")
    is_local: Optional[StrictBool] = Field(None, description="If the campaign should be sent with local recipient timezone send (requires UTC time) or statically sent at the given time. Defaults to False.")
    send_past_recipients_immediately: Optional[StrictBool] = Field(None, description="Determines if we should send to local recipient timezone if the given time has passed. Only applicable to local sends. Defaults to False.")
    __properties = ["datetime", "is_local", "send_past_recipients_immediately"]

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
    def from_json(cls, json_str: str) -> StaticScheduleOptions:
        """Create an instance of StaticScheduleOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StaticScheduleOptions:
        """Create an instance of StaticScheduleOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StaticScheduleOptions.parse_obj(obj)

        _obj = StaticScheduleOptions.parse_obj({
            "datetime": obj.get("datetime"),
            "is_local": obj.get("is_local"),
            "send_past_recipients_immediately": obj.get("send_past_recipients_immediately")
        })
        return _obj

