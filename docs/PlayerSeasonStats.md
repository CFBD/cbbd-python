# PlayerSeasonStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**season_label** | **str** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**athlete_id** | **int** |  | 
**athlete_source_id** | **str** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**games** | **float** |  | 
**starts** | **float** |  | 
**minutes** | **float** |  | 
**points** | **float** |  | 
**turnovers** | **float** |  | 
**fouls** | **float** |  | 
**assists** | **float** |  | 
**steals** | **float** |  | 
**blocks** | **float** |  | 
**usage** | **float** |  | 
**offensive_rating** | **float** |  | 
**defensive_rating** | **float** |  | 
**net_rating** | **float** |  | 
**effective_field_goal_pct** | **float** |  | 
**true_shooting_pct** | **float** |  | 
**assists_turnover_ratio** | **float** |  | 
**free_throw_rate** | **float** |  | 
**offensive_rebound_pct** | **float** |  | 
**field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**two_point_field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**three_point_field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**free_throws** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**rebounds** | [**TeamSeasonUnitStatsRebounds**](TeamSeasonUnitStatsRebounds.md) |  | 
**win_shares** | [**TeamSeasonUnitStatsRebounds**](TeamSeasonUnitStatsRebounds.md) |  | 

## Example

```python
from cbbd.models.player_season_stats import PlayerSeasonStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonStats from a JSON string
player_season_stats_instance = PlayerSeasonStats.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonStats.to_json()

# convert the object into a dict
player_season_stats_dict = player_season_stats_instance.to_dict()
# create an instance of PlayerSeasonStats from a dict
player_season_stats_from_dict = PlayerSeasonStats.from_dict(player_season_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


