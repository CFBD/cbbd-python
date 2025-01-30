# coding: utf-8

"""
    College Basketball Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 1.3.0
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
from cbbd.models.team_season_unit_stats_field_goals import TeamSeasonUnitStatsFieldGoals
from cbbd.models.team_season_unit_stats_rebounds import TeamSeasonUnitStatsRebounds

class PlayerSeasonStats(BaseModel):
    """
    PlayerSeasonStats
    """
    season: StrictInt = Field(...)
    season_label: StrictStr = Field(default=..., alias="seasonLabel")
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    athlete_id: StrictInt = Field(default=..., alias="athleteId")
    athlete_source_id: StrictStr = Field(default=..., alias="athleteSourceId")
    name: StrictStr = Field(...)
    position: StrictStr = Field(...)
    games: Union[StrictFloat, StrictInt] = Field(...)
    starts: Union[StrictFloat, StrictInt] = Field(...)
    minutes: Union[StrictFloat, StrictInt] = Field(...)
    points: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    turnovers: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    fouls: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    assists: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    steals: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    blocks: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    usage: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    offensive_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="offensiveRating")
    defensive_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="defensiveRating")
    net_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="netRating")
    effective_field_goal_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="effectiveFieldGoalPct")
    true_shooting_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="trueShootingPct")
    assists_turnover_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="assistsTurnoverRatio")
    free_throw_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="freeThrowRate")
    offensive_rebound_pct: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="offensiveReboundPct")
    field_goals: TeamSeasonUnitStatsFieldGoals = Field(default=..., alias="fieldGoals")
    two_point_field_goals: TeamSeasonUnitStatsFieldGoals = Field(default=..., alias="twoPointFieldGoals")
    three_point_field_goals: TeamSeasonUnitStatsFieldGoals = Field(default=..., alias="threePointFieldGoals")
    free_throws: TeamSeasonUnitStatsFieldGoals = Field(default=..., alias="freeThrows")
    rebounds: TeamSeasonUnitStatsRebounds = Field(...)
    __properties = ["season", "seasonLabel", "teamId", "team", "conference", "athleteId", "athleteSourceId", "name", "position", "games", "starts", "minutes", "points", "turnovers", "fouls", "assists", "steals", "blocks", "usage", "offensiveRating", "defensiveRating", "netRating", "effectiveFieldGoalPct", "trueShootingPct", "assistsTurnoverRatio", "freeThrowRate", "offensiveReboundPct", "fieldGoals", "twoPointFieldGoals", "threePointFieldGoals", "freeThrows", "rebounds"]

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
    def from_json(cls, json_str: str) -> PlayerSeasonStats:
        """Create an instance of PlayerSeasonStats from a JSON string"""
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
        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        # set to None if turnovers (nullable) is None
        # and __fields_set__ contains the field
        if self.turnovers is None and "turnovers" in self.__fields_set__:
            _dict['turnovers'] = None

        # set to None if fouls (nullable) is None
        # and __fields_set__ contains the field
        if self.fouls is None and "fouls" in self.__fields_set__:
            _dict['fouls'] = None

        # set to None if assists (nullable) is None
        # and __fields_set__ contains the field
        if self.assists is None and "assists" in self.__fields_set__:
            _dict['assists'] = None

        # set to None if steals (nullable) is None
        # and __fields_set__ contains the field
        if self.steals is None and "steals" in self.__fields_set__:
            _dict['steals'] = None

        # set to None if blocks (nullable) is None
        # and __fields_set__ contains the field
        if self.blocks is None and "blocks" in self.__fields_set__:
            _dict['blocks'] = None

        # set to None if usage (nullable) is None
        # and __fields_set__ contains the field
        if self.usage is None and "usage" in self.__fields_set__:
            _dict['usage'] = None

        # set to None if offensive_rating (nullable) is None
        # and __fields_set__ contains the field
        if self.offensive_rating is None and "offensive_rating" in self.__fields_set__:
            _dict['offensiveRating'] = None

        # set to None if defensive_rating (nullable) is None
        # and __fields_set__ contains the field
        if self.defensive_rating is None and "defensive_rating" in self.__fields_set__:
            _dict['defensiveRating'] = None

        # set to None if net_rating (nullable) is None
        # and __fields_set__ contains the field
        if self.net_rating is None and "net_rating" in self.__fields_set__:
            _dict['netRating'] = None

        # set to None if effective_field_goal_pct (nullable) is None
        # and __fields_set__ contains the field
        if self.effective_field_goal_pct is None and "effective_field_goal_pct" in self.__fields_set__:
            _dict['effectiveFieldGoalPct'] = None

        # set to None if true_shooting_pct (nullable) is None
        # and __fields_set__ contains the field
        if self.true_shooting_pct is None and "true_shooting_pct" in self.__fields_set__:
            _dict['trueShootingPct'] = None

        # set to None if assists_turnover_ratio (nullable) is None
        # and __fields_set__ contains the field
        if self.assists_turnover_ratio is None and "assists_turnover_ratio" in self.__fields_set__:
            _dict['assistsTurnoverRatio'] = None

        # set to None if free_throw_rate (nullable) is None
        # and __fields_set__ contains the field
        if self.free_throw_rate is None and "free_throw_rate" in self.__fields_set__:
            _dict['freeThrowRate'] = None

        # set to None if offensive_rebound_pct (nullable) is None
        # and __fields_set__ contains the field
        if self.offensive_rebound_pct is None and "offensive_rebound_pct" in self.__fields_set__:
            _dict['offensiveReboundPct'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerSeasonStats:
        """Create an instance of PlayerSeasonStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerSeasonStats.parse_obj(obj)

        _obj = PlayerSeasonStats.parse_obj({
            "season": obj.get("season"),
            "season_label": obj.get("seasonLabel"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "athlete_id": obj.get("athleteId"),
            "athlete_source_id": obj.get("athleteSourceId"),
            "name": obj.get("name"),
            "position": obj.get("position"),
            "games": obj.get("games"),
            "starts": obj.get("starts"),
            "minutes": obj.get("minutes"),
            "points": obj.get("points"),
            "turnovers": obj.get("turnovers"),
            "fouls": obj.get("fouls"),
            "assists": obj.get("assists"),
            "steals": obj.get("steals"),
            "blocks": obj.get("blocks"),
            "usage": obj.get("usage"),
            "offensive_rating": obj.get("offensiveRating"),
            "defensive_rating": obj.get("defensiveRating"),
            "net_rating": obj.get("netRating"),
            "effective_field_goal_pct": obj.get("effectiveFieldGoalPct"),
            "true_shooting_pct": obj.get("trueShootingPct"),
            "assists_turnover_ratio": obj.get("assistsTurnoverRatio"),
            "free_throw_rate": obj.get("freeThrowRate"),
            "offensive_rebound_pct": obj.get("offensiveReboundPct"),
            "field_goals": TeamSeasonUnitStatsFieldGoals.from_dict(obj.get("fieldGoals")) if obj.get("fieldGoals") is not None else None,
            "two_point_field_goals": TeamSeasonUnitStatsFieldGoals.from_dict(obj.get("twoPointFieldGoals")) if obj.get("twoPointFieldGoals") is not None else None,
            "three_point_field_goals": TeamSeasonUnitStatsFieldGoals.from_dict(obj.get("threePointFieldGoals")) if obj.get("threePointFieldGoals") is not None else None,
            "free_throws": TeamSeasonUnitStatsFieldGoals.from_dict(obj.get("freeThrows")) if obj.get("freeThrows") is not None else None,
            "rebounds": TeamSeasonUnitStatsRebounds.from_dict(obj.get("rebounds")) if obj.get("rebounds") is not None else None
        })
        return _obj


