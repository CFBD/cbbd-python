# TeamSeasonUnitStatsFouls


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flagrant** | **float** |  | 
**technical** | **float** |  | 
**total** | **float** |  | 

## Example

```python
from cbbd.models.team_season_unit_stats_fouls import TeamSeasonUnitStatsFouls

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonUnitStatsFouls from a JSON string
team_season_unit_stats_fouls_instance = TeamSeasonUnitStatsFouls.from_json(json)
# print the JSON string representation of the object
print TeamSeasonUnitStatsFouls.to_json()

# convert the object into a dict
team_season_unit_stats_fouls_dict = team_season_unit_stats_fouls_instance.to_dict()
# create an instance of TeamSeasonUnitStatsFouls from a dict
team_season_unit_stats_fouls_from_dict = TeamSeasonUnitStatsFouls.from_dict(team_season_unit_stats_fouls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


