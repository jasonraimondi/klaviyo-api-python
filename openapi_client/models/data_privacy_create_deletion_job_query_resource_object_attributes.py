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
from openapi_client.models.data_privacy_create_deletion_job_query_resource_object_attributes_profile import DataPrivacyCreateDeletionJobQueryResourceObjectAttributesProfile

class DataPrivacyCreateDeletionJobQueryResourceObjectAttributes(BaseModel):
    """
    DataPrivacyCreateDeletionJobQueryResourceObjectAttributes
    """
    profile: DataPrivacyCreateDeletionJobQueryResourceObjectAttributesProfile = Field(...)
    __properties = ["profile"]

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
    def from_json(cls, json_str: str) -> DataPrivacyCreateDeletionJobQueryResourceObjectAttributes:
        """Create an instance of DataPrivacyCreateDeletionJobQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataPrivacyCreateDeletionJobQueryResourceObjectAttributes:
        """Create an instance of DataPrivacyCreateDeletionJobQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataPrivacyCreateDeletionJobQueryResourceObjectAttributes.parse_obj(obj)

        _obj = DataPrivacyCreateDeletionJobQueryResourceObjectAttributes.parse_obj({
            "profile": DataPrivacyCreateDeletionJobQueryResourceObjectAttributesProfile.from_dict(obj.get("profile")) if obj.get("profile") is not None else None
        })
        return _obj

