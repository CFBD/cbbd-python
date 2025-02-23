# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.15.1
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

class TeamSeasonUnitStatsFieldGoals(BaseModel):
    """
    TeamSeasonUnitStatsFieldGoals
    """
    pct: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    attempted: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    made: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["pct", "attempted", "made"]

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
    def from_json(cls, json_str: str) -> TeamSeasonUnitStatsFieldGoals:
        """Create an instance of TeamSeasonUnitStatsFieldGoals from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if pct (nullable) is None
        # and __fields_set__ contains the field
        if self.pct is None and "pct" in self.__fields_set__:
            _dict['pct'] = None

        # set to None if attempted (nullable) is None
        # and __fields_set__ contains the field
        if self.attempted is None and "attempted" in self.__fields_set__:
            _dict['attempted'] = None

        # set to None if made (nullable) is None
        # and __fields_set__ contains the field
        if self.made is None and "made" in self.__fields_set__:
            _dict['made'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamSeasonUnitStatsFieldGoals:
        """Create an instance of TeamSeasonUnitStatsFieldGoals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamSeasonUnitStatsFieldGoals.parse_obj(obj)

        _obj = TeamSeasonUnitStatsFieldGoals.parse_obj({
            "pct": obj.get("pct"),
            "attempted": obj.get("attempted"),
            "made": obj.get("made")
        })
        return _obj


