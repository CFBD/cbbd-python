# TeamSeasonUnitStatsFourFactors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_throw_rate** | **float** |  | 
**offensive_rebound_pct** | **float** |  | 
**turnover_ratio** | **float** |  | 
**effective_field_goal_pct** | **float** |  | 

## Example

```python
from cbbd.models.team_season_unit_stats_four_factors import TeamSeasonUnitStatsFourFactors

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonUnitStatsFourFactors from a JSON string
team_season_unit_stats_four_factors_instance = TeamSeasonUnitStatsFourFactors.from_json(json)
# print the JSON string representation of the object
print TeamSeasonUnitStatsFourFactors.to_json()

# convert the object into a dict
team_season_unit_stats_four_factors_dict = team_season_unit_stats_four_factors_instance.to_dict()
# create an instance of TeamSeasonUnitStatsFourFactors from a dict
team_season_unit_stats_four_factors_from_dict = TeamSeasonUnitStatsFourFactors.from_dict(team_season_unit_stats_four_factors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


