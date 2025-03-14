# GameMediaInfo


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
**home_team_id** | **int** |  | 
**home_team** | **str** |  | 
**home_conference** | **str** |  | 
**away_team_id** | **int** |  | 
**away_team** | **str** |  | 
**away_conference** | **str** |  | 
**neutral_site** | **bool** |  | 
**conference_game** | **bool** |  | 
**game_type** | **str** |  | 
**notes** | **str** |  | 
**broadcasts** | [**List[GameMediaInfoBroadcastsInner]**](GameMediaInfoBroadcastsInner.md) |  | 

## Example

```python
from cbbd.models.game_media_info import GameMediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GameMediaInfo from a JSON string
game_media_info_instance = GameMediaInfo.from_json(json)
# print the JSON string representation of the object
print GameMediaInfo.to_json()

# convert the object into a dict
game_media_info_dict = game_media_info_instance.to_dict()
# create an instance of GameMediaInfo from a dict
game_media_info_from_dict = GameMediaInfo.from_dict(game_media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


