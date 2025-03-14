# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.19.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from cbbd.models.shooting_stats import ShootingStats

class LineupUnitStatsTwoPointers(BaseModel):
    """
    LineupUnitStatsTwoPointers
    """
    made: StrictInt = Field(...)
    attempted: StrictInt = Field(...)
    pct: Union[StrictFloat, StrictInt] = Field(...)
    jumpers: ShootingStats = Field(...)
    layups: ShootingStats = Field(...)
    dunks: ShootingStats = Field(...)
    tip_ins: ShootingStats = Field(default=..., alias="tipIns")
    __properties = ["made", "attempted", "pct", "jumpers", "layups", "dunks", "tipIns"]

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
    def from_json(cls, json_str: str) -> LineupUnitStatsTwoPointers:
        """Create an instance of LineupUnitStatsTwoPointers from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of jumpers
        if self.jumpers:
            _dict['jumpers'] = self.jumpers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of layups
        if self.layups:
            _dict['layups'] = self.layups.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dunks
        if self.dunks:
            _dict['dunks'] = self.dunks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tip_ins
        if self.tip_ins:
            _dict['tipIns'] = self.tip_ins.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LineupUnitStatsTwoPointers:
        """Create an instance of LineupUnitStatsTwoPointers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LineupUnitStatsTwoPointers.parse_obj(obj)

        _obj = LineupUnitStatsTwoPointers.parse_obj({
            "made": obj.get("made"),
            "attempted": obj.get("attempted"),
            "pct": obj.get("pct"),
            "jumpers": ShootingStats.from_dict(obj.get("jumpers")) if obj.get("jumpers") is not None else None,
            "layups": ShootingStats.from_dict(obj.get("layups")) if obj.get("layups") is not None else None,
            "dunks": ShootingStats.from_dict(obj.get("dunks")) if obj.get("dunks") is not None else None,
            "tip_ins": ShootingStats.from_dict(obj.get("tipIns")) if obj.get("tipIns") is not None else None
        })
        return _obj


