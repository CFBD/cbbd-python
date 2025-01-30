# GameLineInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**spread** | **float** |  | 
**over_under** | **float** |  | 
**home_moneyline** | **float** |  | 
**away_moneyline** | **float** |  | 
**spread_open** | **float** |  | 
**over_under_open** | **float** |  | 

## Example

```python
from cbbd.models.game_line_info import GameLineInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GameLineInfo from a JSON string
game_line_info_instance = GameLineInfo.from_json(json)
# print the JSON string representation of the object
print GameLineInfo.to_json()

# convert the object into a dict
game_line_info_dict = game_line_info_instance.to_dict()
# create an instance of GameLineInfo from a dict
game_line_info_from_dict = GameLineInfo.from_dict(game_line_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


