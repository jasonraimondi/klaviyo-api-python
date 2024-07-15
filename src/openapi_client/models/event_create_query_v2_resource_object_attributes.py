# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-07-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.event_create_query_v2_resource_object_attributes_metric import EventCreateQueryV2ResourceObjectAttributesMetric
from openapi_client.models.event_create_query_v2_resource_object_attributes_profile import EventCreateQueryV2ResourceObjectAttributesProfile
from typing import Optional, Set
from typing_extensions import Self

class EventCreateQueryV2ResourceObjectAttributes(BaseModel):
    """
    EventCreateQueryV2ResourceObjectAttributes
    """ # noqa: E501
    properties: Dict[str, Any] = Field(description="Properties of this event. Any top level property (that are not objects) can be used to create segments. The $extra property is a special property. This records any non-segmentable values that can be referenced later. For example, HTML templates are useful on a segment but are not used to create a segment. There are limits placed onto the size of the data present. This must not exceed 5 MB. This must not exceed 300 event properties. A single string cannot be larger than 100 KB. Each array must not exceed 4000 elements. The properties cannot contain more than 10 nested levels.")
    time: Optional[datetime] = Field(default=None, description="When this event occurred. By default, the time the request was received will be used. The time is truncated to the second. The time must be after the year 2000 and can only be up to 1 year in the future.")
    value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A numeric, monetary value to associate with this event. For example, the dollar amount of a purchase.")
    value_currency: Optional[StrictStr] = Field(default=None, description="The ISO 4217 currency code of the value associated with the event.")
    unique_id: Optional[StrictStr] = Field(default=None, description="A unique identifier for an event. If the unique_id is repeated for the same profile and metric, only the first processed event will be recorded. If this is not present, this will use the time to the second. Using the default, this limits only one event per profile per second.")
    metric: EventCreateQueryV2ResourceObjectAttributesMetric
    profile: EventCreateQueryV2ResourceObjectAttributesProfile
    __properties: ClassVar[List[str]] = ["properties", "time", "value", "value_currency", "unique_id", "metric", "profile"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EventCreateQueryV2ResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict['metric'] = self.metric.to_dict()
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        # set to None if time (nullable) is None
        # and model_fields_set contains the field
        if self.time is None and "time" in self.model_fields_set:
            _dict['time'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if value_currency (nullable) is None
        # and model_fields_set contains the field
        if self.value_currency is None and "value_currency" in self.model_fields_set:
            _dict['value_currency'] = None

        # set to None if unique_id (nullable) is None
        # and model_fields_set contains the field
        if self.unique_id is None and "unique_id" in self.model_fields_set:
            _dict['unique_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventCreateQueryV2ResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "properties": obj.get("properties"),
            "time": obj.get("time"),
            "value": obj.get("value"),
            "value_currency": obj.get("value_currency"),
            "unique_id": obj.get("unique_id"),
            "metric": EventCreateQueryV2ResourceObjectAttributesMetric.from_dict(obj["metric"]) if obj.get("metric") is not None else None,
            "profile": EventCreateQueryV2ResourceObjectAttributesProfile.from_dict(obj["profile"]) if obj.get("profile") is not None else None
        })
        return _obj


