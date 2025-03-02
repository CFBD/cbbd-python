# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.16.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cbbd.models.team_roster_player_hometown import TeamRosterPlayerHometown

class TeamRosterPlayer(BaseModel):
    """
    TeamRosterPlayer
    """
    id: StrictInt = Field(...)
    source_id: StrictStr = Field(default=..., alias="sourceId")
    name: StrictStr = Field(...)
    first_name: Optional[StrictStr] = Field(default=..., alias="firstName")
    last_name: Optional[StrictStr] = Field(default=..., alias="lastName")
    jersey: Optional[StrictStr] = Field(...)
    position: Optional[StrictStr] = Field(...)
    height: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    hometown: TeamRosterPlayerHometown = Field(...)
    date_of_birth: Optional[date] = Field(default=..., alias="dateOfBirth")
    start_season: Union[StrictFloat, StrictInt] = Field(default=..., alias="startSeason")
    end_season: Union[StrictFloat, StrictInt] = Field(default=..., alias="endSeason")
    __properties = ["id", "sourceId", "name", "firstName", "lastName", "jersey", "position", "height", "weight", "hometown", "dateOfBirth", "startSeason", "endSeason"]

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
    def from_json(cls, json_str: str) -> TeamRosterPlayer:
        """Create an instance of TeamRosterPlayer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of hometown
        if self.hometown:
            _dict['hometown'] = self.hometown.to_dict()
        # set to None if first_name (nullable) is None
        # and __fields_set__ contains the field
        if self.first_name is None and "first_name" in self.__fields_set__:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and __fields_set__ contains the field
        if self.last_name is None and "last_name" in self.__fields_set__:
            _dict['lastName'] = None

        # set to None if jersey (nullable) is None
        # and __fields_set__ contains the field
        if self.jersey is None and "jersey" in self.__fields_set__:
            _dict['jersey'] = None

        # set to None if position (nullable) is None
        # and __fields_set__ contains the field
        if self.position is None and "position" in self.__fields_set__:
            _dict['position'] = None

        # set to None if height (nullable) is None
        # and __fields_set__ contains the field
        if self.height is None and "height" in self.__fields_set__:
            _dict['height'] = None

        # set to None if weight (nullable) is None
        # and __fields_set__ contains the field
        if self.weight is None and "weight" in self.__fields_set__:
            _dict['weight'] = None

        # set to None if date_of_birth (nullable) is None
        # and __fields_set__ contains the field
        if self.date_of_birth is None and "date_of_birth" in self.__fields_set__:
            _dict['dateOfBirth'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamRosterPlayer:
        """Create an instance of TeamRosterPlayer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamRosterPlayer.parse_obj(obj)

        _obj = TeamRosterPlayer.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "name": obj.get("name"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "jersey": obj.get("jersey"),
            "position": obj.get("position"),
            "height": obj.get("height"),
            "weight": obj.get("weight"),
            "hometown": TeamRosterPlayerHometown.from_dict(obj.get("hometown")) if obj.get("hometown") is not None else None,
            "date_of_birth": obj.get("dateOfBirth"),
            "start_season": obj.get("startSeason"),
            "end_season": obj.get("endSeason")
        })
        return _obj


