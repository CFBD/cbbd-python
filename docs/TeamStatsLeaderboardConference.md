# TeamStatsLeaderboardConference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**abbreviation** | **str** |  | 

## Example

```python
from cbbd.models.team_stats_leaderboard_conference import TeamStatsLeaderboardConference

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatsLeaderboardConference from a JSON string
team_stats_leaderboard_conference_instance = TeamStatsLeaderboardConference.from_json(json)
# print the JSON string representation of the object
print TeamStatsLeaderboardConference.to_json()

# convert the object into a dict
team_stats_leaderboard_conference_dict = team_stats_leaderboard_conference_instance.to_dict()
# create an instance of TeamStatsLeaderboardConference from a dict
team_stats_leaderboard_conference_from_dict = TeamStatsLeaderboardConference.from_dict(team_stats_leaderboard_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


