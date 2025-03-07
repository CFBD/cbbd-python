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



from pydantic import BaseModel, Field, StrictInt

class PlayerSubsititutionSubIn(BaseModel):
    """
    PlayerSubsititutionSubIn
    """
    opponent_points: StrictInt = Field(default=..., alias="opponentPoints")
    team_points: StrictInt = Field(default=..., alias="teamPoints")
    seconds_remaining: StrictInt = Field(default=..., alias="secondsRemaining")
    period: StrictInt = Field(...)
    __properties = ["opponentPoints", "teamPoints", "secondsRemaining", "period"]

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
    def from_json(cls, json_str: str) -> PlayerSubsititutionSubIn:
        """Create an instance of PlayerSubsititutionSubIn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerSubsititutionSubIn:
        """Create an instance of PlayerSubsititutionSubIn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerSubsititutionSubIn.parse_obj(obj)

        _obj = PlayerSubsititutionSubIn.parse_obj({
            "opponent_points": obj.get("opponentPoints"),
            "team_points": obj.get("teamPoints"),
            "seconds_remaining": obj.get("secondsRemaining"),
            "period": obj.get("period")
        })
        return _obj


