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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class TeamRosterPlayerHometown(BaseModel):
    """
    TeamRosterPlayerHometown
    """
    county_fips: Optional[StrictStr] = Field(default=..., alias="countyFips")
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    country: Optional[StrictStr] = Field(...)
    state: Optional[StrictStr] = Field(...)
    city: Optional[StrictStr] = Field(...)
    __properties = ["countyFips", "longitude", "latitude", "country", "state", "city"]

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
    def from_json(cls, json_str: str) -> TeamRosterPlayerHometown:
        """Create an instance of TeamRosterPlayerHometown from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if county_fips (nullable) is None
        # and __fields_set__ contains the field
        if self.county_fips is None and "county_fips" in self.__fields_set__:
            _dict['countyFips'] = None

        # set to None if longitude (nullable) is None
        # and __fields_set__ contains the field
        if self.longitude is None and "longitude" in self.__fields_set__:
            _dict['longitude'] = None

        # set to None if latitude (nullable) is None
        # and __fields_set__ contains the field
        if self.latitude is None and "latitude" in self.__fields_set__:
            _dict['latitude'] = None

        # set to None if country (nullable) is None
        # and __fields_set__ contains the field
        if self.country is None and "country" in self.__fields_set__:
            _dict['country'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamRosterPlayerHometown:
        """Create an instance of TeamRosterPlayerHometown from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamRosterPlayerHometown.parse_obj(obj)

        _obj = TeamRosterPlayerHometown.parse_obj({
            "county_fips": obj.get("countyFips"),
            "longitude": obj.get("longitude"),
            "latitude": obj.get("latitude"),
            "country": obj.get("country"),
            "state": obj.get("state"),
            "city": obj.get("city")
        })
        return _obj


