# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.19.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from cbbd.models.lineup_unit_stats_four_factors import LineupUnitStatsFourFactors
from cbbd.models.lineup_unit_stats_two_pointers import LineupUnitStatsTwoPointers
from cbbd.models.shooting_stats import ShootingStats

class LineupUnitStats(BaseModel):
    """
    LineupUnitStats
    """
    possessions: StrictInt = Field(...)
    points: StrictInt = Field(...)
    blocks: StrictInt = Field(...)
    assists: StrictInt = Field(...)
    steals: StrictInt = Field(...)
    turnovers: StrictInt = Field(...)
    defensive_rebounds: StrictInt = Field(default=..., alias="defensiveRebounds")
    offensive_rebounds: StrictInt = Field(default=..., alias="offensiveRebounds")
    true_shooting: Union[StrictFloat, StrictInt] = Field(default=..., alias="trueShooting")
    field_goals: ShootingStats = Field(default=..., alias="fieldGoals")
    two_pointers: LineupUnitStatsTwoPointers = Field(default=..., alias="twoPointers")
    three_pointers: ShootingStats = Field(default=..., alias="threePointers")
    free_throws: ShootingStats = Field(default=..., alias="freeThrows")
    four_factors: LineupUnitStatsFourFactors = Field(default=..., alias="fourFactors")
    __properties = ["possessions", "points", "blocks", "assists", "steals", "turnovers", "defensiveRebounds", "offensiveRebounds", "trueShooting", "fieldGoals", "twoPointers", "threePointers", "freeThrows", "fourFactors"]

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
    def from_json(cls, json_str: str) -> LineupUnitStats:
        """Create an instance of LineupUnitStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of field_goals
        if self.field_goals:
            _dict['fieldGoals'] = self.field_goals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of two_pointers
        if self.two_pointers:
            _dict['twoPointers'] = self.two_pointers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of three_pointers
        if self.three_pointers:
            _dict['threePointers'] = self.three_pointers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of free_throws
        if self.free_throws:
            _dict['freeThrows'] = self.free_throws.to_dict()
        # override the default output from pydantic by calling `to_dict()` of four_factors
        if self.four_factors:
            _dict['fourFactors'] = self.four_factors.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LineupUnitStats:
        """Create an instance of LineupUnitStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LineupUnitStats.parse_obj(obj)

        _obj = LineupUnitStats.parse_obj({
            "possessions": obj.get("possessions"),
            "points": obj.get("points"),
            "blocks": obj.get("blocks"),
            "assists": obj.get("assists"),
            "steals": obj.get("steals"),
            "turnovers": obj.get("turnovers"),
            "defensive_rebounds": obj.get("defensiveRebounds"),
            "offensive_rebounds": obj.get("offensiveRebounds"),
            "true_shooting": obj.get("trueShooting"),
            "field_goals": ShootingStats.from_dict(obj.get("fieldGoals")) if obj.get("fieldGoals") is not None else None,
            "two_pointers": LineupUnitStatsTwoPointers.from_dict(obj.get("twoPointers")) if obj.get("twoPointers") is not None else None,
            "three_pointers": ShootingStats.from_dict(obj.get("threePointers")) if obj.get("threePointers") is not None else None,
            "free_throws": ShootingStats.from_dict(obj.get("freeThrows")) if obj.get("freeThrows") is not None else None,
            "four_factors": LineupUnitStatsFourFactors.from_dict(obj.get("fourFactors")) if obj.get("fourFactors") is not None else None
        })
        return _obj


