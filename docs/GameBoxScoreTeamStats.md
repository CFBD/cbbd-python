# GameBoxScoreTeamStats


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
**points** | [**GameBoxScoreTeamStatsPoints**](GameBoxScoreTeamStatsPoints.md) |  | 
**four_factors** | [**TeamSeasonUnitStatsFourFactors**](TeamSeasonUnitStatsFourFactors.md) |  | 
**assists** | **float** |  | 
**blocks** | **float** |  | 
**steals** | **float** |  | 
**possessions** | **float** |  | 
**rating** | **float** |  | 
**true_shooting** | **float** |  | 
**game_score** | **float** |  | 

## Example

```python
from cbbd.models.game_box_score_team_stats import GameBoxScoreTeamStats

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxScoreTeamStats from a JSON string
game_box_score_team_stats_instance = GameBoxScoreTeamStats.from_json(json)
# print the JSON string representation of the object
print GameBoxScoreTeamStats.to_json()

# convert the object into a dict
game_box_score_team_stats_dict = game_box_score_team_stats_instance.to_dict()
# create an instance of GameBoxScoreTeamStats from a dict
game_box_score_team_stats_from_dict = GameBoxScoreTeamStats.from_dict(game_box_score_team_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


