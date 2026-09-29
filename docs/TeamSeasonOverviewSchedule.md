# TeamSeasonOverviewSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | [**List[ProfileGame]**](ProfileGame.md) |  | 

## Example

```python
from cbbd.models.team_season_overview_schedule import TeamSeasonOverviewSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewSchedule from a JSON string
team_season_overview_schedule_instance = TeamSeasonOverviewSchedule.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewSchedule.to_json()

# convert the object into a dict
team_season_overview_schedule_dict = team_season_overview_schedule_instance.to_dict()
# create an instance of TeamSeasonOverviewSchedule from a dict
team_season_overview_schedule_from_dict = TeamSeasonOverviewSchedule.from_dict(team_season_overview_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


