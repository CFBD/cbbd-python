# TeamStatsLeaderboardRecordSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | **float** |  | 
**wins** | **float** |  | 
**losses** | **float** |  | 

## Example

```python
from cbbd.models.team_stats_leaderboard_record_summary import TeamStatsLeaderboardRecordSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatsLeaderboardRecordSummary from a JSON string
team_stats_leaderboard_record_summary_instance = TeamStatsLeaderboardRecordSummary.from_json(json)
# print the JSON string representation of the object
print TeamStatsLeaderboardRecordSummary.to_json()

# convert the object into a dict
team_stats_leaderboard_record_summary_dict = team_stats_leaderboard_record_summary_instance.to_dict()
# create an instance of TeamStatsLeaderboardRecordSummary from a dict
team_stats_leaderboard_record_summary_from_dict = TeamStatsLeaderboardRecordSummary.from_dict(team_stats_leaderboard_record_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


