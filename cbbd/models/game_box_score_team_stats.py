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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt
from cbbd.models.game_box_score_team_stats_points import GameBoxScoreTeamStatsPoints
from cbbd.models.team_season_unit_stats_field_goals import TeamSeasonUnitStatsFieldGoals
from cbbd.models.team_season_unit_stats_fouls import TeamSeasonUnitStatsFouls
from cbbd.models.team_season_unit_stats_four_factors import TeamSeasonUnitStatsFourFactors
from cbbd.models.team_season_unit_stats_rebounds import TeamSeasonUnitStatsRebounds
from cbbd.models.team_season_unit_stats_turnovers import TeamSeasonUnitStatsTurnovers

class GameBoxScoreTeamStats(BaseModel):
    """
    GameBoxScoreTeamStats
    """
    field_goals: TeamSeasonUnitStatsFieldGoals = Field(default=..., alias="fieldGoals")
    two_point_field_goals: TeamSeasonUnitStatsFieldGoals = Field(default=..., alias="twoPointFieldGoals")
    three_point_field_goals: TeamSeasonUnitStatsFieldGoals = Field(default=..., alias="threePointFieldGoals")
    free_throws: TeamSeasonUnitStatsFieldGoals = Field(default=..., alias="freeThrows")
    rebounds: TeamSeasonUnitStatsRebounds = Field(...)
    turnovers: TeamSeasonUnitStatsTurnovers = Field(...)
    fouls: TeamSeasonUnitStatsFouls = Field(...)
    points: GameBoxScoreTeamStatsPoints = Field(...)
    four_factors: TeamSeasonUnitStatsFourFactors = Field(default=..., alias="fourFactors")
    assists: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    blocks: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    steals: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    possessions: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    rating: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    true_shooting: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="trueShooting")
    game_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="gameScore")
    __properties = ["fieldGoals", "twoPointFieldGoals", "threePointFieldGoals", "freeThrows", "rebounds", "turnovers", "fouls", "points", "fourFactors", "assists", "blocks", "steals", "possessions", "rating", "trueShooting", "gameScore"]

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
    def from_json(cls, json_str: str) -> GameBoxScoreTeamStats:
        """Create an instance of GameBoxScoreTeamStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of field_goals
        if self.field_goals:
            _dict['fieldGoals'] = self.field_goals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of two_point_field_goals
        if self.two_point_field_goals:
            _dict['twoPointFieldGoals'] = self.two_point_field_goals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of three_point_field_goals
        if self.three_point_field_goals:
            _dict['threePointFieldGoals'] = self.three_point_field_goals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of free_throws
        if self.free_throws:
            _dict['freeThrows'] = self.free_throws.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rebounds
        if self.rebounds:
            _dict['rebounds'] = self.rebounds.to_dict()
        # override the default output from pydantic by calling `to_dict()` of turnovers
        if self.turnovers:
            _dict['turnovers'] = self.turnovers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fouls
        if self.fouls:
            _dict['fouls'] = self.fouls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of points
        if self.points:
            _dict['points'] = self.points.to_dict()
        # override the default output from pydantic by calling `to_dict()` of four_factors
        if self.four_factors:
            _dict['fourFactors'] = self.four_factors.to_dict()
        # set to None if assists (nullable) is None
        # and __fields_set__ contains the field
        if self.assists is None and "assists" in self.__fields_set__:
            _dict['assists'] = None

        # set to None if blocks (nullable) is None
        # and __fields_set__ contains the field
        if self.blocks is None and "blocks" in self.__fields_set__:
            _dict['blocks'] = None

        # set to None if steals (nullable) is None
        # and __fields_set__ contains the field
        if self.steals is None and "steals" in self.__fields_set__:
            _dict['steals'] = None

        # set to None if possessions (nullable) is None
        # and __fields_set__ contains the field
        if self.possessions is None and "possessions" in self.__fields_set__:
            _dict['possessions'] = None

        # set to None if rating (nullable) is None
        # and __fields_set__ contains the field
        if self.rating is None and "rating" in self.__fields_set__:
            _dict['rating'] = None

        # set to None if true_shooting (nullable) is None
        # and __fields_set__ contains the field
        if self.true_shooting is None and "true_shooting" in self.__fields_set__:
            _dict['trueShooting'] = None

        # set to None if game_score (nullable) is None
        # and __fields_set__ contains the field
        if self.game_score is None and "game_score" in self.__fields_set__:
            _dict['gameScore'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GameBoxScoreTeamStats:
        """Create an instance of GameBoxScoreTeamStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GameBoxScoreTeamStats.parse_obj(obj)

        _obj = GameBoxScoreTeamStats.parse_obj({
            "field_goals": TeamSeasonUnitStatsFieldGoals.from_dict(obj.get("fieldGoals")) if obj.get("fieldGoals") is not None else None,
            "two_point_field_goals": TeamSeasonUnitStatsFieldGoals.from_dict(obj.get("twoPointFieldGoals")) if obj.get("twoPointFieldGoals") is not None else None,
            "three_point_field_goals": TeamSeasonUnitStatsFieldGoals.from_dict(obj.get("threePointFieldGoals")) if obj.get("threePointFieldGoals") is not None else None,
            "free_throws": TeamSeasonUnitStatsFieldGoals.from_dict(obj.get("freeThrows")) if obj.get("freeThrows") is not None else None,
            "rebounds": TeamSeasonUnitStatsRebounds.from_dict(obj.get("rebounds")) if obj.get("rebounds") is not None else None,
            "turnovers": TeamSeasonUnitStatsTurnovers.from_dict(obj.get("turnovers")) if obj.get("turnovers") is not None else None,
            "fouls": TeamSeasonUnitStatsFouls.from_dict(obj.get("fouls")) if obj.get("fouls") is not None else None,
            "points": GameBoxScoreTeamStatsPoints.from_dict(obj.get("points")) if obj.get("points") is not None else None,
            "four_factors": TeamSeasonUnitStatsFourFactors.from_dict(obj.get("fourFactors")) if obj.get("fourFactors") is not None else None,
            "assists": obj.get("assists"),
            "blocks": obj.get("blocks"),
            "steals": obj.get("steals"),
            "possessions": obj.get("possessions"),
            "rating": obj.get("rating"),
            "true_shooting": obj.get("trueShooting"),
            "game_score": obj.get("gameScore")
        })
        return _obj


