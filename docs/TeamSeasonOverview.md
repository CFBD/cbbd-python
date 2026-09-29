# TeamSeasonOverview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format_version** | **float** |  | 
**team_id** | **float** |  | 
**season** | **float** |  | 
**season_label** | **str** |  | 
**generated_at** | **str** |  | 
**team** | [**TeamSeasonOverviewTeam**](TeamSeasonOverviewTeam.md) |  | 
**record** | [**TeamSeasonOverviewRecord**](TeamSeasonOverviewRecord.md) |  | 
**ratings** | [**TeamSeasonOverviewRatings**](TeamSeasonOverviewRatings.md) |  | 
**efficiency** | [**TeamSeasonOverviewEfficiency**](TeamSeasonOverviewEfficiency.md) |  | 
**shooting** | [**TeamSeasonOverviewShooting**](TeamSeasonOverviewShooting.md) |  | 
**players** | [**TeamSeasonOverviewPlayers**](TeamSeasonOverviewPlayers.md) |  | 
**schedule** | [**TeamSeasonOverviewSchedule**](TeamSeasonOverviewSchedule.md) |  | 
**sources** | [**TeamSeasonOverviewSources**](TeamSeasonOverviewSources.md) |  | 

## Example

```python
from cbbd.models.team_season_overview import TeamSeasonOverview

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverview from a JSON string
team_season_overview_instance = TeamSeasonOverview.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverview.to_json()

# convert the object into a dict
team_season_overview_dict = team_season_overview_instance.to_dict()
# create an instance of TeamSeasonOverview from a dict
team_season_overview_from_dict = TeamSeasonOverview.from_dict(team_season_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


