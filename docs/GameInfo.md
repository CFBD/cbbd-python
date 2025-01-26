# GameInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_id** | **str** |  | 
**season_label** | **str** |  | 
**season** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**start_date** | **datetime** |  | 
**start_time_tbd** | **bool** |  | 
**neutral_site** | **bool** |  | 
**conference_game** | **bool** |  | 
**game_type** | **str** |  | 
**status** | [**GameStatus**](GameStatus.md) |  | 
**attendance** | **int** |  | 
**home_team_id** | **int** |  | 
**home_team** | **str** |  | 
**home_conference_id** | **int** |  | 
**home_conference** | **str** |  | 
**home_points** | **int** |  | 
**home_period_points** | **List[int]** |  | 
**home_winner** | **bool** |  | 
**away_team_id** | **int** |  | 
**away_team** | **str** |  | 
**away_conference_id** | **int** |  | 
**away_conference** | **str** |  | 
**away_points** | **int** |  | 
**away_period_points** | **List[int]** |  | 
**away_winner** | **bool** |  | 
**venue_id** | **int** |  | 
**venue** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from cbbd.models.game_info import GameInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GameInfo from a JSON string
game_info_instance = GameInfo.from_json(json)
# print the JSON string representation of the object
print GameInfo.to_json()

# convert the object into a dict
game_info_dict = game_info_instance.to_dict()
# create an instance of GameInfo from a dict
game_info_from_dict = GameInfo.from_dict(game_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


