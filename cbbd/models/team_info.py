# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.7.3
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

class TeamInfo(BaseModel):
    """
    TeamInfo
    """
    id: StrictInt = Field(...)
    source_id: StrictStr = Field(default=..., alias="sourceId")
    school: StrictStr = Field(...)
    mascot: Optional[StrictStr] = Field(...)
    abbreviation: Optional[StrictStr] = Field(...)
    display_name: Optional[StrictStr] = Field(default=..., alias="displayName")
    short_display_name: Optional[StrictStr] = Field(default=..., alias="shortDisplayName")
    primary_color: Optional[StrictStr] = Field(default=..., alias="primaryColor")
    secondary_color: Optional[StrictStr] = Field(default=..., alias="secondaryColor")
    current_venue_id: Optional[StrictInt] = Field(default=..., alias="currentVenueId")
    current_venue: Optional[StrictStr] = Field(default=..., alias="currentVenue")
    current_city: Optional[StrictStr] = Field(default=..., alias="currentCity")
    current_state: Optional[StrictStr] = Field(default=..., alias="currentState")
    conference_id: Optional[StrictInt] = Field(default=..., alias="conferenceId")
    conference: Optional[StrictStr] = Field(...)
    __properties = ["id", "sourceId", "school", "mascot", "abbreviation", "displayName", "shortDisplayName", "primaryColor", "secondaryColor", "currentVenueId", "currentVenue", "currentCity", "currentState", "conferenceId", "conference"]

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
    def from_json(cls, json_str: str) -> TeamInfo:
        """Create an instance of TeamInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if mascot (nullable) is None
        # and __fields_set__ contains the field
        if self.mascot is None and "mascot" in self.__fields_set__:
            _dict['mascot'] = None

        # set to None if abbreviation (nullable) is None
        # and __fields_set__ contains the field
        if self.abbreviation is None and "abbreviation" in self.__fields_set__:
            _dict['abbreviation'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if short_display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.short_display_name is None and "short_display_name" in self.__fields_set__:
            _dict['shortDisplayName'] = None

        # set to None if primary_color (nullable) is None
        # and __fields_set__ contains the field
        if self.primary_color is None and "primary_color" in self.__fields_set__:
            _dict['primaryColor'] = None

        # set to None if secondary_color (nullable) is None
        # and __fields_set__ contains the field
        if self.secondary_color is None and "secondary_color" in self.__fields_set__:
            _dict['secondaryColor'] = None

        # set to None if current_venue_id (nullable) is None
        # and __fields_set__ contains the field
        if self.current_venue_id is None and "current_venue_id" in self.__fields_set__:
            _dict['currentVenueId'] = None

        # set to None if current_venue (nullable) is None
        # and __fields_set__ contains the field
        if self.current_venue is None and "current_venue" in self.__fields_set__:
            _dict['currentVenue'] = None

        # set to None if current_city (nullable) is None
        # and __fields_set__ contains the field
        if self.current_city is None and "current_city" in self.__fields_set__:
            _dict['currentCity'] = None

        # set to None if current_state (nullable) is None
        # and __fields_set__ contains the field
        if self.current_state is None and "current_state" in self.__fields_set__:
            _dict['currentState'] = None

        # set to None if conference_id (nullable) is None
        # and __fields_set__ contains the field
        if self.conference_id is None and "conference_id" in self.__fields_set__:
            _dict['conferenceId'] = None

        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamInfo:
        """Create an instance of TeamInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamInfo.parse_obj(obj)

        _obj = TeamInfo.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "school": obj.get("school"),
            "mascot": obj.get("mascot"),
            "abbreviation": obj.get("abbreviation"),
            "display_name": obj.get("displayName"),
            "short_display_name": obj.get("shortDisplayName"),
            "primary_color": obj.get("primaryColor"),
            "secondary_color": obj.get("secondaryColor"),
            "current_venue_id": obj.get("currentVenueId"),
            "current_venue": obj.get("currentVenue"),
            "current_city": obj.get("currentCity"),
            "current_state": obj.get("currentState"),
            "conference_id": obj.get("conferenceId"),
            "conference": obj.get("conference")
        })
        return _obj


