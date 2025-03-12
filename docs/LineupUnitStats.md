# LineupUnitStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**possessions** | **int** |  | 
**points** | **int** |  | 
**blocks** | **int** |  | 
**assists** | **int** |  | 
**steals** | **int** |  | 
**turnovers** | **int** |  | 
**defensive_rebounds** | **int** |  | 
**offensive_rebounds** | **int** |  | 
**true_shooting** | **float** |  | 
**field_goals** | [**ShootingStats**](ShootingStats.md) |  | 
**two_pointers** | [**LineupUnitStatsTwoPointers**](LineupUnitStatsTwoPointers.md) |  | 
**three_pointers** | [**ShootingStats**](ShootingStats.md) |  | 
**free_throws** | [**ShootingStats**](ShootingStats.md) |  | 
**four_factors** | [**LineupUnitStatsFourFactors**](LineupUnitStatsFourFactors.md) |  | 

## Example

```python
from cbbd.models.lineup_unit_stats import LineupUnitStats

# TODO update the JSON string below
json = "{}"
# create an instance of LineupUnitStats from a JSON string
lineup_unit_stats_instance = LineupUnitStats.from_json(json)
# print the JSON string representation of the object
print LineupUnitStats.to_json()

# convert the object into a dict
lineup_unit_stats_dict = lineup_unit_stats_instance.to_dict()
# create an instance of LineupUnitStats from a dict
lineup_unit_stats_from_dict = LineupUnitStats.from_dict(lineup_unit_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


