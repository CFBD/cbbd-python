# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.15.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class ConferenceHistoryTeamsInner(BaseModel):
    """
    ConferenceHistoryTeamsInner
    """
    end_season: Optional[StrictInt] = Field(default=..., alias="endSeason")
    start_season: StrictInt = Field(default=..., alias="startSeason")
    mascot: Optional[StrictStr] = Field(...)
    school: StrictStr = Field(...)
    source_id: StrictStr = Field(default=..., alias="sourceId")
    id: StrictInt = Field(...)
    __properties = ["endSeason", "startSeason", "mascot", "school", "sourceId", "id"]

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
    def from_json(cls, json_str: str) -> ConferenceHistoryTeamsInner:
        """Create an instance of ConferenceHistoryTeamsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if end_season (nullable) is None
        # and __fields_set__ contains the field
        if self.end_season is None and "end_season" in self.__fields_set__:
            _dict['endSeason'] = None

        # set to None if mascot (nullable) is None
        # and __fields_set__ contains the field
        if self.mascot is None and "mascot" in self.__fields_set__:
            _dict['mascot'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConferenceHistoryTeamsInner:
        """Create an instance of ConferenceHistoryTeamsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConferenceHistoryTeamsInner.parse_obj(obj)

        _obj = ConferenceHistoryTeamsInner.parse_obj({
            "end_season": obj.get("endSeason"),
            "start_season": obj.get("startSeason"),
            "mascot": obj.get("mascot"),
            "school": obj.get("school"),
            "source_id": obj.get("sourceId"),
            "id": obj.get("id")
        })
        return _obj


