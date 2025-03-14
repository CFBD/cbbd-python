# GameBoxScorePlayers


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**season_label** | **str** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**tournament** | **str** |  | 
**start_date** | **datetime** |  | 
**start_time_tbd** | **bool** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**team_seed** | **int** |  | 
**opponent_id** | **int** |  | 
**opponent** | **str** |  | 
**opponent_conference** | **str** |  | 
**opponent_seed** | **int** |  | 
**neutral_site** | **bool** |  | 
**conference_game** | **bool** |  | 
**game_type** | **str** |  | 
**notes** | **str** |  | 
**game_minutes** | **float** |  | 
**game_pace** | **float** |  | 
**players** | [**List[GameBoxScorePlayersPlayersInner]**](GameBoxScorePlayersPlayersInner.md) |  | 

## Example

```python
from cbbd.models.game_box_score_players import GameBoxScorePlayers

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxScorePlayers from a JSON string
game_box_score_players_instance = GameBoxScorePlayers.from_json(json)
# print the JSON string representation of the object
print GameBoxScorePlayers.to_json()

# convert the object into a dict
game_box_score_players_dict = game_box_score_players_instance.to_dict()
# create an instance of GameBoxScorePlayers from a dict
game_box_score_players_from_dict = GameBoxScorePlayers.from_dict(game_box_score_players_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


