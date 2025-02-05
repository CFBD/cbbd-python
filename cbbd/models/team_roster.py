# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.7.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from cbbd.models.team_roster_player import TeamRosterPlayer

class TeamRoster(BaseModel):
    """
    TeamRoster
    """
    team_id: StrictInt = Field(default=..., alias="teamId")
    team_source_id: StrictStr = Field(default=..., alias="teamSourceId")
    team: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    season: Union[StrictFloat, StrictInt] = Field(...)
    players: conlist(TeamRosterPlayer) = Field(...)
    __properties = ["teamId", "teamSourceId", "team", "conference", "season", "players"]

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
    def from_json(cls, json_str: str) -> TeamRoster:
        """Create an instance of TeamRoster from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamRoster:
        """Create an instance of TeamRoster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamRoster.parse_obj(obj)

        _obj = TeamRoster.parse_obj({
            "team_id": obj.get("teamId"),
            "team_source_id": obj.get("teamSourceId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "season": obj.get("season"),
            "players": [TeamRosterPlayer.from_dict(_item) for _item in obj.get("players")] if obj.get("players") is not None else None
        })
        return _obj


