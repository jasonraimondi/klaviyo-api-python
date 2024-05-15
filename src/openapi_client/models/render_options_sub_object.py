# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2024-05-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RenderOptionsSubObject(BaseModel):
    """
    RenderOptionsSubObject
    """ # noqa: E501
    shorten_links: Optional[StrictBool] = True
    add_org_prefix: Optional[StrictBool] = True
    add_info_link: Optional[StrictBool] = True
    add_opt_out_language: Optional[StrictBool] = False
    __properties: ClassVar[List[str]] = ["shorten_links", "add_org_prefix", "add_info_link", "add_opt_out_language"]

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
        """Create an instance of RenderOptionsSubObject from a JSON string"""
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
        # set to None if shorten_links (nullable) is None
        # and model_fields_set contains the field
        if self.shorten_links is None and "shorten_links" in self.model_fields_set:
            _dict['shorten_links'] = None

        # set to None if add_org_prefix (nullable) is None
        # and model_fields_set contains the field
        if self.add_org_prefix is None and "add_org_prefix" in self.model_fields_set:
            _dict['add_org_prefix'] = None

        # set to None if add_info_link (nullable) is None
        # and model_fields_set contains the field
        if self.add_info_link is None and "add_info_link" in self.model_fields_set:
            _dict['add_info_link'] = None

        # set to None if add_opt_out_language (nullable) is None
        # and model_fields_set contains the field
        if self.add_opt_out_language is None and "add_opt_out_language" in self.model_fields_set:
            _dict['add_opt_out_language'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RenderOptionsSubObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shorten_links": obj.get("shorten_links") if obj.get("shorten_links") is not None else True,
            "add_org_prefix": obj.get("add_org_prefix") if obj.get("add_org_prefix") is not None else True,
            "add_info_link": obj.get("add_info_link") if obj.get("add_info_link") is not None else True,
            "add_opt_out_language": obj.get("add_opt_out_language") if obj.get("add_opt_out_language") is not None else False
        })
        return _obj


