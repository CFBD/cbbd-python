# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.11.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class SeasonType(str, Enum):
    """
    SeasonType
    """

    """
    allowed enum values
    """
    POSTSEASON = 'postseason'
    PRESEASON = 'preseason'
    REGULAR = 'regular'

    @classmethod
    def from_json(cls, json_str: str) -> SeasonType:
        """Create an instance of SeasonType from a JSON string"""
        return SeasonType(json.loads(json_str))


