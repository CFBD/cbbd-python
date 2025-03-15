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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class DraftPick(BaseModel):
    """
    DraftPick
    """
    athlete_id: Optional[StrictInt] = Field(default=..., alias="athleteId")
    source_team_id: Optional[StrictInt] = Field(default=..., alias="sourceTeamId")
    source_team_location: Optional[StrictStr] = Field(default=..., alias="sourceTeamLocation")
    source_team_name: Optional[StrictStr] = Field(default=..., alias="sourceTeamName")
    source_team_league_affiliation: Optional[StrictStr] = Field(default=..., alias="sourceTeamLeagueAffiliation")
    source_team_college_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="sourceTeamCollegeId")
    draft_team_id: Union[StrictFloat, StrictInt] = Field(default=..., alias="draftTeamId")
    draft_team: StrictStr = Field(default=..., alias="draftTeam")
    year: StrictInt = Field(...)
    overall: StrictInt = Field(...)
    round: StrictInt = Field(...)
    pick: StrictInt = Field(...)
    name: StrictStr = Field(...)
    overall_rank: Optional[StrictInt] = Field(default=..., alias="overallRank")
    position_rank: Optional[StrictInt] = Field(default=..., alias="positionRank")
    height: Optional[StrictInt] = Field(...)
    weight: Optional[StrictInt] = Field(...)
    __properties = ["athleteId", "sourceTeamId", "sourceTeamLocation", "sourceTeamName", "sourceTeamLeagueAffiliation", "sourceTeamCollegeId", "draftTeamId", "draftTeam", "year", "overall", "round", "pick", "name", "overallRank", "positionRank", "height", "weight"]

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
    def from_json(cls, json_str: str) -> DraftPick:
        """Create an instance of DraftPick from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if athlete_id (nullable) is None
        # and __fields_set__ contains the field
        if self.athlete_id is None and "athlete_id" in self.__fields_set__:
            _dict['athleteId'] = None

        # set to None if source_team_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_team_id is None and "source_team_id" in self.__fields_set__:
            _dict['sourceTeamId'] = None

        # set to None if source_team_location (nullable) is None
        # and __fields_set__ contains the field
        if self.source_team_location is None and "source_team_location" in self.__fields_set__:
            _dict['sourceTeamLocation'] = None

        # set to None if source_team_name (nullable) is None
        # and __fields_set__ contains the field
        if self.source_team_name is None and "source_team_name" in self.__fields_set__:
            _dict['sourceTeamName'] = None

        # set to None if source_team_league_affiliation (nullable) is None
        # and __fields_set__ contains the field
        if self.source_team_league_affiliation is None and "source_team_league_affiliation" in self.__fields_set__:
            _dict['sourceTeamLeagueAffiliation'] = None

        # set to None if source_team_college_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_team_college_id is None and "source_team_college_id" in self.__fields_set__:
            _dict['sourceTeamCollegeId'] = None

        # set to None if overall_rank (nullable) is None
        # and __fields_set__ contains the field
        if self.overall_rank is None and "overall_rank" in self.__fields_set__:
            _dict['overallRank'] = None

        # set to None if position_rank (nullable) is None
        # and __fields_set__ contains the field
        if self.position_rank is None and "position_rank" in self.__fields_set__:
            _dict['positionRank'] = None

        # set to None if height (nullable) is None
        # and __fields_set__ contains the field
        if self.height is None and "height" in self.__fields_set__:
            _dict['height'] = None

        # set to None if weight (nullable) is None
        # and __fields_set__ contains the field
        if self.weight is None and "weight" in self.__fields_set__:
            _dict['weight'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DraftPick:
        """Create an instance of DraftPick from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DraftPick.parse_obj(obj)

        _obj = DraftPick.parse_obj({
            "athlete_id": obj.get("athleteId"),
            "source_team_id": obj.get("sourceTeamId"),
            "source_team_location": obj.get("sourceTeamLocation"),
            "source_team_name": obj.get("sourceTeamName"),
            "source_team_league_affiliation": obj.get("sourceTeamLeagueAffiliation"),
            "source_team_college_id": obj.get("sourceTeamCollegeId"),
            "draft_team_id": obj.get("draftTeamId"),
            "draft_team": obj.get("draftTeam"),
            "year": obj.get("year"),
            "overall": obj.get("overall"),
            "round": obj.get("round"),
            "pick": obj.get("pick"),
            "name": obj.get("name"),
            "overall_rank": obj.get("overallRank"),
            "position_rank": obj.get("positionRank"),
            "height": obj.get("height"),
            "weight": obj.get("weight")
        })
        return _obj


