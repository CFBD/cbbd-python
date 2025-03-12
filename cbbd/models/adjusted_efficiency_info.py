# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.18.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cbbd.models.adjusted_efficiency_info_rankings import AdjustedEfficiencyInfoRankings

class AdjustedEfficiencyInfo(BaseModel):
    """
    AdjustedEfficiencyInfo
    """
    season: StrictInt = Field(...)
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    offensive_rating: Union[StrictFloat, StrictInt] = Field(default=..., alias="offensiveRating")
    defensive_rating: Union[StrictFloat, StrictInt] = Field(default=..., alias="defensiveRating")
    net_rating: Union[StrictFloat, StrictInt] = Field(default=..., alias="netRating")
    rankings: AdjustedEfficiencyInfoRankings = Field(...)
    __properties = ["season", "teamId", "team", "conference", "offensiveRating", "defensiveRating", "netRating", "rankings"]

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
    def from_json(cls, json_str: str) -> AdjustedEfficiencyInfo:
        """Create an instance of AdjustedEfficiencyInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of rankings
        if self.rankings:
            _dict['rankings'] = self.rankings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdjustedEfficiencyInfo:
        """Create an instance of AdjustedEfficiencyInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdjustedEfficiencyInfo.parse_obj(obj)

        _obj = AdjustedEfficiencyInfo.parse_obj({
            "season": obj.get("season"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "offensive_rating": obj.get("offensiveRating"),
            "defensive_rating": obj.get("defensiveRating"),
            "net_rating": obj.get("netRating"),
            "rankings": AdjustedEfficiencyInfoRankings.from_dict(obj.get("rankings")) if obj.get("rankings") is not None else None
        })
        return _obj


