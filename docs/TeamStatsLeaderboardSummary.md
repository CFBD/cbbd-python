# TeamStatsLeaderboardSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_minutes** | **float** |  | 
**tracked_shots** | **float** |  | 
**pace** | **float** |  | 
**raw_net_rating** | **float** |  | 

## Example

```python
from cbbd.models.team_stats_leaderboard_summary import TeamStatsLeaderboardSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatsLeaderboardSummary from a JSON string
team_stats_leaderboard_summary_instance = TeamStatsLeaderboardSummary.from_json(json)
# print the JSON string representation of the object
print TeamStatsLeaderboardSummary.to_json()

# convert the object into a dict
team_stats_leaderboard_summary_dict = team_stats_leaderboard_summary_instance.to_dict()
# create an instance of TeamStatsLeaderboardSummary from a dict
team_stats_leaderboard_summary_from_dict = TeamStatsLeaderboardSummary.from_dict(team_stats_leaderboard_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


