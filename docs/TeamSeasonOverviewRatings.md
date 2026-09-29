# TeamSeasonOverviewRatings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polls** | [**TeamSeasonOverviewRatingsPolls**](TeamSeasonOverviewRatingsPolls.md) |  | 
**srs** | **float** |  | 
**elo** | **float** |  | 
**adjusted** | [**AdjustedRatings**](AdjustedRatings.md) |  | 

## Example

```python
from cbbd.models.team_season_overview_ratings import TeamSeasonOverviewRatings

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewRatings from a JSON string
team_season_overview_ratings_instance = TeamSeasonOverviewRatings.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewRatings.to_json()

# convert the object into a dict
team_season_overview_ratings_dict = team_season_overview_ratings_instance.to_dict()
# create an instance of TeamSeasonOverviewRatings from a dict
team_season_overview_ratings_from_dict = TeamSeasonOverviewRatings.from_dict(team_season_overview_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


