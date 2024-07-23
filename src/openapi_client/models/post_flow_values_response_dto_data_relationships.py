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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_flow_action_response_compound_document_data_all_of_relationships_flow_messages import GetFlowActionResponseCompoundDocumentDataAllOfRelationshipsFlowMessages
from openapi_client.models.post_tag_response_data_relationships_flows import PostTagResponseDataRelationshipsFlows
from typing import Optional, Set
from typing_extensions import Self

class PostFlowValuesResponseDTODataRelationships(BaseModel):
    """
    PostFlowValuesResponseDTODataRelationships
    """ # noqa: E501
    flows: Optional[PostTagResponseDataRelationshipsFlows] = None
    flow_messages: Optional[GetFlowActionResponseCompoundDocumentDataAllOfRelationshipsFlowMessages] = Field(default=None, alias="flow-messages")
    __properties: ClassVar[List[str]] = ["flows", "flow-messages"]

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
        """Create an instance of PostFlowValuesResponseDTODataRelationships from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of flows
        if self.flows:
            _dict['flows'] = self.flows.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flow_messages
        if self.flow_messages:
            _dict['flow-messages'] = self.flow_messages.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostFlowValuesResponseDTODataRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "flows": PostTagResponseDataRelationshipsFlows.from_dict(obj["flows"]) if obj.get("flows") is not None else None,
            "flow-messages": GetFlowActionResponseCompoundDocumentDataAllOfRelationshipsFlowMessages.from_dict(obj["flow-messages"]) if obj.get("flow-messages") is not None else None
        })
        return _obj


