# LineupUnitStatsFourFactors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_throw_rate** | **float** |  | 
**offensive_rebound_pct** | **float** |  | 
**turnover_ratio** | **float** |  | 
**effective_field_goal_pct** | **float** |  | 

## Example

```python
from cbbd.models.lineup_unit_stats_four_factors import LineupUnitStatsFourFactors

# TODO update the JSON string below
json = "{}"
# create an instance of LineupUnitStatsFourFactors from a JSON string
lineup_unit_stats_four_factors_instance = LineupUnitStatsFourFactors.from_json(json)
# print the JSON string representation of the object
print LineupUnitStatsFourFactors.to_json()

# convert the object into a dict
lineup_unit_stats_four_factors_dict = lineup_unit_stats_four_factors_instance.to_dict()
# create an instance of LineupUnitStatsFourFactors from a dict
lineup_unit_stats_four_factors_from_dict = LineupUnitStatsFourFactors.from_dict(lineup_unit_stats_four_factors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


