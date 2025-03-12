# LineupUnitStatsTwoPointers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**made** | **int** |  | 
**attempted** | **int** |  | 
**pct** | **float** |  | 
**jumpers** | [**ShootingStats**](ShootingStats.md) |  | 
**layups** | [**ShootingStats**](ShootingStats.md) |  | 
**dunks** | [**ShootingStats**](ShootingStats.md) |  | 
**tip_ins** | [**ShootingStats**](ShootingStats.md) |  | 

## Example

```python
from cbbd.models.lineup_unit_stats_two_pointers import LineupUnitStatsTwoPointers

# TODO update the JSON string below
json = "{}"
# create an instance of LineupUnitStatsTwoPointers from a JSON string
lineup_unit_stats_two_pointers_instance = LineupUnitStatsTwoPointers.from_json(json)
# print the JSON string representation of the object
print LineupUnitStatsTwoPointers.to_json()

# convert the object into a dict
lineup_unit_stats_two_pointers_dict = lineup_unit_stats_two_pointers_instance.to_dict()
# create an instance of LineupUnitStatsTwoPointers from a dict
lineup_unit_stats_two_pointers_from_dict = LineupUnitStatsTwoPointers.from_dict(lineup_unit_stats_two_pointers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


