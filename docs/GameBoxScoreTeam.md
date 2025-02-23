# GameBoxScoreTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**season_label** | **str** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**start_date** | **datetime** |  | 
**start_time_tbd** | **bool** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**opponent_id** | **int** |  | 
**opponent** | **str** |  | 
**opponent_conference** | **str** |  | 
**neutral_site** | **bool** |  | 
**conference_game** | **bool** |  | 
**game_type** | **str** |  | 
**notes** | **str** |  | 
**game_minutes** | **float** |  | 
**pace** | **float** |  | 
**team_stats** | [**GameBoxScoreTeamStats**](GameBoxScoreTeamStats.md) |  | 
**opponent_stats** | [**GameBoxScoreTeamStats**](GameBoxScoreTeamStats.md) |  | 

## Example

```python
from cbbd.models.game_box_score_team import GameBoxScoreTeam

# TODO update the JSON string below
json = "{}"
# create an instance of GameBoxScoreTeam from a JSON string
game_box_score_team_instance = GameBoxScoreTeam.from_json(json)
# print the JSON string representation of the object
print GameBoxScoreTeam.to_json()

# convert the object into a dict
game_box_score_team_dict = game_box_score_team_instance.to_dict()
# create an instance of GameBoxScoreTeam from a dict
game_box_score_team_from_dict = GameBoxScoreTeam.from_dict(game_box_score_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


