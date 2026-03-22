# TeamStatsLeaderboardRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | [**TeamStatsLeaderboardConference**](TeamStatsLeaderboardConference.md) |  | 
**record** | [**TeamStatsLeaderboardRecordSummary**](TeamStatsLeaderboardRecordSummary.md) |  | 
**summary** | [**TeamStatsLeaderboardSummary**](TeamStatsLeaderboardSummary.md) |  | 
**team_stats** | [**TeamStatsLeaderboardUnitStats**](TeamStatsLeaderboardUnitStats.md) |  | 
**opponent_stats** | [**TeamStatsLeaderboardUnitStats**](TeamStatsLeaderboardUnitStats.md) |  | 
**shot_profile** | [**TeamStatsLeaderboardShotProfile**](TeamStatsLeaderboardShotProfile.md) |  | 
**adjusted_efficiency** | [**TeamLeaderboardAdjustedEfficiency**](TeamLeaderboardAdjustedEfficiency.md) |  | 

## Example

```python
from cbbd.models.team_stats_leaderboard_record import TeamStatsLeaderboardRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatsLeaderboardRecord from a JSON string
team_stats_leaderboard_record_instance = TeamStatsLeaderboardRecord.from_json(json)
# print the JSON string representation of the object
print TeamStatsLeaderboardRecord.to_json()

# convert the object into a dict
team_stats_leaderboard_record_dict = team_stats_leaderboard_record_instance.to_dict()
# create an instance of TeamStatsLeaderboardRecord from a dict
team_stats_leaderboard_record_from_dict = TeamStatsLeaderboardRecord.from_dict(team_stats_leaderboard_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


