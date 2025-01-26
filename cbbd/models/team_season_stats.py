# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.1.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cbbd.models.team_season_unit_stats import TeamSeasonUnitStats

class TeamSeasonStats(BaseModel):
    """
    TeamSeasonStats
    """
    season: StrictInt = Field(...)
    season_label: StrictStr = Field(default=..., alias="seasonLabel")
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    games: StrictInt = Field(...)
    total_minutes: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="totalMinutes")
    pace: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    offense: TeamSeasonUnitStats = Field(...)
    defense: TeamSeasonUnitStats = Field(...)
    __properties = ["season", "seasonLabel", "teamId", "team", "conference", "games", "totalMinutes", "pace", "offense", "defense"]

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
    def from_json(cls, json_str: str) -> TeamSeasonStats:
        """Create an instance of TeamSeasonStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of offense
        if self.offense:
            _dict['offense'] = self.offense.to_dict()
        # override the default output from pydantic by calling `to_dict()` of defense
        if self.defense:
            _dict['defense'] = self.defense.to_dict()
        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if total_minutes (nullable) is None
        # and __fields_set__ contains the field
        if self.total_minutes is None and "total_minutes" in self.__fields_set__:
            _dict['totalMinutes'] = None

        # set to None if pace (nullable) is None
        # and __fields_set__ contains the field
        if self.pace is None and "pace" in self.__fields_set__:
            _dict['pace'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamSeasonStats:
        """Create an instance of TeamSeasonStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamSeasonStats.parse_obj(obj)

        _obj = TeamSeasonStats.parse_obj({
            "season": obj.get("season"),
            "season_label": obj.get("seasonLabel"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "games": obj.get("games"),
            "total_minutes": obj.get("totalMinutes"),
            "pace": obj.get("pace"),
            "offense": TeamSeasonUnitStats.from_dict(obj.get("offense")) if obj.get("offense") is not None else None,
            "defense": TeamSeasonUnitStats.from_dict(obj.get("defense")) if obj.get("defense") is not None else None
        })
        return _obj


