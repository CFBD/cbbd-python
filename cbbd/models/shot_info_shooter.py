# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.10.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr

class ShotInfoShooter(BaseModel):
    """
    ShotInfoShooter
    """
    name: StrictStr = Field(...)
    id: StrictInt = Field(...)
    __properties = ["name", "id"]

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
    def from_json(cls, json_str: str) -> ShotInfoShooter:
        """Create an instance of ShotInfoShooter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ShotInfoShooter:
        """Create an instance of ShotInfoShooter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ShotInfoShooter.parse_obj(obj)

        _obj = ShotInfoShooter.parse_obj({
            "name": obj.get("name"),
            "id": obj.get("id")
        })
        return _obj


