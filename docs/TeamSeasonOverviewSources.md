# TeamSeasonOverviewSources


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **List[str]** |  | 
**latest_final_start_date** | **str** |  | 
**leaderboard_updated_at** | **str** |  | 

## Example

```python
from cbbd.models.team_season_overview_sources import TeamSeasonOverviewSources

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewSources from a JSON string
team_season_overview_sources_instance = TeamSeasonOverviewSources.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewSources.to_json()

# convert the object into a dict
team_season_overview_sources_dict = team_season_overview_sources_instance.to_dict()
# create an instance of TeamSeasonOverviewSources from a dict
team_season_overview_sources_from_dict = TeamSeasonOverviewSources.from_dict(team_season_overview_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


