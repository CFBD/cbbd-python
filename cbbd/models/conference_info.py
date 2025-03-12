# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.18.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr

class ConferenceInfo(BaseModel):
    """
    ConferenceInfo
    """
    id: StrictInt = Field(...)
    source_id: StrictStr = Field(default=..., alias="sourceId")
    name: StrictStr = Field(...)
    abbreviation: StrictStr = Field(...)
    short_name: StrictStr = Field(default=..., alias="shortName")
    __properties = ["id", "sourceId", "name", "abbreviation", "shortName"]

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
    def from_json(cls, json_str: str) -> ConferenceInfo:
        """Create an instance of ConferenceInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConferenceInfo:
        """Create an instance of ConferenceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConferenceInfo.parse_obj(obj)

        _obj = ConferenceInfo.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "name": obj.get("name"),
            "abbreviation": obj.get("abbreviation"),
            "short_name": obj.get("shortName")
        })
        return _obj


