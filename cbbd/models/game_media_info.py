# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.11.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from cbbd.models.game_media_info_broadcasts_inner import GameMediaInfoBroadcastsInner
from cbbd.models.season_type import SeasonType

class GameMediaInfo(BaseModel):
    """
    GameMediaInfo
    """
    game_id: StrictInt = Field(default=..., alias="gameId")
    season: StrictInt = Field(...)
    season_label: StrictStr = Field(default=..., alias="seasonLabel")
    season_type: SeasonType = Field(default=..., alias="seasonType")
    start_date: datetime = Field(default=..., alias="startDate")
    start_time_tbd: StrictBool = Field(default=..., alias="startTimeTbd")
    home_team_id: StrictInt = Field(default=..., alias="homeTeamId")
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    home_conference: Optional[StrictStr] = Field(default=..., alias="homeConference")
    away_team_id: StrictInt = Field(default=..., alias="awayTeamId")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    away_conference: Optional[StrictStr] = Field(default=..., alias="awayConference")
    neutral_site: StrictBool = Field(default=..., alias="neutralSite")
    conference_game: StrictBool = Field(default=..., alias="conferenceGame")
    game_type: Optional[StrictStr] = Field(default=..., alias="gameType")
    notes: Optional[StrictStr] = Field(...)
    broadcasts: conlist(GameMediaInfoBroadcastsInner) = Field(...)
    __properties = ["gameId", "season", "seasonLabel", "seasonType", "startDate", "startTimeTbd", "homeTeamId", "homeTeam", "homeConference", "awayTeamId", "awayTeam", "awayConference", "neutralSite", "conferenceGame", "gameType", "notes", "broadcasts"]

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
    def from_json(cls, json_str: str) -> GameMediaInfo:
        """Create an instance of GameMediaInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in broadcasts (list)
        _items = []
        if self.broadcasts:
            for _item in self.broadcasts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['broadcasts'] = _items
        # set to None if home_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.home_conference is None and "home_conference" in self.__fields_set__:
            _dict['homeConference'] = None

        # set to None if away_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.away_conference is None and "away_conference" in self.__fields_set__:
            _dict['awayConference'] = None

        # set to None if game_type (nullable) is None
        # and __fields_set__ contains the field
        if self.game_type is None and "game_type" in self.__fields_set__:
            _dict['gameType'] = None

        # set to None if notes (nullable) is None
        # and __fields_set__ contains the field
        if self.notes is None and "notes" in self.__fields_set__:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameMediaInfo:
        """Create an instance of GameMediaInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameMediaInfo.parse_obj(obj)

        _obj = GameMediaInfo.parse_obj({
            "game_id": obj.get("gameId"),
            "season": obj.get("season"),
            "season_label": obj.get("seasonLabel"),
            "season_type": obj.get("seasonType"),
            "start_date": obj.get("startDate"),
            "start_time_tbd": obj.get("startTimeTbd"),
            "home_team_id": obj.get("homeTeamId"),
            "home_team": obj.get("homeTeam"),
            "home_conference": obj.get("homeConference"),
            "away_team_id": obj.get("awayTeamId"),
            "away_team": obj.get("awayTeam"),
            "away_conference": obj.get("awayConference"),
            "neutral_site": obj.get("neutralSite"),
            "conference_game": obj.get("conferenceGame"),
            "game_type": obj.get("gameType"),
            "notes": obj.get("notes"),
            "broadcasts": [GameMediaInfoBroadcastsInner.from_dict(_item) for _item in obj.get("broadcasts")] if obj.get("broadcasts") is not None else None
        })
        return _obj


