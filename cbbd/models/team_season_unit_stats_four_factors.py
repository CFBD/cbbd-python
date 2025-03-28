# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.20.0
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

class TeamSeasonUnitStatsFourFactors(BaseModel):
    """
    TeamSeasonUnitStatsFourFactors
    """
    free_throw_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="freeThrowRate")
    offensive_rebound_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="offensiveReboundPct")
    turnover_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="turnoverRatio")
    effective_field_goal_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="effectiveFieldGoalPct")
    __properties = ["freeThrowRate", "offensiveReboundPct", "turnoverRatio", "effectiveFieldGoalPct"]

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
    def from_json(cls, json_str: str) -> TeamSeasonUnitStatsFourFactors:
        """Create an instance of TeamSeasonUnitStatsFourFactors from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if free_throw_rate (nullable) is None
        # and __fields_set__ contains the field
        if self.free_throw_rate is None and "free_throw_rate" in self.__fields_set__:
            _dict['freeThrowRate'] = None

        # set to None if offensive_rebound_pct (nullable) is None
        # and __fields_set__ contains the field
        if self.offensive_rebound_pct is None and "offensive_rebound_pct" in self.__fields_set__:
            _dict['offensiveReboundPct'] = None

        # set to None if turnover_ratio (nullable) is None
        # and __fields_set__ contains the field
        if self.turnover_ratio is None and "turnover_ratio" in self.__fields_set__:
            _dict['turnoverRatio'] = None

        # set to None if effective_field_goal_pct (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_field_goal_pct is None and "effective_field_goal_pct" in self.__fields_set__:
            _dict['effectiveFieldGoalPct'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamSeasonUnitStatsFourFactors:
        """Create an instance of TeamSeasonUnitStatsFourFactors from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamSeasonUnitStatsFourFactors.parse_obj(obj)

        _obj = TeamSeasonUnitStatsFourFactors.parse_obj({
            "free_throw_rate": obj.get("freeThrowRate"),
            "offensive_rebound_pct": obj.get("offensiveReboundPct"),
            "turnover_ratio": obj.get("turnoverRatio"),
            "effective_field_goal_pct": obj.get("effectiveFieldGoalPct")
        })
        return _obj


