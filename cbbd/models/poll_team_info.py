# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.17.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cbbd.models.season_type import SeasonType

class PollTeamInfo(BaseModel):
    """
    PollTeamInfo
    """
    season: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    week: StrictInt = Field(...)
    poll_date: Optional[datetime] = Field(default=..., alias="pollDate")
    poll_type: StrictStr = Field(default=..., alias="pollType")
    team_id: Union[StrictFloat, StrictInt] = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    ranking: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    points: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    first_place_votes: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="firstPlaceVotes")
    __properties = ["season", "seasonType", "week", "pollDate", "pollType", "teamId", "team", "conference", "ranking", "points", "firstPlaceVotes"]

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
    def from_json(cls, json_str: str) -> PollTeamInfo:
        """Create an instance of PollTeamInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if poll_date (nullable) is None
        # and __fields_set__ contains the field
        if self.poll_date is None and "poll_date" in self.__fields_set__:
            _dict['pollDate'] = None

        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if ranking (nullable) is None
        # and __fields_set__ contains the field
        if self.ranking is None and "ranking" in self.__fields_set__:
            _dict['ranking'] = None

        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        # set to None if first_place_votes (nullable) is None
        # and __fields_set__ contains the field
        if self.first_place_votes is None and "first_place_votes" in self.__fields_set__:
            _dict['firstPlaceVotes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PollTeamInfo:
        """Create an instance of PollTeamInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PollTeamInfo.parse_obj(obj)

        _obj = PollTeamInfo.parse_obj({
            "season": obj.get("season"),
            "season_type": obj.get("seasonType"),
            "week": obj.get("week"),
            "poll_date": obj.get("pollDate"),
            "poll_type": obj.get("pollType"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "ranking": obj.get("ranking"),
            "points": obj.get("points"),
            "first_place_votes": obj.get("firstPlaceVotes")
        })
        return _obj


