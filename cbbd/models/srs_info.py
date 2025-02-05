# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.7.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class SrsInfo(BaseModel):
    """
    SrsInfo
    """
    season: StrictInt = Field(...)
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    rating: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["season", "teamId", "team", "conference", "rating"]

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
    def from_json(cls, json_str: str) -> SrsInfo:
        """Create an instance of SrsInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SrsInfo:
        """Create an instance of SrsInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SrsInfo.parse_obj(obj)

        _obj = SrsInfo.parse_obj({
            "season": obj.get("season"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "rating": obj.get("rating")
        })
        return _obj


