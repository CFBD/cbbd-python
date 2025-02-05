# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.7.2
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
from cbbd.models.play_info_participants_inner import PlayInfoParticipantsInner
from cbbd.models.season_type import SeasonType

class PlayInfo(BaseModel):
    """
    PlayInfo
    """
    id: StrictInt = Field(...)
    source_id: StrictStr = Field(default=..., alias="sourceId")
    game_id: StrictInt = Field(default=..., alias="gameId")
    game_source_id: StrictStr = Field(default=..., alias="gameSourceId")
    game_start_date: datetime = Field(default=..., alias="gameStartDate")
    season: Union[StrictFloat, StrictInt] = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    game_type: StrictStr = Field(default=..., alias="gameType")
    play_type: StrictStr = Field(default=..., alias="playType")
    is_home_team: Optional[StrictBool] = Field(default=..., alias="isHomeTeam")
    team_id: Optional[StrictInt] = Field(default=..., alias="teamId")
    team: Optional[StrictStr] = Field(...)
    conference: Optional[StrictStr] = Field(...)
    opponent_id: Optional[StrictInt] = Field(default=..., alias="opponentId")
    opponent: Optional[StrictStr] = Field(...)
    opponent_conference: Optional[StrictStr] = Field(default=..., alias="opponentConference")
    period: StrictInt = Field(...)
    clock: StrictStr = Field(...)
    seconds_remaining: StrictInt = Field(default=..., alias="secondsRemaining")
    home_score: StrictInt = Field(default=..., alias="homeScore")
    away_score: StrictInt = Field(default=..., alias="awayScore")
    home_win_probability: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="homeWinProbability")
    scoring_play: Optional[StrictBool] = Field(default=..., alias="scoringPlay")
    shooting_play: Optional[StrictBool] = Field(default=..., alias="shootingPlay")
    score_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="scoreValue")
    wallclock: Optional[datetime] = Field(...)
    play_text: Optional[StrictStr] = Field(default=..., alias="playText")
    participants: conlist(PlayInfoParticipantsInner) = Field(...)
    __properties = ["id", "sourceId", "gameId", "gameSourceId", "gameStartDate", "season", "seasonType", "gameType", "playType", "isHomeTeam", "teamId", "team", "conference", "opponentId", "opponent", "opponentConference", "period", "clock", "secondsRemaining", "homeScore", "awayScore", "homeWinProbability", "scoringPlay", "shootingPlay", "scoreValue", "wallclock", "playText", "participants"]

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
    def from_json(cls, json_str: str) -> PlayInfo:
        """Create an instance of PlayInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in participants (list)
        _items = []
        if self.participants:
            for _item in self.participants:
                if _item:
                    _items.append(_item.to_dict())
            _dict['participants'] = _items
        # set to None if is_home_team (nullable) is None
        # and __fields_set__ contains the field
        if self.is_home_team is None and "is_home_team" in self.__fields_set__:
            _dict['isHomeTeam'] = None

        # set to None if team_id (nullable) is None
        # and __fields_set__ contains the field
        if self.team_id is None and "team_id" in self.__fields_set__:
            _dict['teamId'] = None

        # set to None if team (nullable) is None
        # and __fields_set__ contains the field
        if self.team is None and "team" in self.__fields_set__:
            _dict['team'] = None

        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if opponent_id (nullable) is None
        # and __fields_set__ contains the field
        if self.opponent_id is None and "opponent_id" in self.__fields_set__:
            _dict['opponentId'] = None

        # set to None if opponent (nullable) is None
        # and __fields_set__ contains the field
        if self.opponent is None and "opponent" in self.__fields_set__:
            _dict['opponent'] = None

        # set to None if opponent_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.opponent_conference is None and "opponent_conference" in self.__fields_set__:
            _dict['opponentConference'] = None

        # set to None if home_win_probability (nullable) is None
        # and __fields_set__ contains the field
        if self.home_win_probability is None and "home_win_probability" in self.__fields_set__:
            _dict['homeWinProbability'] = None

        # set to None if scoring_play (nullable) is None
        # and __fields_set__ contains the field
        if self.scoring_play is None and "scoring_play" in self.__fields_set__:
            _dict['scoringPlay'] = None

        # set to None if shooting_play (nullable) is None
        # and __fields_set__ contains the field
        if self.shooting_play is None and "shooting_play" in self.__fields_set__:
            _dict['shootingPlay'] = None

        # set to None if score_value (nullable) is None
        # and __fields_set__ contains the field
        if self.score_value is None and "score_value" in self.__fields_set__:
            _dict['scoreValue'] = None

        # set to None if wallclock (nullable) is None
        # and __fields_set__ contains the field
        if self.wallclock is None and "wallclock" in self.__fields_set__:
            _dict['wallclock'] = None

        # set to None if play_text (nullable) is None
        # and __fields_set__ contains the field
        if self.play_text is None and "play_text" in self.__fields_set__:
            _dict['playText'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayInfo:
        """Create an instance of PlayInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayInfo.parse_obj(obj)

        _obj = PlayInfo.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "game_id": obj.get("gameId"),
            "game_source_id": obj.get("gameSourceId"),
            "game_start_date": obj.get("gameStartDate"),
            "season": obj.get("season"),
            "season_type": obj.get("seasonType"),
            "game_type": obj.get("gameType"),
            "play_type": obj.get("playType"),
            "is_home_team": obj.get("isHomeTeam"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "opponent_id": obj.get("opponentId"),
            "opponent": obj.get("opponent"),
            "opponent_conference": obj.get("opponentConference"),
            "period": obj.get("period"),
            "clock": obj.get("clock"),
            "seconds_remaining": obj.get("secondsRemaining"),
            "home_score": obj.get("homeScore"),
            "away_score": obj.get("awayScore"),
            "home_win_probability": obj.get("homeWinProbability"),
            "scoring_play": obj.get("scoringPlay"),
            "shooting_play": obj.get("shootingPlay"),
            "score_value": obj.get("scoreValue"),
            "wallclock": obj.get("wallclock"),
            "play_text": obj.get("playText"),
            "participants": [PlayInfoParticipantsInner.from_dict(_item) for _item in obj.get("participants")] if obj.get("participants") is not None else None
        })
        return _obj


