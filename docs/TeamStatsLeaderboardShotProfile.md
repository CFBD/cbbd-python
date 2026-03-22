# TeamStatsLeaderboardShotProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assisted_pct** | **float** |  | 
**at_rim** | [**TeamStatsLeaderboardShotProfileAtRim**](TeamStatsLeaderboardShotProfileAtRim.md) |  | 
**dunk** | [**TeamStatsLeaderboardShotProfileDunk**](TeamStatsLeaderboardShotProfileDunk.md) |  | 
**layup** | [**TeamStatsLeaderboardShotProfileDunk**](TeamStatsLeaderboardShotProfileDunk.md) |  | 
**tip_in** | [**TeamStatsLeaderboardShotProfileTipIn**](TeamStatsLeaderboardShotProfileTipIn.md) |  | 
**two_point_jumper** | [**TeamStatsLeaderboardShotProfileTwoPointJumper**](TeamStatsLeaderboardShotProfileTwoPointJumper.md) |  | 
**three_point_jumper** | [**TeamStatsLeaderboardShotProfileTwoPointJumper**](TeamStatsLeaderboardShotProfileTwoPointJumper.md) |  | 
**free_throws** | [**TeamStatsLeaderboardShotProfileFreeThrows**](TeamStatsLeaderboardShotProfileFreeThrows.md) |  | 
**distribution** | [**TeamStatsLeaderboardShotProfileDistribution**](TeamStatsLeaderboardShotProfileDistribution.md) |  | 

## Example

```python
from cbbd.models.team_stats_leaderboard_shot_profile import TeamStatsLeaderboardShotProfile

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStatsLeaderboardShotProfile from a JSON string
team_stats_leaderboard_shot_profile_instance = TeamStatsLeaderboardShotProfile.from_json(json)
# print the JSON string representation of the object
print TeamStatsLeaderboardShotProfile.to_json()

# convert the object into a dict
team_stats_leaderboard_shot_profile_dict = team_stats_leaderboard_shot_profile_instance.to_dict()
# create an instance of TeamStatsLeaderboardShotProfile from a dict
team_stats_leaderboard_shot_profile_from_dict = TeamStatsLeaderboardShotProfile.from_dict(team_stats_leaderboard_shot_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


