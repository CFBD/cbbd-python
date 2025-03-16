# SeasonShootingStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**tracked_shots** | **int** |  | 
**assisted_pct** | **float** |  | 
**dunks** | [**SeasonShootingStatsDunks**](SeasonShootingStatsDunks.md) |  | 
**layups** | [**SeasonShootingStatsDunks**](SeasonShootingStatsDunks.md) |  | 
**tip_ins** | [**ShotTypeBreakdown**](ShotTypeBreakdown.md) |  | 
**two_point_jumpers** | [**SeasonShootingStatsDunks**](SeasonShootingStatsDunks.md) |  | 
**three_point_jumpers** | [**SeasonShootingStatsDunks**](SeasonShootingStatsDunks.md) |  | 
**attempts_breakdown** | [**SeasonShootingStatsAttemptsBreakdown**](SeasonShootingStatsAttemptsBreakdown.md) |  | 

## Example

```python
from cbbd.models.season_shooting_stats import SeasonShootingStats

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonShootingStats from a JSON string
season_shooting_stats_instance = SeasonShootingStats.from_json(json)
# print the JSON string representation of the object
print SeasonShootingStats.to_json()

# convert the object into a dict
season_shooting_stats_dict = season_shooting_stats_instance.to_dict()
# create an instance of SeasonShootingStats from a dict
season_shooting_stats_from_dict = SeasonShootingStats.from_dict(season_shooting_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


