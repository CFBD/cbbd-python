# LineupStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**id_hash** | **str** |  | 
**athletes** | [**List[PlayInfoParticipantsInner]**](PlayInfoParticipantsInner.md) |  | 
**total_seconds** | **float** |  | 
**pace** | **float** |  | 
**offense_rating** | **float** |  | 
**defense_rating** | **float** |  | 
**net_rating** | **float** |  | 
**team_stats** | [**LineupUnitStats**](LineupUnitStats.md) |  | 
**opponent_stats** | [**LineupUnitStats**](LineupUnitStats.md) |  | 

## Example

```python
from cbbd.models.lineup_stats import LineupStats

# TODO update the JSON string below
json = "{}"
# create an instance of LineupStats from a JSON string
lineup_stats_instance = LineupStats.from_json(json)
# print the JSON string representation of the object
print LineupStats.to_json()

# convert the object into a dict
lineup_stats_dict = lineup_stats_instance.to_dict()
# create an instance of LineupStats from a dict
lineup_stats_from_dict = LineupStats.from_dict(lineup_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


