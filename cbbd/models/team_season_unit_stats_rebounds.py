# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.13.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class TeamSeasonUnitStatsRebounds(BaseModel):
    """
    TeamSeasonUnitStatsRebounds
    """
    total: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    defensive: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    offensive: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["total", "defensive", "offensive"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TeamSeasonUnitStatsRebounds:
        """Create an instance of TeamSeasonUnitStatsRebounds from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        # set to None if defensive (nullable) is None
        # and __fields_set__ contains the field
        if self.defensive is None and "defensive" in self.__fields_set__:
            _dict['defensive'] = None

        # set to None if offensive (nullable) is None
        # and __fields_set__ contains the field
        if self.offensive is None and "offensive" in self.__fields_set__:
            _dict['offensive'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamSeasonUnitStatsRebounds:
        """Create an instance of TeamSeasonUnitStatsRebounds from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamSeasonUnitStatsRebounds.parse_obj(obj)

        _obj = TeamSeasonUnitStatsRebounds.parse_obj({
            "total": obj.get("total"),
            "defensive": obj.get("defensive"),
            "offensive": obj.get("offensive")
        })
        return _obj


