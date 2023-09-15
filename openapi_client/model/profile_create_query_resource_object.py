# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-09-15
    Contact: developers@klaviyo.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ProfileCreateQueryResourceObject(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "attributes",
            "type",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['ProfileEnum']:
                return ProfileEnum
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class email(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'email':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class phone_number(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'phone_number':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class external_id(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'external_id':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class first_name(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'first_name':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class last_name(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last_name':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class organization(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'organization':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class title(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'title':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class image(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'image':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                    
                        @staticmethod
                        def location() -> typing.Type['ProfileLocation']:
                            return ProfileLocation
                        properties = schemas.DictSchema
                        __annotations__ = {
                            "email": email,
                            "phone_number": phone_number,
                            "external_id": external_id,
                            "first_name": first_name,
                            "last_name": last_name,
                            "organization": organization,
                            "title": title,
                            "image": image,
                            "location": location,
                            "properties": properties,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["organization"]) -> MetaOapg.properties.organization: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["location"]) -> 'ProfileLocation': ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "phone_number", "external_id", "first_name", "last_name", "organization", "title", "image", "location", "properties", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> typing.Union[MetaOapg.properties.organization, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union['ProfileLocation', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union[MetaOapg.properties.properties, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "phone_number", "external_id", "first_name", "last_name", "organization", "title", "image", "location", "properties", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
                    phone_number: typing.Union[MetaOapg.properties.phone_number, None, str, schemas.Unset] = schemas.unset,
                    external_id: typing.Union[MetaOapg.properties.external_id, None, str, schemas.Unset] = schemas.unset,
                    first_name: typing.Union[MetaOapg.properties.first_name, None, str, schemas.Unset] = schemas.unset,
                    last_name: typing.Union[MetaOapg.properties.last_name, None, str, schemas.Unset] = schemas.unset,
                    organization: typing.Union[MetaOapg.properties.organization, None, str, schemas.Unset] = schemas.unset,
                    title: typing.Union[MetaOapg.properties.title, None, str, schemas.Unset] = schemas.unset,
                    image: typing.Union[MetaOapg.properties.image, None, str, schemas.Unset] = schemas.unset,
                    location: typing.Union['ProfileLocation', schemas.Unset] = schemas.unset,
                    properties: typing.Union[MetaOapg.properties.properties, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        email=email,
                        phone_number=phone_number,
                        external_id=external_id,
                        first_name=first_name,
                        last_name=last_name,
                        organization=organization,
                        title=title,
                        image=image,
                        location=location,
                        properties=properties,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "attributes": attributes,
            }
    
    attributes: MetaOapg.properties.attributes
    type: 'ProfileEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ProfileEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'ProfileEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, ],
        type: 'ProfileEnum',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProfileCreateQueryResourceObject':
        return super().__new__(
            cls,
            *_args,
            attributes=attributes,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.profile_enum import ProfileEnum
from openapi_client.model.profile_location import ProfileLocation
