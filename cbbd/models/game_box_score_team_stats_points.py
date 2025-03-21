# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.20.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist

class GameBoxScoreTeamStatsPoints(BaseModel):
    """
    GameBoxScoreTeamStatsPoints
    """
    fast_break: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="fastBreak")
    off_turnovers: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="offTurnovers")
    in_paint: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="inPaint")
    by_period: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(default=..., alias="byPeriod")
    largest_lead: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="largestLead")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["fastBreak", "offTurnovers", "inPaint", "byPeriod", "largestLead", "total"]

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
    def from_json(cls, json_str: str) -> GameBoxScoreTeamStatsPoints:
        """Create an instance of GameBoxScoreTeamStatsPoints from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if fast_break (nullable) is None
        # and __fields_set__ contains the field
        if self.fast_break is None and "fast_break" in self.__fields_set__:
            _dict['fastBreak'] = None

        # set to None if off_turnovers (nullable) is None
        # and __fields_set__ contains the field
        if self.off_turnovers is None and "off_turnovers" in self.__fields_set__:
            _dict['offTurnovers'] = None

        # set to None if in_paint (nullable) is None
        # and __fields_set__ contains the field
        if self.in_paint is None and "in_paint" in self.__fields_set__:
            _dict['inPaint'] = None

        # set to None if by_period (nullable) is None
        # and __fields_set__ contains the field
        if self.by_period is None and "by_period" in self.__fields_set__:
            _dict['byPeriod'] = None

        # set to None if largest_lead (nullable) is None
        # and __fields_set__ contains the field
        if self.largest_lead is None and "largest_lead" in self.__fields_set__:
            _dict['largestLead'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameBoxScoreTeamStatsPoints:
        """Create an instance of GameBoxScoreTeamStatsPoints from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameBoxScoreTeamStatsPoints.parse_obj(obj)

        _obj = GameBoxScoreTeamStatsPoints.parse_obj({
            "fast_break": obj.get("fastBreak"),
            "off_turnovers": obj.get("offTurnovers"),
            "in_paint": obj.get("inPaint"),
            "by_period": obj.get("byPeriod"),
            "largest_lead": obj.get("largestLead"),
            "total": obj.get("total")
        })
        return _obj


