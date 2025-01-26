# TeamSeasonUnitStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**two_point_field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**three_point_field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**free_throws** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**rebounds** | [**TeamSeasonUnitStatsRebounds**](TeamSeasonUnitStatsRebounds.md) |  | 
**turnovers** | [**TeamSeasonUnitStatsTurnovers**](TeamSeasonUnitStatsTurnovers.md) |  | 
**fouls** | [**TeamSeasonUnitStatsFouls**](TeamSeasonUnitStatsFouls.md) |  | 
**points** | [**TeamSeasonUnitStatsPoints**](TeamSeasonUnitStatsPoints.md) |  | 
**four_factors** | [**TeamSeasonUnitStatsFourFactors**](TeamSeasonUnitStatsFourFactors.md) |  | 
**assists** | **float** |  | 
**blocks** | **float** |  | 
**steals** | **float** |  | 
**possessions** | **float** |  | 
**rating** | **float** |  | 
**true_shooting** | **float** |  | 

## Example

```python
from cbbd.models.team_season_unit_stats import TeamSeasonUnitStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonUnitStats from a JSON string
team_season_unit_stats_instance = TeamSeasonUnitStats.from_json(json)
# print the JSON string representation of the object
print TeamSeasonUnitStats.to_json()

# convert the object into a dict
team_season_unit_stats_dict = team_season_unit_stats_instance.to_dict()
# create an instance of TeamSeasonUnitStats from a dict
team_season_unit_stats_from_dict = TeamSeasonUnitStats.from_dict(team_season_unit_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


