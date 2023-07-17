"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-07-15
    Contact: developers@klaviyo.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_client.exceptions import ApiAttributeError



class MetricAggregateQueryResourceObjectAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('measurements',): {
            'COUNT': "count",
            'SUM_VALUE': "sum_value",
            'UNIQUE': "unique",
        },
        ('sort',): {
            'None': None,
            '$ATTRIBUTED_CHANNEL': "$attributed_channel",
            '-$ATTRIBUTED_CHANNEL': "-$attributed_channel",
            '$ATTRIBUTED_FLOW': "$attributed_flow",
            '-$ATTRIBUTED_FLOW': "-$attributed_flow",
            '$ATTRIBUTED_MESSAGE': "$attributed_message",
            '-$ATTRIBUTED_MESSAGE': "-$attributed_message",
            '$ATTRIBUTED_VARIATION': "$attributed_variation",
            '-$ATTRIBUTED_VARIATION': "-$attributed_variation",
            '$CAMPAIGN_CHANNEL': "$campaign_channel",
            '-$CAMPAIGN_CHANNEL': "-$campaign_channel",
            '$FLOW': "$flow",
            '-$FLOW': "-$flow",
            '$FLOW_CHANNEL': "$flow_channel",
            '-$FLOW_CHANNEL': "-$flow_channel",
            '$MESSAGE': "$message",
            '-$MESSAGE': "-$message",
            '$MESSAGE_SEND_COHORT': "$message_send_cohort",
            '-$MESSAGE_SEND_COHORT': "-$message_send_cohort",
            '$VARIATION': "$variation",
            '-$VARIATION': "-$variation",
            '$VARIATION_SEND_COHORT': "$variation_send_cohort",
            '-$VARIATION_SEND_COHORT': "-$variation_send_cohort",
            'BOUNCE_TYPE': "Bounce Type",
            '-BOUNCE_TYPE': "-Bounce Type",
            'CAMPAIGN_NAME': "Campaign Name",
            '-CAMPAIGN_NAME': "-Campaign Name",
            'CLIENT_CANONICAL': "Client Canonical",
            '-CLIENT_CANONICAL': "-Client Canonical",
            'CLIENT_NAME': "Client Name",
            '-CLIENT_NAME': "-Client Name",
            'CLIENT_TYPE': "Client Type",
            '-CLIENT_TYPE': "-Client Type",
            'EMAIL_DOMAIN': "Email Domain",
            '-EMAIL_DOMAIN': "-Email Domain",
            'FAILURE_SOURCE': "Failure Source",
            '-FAILURE_SOURCE': "-Failure Source",
            'FAILURE_TYPE': "Failure Type",
            '-FAILURE_TYPE': "-Failure Type",
            'FROM_NUMBER': "From Number",
            '-FROM_NUMBER': "-From Number",
            'FROM_PHONE_REGION': "From Phone Region",
            '-FROM_PHONE_REGION': "-From Phone Region",
            'LIST': "List",
            '-LIST': "-List",
            'MESSAGE_NAME': "Message Name",
            '-MESSAGE_NAME': "-Message Name",
            'MESSAGE_TYPE': "Message Type",
            '-MESSAGE_TYPE': "-Message Type",
            'METHOD': "Method",
            '-METHOD': "-Method",
            'SUBJECT': "Subject",
            '-SUBJECT': "-Subject",
            'TO_NUMBER': "To Number",
            '-TO_NUMBER': "-To Number",
            'TO_PHONE_REGION': "To Phone Region",
            '-TO_PHONE_REGION': "-To Phone Region",
            'URL': "URL",
            '-URL': "-URL",
            'COUNT': "count",
            '-COUNT': "-count",
            'FORM_ID': "form_id",
            '-FORM_ID': "-form_id",
            'SUM_VALUE': "sum_value",
            '-SUM_VALUE': "-sum_value",
            'UNIQUE': "unique",
            '-UNIQUE': "-unique",
        },
        ('interval',): {
            'None': None,
            'DAY': "day",
            'HOUR': "hour",
            'MONTH': "month",
            'WEEK': "week",
        },
        ('by',): {
            '$ATTRIBUTED_CHANNEL': "$attributed_channel",
            '$ATTRIBUTED_FLOW': "$attributed_flow",
            '$ATTRIBUTED_MESSAGE': "$attributed_message",
            '$ATTRIBUTED_VARIATION': "$attributed_variation",
            '$CAMPAIGN_CHANNEL': "$campaign_channel",
            '$FLOW': "$flow",
            '$FLOW_CHANNEL': "$flow_channel",
            '$MESSAGE': "$message",
            '$MESSAGE_SEND_COHORT': "$message_send_cohort",
            '$VARIATION': "$variation",
            '$VARIATION_SEND_COHORT': "$variation_send_cohort",
            'BOUNCE_TYPE': "Bounce Type",
            'CAMPAIGN_NAME': "Campaign Name",
            'CLIENT_CANONICAL': "Client Canonical",
            'CLIENT_NAME': "Client Name",
            'CLIENT_TYPE': "Client Type",
            'EMAIL_DOMAIN': "Email Domain",
            'FAILURE_SOURCE': "Failure Source",
            'FAILURE_TYPE': "Failure Type",
            'FROM_NUMBER': "From Number",
            'FROM_PHONE_REGION': "From Phone Region",
            'LIST': "List",
            'MESSAGE_NAME': "Message Name",
            'MESSAGE_TYPE': "Message Type",
            'METHOD': "Method",
            'SUBJECT': "Subject",
            'TO_NUMBER': "To Number",
            'TO_PHONE_REGION': "To Phone Region",
            'URL': "URL",
            'FORM_ID': "form_id",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'metric_id': (str, none_type,),  # noqa: E501
            'measurements': ([str],),  # noqa: E501
            'filter': ([str],),  # noqa: E501
            'sort': (str, none_type,),  # noqa: E501
            'page_cursor': (str, none_type,),  # noqa: E501
            'interval': (str, none_type,),  # noqa: E501
            'return_fields': ([str],),  # noqa: E501
            'page_size': (int,),  # noqa: E501
            'timezone': (str, none_type,),  # noqa: E501
            'by': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'metric_id': 'metric_id',  # noqa: E501
        'measurements': 'measurements',  # noqa: E501
        'filter': 'filter',  # noqa: E501
        'sort': 'sort',  # noqa: E501
        'page_cursor': 'page_cursor',  # noqa: E501
        'interval': 'interval',  # noqa: E501
        'return_fields': 'return_fields',  # noqa: E501
        'page_size': 'page_size',  # noqa: E501
        'timezone': 'timezone',  # noqa: E501
        'by': 'by',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, metric_id, measurements, filter, *args, **kwargs):  # noqa: E501
        """MetricAggregateQueryResourceObjectAttributes - a model defined in OpenAPI

        Args:
            metric_id (str, none_type): The metric ID used in the aggregation.
            measurements ([str]): Measurement key, e.g. `unique`, `sum_value`, `count`
            filter ([str]): List of filters, must include time range using ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm).             These filters follow a similar format to those in `GET` requests, the primary difference is that this endpoint asks for a list.             The time range can be filtered by providing a `greater-or-equal` and a `less-than` filter on the `datetime` field.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            sort (str, none_type): Provide a sort key (e.g. -$message). [optional]  # noqa: E501
            page_cursor (str, none_type): Optional pagination cursor to iterate over large result sets. [optional]  # noqa: E501
            interval (str, none_type): Aggregation interval, e.g. \"hour\", \"day\", \"week\", \"month\". [optional] if omitted the server will use the default value of "day"  # noqa: E501
            return_fields ([str]): Provide fields to limit the returned data. [optional]  # noqa: E501
            page_size (int): Alter the maximum number of returned rows in a single page of aggregation results. [optional] if omitted the server will use the default value of 500  # noqa: E501
            timezone (str, none_type): The timezone used for processing the query, e.g. `'America/New_York'`.             This field is validated against a list of common timezones from the [IANA Time Zone Database](https://www.iana.org/time-zones).             While most are supported, a few notable exceptions are `Factory`, `Europe/Kyiv` and `Pacific/Kanton`. This field is case-sensitive.. [optional] if omitted the server will use the default value of "UTC"  # noqa: E501
            by ([str]): Optional attribute(s) used for partitioning by the aggregation function. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.metric_id = metric_id
        self.measurements = measurements
        self.filter = filter
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, metric_id, measurements, filter, *args, **kwargs):  # noqa: E501
        """MetricAggregateQueryResourceObjectAttributes - a model defined in OpenAPI

        Args:
            metric_id (str, none_type): The metric ID used in the aggregation.
            measurements ([str]): Measurement key, e.g. `unique`, `sum_value`, `count`
            filter ([str]): List of filters, must include time range using ISO 8601 format (YYYY-MM-DDTHH:MM:SS.mmmmmm).             These filters follow a similar format to those in `GET` requests, the primary difference is that this endpoint asks for a list.             The time range can be filtered by providing a `greater-or-equal` and a `less-than` filter on the `datetime` field.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            sort (str, none_type): Provide a sort key (e.g. -$message). [optional]  # noqa: E501
            page_cursor (str, none_type): Optional pagination cursor to iterate over large result sets. [optional]  # noqa: E501
            interval (str, none_type): Aggregation interval, e.g. \"hour\", \"day\", \"week\", \"month\". [optional] if omitted the server will use the default value of "day"  # noqa: E501
            return_fields ([str]): Provide fields to limit the returned data. [optional]  # noqa: E501
            page_size (int): Alter the maximum number of returned rows in a single page of aggregation results. [optional] if omitted the server will use the default value of 500  # noqa: E501
            timezone (str, none_type): The timezone used for processing the query, e.g. `'America/New_York'`.             This field is validated against a list of common timezones from the [IANA Time Zone Database](https://www.iana.org/time-zones).             While most are supported, a few notable exceptions are `Factory`, `Europe/Kyiv` and `Pacific/Kanton`. This field is case-sensitive.. [optional] if omitted the server will use the default value of "UTC"  # noqa: E501
            by ([str]): Optional attribute(s) used for partitioning by the aggregation function. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.metric_id = metric_id
        self.measurements = measurements
        self.filter = filter
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
