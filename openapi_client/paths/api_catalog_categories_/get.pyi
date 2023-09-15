# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
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

# Query params


class FieldsCatalogCategorySchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def EXTERNAL_ID(cls):
                return cls("external_id")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def UPDATED(cls):
                return cls("updated")

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldsCatalogCategorySchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
FilterSchema = schemas.StrSchema
PageCursorSchema = schemas.StrSchema


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CREATED(cls):
        return cls("created")
    
    @schemas.classproperty
    def CREATED(cls):
        return cls("-created")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'fields[catalog-category]': typing.Union[FieldsCatalogCategorySchema, list, tuple, ],
        'filter': typing.Union[FilterSchema, str, ],
        'page[cursor]': typing.Union[PageCursorSchema, str, ],
        'sort': typing.Union[SortSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_fields_catalog_category = api_client.QueryParameter(
    name="fields[catalog-category]",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsCatalogCategorySchema,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_page_cursor = api_client.QueryParameter(
    name="page[cursor]",
    style=api_client.ParameterStyle.FORM,
    schema=PageCursorSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        additional_properties = schemas.AnyTypeSchema
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


class SchemaFor4XXResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "errors",
        }
        
        class properties:
            
            
            class errors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "code",
                                "detail",
                                "id",
                                "title",
                            }
                            
                            class properties:
                                id = schemas.StrSchema
                                code = schemas.StrSchema
                                title = schemas.StrSchema
                                detail = schemas.StrSchema
                                
                                
                                class source(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            pointer = schemas.StrSchema
                                            parameter = schemas.StrSchema
                                            __annotations__ = {
                                                "pointer": pointer,
                                                "parameter": parameter,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["pointer"]) -> MetaOapg.properties.pointer: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["parameter"]) -> MetaOapg.properties.parameter: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pointer", "parameter", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["pointer"]) -> typing.Union[MetaOapg.properties.pointer, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["parameter"]) -> typing.Union[MetaOapg.properties.parameter, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pointer", "parameter", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        pointer: typing.Union[MetaOapg.properties.pointer, str, schemas.Unset] = schemas.unset,
                                        parameter: typing.Union[MetaOapg.properties.parameter, str, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'source':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            pointer=pointer,
                                            parameter=parameter,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "id": id,
                                    "code": code,
                                    "title": title,
                                    "detail": detail,
                                    "source": source,
                                }
                        
                        code: MetaOapg.properties.code
                        detail: MetaOapg.properties.detail
                        id: MetaOapg.properties.id
                        title: MetaOapg.properties.title
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "code", "title", "detail", "source", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "code", "title", "detail", "source", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            code: typing.Union[MetaOapg.properties.code, str, ],
                            detail: typing.Union[MetaOapg.properties.detail, str, ],
                            id: typing.Union[MetaOapg.properties.id, str, ],
                            title: typing.Union[MetaOapg.properties.title, str, ],
                            source: typing.Union[MetaOapg.properties.source, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                code=code,
                                detail=detail,
                                id=id,
                                title=title,
                                source=source,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'errors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "errors": errors,
            }
    
    errors: MetaOapg.properties.errors
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        errors: typing.Union[MetaOapg.properties.errors, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor4XXResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor4XX(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor4XXResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_4XX = api_client.OpenApiResponse(
    response_cls=ApiResponseFor4XX,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor4XXResponseBodyApplicationJson),
    },
)


class SchemaFor5XXResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "errors",
        }
        
        class properties:
            
            
            class errors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "code",
                                "detail",
                                "id",
                                "title",
                            }
                            
                            class properties:
                                id = schemas.StrSchema
                                code = schemas.StrSchema
                                title = schemas.StrSchema
                                detail = schemas.StrSchema
                                
                                
                                class source(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            pointer = schemas.StrSchema
                                            parameter = schemas.StrSchema
                                            __annotations__ = {
                                                "pointer": pointer,
                                                "parameter": parameter,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["pointer"]) -> MetaOapg.properties.pointer: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["parameter"]) -> MetaOapg.properties.parameter: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pointer", "parameter", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["pointer"]) -> typing.Union[MetaOapg.properties.pointer, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["parameter"]) -> typing.Union[MetaOapg.properties.parameter, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pointer", "parameter", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        pointer: typing.Union[MetaOapg.properties.pointer, str, schemas.Unset] = schemas.unset,
                                        parameter: typing.Union[MetaOapg.properties.parameter, str, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'source':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            pointer=pointer,
                                            parameter=parameter,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "id": id,
                                    "code": code,
                                    "title": title,
                                    "detail": detail,
                                    "source": source,
                                }
                        
                        code: MetaOapg.properties.code
                        detail: MetaOapg.properties.detail
                        id: MetaOapg.properties.id
                        title: MetaOapg.properties.title
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "code", "title", "detail", "source", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "code", "title", "detail", "source", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            code: typing.Union[MetaOapg.properties.code, str, ],
                            detail: typing.Union[MetaOapg.properties.detail, str, ],
                            id: typing.Union[MetaOapg.properties.id, str, ],
                            title: typing.Union[MetaOapg.properties.title, str, ],
                            source: typing.Union[MetaOapg.properties.source, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                code=code,
                                detail=detail,
                                id=id,
                                title=title,
                                source=source,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'errors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "errors": errors,
            }
    
    errors: MetaOapg.properties.errors
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        errors: typing.Union[MetaOapg.properties.errors, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor5XXResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor5XX(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor5XXResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_5XX = api_client.OpenApiResponse(
    response_cls=ApiResponseFor5XX,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor5XXResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_catalog_categories_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _get_catalog_categories_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_catalog_categories_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_catalog_categories_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Get Catalog Categories
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_fields_catalog_category,
            request_query_filter,
            request_query_page_cursor,
            request_query_sort,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GetCatalogCategories(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_catalog_categories(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get_catalog_categories(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_catalog_categories(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_catalog_categories(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_catalog_categories_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_catalog_categories_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


