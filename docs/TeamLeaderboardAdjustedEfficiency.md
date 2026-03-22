# TeamLeaderboardAdjustedEfficiency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offensive_rating** | **float** |  | 
**defensive_rating** | **float** |  | 
**net_rating** | **float** |  | 
**rankings** | [**TeamLeaderboardAdjustedEfficiencyRankings**](TeamLeaderboardAdjustedEfficiencyRankings.md) |  | 

## Example

```python
from cbbd.models.team_leaderboard_adjusted_efficiency import TeamLeaderboardAdjustedEfficiency

# TODO update the JSON string below
json = "{}"
# create an instance of TeamLeaderboardAdjustedEfficiency from a JSON string
team_leaderboard_adjusted_efficiency_instance = TeamLeaderboardAdjustedEfficiency.from_json(json)
# print the JSON string representation of the object
print TeamLeaderboardAdjustedEfficiency.to_json()

# convert the object into a dict
team_leaderboard_adjusted_efficiency_dict = team_leaderboard_adjusted_efficiency_instance.to_dict()
# create an instance of TeamLeaderboardAdjustedEfficiency from a dict
team_leaderboard_adjusted_efficiency_from_dict = TeamLeaderboardAdjustedEfficiency.from_dict(team_leaderboard_adjusted_efficiency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


