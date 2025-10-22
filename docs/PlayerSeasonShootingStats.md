# PlayerSeasonShootingStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**tracked_shots** | **int** |  | 
**assisted_pct** | **float** |  | 
**free_throw_rate** | **float** |  | 
**dunks** | [**SeasonShootingStatsDunks**](SeasonShootingStatsDunks.md) |  | 
**layups** | [**SeasonShootingStatsDunks**](SeasonShootingStatsDunks.md) |  | 
**tip_ins** | [**ShotTypeBreakdown**](ShotTypeBreakdown.md) |  | 
**two_point_jumpers** | [**SeasonShootingStatsDunks**](SeasonShootingStatsDunks.md) |  | 
**three_point_jumpers** | [**SeasonShootingStatsDunks**](SeasonShootingStatsDunks.md) |  | 
**free_throws** | [**ShotTypeBreakdown**](ShotTypeBreakdown.md) |  | 
**attempts_breakdown** | [**SeasonShootingStatsAttemptsBreakdown**](SeasonShootingStatsAttemptsBreakdown.md) |  | 
**athlete_id** | **int** |  | 
**athlete_name** | **str** |  | 

## Example

```python
from cbbd.models.player_season_shooting_stats import PlayerSeasonShootingStats

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonShootingStats from a JSON string
player_season_shooting_stats_instance = PlayerSeasonShootingStats.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonShootingStats.to_json()

# convert the object into a dict
player_season_shooting_stats_dict = player_season_shooting_stats_instance.to_dict()
# create an instance of PlayerSeasonShootingStats from a dict
player_season_shooting_stats_from_dict = PlayerSeasonShootingStats.from_dict(player_season_shooting_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


