# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.18.1
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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from cbbd.models.game_status import GameStatus
from cbbd.models.season_type import SeasonType

class GameInfo(BaseModel):
    """
    GameInfo
    """
    id: StrictInt = Field(...)
    source_id: StrictStr = Field(default=..., alias="sourceId")
    season_label: StrictStr = Field(default=..., alias="seasonLabel")
    season: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    start_date: datetime = Field(default=..., alias="startDate")
    start_time_tbd: StrictBool = Field(default=..., alias="startTimeTbd")
    neutral_site: StrictBool = Field(default=..., alias="neutralSite")
    conference_game: StrictBool = Field(default=..., alias="conferenceGame")
    game_type: Optional[StrictStr] = Field(default=..., alias="gameType")
    status: GameStatus = Field(...)
    attendance: Optional[StrictInt] = Field(...)
    home_team_id: StrictInt = Field(default=..., alias="homeTeamId")
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    home_conference_id: Optional[StrictInt] = Field(default=..., alias="homeConferenceId")
    home_conference: Optional[StrictStr] = Field(default=..., alias="homeConference")
    home_points: Optional[StrictInt] = Field(default=..., alias="homePoints")
    home_period_points: Optional[conlist(StrictInt)] = Field(default=..., alias="homePeriodPoints")
    home_winner: Optional[StrictBool] = Field(default=..., alias="homeWinner")
    away_team_id: StrictInt = Field(default=..., alias="awayTeamId")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    away_conference_id: Optional[StrictInt] = Field(default=..., alias="awayConferenceId")
    away_conference: Optional[StrictStr] = Field(default=..., alias="awayConference")
    away_points: Optional[StrictInt] = Field(default=..., alias="awayPoints")
    away_period_points: Optional[conlist(StrictInt)] = Field(default=..., alias="awayPeriodPoints")
    away_winner: Optional[StrictBool] = Field(default=..., alias="awayWinner")
    excitement: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    venue_id: Optional[StrictInt] = Field(default=..., alias="venueId")
    venue: Optional[StrictStr] = Field(...)
    city: Optional[StrictStr] = Field(...)
    state: Optional[StrictStr] = Field(...)
    __properties = ["id", "sourceId", "seasonLabel", "season", "seasonType", "startDate", "startTimeTbd", "neutralSite", "conferenceGame", "gameType", "status", "attendance", "homeTeamId", "homeTeam", "homeConferenceId", "homeConference", "homePoints", "homePeriodPoints", "homeWinner", "awayTeamId", "awayTeam", "awayConferenceId", "awayConference", "awayPoints", "awayPeriodPoints", "awayWinner", "excitement", "venueId", "venue", "city", "state"]

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
    def from_json(cls, json_str: str) -> GameInfo:
        """Create an instance of GameInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if game_type (nullable) is None
        # and __fields_set__ contains the field
        if self.game_type is None and "game_type" in self.__fields_set__:
            _dict['gameType'] = None

        # set to None if attendance (nullable) is None
        # and __fields_set__ contains the field
        if self.attendance is None and "attendance" in self.__fields_set__:
            _dict['attendance'] = None

        # set to None if home_conference_id (nullable) is None
        # and __fields_set__ contains the field
        if self.home_conference_id is None and "home_conference_id" in self.__fields_set__:
            _dict['homeConferenceId'] = None

        # set to None if home_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.home_conference is None and "home_conference" in self.__fields_set__:
            _dict['homeConference'] = None

        # set to None if home_points (nullable) is None
        # and __fields_set__ contains the field
        if self.home_points is None and "home_points" in self.__fields_set__:
            _dict['homePoints'] = None

        # set to None if home_period_points (nullable) is None
        # and __fields_set__ contains the field
        if self.home_period_points is None and "home_period_points" in self.__fields_set__:
            _dict['homePeriodPoints'] = None

        # set to None if home_winner (nullable) is None
        # and __fields_set__ contains the field
        if self.home_winner is None and "home_winner" in self.__fields_set__:
            _dict['homeWinner'] = None

        # set to None if away_conference_id (nullable) is None
        # and __fields_set__ contains the field
        if self.away_conference_id is None and "away_conference_id" in self.__fields_set__:
            _dict['awayConferenceId'] = None

        # set to None if away_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.away_conference is None and "away_conference" in self.__fields_set__:
            _dict['awayConference'] = None

        # set to None if away_points (nullable) is None
        # and __fields_set__ contains the field
        if self.away_points is None and "away_points" in self.__fields_set__:
            _dict['awayPoints'] = None

        # set to None if away_period_points (nullable) is None
        # and __fields_set__ contains the field
        if self.away_period_points is None and "away_period_points" in self.__fields_set__:
            _dict['awayPeriodPoints'] = None

        # set to None if away_winner (nullable) is None
        # and __fields_set__ contains the field
        if self.away_winner is None and "away_winner" in self.__fields_set__:
            _dict['awayWinner'] = None

        # set to None if excitement (nullable) is None
        # and __fields_set__ contains the field
        if self.excitement is None and "excitement" in self.__fields_set__:
            _dict['excitement'] = None

        # set to None if venue_id (nullable) is None
        # and __fields_set__ contains the field
        if self.venue_id is None and "venue_id" in self.__fields_set__:
            _dict['venueId'] = None

        # set to None if venue (nullable) is None
        # and __fields_set__ contains the field
        if self.venue is None and "venue" in self.__fields_set__:
            _dict['venue'] = None

        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameInfo:
        """Create an instance of GameInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameInfo.parse_obj(obj)

        _obj = GameInfo.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "season_label": obj.get("seasonLabel"),
            "season": obj.get("season"),
            "season_type": obj.get("seasonType"),
            "start_date": obj.get("startDate"),
            "start_time_tbd": obj.get("startTimeTbd"),
            "neutral_site": obj.get("neutralSite"),
            "conference_game": obj.get("conferenceGame"),
            "game_type": obj.get("gameType"),
            "status": obj.get("status"),
            "attendance": obj.get("attendance"),
            "home_team_id": obj.get("homeTeamId"),
            "home_team": obj.get("homeTeam"),
            "home_conference_id": obj.get("homeConferenceId"),
            "home_conference": obj.get("homeConference"),
            "home_points": obj.get("homePoints"),
            "home_period_points": obj.get("homePeriodPoints"),
            "home_winner": obj.get("homeWinner"),
            "away_team_id": obj.get("awayTeamId"),
            "away_team": obj.get("awayTeam"),
            "away_conference_id": obj.get("awayConferenceId"),
            "away_conference": obj.get("awayConference"),
            "away_points": obj.get("awayPoints"),
            "away_period_points": obj.get("awayPeriodPoints"),
            "away_winner": obj.get("awayWinner"),
            "excitement": obj.get("excitement"),
            "venue_id": obj.get("venueId"),
            "venue": obj.get("venue"),
            "city": obj.get("city"),
            "state": obj.get("state")
        })
        return _obj


