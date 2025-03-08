# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.17.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictBool, StrictStr, validator
from cbbd.models.shot_info_location import ShotInfoLocation
from cbbd.models.shot_info_shooter import ShotInfoShooter

class ShotInfo(BaseModel):
    """
    ShotInfo
    """
    shooter: ShotInfoShooter = Field(...)
    made: StrictBool = Field(...)
    range: StrictStr = Field(...)
    assisted: StrictBool = Field(...)
    assisted_by: ShotInfoShooter = Field(default=..., alias="assistedBy")
    location: ShotInfoLocation = Field(...)
    __properties = ["shooter", "made", "range", "assisted", "assistedBy", "location"]

    @validator('range')
    def range_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('rim', 'jumper', 'three_pointer', 'free_throw',):
            raise ValueError("must be one of enum values ('rim', 'jumper', 'three_pointer', 'free_throw')")
        return value

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
    def from_json(cls, json_str: str) -> ShotInfo:
        """Create an instance of ShotInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of shooter
        if self.shooter:
            _dict['shooter'] = self.shooter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assisted_by
        if self.assisted_by:
            _dict['assistedBy'] = self.assisted_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ShotInfo:
        """Create an instance of ShotInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ShotInfo.parse_obj(obj)

        _obj = ShotInfo.parse_obj({
            "shooter": ShotInfoShooter.from_dict(obj.get("shooter")) if obj.get("shooter") is not None else None,
            "made": obj.get("made"),
            "range": obj.get("range"),
            "assisted": obj.get("assisted"),
            "assisted_by": ShotInfoShooter.from_dict(obj.get("assistedBy")) if obj.get("assistedBy") is not None else None,
            "location": ShotInfoLocation.from_dict(obj.get("location")) if obj.get("location") is not None else None
        })
        return _obj


