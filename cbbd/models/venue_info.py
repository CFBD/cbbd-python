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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class VenueInfo(BaseModel):
    """
    VenueInfo
    """
    id: Union[StrictFloat, StrictInt] = Field(...)
    source_id: Optional[StrictStr] = Field(default=..., alias="sourceId")
    name: StrictStr = Field(...)
    city: Optional[StrictStr] = Field(...)
    state: Optional[StrictStr] = Field(...)
    country: Optional[StrictStr] = Field(...)
    __properties = ["id", "sourceId", "name", "city", "state", "country"]

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
    def from_json(cls, json_str: str) -> VenueInfo:
        """Create an instance of VenueInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['sourceId'] = None

        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        # set to None if country (nullable) is None
        # and __fields_set__ contains the field
        if self.country is None and "country" in self.__fields_set__:
            _dict['country'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VenueInfo:
        """Create an instance of VenueInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VenueInfo.parse_obj(obj)

        _obj = VenueInfo.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "name": obj.get("name"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "country": obj.get("country")
        })
        return _obj


