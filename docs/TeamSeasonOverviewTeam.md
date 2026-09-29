# TeamSeasonOverviewTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | [**Conference**](Conference.md) |  | 
**source_id** | **str** |  | 
**mascot** | **str** |  | 
**school** | **str** |  | 

## Example

```python
from cbbd.models.team_season_overview_team import TeamSeasonOverviewTeam

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewTeam from a JSON string
team_season_overview_team_instance = TeamSeasonOverviewTeam.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewTeam.to_json()

# convert the object into a dict
team_season_overview_team_dict = team_season_overview_team_instance.to_dict()
# create an instance of TeamSeasonOverviewTeam from a dict
team_season_overview_team_from_dict = TeamSeasonOverviewTeam.from_dict(team_season_overview_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


