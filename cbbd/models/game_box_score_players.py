# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.4.0
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
from cbbd.models.game_box_score_players_players_inner import GameBoxScorePlayersPlayersInner
from cbbd.models.season_type import SeasonType

class GameBoxScorePlayers(BaseModel):
    """
    GameBoxScorePlayers
    """
    game_id: StrictInt = Field(default=..., alias="gameId")
    season: StrictInt = Field(...)
    season_label: StrictStr = Field(default=..., alias="seasonLabel")
    season_type: SeasonType = Field(default=..., alias="seasonType")
    start_date: datetime = Field(default=..., alias="startDate")
    start_time_tbd: StrictBool = Field(default=..., alias="startTimeTbd")
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    opponent_id: StrictInt = Field(default=..., alias="opponentId")
    opponent: StrictStr = Field(...)
    opponent_conference: Optional[StrictStr] = Field(default=..., alias="opponentConference")
    neutral_site: StrictBool = Field(default=..., alias="neutralSite")
    conference_game: StrictBool = Field(default=..., alias="conferenceGame")
    game_type: Optional[StrictStr] = Field(default=..., alias="gameType")
    notes: Optional[StrictStr] = Field(...)
    game_minutes: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="gameMinutes")
    game_pace: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="gamePace")
    players: conlist(GameBoxScorePlayersPlayersInner) = Field(...)
    __properties = ["gameId", "season", "seasonLabel", "seasonType", "startDate", "startTimeTbd", "teamId", "team", "conference", "opponentId", "opponent", "opponentConference", "neutralSite", "conferenceGame", "gameType", "notes", "gameMinutes", "gamePace", "players"]

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
    def from_json(cls, json_str: str) -> GameBoxScorePlayers:
        """Create an instance of GameBoxScorePlayers from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in players (list)
        _items = []
        if self.players:
            for _item in self.players:
                if _item:
                    _items.append(_item.to_dict())
            _dict['players'] = _items
        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if opponent_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.opponent_conference is None and "opponent_conference" in self.__fields_set__:
            _dict['opponentConference'] = None

        # set to None if game_type (nullable) is None
        # and __fields_set__ contains the field
        if self.game_type is None and "game_type" in self.__fields_set__:
            _dict['gameType'] = None

        # set to None if notes (nullable) is None
        # and __fields_set__ contains the field
        if self.notes is None and "notes" in self.__fields_set__:
            _dict['notes'] = None

        # set to None if game_minutes (nullable) is None
        # and __fields_set__ contains the field
        if self.game_minutes is None and "game_minutes" in self.__fields_set__:
            _dict['gameMinutes'] = None

        # set to None if game_pace (nullable) is None
        # and __fields_set__ contains the field
        if self.game_pace is None and "game_pace" in self.__fields_set__:
            _dict['gamePace'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameBoxScorePlayers:
        """Create an instance of GameBoxScorePlayers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameBoxScorePlayers.parse_obj(obj)

        _obj = GameBoxScorePlayers.parse_obj({
            "game_id": obj.get("gameId"),
            "season": obj.get("season"),
            "season_label": obj.get("seasonLabel"),
            "season_type": obj.get("seasonType"),
            "start_date": obj.get("startDate"),
            "start_time_tbd": obj.get("startTimeTbd"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "opponent_id": obj.get("opponentId"),
            "opponent": obj.get("opponent"),
            "opponent_conference": obj.get("opponentConference"),
            "neutral_site": obj.get("neutralSite"),
            "conference_game": obj.get("conferenceGame"),
            "game_type": obj.get("gameType"),
            "notes": obj.get("notes"),
            "game_minutes": obj.get("gameMinutes"),
            "game_pace": obj.get("gamePace"),
            "players": [GameBoxScorePlayersPlayersInner.from_dict(_item) for _item in obj.get("players")] if obj.get("players") is not None else None
        })
        return _obj


