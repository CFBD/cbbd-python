# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.6.0
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

class TeamSeasonUnitStatsFouls(BaseModel):
    """
    TeamSeasonUnitStatsFouls
    """
    flagrant: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    technical: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    total: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["flagrant", "technical", "total"]

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
    def from_json(cls, json_str: str) -> TeamSeasonUnitStatsFouls:
        """Create an instance of TeamSeasonUnitStatsFouls from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if flagrant (nullable) is None
        # and __fields_set__ contains the field
        if self.flagrant is None and "flagrant" in self.__fields_set__:
            _dict['flagrant'] = None

        # set to None if technical (nullable) is None
        # and __fields_set__ contains the field
        if self.technical is None and "technical" in self.__fields_set__:
            _dict['technical'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamSeasonUnitStatsFouls:
        """Create an instance of TeamSeasonUnitStatsFouls from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamSeasonUnitStatsFouls.parse_obj(obj)

        _obj = TeamSeasonUnitStatsFouls.parse_obj({
            "flagrant": obj.get("flagrant"),
            "technical": obj.get("technical"),
            "total": obj.get("total")
        })
        return _obj


