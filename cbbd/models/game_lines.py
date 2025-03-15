# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.19.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from cbbd.models.game_line_info import GameLineInfo
from cbbd.models.season_type import SeasonType

class GameLines(BaseModel):
    """
    GameLines
    """
    game_id: StrictInt = Field(default=..., alias="gameId")
    season: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    start_date: datetime = Field(default=..., alias="startDate")
    home_team_id: StrictInt = Field(default=..., alias="homeTeamId")
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    home_conference: Optional[StrictStr] = Field(default=..., alias="homeConference")
    home_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="homeScore")
    away_team_id: StrictInt = Field(default=..., alias="awayTeamId")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    away_conference: Optional[StrictStr] = Field(default=..., alias="awayConference")
    away_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="awayScore")
    lines: conlist(GameLineInfo) = Field(...)
    __properties = ["gameId", "season", "seasonType", "startDate", "homeTeamId", "homeTeam", "homeConference", "homeScore", "awayTeamId", "awayTeam", "awayConference", "awayScore", "lines"]

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
    def from_json(cls, json_str: str) -> GameLines:
        """Create an instance of GameLines from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        # set to None if home_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.home_conference is None and "home_conference" in self.__fields_set__:
            _dict['homeConference'] = None

        # set to None if home_score (nullable) is None
        # and __fields_set__ contains the field
        if self.home_score is None and "home_score" in self.__fields_set__:
            _dict['homeScore'] = None

        # set to None if away_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.away_conference is None and "away_conference" in self.__fields_set__:
            _dict['awayConference'] = None

        # set to None if away_score (nullable) is None
        # and __fields_set__ contains the field
        if self.away_score is None and "away_score" in self.__fields_set__:
            _dict['awayScore'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameLines:
        """Create an instance of GameLines from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameLines.parse_obj(obj)

        _obj = GameLines.parse_obj({
            "game_id": obj.get("gameId"),
            "season": obj.get("season"),
            "season_type": obj.get("seasonType"),
            "start_date": obj.get("startDate"),
            "home_team_id": obj.get("homeTeamId"),
            "home_team": obj.get("homeTeam"),
            "home_conference": obj.get("homeConference"),
            "home_score": obj.get("homeScore"),
            "away_team_id": obj.get("awayTeamId"),
            "away_team": obj.get("awayTeam"),
            "away_conference": obj.get("awayConference"),
            "away_score": obj.get("awayScore"),
            "lines": [GameLineInfo.from_dict(_item) for _item in obj.get("lines")] if obj.get("lines") is not None else None
        })
        return _obj


