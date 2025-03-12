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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class TeamSeasonUnitStatsTurnovers(BaseModel):
    """
    TeamSeasonUnitStatsTurnovers
    """
    team_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="teamTotal")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["teamTotal", "total"]

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
    def from_json(cls, json_str: str) -> TeamSeasonUnitStatsTurnovers:
        """Create an instance of TeamSeasonUnitStatsTurnovers from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if team_total (nullable) is None
        # and __fields_set__ contains the field
        if self.team_total is None and "team_total" in self.__fields_set__:
            _dict['teamTotal'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamSeasonUnitStatsTurnovers:
        """Create an instance of TeamSeasonUnitStatsTurnovers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamSeasonUnitStatsTurnovers.parse_obj(obj)

        _obj = TeamSeasonUnitStatsTurnovers.parse_obj({
            "team_total": obj.get("teamTotal"),
            "total": obj.get("total")
        })
        return _obj


