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


class CatalogVariantCreateJobCreateQueryResourceObject(
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
            def type() -> typing.Type['CatalogVariantBulkCreateJobEnum']:
                return CatalogVariantBulkCreateJobEnum
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "variants",
                    }
                    
                    class properties:
                        
                        
                        class variants(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                required = {
                                    "data",
                                }
                                
                                class properties:
                                    
                                    
                                    class data(
                                        schemas.ListSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            
                                            @staticmethod
                                            def items() -> typing.Type['CatalogVariantCreateQueryResourceObject']:
                                                return CatalogVariantCreateQueryResourceObject
                                    
                                        def __new__(
                                            cls,
                                            _arg: typing.Union[typing.Tuple['CatalogVariantCreateQueryResourceObject'], typing.List['CatalogVariantCreateQueryResourceObject']],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                        ) -> 'data':
                                            return super().__new__(
                                                cls,
                                                _arg,
                                                _configuration=_configuration,
                                            )
                                    
                                        def __getitem__(self, i: int) -> 'CatalogVariantCreateQueryResourceObject':
                                            return super().__getitem__(i)
                                    __annotations__ = {
                                        "data": data,
                                    }
                            
                            data: MetaOapg.properties.data
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                data: typing.Union[MetaOapg.properties.data, list, tuple, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'variants':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    data=data,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "variants": variants,
                        }
                
                variants: MetaOapg.properties.variants
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["variants"]) -> MetaOapg.properties.variants: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["variants", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["variants"]) -> MetaOapg.properties.variants: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["variants", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    variants: typing.Union[MetaOapg.properties.variants, dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        variants=variants,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "attributes": attributes,
            }
    
    attributes: MetaOapg.properties.attributes
    type: 'CatalogVariantBulkCreateJobEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'CatalogVariantBulkCreateJobEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'CatalogVariantBulkCreateJobEnum': ...
    
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
        type: 'CatalogVariantBulkCreateJobEnum',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CatalogVariantCreateJobCreateQueryResourceObject':
        return super().__new__(
            cls,
            *_args,
            attributes=attributes,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.catalog_variant_bulk_create_job_enum import CatalogVariantBulkCreateJobEnum
from openapi_client.model.catalog_variant_create_query_resource_object import CatalogVariantCreateQueryResourceObject
