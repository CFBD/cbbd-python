# GameBoxScorePlayersPlayersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rebounds** | [**TeamSeasonUnitStatsRebounds**](TeamSeasonUnitStatsRebounds.md) |  | 
**free_throws** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**three_point_field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**two_point_field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**field_goals** | [**TeamSeasonUnitStatsFieldGoals**](TeamSeasonUnitStatsFieldGoals.md) |  | 
**offensive_rebound_pct** | **float** |  | 
**free_throw_rate** | **float** |  | 
**assists_turnover_ratio** | **float** |  | 
**game_score** | **float** |  | 
**true_shooting_pct** | **float** |  | 
**effective_field_goal_pct** | **float** |  | 
**net_rating** | **float** |  | 
**defensive_rating** | **float** |  | 
**offensive_rating** | **float** |  | 
**usage** | **float** |  | 
**blocks** | **float** |  | 
**steals** | **float** |  | 
**assists** | **float** |  | 
**fouls** | **float** |  | 
**turnovers** | **float** |  | 
**points** | **float** |  | 
**minutes** | **float** |  | 
**ejected** | **bool** |  | 
**starter** | **bool** |  | 
**position** | **str** |  | 
**name** | **str** |  | 
**athlete_source_id** | **str** |  | 
**athlete_id** | **int** |  | 

## Example

```python
from cbbd.models.game_box_score_players_players_inner import GameBoxScorePlayersPlayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxScorePlayersPlayersInner from a JSON string
game_box_score_players_players_inner_instance = GameBoxScorePlayersPlayersInner.from_json(json)
# print the JSON string representation of the object
print GameBoxScorePlayersPlayersInner.to_json()

# convert the object into a dict
game_box_score_players_players_inner_dict = game_box_score_players_players_inner_instance.to_dict()
# create an instance of GameBoxScorePlayersPlayersInner from a dict
game_box_score_players_players_inner_from_dict = GameBoxScorePlayersPlayersInner.from_dict(game_box_score_players_players_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


