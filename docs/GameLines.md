# GameLines


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**season** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**start_date** | **datetime** |  | 
**home_team_id** | **int** |  | 
**home_team** | **str** |  | 
**home_conference** | **str** |  | 
**home_score** | **float** |  | 
**away_team_id** | **int** |  | 
**away_team** | **str** |  | 
**away_conference** | **str** |  | 
**away_score** | **float** |  | 
**lines** | [**List[GameLineInfo]**](GameLineInfo.md) |  | 

## Example

```python
from cbbd.models.game_lines import GameLines

# TODO update the JSON string below
json = "{}"
# create an instance of GameLines from a JSON string
game_lines_instance = GameLines.from_json(json)
# print the JSON string representation of the object
print GameLines.to_json()

# convert the object into a dict
game_lines_dict = game_lines_instance.to_dict()
# create an instance of GameLines from a dict
game_lines_from_dict = GameLines.from_dict(game_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


