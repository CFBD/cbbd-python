# TeamSeasonOverviewRatingsPolls


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coaches** | [**PollStanding**](PollStanding.md) |  | 
**ap** | [**PollStanding**](PollStanding.md) |  | 

## Example

```python
from cbbd.models.team_season_overview_ratings_polls import TeamSeasonOverviewRatingsPolls

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewRatingsPolls from a JSON string
team_season_overview_ratings_polls_instance = TeamSeasonOverviewRatingsPolls.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewRatingsPolls.to_json()

# convert the object into a dict
team_season_overview_ratings_polls_dict = team_season_overview_ratings_polls_instance.to_dict()
# create an instance of TeamSeasonOverviewRatingsPolls from a dict
team_season_overview_ratings_polls_from_dict = TeamSeasonOverviewRatingsPolls.from_dict(team_season_overview_ratings_polls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


