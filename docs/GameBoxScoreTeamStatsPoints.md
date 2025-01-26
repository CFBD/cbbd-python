# GameBoxScoreTeamStatsPoints


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fast_break** | **float** |  | 
**off_turnovers** | **float** |  | 
**in_paint** | **float** |  | 
**by_period** | **List[float]** |  | 
**largest_lead** | **float** |  | 
**total** | **float** |  | 

## Example

```python
from cbbd.models.game_box_score_team_stats_points import GameBoxScoreTeamStatsPoints

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxScoreTeamStatsPoints from a JSON string
game_box_score_team_stats_points_instance = GameBoxScoreTeamStatsPoints.from_json(json)
# print the JSON string representation of the object
print GameBoxScoreTeamStatsPoints.to_json()

# convert the object into a dict
game_box_score_team_stats_points_dict = game_box_score_team_stats_points_instance.to_dict()
# create an instance of GameBoxScoreTeamStatsPoints from a dict
game_box_score_team_stats_points_from_dict = GameBoxScoreTeamStatsPoints.from_dict(game_box_score_team_stats_points_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


