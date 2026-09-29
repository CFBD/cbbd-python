# TeamSeasonOverviewEfficiency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defense** | [**UnitMetrics**](UnitMetrics.md) |  | 
**offense** | [**UnitMetrics**](UnitMetrics.md) |  | 
**pace_games** | **float** |  | 
**pace** | **float** |  | 
**coverage** | [**Coverage**](Coverage.md) |  | 

## Example

```python
from cbbd.models.team_season_overview_efficiency import TeamSeasonOverviewEfficiency

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewEfficiency from a JSON string
team_season_overview_efficiency_instance = TeamSeasonOverviewEfficiency.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewEfficiency.to_json()

# convert the object into a dict
team_season_overview_efficiency_dict = team_season_overview_efficiency_instance.to_dict()
# create an instance of TeamSeasonOverviewEfficiency from a dict
team_season_overview_efficiency_from_dict = TeamSeasonOverviewEfficiency.from_dict(team_season_overview_efficiency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


