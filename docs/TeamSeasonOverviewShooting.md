# TeamSeasonOverviewShooting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**List[ShotBucket]**](ShotBucket.md) |  | 
**tracked_attempts** | **float** |  | 
**coverage** | [**Coverage**](Coverage.md) |  | 

## Example

```python
from cbbd.models.team_season_overview_shooting import TeamSeasonOverviewShooting

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewShooting from a JSON string
team_season_overview_shooting_instance = TeamSeasonOverviewShooting.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewShooting.to_json()

# convert the object into a dict
team_season_overview_shooting_dict = team_season_overview_shooting_instance.to_dict()
# create an instance of TeamSeasonOverviewShooting from a dict
team_season_overview_shooting_from_dict = TeamSeasonOverviewShooting.from_dict(team_season_overview_shooting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


