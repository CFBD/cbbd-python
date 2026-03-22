# TeamStatsLeaderboardUnitStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**TeamStatsLeaderboardUnitStatsPoints**](TeamStatsLeaderboardUnitStatsPoints.md) |  | 
**possessions** | **float** |  | 
**raw_offensive_rating** | **float** |  | 
**true_shooting_pct** | **float** |  | 
**effective_field_goal_pct** | **float** |  | 
**turnover_ratio** | **float** |  | 
**offensive_rebound_pct** | **float** |  | 
**free_throw_rate** | **float** |  | 
**field_goals** | [**TeamStatsLeaderboardUnitStatsFieldGoals**](TeamStatsLeaderboardUnitStatsFieldGoals.md) |  | 
**two_point_field_goals** | [**TeamStatsLeaderboardUnitStatsFieldGoals**](TeamStatsLeaderboardUnitStatsFieldGoals.md) |  | 
**three_point_field_goals** | [**TeamStatsLeaderboardUnitStatsFieldGoals**](TeamStatsLeaderboardUnitStatsFieldGoals.md) |  | 
**free_throws** | [**TeamStatsLeaderboardUnitStatsFieldGoals**](TeamStatsLeaderboardUnitStatsFieldGoals.md) |  | 
**rebounds** | [**TeamStatsLeaderboardUnitStatsRebounds**](TeamStatsLeaderboardUnitStatsRebounds.md) |  | 
**turnovers** | [**TeamStatsLeaderboardUnitStatsTurnovers**](TeamStatsLeaderboardUnitStatsTurnovers.md) |  | 
**fouls** | [**TeamStatsLeaderboardUnitStatsFouls**](TeamStatsLeaderboardUnitStatsFouls.md) |  | 
**assists** | **float** |  | 
**blocks** | **float** |  | 
**steals** | **float** |  | 

## Example

```python
from cbbd.models.team_stats_leaderboard_unit_stats import TeamStatsLeaderboardUnitStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatsLeaderboardUnitStats from a JSON string
team_stats_leaderboard_unit_stats_instance = TeamStatsLeaderboardUnitStats.from_json(json)
# print the JSON string representation of the object
print TeamStatsLeaderboardUnitStats.to_json()

# convert the object into a dict
team_stats_leaderboard_unit_stats_dict = team_stats_leaderboard_unit_stats_instance.to_dict()
# create an instance of TeamStatsLeaderboardUnitStats from a dict
team_stats_leaderboard_unit_stats_from_dict = TeamStatsLeaderboardUnitStats.from_dict(team_stats_leaderboard_unit_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


