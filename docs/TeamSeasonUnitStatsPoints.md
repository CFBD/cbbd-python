# TeamSeasonUnitStatsPoints


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fast_break** | **float** |  | 
**off_turnovers** | **float** |  | 
**in_paint** | **float** |  | 
**total** | **float** |  | 

## Example

```python
from cbbd.models.team_season_unit_stats_points import TeamSeasonUnitStatsPoints

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonUnitStatsPoints from a JSON string
team_season_unit_stats_points_instance = TeamSeasonUnitStatsPoints.from_json(json)
# print the JSON string representation of the object
print TeamSeasonUnitStatsPoints.to_json()

# convert the object into a dict
team_season_unit_stats_points_dict = team_season_unit_stats_points_instance.to_dict()
# create an instance of TeamSeasonUnitStatsPoints from a dict
team_season_unit_stats_points_from_dict = TeamSeasonUnitStatsPoints.from_dict(team_season_unit_stats_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


