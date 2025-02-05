# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.7.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from datetime import datetime

from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from cbbd.models.game_lines import GameLines
from cbbd.models.line_provider_info import LineProviderInfo

from cbbd.api_client import ApiClient
from cbbd.api_response import ApiResponse
from cbbd.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LinesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_lines(self, season : Annotated[Optional[StrictInt], Field(description="Optional season filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team name filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, start_date_range : Annotated[Optional[datetime], Field(description="Optional start timestamp in ISO 8601 format")] = None, end_date_range : Annotated[Optional[datetime], Field(description="Optional end timestamp in ISO 8601 format")] = None, **kwargs) -> List[GameLines]:  # noqa: E501
        """get_lines  # noqa: E501

        Returns betting lines for the first 3000 games that match the provided filters, ordered by start date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_lines(season, team, conference, start_date_range, end_date_range, async_req=True)
        >>> result = thread.get()

        :param season: Optional season filter
        :type season: int
        :param team: Optional team name filter
        :type team: str
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param start_date_range: Optional start timestamp in ISO 8601 format
        :type start_date_range: datetime
        :param end_date_range: Optional end timestamp in ISO 8601 format
        :type end_date_range: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[GameLines]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_lines_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_lines_with_http_info(season, team, conference, start_date_range, end_date_range, **kwargs)  # noqa: E501

    @validate_arguments
    def get_lines_with_http_info(self, season : Annotated[Optional[StrictInt], Field(description="Optional season filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team name filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference abbreviation filter")] = None, start_date_range : Annotated[Optional[datetime], Field(description="Optional start timestamp in ISO 8601 format")] = None, end_date_range : Annotated[Optional[datetime], Field(description="Optional end timestamp in ISO 8601 format")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_lines  # noqa: E501

        Returns betting lines for the first 3000 games that match the provided filters, ordered by start date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_lines_with_http_info(season, team, conference, start_date_range, end_date_range, async_req=True)
        >>> result = thread.get()

        :param season: Optional season filter
        :type season: int
        :param team: Optional team name filter
        :type team: str
        :param conference: Optional conference abbreviation filter
        :type conference: str
        :param start_date_range: Optional start timestamp in ISO 8601 format
        :type start_date_range: datetime
        :param end_date_range: Optional end timestamp in ISO 8601 format
        :type end_date_range: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[GameLines], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'season',
            'team',
            'conference',
            'start_date_range',
            'end_date_range'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lines" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('season') is not None:  # noqa: E501
            _query_params.append(('season', _params['season']))

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('conference') is not None:  # noqa: E501
            _query_params.append(('conference', _params['conference']))

        if _params.get('start_date_range') is not None:  # noqa: E501
            if isinstance(_params['start_date_range'], datetime):
                _query_params.append(('startDateRange', _params['start_date_range'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('startDateRange', _params['start_date_range']))

        if _params.get('end_date_range') is not None:  # noqa: E501
            if isinstance(_params['end_date_range'], datetime):
                _query_params.append(('endDateRange', _params['end_date_range'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('endDateRange', _params['end_date_range']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apiKey']  # noqa: E501

        _response_types_map = {
            '200': "List[GameLines]",
        }

        return self.api_client.call_api(
            '/lines', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_providers(self, **kwargs) -> List[LineProviderInfo]:  # noqa: E501
        """get_providers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_providers(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[LineProviderInfo]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_providers_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_providers_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_providers_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """get_providers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_providers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[LineProviderInfo], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_providers" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apiKey']  # noqa: E501

        _response_types_map = {
            '200': "List[LineProviderInfo]",
        }

        return self.api_client.call_api(
            '/lines/providers', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
