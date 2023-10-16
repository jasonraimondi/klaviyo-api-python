# coding: utf-8

# flake8: noqa

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "6.0.0"

# import apis into sdk package
from openapi_client.api.accounts_api import AccountsApi
from openapi_client.api.campaigns_api import CampaignsApi
from openapi_client.api.catalogs_api import CatalogsApi
from openapi_client.api.coupons_api import CouponsApi
from openapi_client.api.data_privacy_api import DataPrivacyApi
from openapi_client.api.events_api import EventsApi
from openapi_client.api.flows_api import FlowsApi
from openapi_client.api.images_api import ImagesApi
from openapi_client.api.lists_api import ListsApi
from openapi_client.api.metrics_api import MetricsApi
from openapi_client.api.profiles_api import ProfilesApi
from openapi_client.api.segments_api import SegmentsApi
from openapi_client.api.tags_api import TagsApi
from openapi_client.api.templates_api import TemplatesApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.audiences_sub_object import AudiencesSubObject
from openapi_client.models.back_in_stock_subscription_enum import BackInStockSubscriptionEnum
from openapi_client.models.campaign_clone_query import CampaignCloneQuery
from openapi_client.models.campaign_clone_query_resource_object import CampaignCloneQueryResourceObject
from openapi_client.models.campaign_clone_query_resource_object_attributes import CampaignCloneQueryResourceObjectAttributes
from openapi_client.models.campaign_create_query import CampaignCreateQuery
from openapi_client.models.campaign_create_query_resource_object import CampaignCreateQueryResourceObject
from openapi_client.models.campaign_create_query_resource_object_attributes import CampaignCreateQueryResourceObjectAttributes
from openapi_client.models.campaign_create_query_resource_object_attributes_campaign_messages import CampaignCreateQueryResourceObjectAttributesCampaignMessages
from openapi_client.models.campaign_enum import CampaignEnum
from openapi_client.models.campaign_message_assign_template_query import CampaignMessageAssignTemplateQuery
from openapi_client.models.campaign_message_assign_template_query_resource_object import CampaignMessageAssignTemplateQueryResourceObject
from openapi_client.models.campaign_message_assign_template_query_resource_object_relationships import CampaignMessageAssignTemplateQueryResourceObjectRelationships
from openapi_client.models.campaign_message_assign_template_query_resource_object_relationships_template import CampaignMessageAssignTemplateQueryResourceObjectRelationshipsTemplate
from openapi_client.models.campaign_message_assign_template_query_resource_object_relationships_template_data import CampaignMessageAssignTemplateQueryResourceObjectRelationshipsTemplateData
from openapi_client.models.campaign_message_create_query_resource_object import CampaignMessageCreateQueryResourceObject
from openapi_client.models.campaign_message_create_query_resource_object_attributes import CampaignMessageCreateQueryResourceObjectAttributes
from openapi_client.models.campaign_message_enum import CampaignMessageEnum
from openapi_client.models.campaign_message_partial_update_query import CampaignMessagePartialUpdateQuery
from openapi_client.models.campaign_message_partial_update_query_resource_object import CampaignMessagePartialUpdateQueryResourceObject
from openapi_client.models.campaign_message_partial_update_query_resource_object_attributes import CampaignMessagePartialUpdateQueryResourceObjectAttributes
from openapi_client.models.campaign_partial_update_query import CampaignPartialUpdateQuery
from openapi_client.models.campaign_partial_update_query_resource_object import CampaignPartialUpdateQueryResourceObject
from openapi_client.models.campaign_partial_update_query_resource_object_attributes import CampaignPartialUpdateQueryResourceObjectAttributes
from openapi_client.models.campaign_recipient_estimation_job_create_query import CampaignRecipientEstimationJobCreateQuery
from openapi_client.models.campaign_recipient_estimation_job_create_query_resource_object import CampaignRecipientEstimationJobCreateQueryResourceObject
from openapi_client.models.campaign_recipient_estimation_job_enum import CampaignRecipientEstimationJobEnum
from openapi_client.models.campaign_send_job_create_query import CampaignSendJobCreateQuery
from openapi_client.models.campaign_send_job_create_query_resource_object import CampaignSendJobCreateQueryResourceObject
from openapi_client.models.campaign_send_job_enum import CampaignSendJobEnum
from openapi_client.models.campaign_send_job_partial_update_query import CampaignSendJobPartialUpdateQuery
from openapi_client.models.campaign_send_job_partial_update_query_resource_object import CampaignSendJobPartialUpdateQueryResourceObject
from openapi_client.models.campaign_send_job_partial_update_query_resource_object_attributes import CampaignSendJobPartialUpdateQueryResourceObjectAttributes
from openapi_client.models.catalog_category_bulk_create_job_enum import CatalogCategoryBulkCreateJobEnum
from openapi_client.models.catalog_category_bulk_delete_job_enum import CatalogCategoryBulkDeleteJobEnum
from openapi_client.models.catalog_category_bulk_update_job_enum import CatalogCategoryBulkUpdateJobEnum
from openapi_client.models.catalog_category_create_job_create_query import CatalogCategoryCreateJobCreateQuery
from openapi_client.models.catalog_category_create_job_create_query_resource_object import CatalogCategoryCreateJobCreateQueryResourceObject
from openapi_client.models.catalog_category_create_job_create_query_resource_object_attributes import CatalogCategoryCreateJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_category_create_job_create_query_resource_object_attributes_categories import CatalogCategoryCreateJobCreateQueryResourceObjectAttributesCategories
from openapi_client.models.catalog_category_create_query import CatalogCategoryCreateQuery
from openapi_client.models.catalog_category_create_query_resource_object import CatalogCategoryCreateQueryResourceObject
from openapi_client.models.catalog_category_create_query_resource_object_attributes import CatalogCategoryCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_category_create_query_resource_object_relationships import CatalogCategoryCreateQueryResourceObjectRelationships
from openapi_client.models.catalog_category_create_query_resource_object_relationships_items import CatalogCategoryCreateQueryResourceObjectRelationshipsItems
from openapi_client.models.catalog_category_create_query_resource_object_relationships_items_data_inner import CatalogCategoryCreateQueryResourceObjectRelationshipsItemsDataInner
from openapi_client.models.catalog_category_delete_job_create_query import CatalogCategoryDeleteJobCreateQuery
from openapi_client.models.catalog_category_delete_job_create_query_resource_object import CatalogCategoryDeleteJobCreateQueryResourceObject
from openapi_client.models.catalog_category_delete_job_create_query_resource_object_attributes import CatalogCategoryDeleteJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_category_delete_job_create_query_resource_object_attributes_categories import CatalogCategoryDeleteJobCreateQueryResourceObjectAttributesCategories
from openapi_client.models.catalog_category_delete_query_resource_object import CatalogCategoryDeleteQueryResourceObject
from openapi_client.models.catalog_category_enum import CatalogCategoryEnum
from openapi_client.models.catalog_category_item_op import CatalogCategoryItemOp
from openapi_client.models.catalog_category_update_job_create_query import CatalogCategoryUpdateJobCreateQuery
from openapi_client.models.catalog_category_update_job_create_query_resource_object import CatalogCategoryUpdateJobCreateQueryResourceObject
from openapi_client.models.catalog_category_update_job_create_query_resource_object_attributes import CatalogCategoryUpdateJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_category_update_job_create_query_resource_object_attributes_categories import CatalogCategoryUpdateJobCreateQueryResourceObjectAttributesCategories
from openapi_client.models.catalog_category_update_query import CatalogCategoryUpdateQuery
from openapi_client.models.catalog_category_update_query_resource_object import CatalogCategoryUpdateQueryResourceObject
from openapi_client.models.catalog_category_update_query_resource_object_attributes import CatalogCategoryUpdateQueryResourceObjectAttributes
from openapi_client.models.catalog_item_bulk_create_job_enum import CatalogItemBulkCreateJobEnum
from openapi_client.models.catalog_item_bulk_delete_job_enum import CatalogItemBulkDeleteJobEnum
from openapi_client.models.catalog_item_bulk_update_job_enum import CatalogItemBulkUpdateJobEnum
from openapi_client.models.catalog_item_category_op import CatalogItemCategoryOp
from openapi_client.models.catalog_item_create_job_create_query import CatalogItemCreateJobCreateQuery
from openapi_client.models.catalog_item_create_job_create_query_resource_object import CatalogItemCreateJobCreateQueryResourceObject
from openapi_client.models.catalog_item_create_job_create_query_resource_object_attributes import CatalogItemCreateJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_item_create_job_create_query_resource_object_attributes_items import CatalogItemCreateJobCreateQueryResourceObjectAttributesItems
from openapi_client.models.catalog_item_create_query import CatalogItemCreateQuery
from openapi_client.models.catalog_item_create_query_resource_object import CatalogItemCreateQueryResourceObject
from openapi_client.models.catalog_item_create_query_resource_object_attributes import CatalogItemCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_item_create_query_resource_object_relationships import CatalogItemCreateQueryResourceObjectRelationships
from openapi_client.models.catalog_item_create_query_resource_object_relationships_categories import CatalogItemCreateQueryResourceObjectRelationshipsCategories
from openapi_client.models.catalog_item_create_query_resource_object_relationships_categories_data_inner import CatalogItemCreateQueryResourceObjectRelationshipsCategoriesDataInner
from openapi_client.models.catalog_item_delete_job_create_query import CatalogItemDeleteJobCreateQuery
from openapi_client.models.catalog_item_delete_job_create_query_resource_object import CatalogItemDeleteJobCreateQueryResourceObject
from openapi_client.models.catalog_item_delete_job_create_query_resource_object_attributes import CatalogItemDeleteJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_item_delete_job_create_query_resource_object_attributes_items import CatalogItemDeleteJobCreateQueryResourceObjectAttributesItems
from openapi_client.models.catalog_item_delete_query_resource_object import CatalogItemDeleteQueryResourceObject
from openapi_client.models.catalog_item_enum import CatalogItemEnum
from openapi_client.models.catalog_item_update_job_create_query import CatalogItemUpdateJobCreateQuery
from openapi_client.models.catalog_item_update_job_create_query_resource_object import CatalogItemUpdateJobCreateQueryResourceObject
from openapi_client.models.catalog_item_update_job_create_query_resource_object_attributes import CatalogItemUpdateJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_item_update_job_create_query_resource_object_attributes_items import CatalogItemUpdateJobCreateQueryResourceObjectAttributesItems
from openapi_client.models.catalog_item_update_query import CatalogItemUpdateQuery
from openapi_client.models.catalog_item_update_query_resource_object import CatalogItemUpdateQueryResourceObject
from openapi_client.models.catalog_item_update_query_resource_object_attributes import CatalogItemUpdateQueryResourceObjectAttributes
from openapi_client.models.catalog_variant_bulk_create_job_enum import CatalogVariantBulkCreateJobEnum
from openapi_client.models.catalog_variant_bulk_delete_job_enum import CatalogVariantBulkDeleteJobEnum
from openapi_client.models.catalog_variant_bulk_update_job_enum import CatalogVariantBulkUpdateJobEnum
from openapi_client.models.catalog_variant_create_job_create_query import CatalogVariantCreateJobCreateQuery
from openapi_client.models.catalog_variant_create_job_create_query_resource_object import CatalogVariantCreateJobCreateQueryResourceObject
from openapi_client.models.catalog_variant_create_job_create_query_resource_object_attributes import CatalogVariantCreateJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_variant_create_job_create_query_resource_object_attributes_variants import CatalogVariantCreateJobCreateQueryResourceObjectAttributesVariants
from openapi_client.models.catalog_variant_create_query import CatalogVariantCreateQuery
from openapi_client.models.catalog_variant_create_query_resource_object import CatalogVariantCreateQueryResourceObject
from openapi_client.models.catalog_variant_create_query_resource_object_attributes import CatalogVariantCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_variant_create_query_resource_object_relationships import CatalogVariantCreateQueryResourceObjectRelationships
from openapi_client.models.catalog_variant_create_query_resource_object_relationships_item import CatalogVariantCreateQueryResourceObjectRelationshipsItem
from openapi_client.models.catalog_variant_create_query_resource_object_relationships_item_data import CatalogVariantCreateQueryResourceObjectRelationshipsItemData
from openapi_client.models.catalog_variant_delete_job_create_query import CatalogVariantDeleteJobCreateQuery
from openapi_client.models.catalog_variant_delete_job_create_query_resource_object import CatalogVariantDeleteJobCreateQueryResourceObject
from openapi_client.models.catalog_variant_delete_job_create_query_resource_object_attributes import CatalogVariantDeleteJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_variant_delete_job_create_query_resource_object_attributes_variants import CatalogVariantDeleteJobCreateQueryResourceObjectAttributesVariants
from openapi_client.models.catalog_variant_delete_query_resource_object import CatalogVariantDeleteQueryResourceObject
from openapi_client.models.catalog_variant_enum import CatalogVariantEnum
from openapi_client.models.catalog_variant_update_job_create_query import CatalogVariantUpdateJobCreateQuery
from openapi_client.models.catalog_variant_update_job_create_query_resource_object import CatalogVariantUpdateJobCreateQueryResourceObject
from openapi_client.models.catalog_variant_update_job_create_query_resource_object_attributes import CatalogVariantUpdateJobCreateQueryResourceObjectAttributes
from openapi_client.models.catalog_variant_update_job_create_query_resource_object_attributes_variants import CatalogVariantUpdateJobCreateQueryResourceObjectAttributesVariants
from openapi_client.models.catalog_variant_update_query import CatalogVariantUpdateQuery
from openapi_client.models.catalog_variant_update_query_resource_object import CatalogVariantUpdateQueryResourceObject
from openapi_client.models.catalog_variant_update_query_resource_object_attributes import CatalogVariantUpdateQueryResourceObjectAttributes
from openapi_client.models.coupon_code_bulk_create_job_enum import CouponCodeBulkCreateJobEnum
from openapi_client.models.coupon_code_create_job_create_query import CouponCodeCreateJobCreateQuery
from openapi_client.models.coupon_code_create_job_create_query_resource_object import CouponCodeCreateJobCreateQueryResourceObject
from openapi_client.models.coupon_code_create_job_create_query_resource_object_attributes import CouponCodeCreateJobCreateQueryResourceObjectAttributes
from openapi_client.models.coupon_code_create_job_create_query_resource_object_attributes_coupon_codes import CouponCodeCreateJobCreateQueryResourceObjectAttributesCouponCodes
from openapi_client.models.coupon_code_create_query import CouponCodeCreateQuery
from openapi_client.models.coupon_code_create_query_resource_object import CouponCodeCreateQueryResourceObject
from openapi_client.models.coupon_code_create_query_resource_object_attributes import CouponCodeCreateQueryResourceObjectAttributes
from openapi_client.models.coupon_code_create_query_resource_object_relationships import CouponCodeCreateQueryResourceObjectRelationships
from openapi_client.models.coupon_code_create_query_resource_object_relationships_coupon import CouponCodeCreateQueryResourceObjectRelationshipsCoupon
from openapi_client.models.coupon_code_create_query_resource_object_relationships_coupon_data import CouponCodeCreateQueryResourceObjectRelationshipsCouponData
from openapi_client.models.coupon_code_enum import CouponCodeEnum
from openapi_client.models.coupon_code_update_query import CouponCodeUpdateQuery
from openapi_client.models.coupon_code_update_query_resource_object import CouponCodeUpdateQueryResourceObject
from openapi_client.models.coupon_code_update_query_resource_object_attributes import CouponCodeUpdateQueryResourceObjectAttributes
from openapi_client.models.coupon_create_query import CouponCreateQuery
from openapi_client.models.coupon_create_query_resource_object import CouponCreateQueryResourceObject
from openapi_client.models.coupon_create_query_resource_object_attributes import CouponCreateQueryResourceObjectAttributes
from openapi_client.models.coupon_enum import CouponEnum
from openapi_client.models.coupon_update_query import CouponUpdateQuery
from openapi_client.models.coupon_update_query_resource_object import CouponUpdateQueryResourceObject
from openapi_client.models.coupon_update_query_resource_object_attributes import CouponUpdateQueryResourceObjectAttributes
from openapi_client.models.data_privacy_create_deletion_job_query import DataPrivacyCreateDeletionJobQuery
from openapi_client.models.data_privacy_create_deletion_job_query_resource_object import DataPrivacyCreateDeletionJobQueryResourceObject
from openapi_client.models.data_privacy_create_deletion_job_query_resource_object_attributes import DataPrivacyCreateDeletionJobQueryResourceObjectAttributes
from openapi_client.models.data_privacy_create_deletion_job_query_resource_object_attributes_profile import DataPrivacyCreateDeletionJobQueryResourceObjectAttributesProfile
from openapi_client.models.data_privacy_deletion_job_enum import DataPrivacyDeletionJobEnum
from openapi_client.models.data_privacy_profile_query_resource_object import DataPrivacyProfileQueryResourceObject
from openapi_client.models.data_privacy_profile_query_resource_object_attributes import DataPrivacyProfileQueryResourceObjectAttributes
from openapi_client.models.device_metadata import DeviceMetadata
from openapi_client.models.email_subscription_parameters import EmailSubscriptionParameters
from openapi_client.models.event_create_query_v2 import EventCreateQueryV2
from openapi_client.models.event_create_query_v2_resource_object import EventCreateQueryV2ResourceObject
from openapi_client.models.event_create_query_v2_resource_object_attributes import EventCreateQueryV2ResourceObjectAttributes
from openapi_client.models.event_create_query_v2_resource_object_attributes_metric import EventCreateQueryV2ResourceObjectAttributesMetric
from openapi_client.models.event_create_query_v2_resource_object_attributes_profile import EventCreateQueryV2ResourceObjectAttributesProfile
from openapi_client.models.event_enum import EventEnum
from openapi_client.models.flow_enum import FlowEnum
from openapi_client.models.flow_update_query import FlowUpdateQuery
from openapi_client.models.flow_update_query_resource_object import FlowUpdateQueryResourceObject
from openapi_client.models.flow_update_query_resource_object_attributes import FlowUpdateQueryResourceObjectAttributes
from openapi_client.models.get_accounts4_xx_response import GetAccounts4XXResponse
from openapi_client.models.get_accounts4_xx_response_errors_inner import GetAccounts4XXResponseErrorsInner
from openapi_client.models.get_accounts4_xx_response_errors_inner_source import GetAccounts4XXResponseErrorsInnerSource
from openapi_client.models.image_create_query import ImageCreateQuery
from openapi_client.models.image_create_query_resource_object import ImageCreateQueryResourceObject
from openapi_client.models.image_create_query_resource_object_attributes import ImageCreateQueryResourceObjectAttributes
from openapi_client.models.image_enum import ImageEnum
from openapi_client.models.image_partial_update_query import ImagePartialUpdateQuery
from openapi_client.models.image_partial_update_query_resource_object import ImagePartialUpdateQueryResourceObject
from openapi_client.models.image_partial_update_query_resource_object_attributes import ImagePartialUpdateQueryResourceObjectAttributes
from openapi_client.models.list_create_query import ListCreateQuery
from openapi_client.models.list_create_query_resource_object import ListCreateQueryResourceObject
from openapi_client.models.list_create_query_resource_object_attributes import ListCreateQueryResourceObjectAttributes
from openapi_client.models.list_enum import ListEnum
from openapi_client.models.list_members_add_query import ListMembersAddQuery
from openapi_client.models.list_members_add_query_data_inner import ListMembersAddQueryDataInner
from openapi_client.models.list_members_delete_query import ListMembersDeleteQuery
from openapi_client.models.list_partial_update_query import ListPartialUpdateQuery
from openapi_client.models.list_partial_update_query_resource_object import ListPartialUpdateQueryResourceObject
from openapi_client.models.marketing_subscription_parameters import MarketingSubscriptionParameters
from openapi_client.models.metric_aggregate_enum import MetricAggregateEnum
from openapi_client.models.metric_aggregate_query import MetricAggregateQuery
from openapi_client.models.metric_aggregate_query_resource_object import MetricAggregateQueryResourceObject
from openapi_client.models.metric_aggregate_query_resource_object_attributes import MetricAggregateQueryResourceObjectAttributes
from openapi_client.models.metric_create_query_resource_object import MetricCreateQueryResourceObject
from openapi_client.models.metric_create_query_resource_object_attributes import MetricCreateQueryResourceObjectAttributes
from openapi_client.models.metric_enum import MetricEnum
from openapi_client.models.onsite_profile_create_query_resource_object import OnsiteProfileCreateQueryResourceObject
from openapi_client.models.onsite_profile_create_query_resource_object_attributes import OnsiteProfileCreateQueryResourceObjectAttributes
from openapi_client.models.onsite_profile_meta import OnsiteProfileMeta
from openapi_client.models.profile_create_query import ProfileCreateQuery
from openapi_client.models.profile_create_query_resource_object import ProfileCreateQueryResourceObject
from openapi_client.models.profile_create_query_resource_object_attributes import ProfileCreateQueryResourceObjectAttributes
from openapi_client.models.profile_enum import ProfileEnum
from openapi_client.models.profile_identifier_dto_resource_object import ProfileIdentifierDTOResourceObject
from openapi_client.models.profile_identifier_dto_resource_object_attributes import ProfileIdentifierDTOResourceObjectAttributes
from openapi_client.models.profile_location import ProfileLocation
from openapi_client.models.profile_merge_enum import ProfileMergeEnum
from openapi_client.models.profile_merge_query import ProfileMergeQuery
from openapi_client.models.profile_merge_query_resource_object import ProfileMergeQueryResourceObject
from openapi_client.models.profile_merge_query_resource_object_relationships import ProfileMergeQueryResourceObjectRelationships
from openapi_client.models.profile_merge_query_resource_object_relationships_profiles import ProfileMergeQueryResourceObjectRelationshipsProfiles
from openapi_client.models.profile_merge_query_resource_object_relationships_profiles_data_inner import ProfileMergeQueryResourceObjectRelationshipsProfilesDataInner
from openapi_client.models.profile_meta import ProfileMeta
from openapi_client.models.profile_meta_patch_properties import ProfileMetaPatchProperties
from openapi_client.models.profile_partial_update_query import ProfilePartialUpdateQuery
from openapi_client.models.profile_partial_update_query_resource_object import ProfilePartialUpdateQueryResourceObject
from openapi_client.models.profile_partial_update_query_resource_object_attributes import ProfilePartialUpdateQueryResourceObjectAttributes
from openapi_client.models.profile_subscription_bulk_create_job_enum import ProfileSubscriptionBulkCreateJobEnum
from openapi_client.models.profile_subscription_bulk_delete_job_enum import ProfileSubscriptionBulkDeleteJobEnum
from openapi_client.models.profile_subscription_create_query_resource_object import ProfileSubscriptionCreateQueryResourceObject
from openapi_client.models.profile_subscription_create_query_resource_object_attributes import ProfileSubscriptionCreateQueryResourceObjectAttributes
from openapi_client.models.profile_subscription_delete_query_resource_object import ProfileSubscriptionDeleteQueryResourceObject
from openapi_client.models.profile_subscription_delete_query_resource_object_attributes import ProfileSubscriptionDeleteQueryResourceObjectAttributes
from openapi_client.models.profile_suppression_bulk_create_job_enum import ProfileSuppressionBulkCreateJobEnum
from openapi_client.models.profile_suppression_bulk_delete_job_enum import ProfileSuppressionBulkDeleteJobEnum
from openapi_client.models.profile_suppression_create_query_resource_object import ProfileSuppressionCreateQueryResourceObject
from openapi_client.models.profile_suppression_create_query_resource_object_attributes import ProfileSuppressionCreateQueryResourceObjectAttributes
from openapi_client.models.profile_suppression_delete_query_resource_object import ProfileSuppressionDeleteQueryResourceObject
from openapi_client.models.profile_suppression_delete_query_resource_object_attributes import ProfileSuppressionDeleteQueryResourceObjectAttributes
from openapi_client.models.profile_upsert_query_resource_object import ProfileUpsertQueryResourceObject
from openapi_client.models.profile_upsert_query_resource_object_attributes import ProfileUpsertQueryResourceObjectAttributes
from openapi_client.models.push_token_create_query import PushTokenCreateQuery
from openapi_client.models.push_token_create_query_resource_object import PushTokenCreateQueryResourceObject
from openapi_client.models.push_token_create_query_resource_object_attributes import PushTokenCreateQueryResourceObjectAttributes
from openapi_client.models.push_token_create_query_resource_object_attributes_profile import PushTokenCreateQueryResourceObjectAttributesProfile
from openapi_client.models.push_token_enum import PushTokenEnum
from openapi_client.models.render_options_sub_object import RenderOptionsSubObject
from openapi_client.models.sms_subscription_parameters import SMSSubscriptionParameters
from openapi_client.models.sto_schedule_options import STOScheduleOptions
from openapi_client.models.segment_enum import SegmentEnum
from openapi_client.models.segment_partial_update_query import SegmentPartialUpdateQuery
from openapi_client.models.segment_partial_update_query_resource_object import SegmentPartialUpdateQueryResourceObject
from openapi_client.models.segment_partial_update_query_resource_object_attributes import SegmentPartialUpdateQueryResourceObjectAttributes
from openapi_client.models.send_strategy_sub_object import SendStrategySubObject
from openapi_client.models.server_bis_subscription_create_query import ServerBISSubscriptionCreateQuery
from openapi_client.models.server_bis_subscription_create_query_resource_object import ServerBISSubscriptionCreateQueryResourceObject
from openapi_client.models.server_bis_subscription_create_query_resource_object_attributes import ServerBISSubscriptionCreateQueryResourceObjectAttributes
from openapi_client.models.server_bis_subscription_create_query_resource_object_attributes_profile import ServerBISSubscriptionCreateQueryResourceObjectAttributesProfile
from openapi_client.models.server_bis_subscription_create_query_resource_object_relationships import ServerBISSubscriptionCreateQueryResourceObjectRelationships
from openapi_client.models.server_bis_subscription_create_query_resource_object_relationships_variant import ServerBISSubscriptionCreateQueryResourceObjectRelationshipsVariant
from openapi_client.models.server_bis_subscription_create_query_resource_object_relationships_variant_data import ServerBISSubscriptionCreateQueryResourceObjectRelationshipsVariantData
from openapi_client.models.static_schedule_options import StaticScheduleOptions
from openapi_client.models.subscription_channels import SubscriptionChannels
from openapi_client.models.subscription_create_job_create_query import SubscriptionCreateJobCreateQuery
from openapi_client.models.subscription_create_job_create_query_resource_object import SubscriptionCreateJobCreateQueryResourceObject
from openapi_client.models.subscription_create_job_create_query_resource_object_attributes import SubscriptionCreateJobCreateQueryResourceObjectAttributes
from openapi_client.models.subscription_create_job_create_query_resource_object_attributes_profiles import SubscriptionCreateJobCreateQueryResourceObjectAttributesProfiles
from openapi_client.models.subscription_create_job_create_query_resource_object_relationships import SubscriptionCreateJobCreateQueryResourceObjectRelationships
from openapi_client.models.subscription_create_job_create_query_resource_object_relationships_list import SubscriptionCreateJobCreateQueryResourceObjectRelationshipsList
from openapi_client.models.subscription_create_job_create_query_resource_object_relationships_list_data import SubscriptionCreateJobCreateQueryResourceObjectRelationshipsListData
from openapi_client.models.subscription_delete_job_create_query import SubscriptionDeleteJobCreateQuery
from openapi_client.models.subscription_delete_job_create_query_resource_object import SubscriptionDeleteJobCreateQueryResourceObject
from openapi_client.models.subscription_delete_job_create_query_resource_object_attributes import SubscriptionDeleteJobCreateQueryResourceObjectAttributes
from openapi_client.models.subscription_delete_job_create_query_resource_object_attributes_profiles import SubscriptionDeleteJobCreateQueryResourceObjectAttributesProfiles
from openapi_client.models.subscription_delete_job_create_query_resource_object_relationships import SubscriptionDeleteJobCreateQueryResourceObjectRelationships
from openapi_client.models.subscription_delete_job_create_query_resource_object_relationships_list import SubscriptionDeleteJobCreateQueryResourceObjectRelationshipsList
from openapi_client.models.subscription_delete_job_create_query_resource_object_relationships_list_data import SubscriptionDeleteJobCreateQueryResourceObjectRelationshipsListData
from openapi_client.models.suppression_create_job_create_query import SuppressionCreateJobCreateQuery
from openapi_client.models.suppression_create_job_create_query_resource_object import SuppressionCreateJobCreateQueryResourceObject
from openapi_client.models.suppression_create_job_create_query_resource_object_attributes import SuppressionCreateJobCreateQueryResourceObjectAttributes
from openapi_client.models.suppression_create_job_create_query_resource_object_attributes_profiles import SuppressionCreateJobCreateQueryResourceObjectAttributesProfiles
from openapi_client.models.suppression_delete_job_create_query import SuppressionDeleteJobCreateQuery
from openapi_client.models.suppression_delete_job_create_query_resource_object import SuppressionDeleteJobCreateQueryResourceObject
from openapi_client.models.suppression_delete_job_create_query_resource_object_attributes import SuppressionDeleteJobCreateQueryResourceObjectAttributes
from openapi_client.models.suppression_delete_job_create_query_resource_object_attributes_profiles import SuppressionDeleteJobCreateQueryResourceObjectAttributesProfiles
from openapi_client.models.tag_campaign_op import TagCampaignOp
from openapi_client.models.tag_campaign_op_data_inner import TagCampaignOpDataInner
from openapi_client.models.tag_create_query import TagCreateQuery
from openapi_client.models.tag_create_query_resource_object import TagCreateQueryResourceObject
from openapi_client.models.tag_create_query_resource_object_attributes import TagCreateQueryResourceObjectAttributes
from openapi_client.models.tag_create_query_resource_object_relationships import TagCreateQueryResourceObjectRelationships
from openapi_client.models.tag_create_query_resource_object_relationships_tag_group import TagCreateQueryResourceObjectRelationshipsTagGroup
from openapi_client.models.tag_create_query_resource_object_relationships_tag_group_data import TagCreateQueryResourceObjectRelationshipsTagGroupData
from openapi_client.models.tag_enum import TagEnum
from openapi_client.models.tag_flow_op import TagFlowOp
from openapi_client.models.tag_flow_op_data_inner import TagFlowOpDataInner
from openapi_client.models.tag_group_create_query import TagGroupCreateQuery
from openapi_client.models.tag_group_create_query_resource_object import TagGroupCreateQueryResourceObject
from openapi_client.models.tag_group_create_query_resource_object_attributes import TagGroupCreateQueryResourceObjectAttributes
from openapi_client.models.tag_group_enum import TagGroupEnum
from openapi_client.models.tag_group_update_query import TagGroupUpdateQuery
from openapi_client.models.tag_group_update_query_resource_object import TagGroupUpdateQueryResourceObject
from openapi_client.models.tag_group_update_query_resource_object_attributes import TagGroupUpdateQueryResourceObjectAttributes
from openapi_client.models.tag_list_op import TagListOp
from openapi_client.models.tag_list_op_data_inner import TagListOpDataInner
from openapi_client.models.tag_segment_op import TagSegmentOp
from openapi_client.models.tag_segment_op_data_inner import TagSegmentOpDataInner
from openapi_client.models.tag_update_query import TagUpdateQuery
from openapi_client.models.tag_update_query_resource_object import TagUpdateQueryResourceObject
from openapi_client.models.template_clone_query import TemplateCloneQuery
from openapi_client.models.template_clone_query_resource_object import TemplateCloneQueryResourceObject
from openapi_client.models.template_clone_query_resource_object_attributes import TemplateCloneQueryResourceObjectAttributes
from openapi_client.models.template_create_query import TemplateCreateQuery
from openapi_client.models.template_create_query_resource_object import TemplateCreateQueryResourceObject
from openapi_client.models.template_create_query_resource_object_attributes import TemplateCreateQueryResourceObjectAttributes
from openapi_client.models.template_enum import TemplateEnum
from openapi_client.models.template_render_query import TemplateRenderQuery
from openapi_client.models.template_render_query_resource_object import TemplateRenderQueryResourceObject
from openapi_client.models.template_render_query_resource_object_attributes import TemplateRenderQueryResourceObjectAttributes
from openapi_client.models.template_update_query import TemplateUpdateQuery
from openapi_client.models.template_update_query_resource_object import TemplateUpdateQueryResourceObject
from openapi_client.models.template_update_query_resource_object_attributes import TemplateUpdateQueryResourceObjectAttributes
from openapi_client.models.throttled_schedule_options import ThrottledScheduleOptions
