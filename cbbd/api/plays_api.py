# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.12.1
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

from pydantic import Field, StrictBool, StrictInt, StrictStr

from typing import List, Optional

from cbbd.models.play_info import PlayInfo
from cbbd.models.play_type_info import PlayTypeInfo

from cbbd.api_client import ApiClient
from cbbd.api_response import ApiResponse
from cbbd.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PlaysApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_play_types(self, **kwargs) -> List[PlayTypeInfo]:  # noqa: E501
        """get_play_types  # noqa: E501

        Retrieve list of play types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_play_types(async_req=True)
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
        :rtype: List[PlayTypeInfo]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_play_types_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_play_types_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_play_types_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """get_play_types  # noqa: E501

        Retrieve list of play types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_play_types_with_http_info(async_req=True)
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
        :rtype: tuple(List[PlayTypeInfo], status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_play_types" % _key
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
            '200': "List[PlayTypeInfo]",
        }

        return self.api_client.call_api(
            '/plays/types', 'GET',
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
    def get_plays(self, game_id : Annotated[StrictInt, Field(..., description="Game id filter")], shooting_plays_only : Annotated[Optional[StrictBool], Field(description="Optional filter to only return shooting plays")] = None, **kwargs) -> List[PlayInfo]:  # noqa: E501
        """get_plays  # noqa: E501

        Returns all plays for a given game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plays(game_id, shooting_plays_only, async_req=True)
        >>> result = thread.get()

        :param game_id: Game id filter (required)
        :type game_id: int
        :param shooting_plays_only: Optional filter to only return shooting plays
        :type shooting_plays_only: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayInfo]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_plays_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_plays_with_http_info(game_id, shooting_plays_only, **kwargs)  # noqa: E501

    @validate_arguments
    def get_plays_with_http_info(self, game_id : Annotated[StrictInt, Field(..., description="Game id filter")], shooting_plays_only : Annotated[Optional[StrictBool], Field(description="Optional filter to only return shooting plays")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_plays  # noqa: E501

        Returns all plays for a given game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plays_with_http_info(game_id, shooting_plays_only, async_req=True)
        >>> result = thread.get()

        :param game_id: Game id filter (required)
        :type game_id: int
        :param shooting_plays_only: Optional filter to only return shooting plays
        :type shooting_plays_only: bool
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
        :rtype: tuple(List[PlayInfo], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'game_id',
            'shooting_plays_only'
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
                    " to method get_plays" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['game_id'] is not None:
            _path_params['gameId'] = _params['game_id']


        # process the query parameters
        _query_params = []
        if _params.get('shooting_plays_only') is not None:  # noqa: E501
            _query_params.append(('shootingPlaysOnly', _params['shooting_plays_only']))

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
            '200': "List[PlayInfo]",
        }

        return self.api_client.call_api(
            '/plays/game/{gameId}', 'GET',
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
    def get_plays_by_date(self, var_date : Annotated[datetime, Field(..., description="Required date filter in ISO 8601 format (YYYY-MM-DD)")], shooting_plays_only : Annotated[Optional[StrictBool], Field(description="Optional filter to only return shooting plays")] = None, **kwargs) -> List[PlayInfo]:  # noqa: E501
        """get_plays_by_date  # noqa: E501

        Retrieve all plays for a given UTC date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plays_by_date(var_date, shooting_plays_only, async_req=True)
        >>> result = thread.get()

        :param var_date: Required date filter in ISO 8601 format (YYYY-MM-DD) (required)
        :type var_date: datetime
        :param shooting_plays_only: Optional filter to only return shooting plays
        :type shooting_plays_only: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayInfo]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_plays_by_date_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_plays_by_date_with_http_info(var_date, shooting_plays_only, **kwargs)  # noqa: E501

    @validate_arguments
    def get_plays_by_date_with_http_info(self, var_date : Annotated[datetime, Field(..., description="Required date filter in ISO 8601 format (YYYY-MM-DD)")], shooting_plays_only : Annotated[Optional[StrictBool], Field(description="Optional filter to only return shooting plays")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_plays_by_date  # noqa: E501

        Retrieve all plays for a given UTC date  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plays_by_date_with_http_info(var_date, shooting_plays_only, async_req=True)
        >>> result = thread.get()

        :param var_date: Required date filter in ISO 8601 format (YYYY-MM-DD) (required)
        :type var_date: datetime
        :param shooting_plays_only: Optional filter to only return shooting plays
        :type shooting_plays_only: bool
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
        :rtype: tuple(List[PlayInfo], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'var_date',
            'shooting_plays_only'
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
                    " to method get_plays_by_date" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('var_date') is not None:  # noqa: E501
            if isinstance(_params['var_date'], datetime):
                _query_params.append(('date', _params['var_date'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('date', _params['var_date']))

        if _params.get('shooting_plays_only') is not None:  # noqa: E501
            _query_params.append(('shootingPlaysOnly', _params['shooting_plays_only']))

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
            '200': "List[PlayInfo]",
        }

        return self.api_client.call_api(
            '/plays/date', 'GET',
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
    def get_plays_by_player_id(self, player_id : Annotated[StrictInt, Field(..., description="Required player id filter")], season : Annotated[StrictInt, Field(..., description="Required season filter")], shooting_plays_only : Annotated[Optional[StrictBool], Field(description="Optional filter to only return shooting plays")] = None, **kwargs) -> List[PlayInfo]:  # noqa: E501
        """get_plays_by_player_id  # noqa: E501

        Retrieve all plays for a given player and season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plays_by_player_id(player_id, season, shooting_plays_only, async_req=True)
        >>> result = thread.get()

        :param player_id: Required player id filter (required)
        :type player_id: int
        :param season: Required season filter (required)
        :type season: int
        :param shooting_plays_only: Optional filter to only return shooting plays
        :type shooting_plays_only: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayInfo]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_plays_by_player_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_plays_by_player_id_with_http_info(player_id, season, shooting_plays_only, **kwargs)  # noqa: E501

    @validate_arguments
    def get_plays_by_player_id_with_http_info(self, player_id : Annotated[StrictInt, Field(..., description="Required player id filter")], season : Annotated[StrictInt, Field(..., description="Required season filter")], shooting_plays_only : Annotated[Optional[StrictBool], Field(description="Optional filter to only return shooting plays")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_plays_by_player_id  # noqa: E501

        Retrieve all plays for a given player and season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plays_by_player_id_with_http_info(player_id, season, shooting_plays_only, async_req=True)
        >>> result = thread.get()

        :param player_id: Required player id filter (required)
        :type player_id: int
        :param season: Required season filter (required)
        :type season: int
        :param shooting_plays_only: Optional filter to only return shooting plays
        :type shooting_plays_only: bool
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
        :rtype: tuple(List[PlayInfo], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'player_id',
            'season',
            'shooting_plays_only'
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
                    " to method get_plays_by_player_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['player_id'] is not None:
            _path_params['playerId'] = _params['player_id']


        # process the query parameters
        _query_params = []
        if _params.get('season') is not None:  # noqa: E501
            _query_params.append(('season', _params['season']))

        if _params.get('shooting_plays_only') is not None:  # noqa: E501
            _query_params.append(('shootingPlaysOnly', _params['shooting_plays_only']))

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
            '200': "List[PlayInfo]",
        }

        return self.api_client.call_api(
            '/plays/player/{playerId}', 'GET',
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
    def get_plays_by_team(self, season : Annotated[StrictInt, Field(..., description="Required season filter")], team : Annotated[StrictStr, Field(..., description="Required team filter")], shooting_plays_only : Annotated[Optional[StrictBool], Field(description="Optional filter to only return shooting plays")] = None, **kwargs) -> List[PlayInfo]:  # noqa: E501
        """get_plays_by_team  # noqa: E501

        Retrieve all plays for a given team and season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plays_by_team(season, team, shooting_plays_only, async_req=True)
        >>> result = thread.get()

        :param season: Required season filter (required)
        :type season: int
        :param team: Required team filter (required)
        :type team: str
        :param shooting_plays_only: Optional filter to only return shooting plays
        :type shooting_plays_only: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayInfo]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_plays_by_team_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_plays_by_team_with_http_info(season, team, shooting_plays_only, **kwargs)  # noqa: E501

    @validate_arguments
    def get_plays_by_team_with_http_info(self, season : Annotated[StrictInt, Field(..., description="Required season filter")], team : Annotated[StrictStr, Field(..., description="Required team filter")], shooting_plays_only : Annotated[Optional[StrictBool], Field(description="Optional filter to only return shooting plays")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_plays_by_team  # noqa: E501

        Retrieve all plays for a given team and season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_plays_by_team_with_http_info(season, team, shooting_plays_only, async_req=True)
        >>> result = thread.get()

        :param season: Required season filter (required)
        :type season: int
        :param team: Required team filter (required)
        :type team: str
        :param shooting_plays_only: Optional filter to only return shooting plays
        :type shooting_plays_only: bool
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
        :rtype: tuple(List[PlayInfo], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'season',
            'team',
            'shooting_plays_only'
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
                    " to method get_plays_by_team" % _key
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

        if _params.get('shooting_plays_only') is not None:  # noqa: E501
            _query_params.append(('shootingPlaysOnly', _params['shooting_plays_only']))

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
            '200': "List[PlayInfo]",
        }

        return self.api_client.call_api(
            '/plays/team', 'GET',
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
