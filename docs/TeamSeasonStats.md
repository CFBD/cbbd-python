# TeamSeasonStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**season_label** | **str** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**games** | **int** |  | 
**total_minutes** | **float** |  | 
**pace** | **float** |  | 
**offense** | [**TeamSeasonUnitStats**](TeamSeasonUnitStats.md) |  | 
**defense** | [**TeamSeasonUnitStats**](TeamSeasonUnitStats.md) |  | 

## Example

```python
from cbbd.models.team_season_stats import TeamSeasonStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonStats from a JSON string
team_season_stats_instance = TeamSeasonStats.from_json(json)
# print the JSON string representation of the object
print TeamSeasonStats.to_json()

# convert the object into a dict
team_season_stats_dict = team_season_stats_instance.to_dict()
# create an instance of TeamSeasonStats from a dict
team_season_stats_from_dict = TeamSeasonStats.from_dict(team_season_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


