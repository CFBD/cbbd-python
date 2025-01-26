# PlayInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_id** | **str** |  | 
**game_id** | **int** |  | 
**game_source_id** | **str** |  | 
**game_start_date** | **datetime** |  | 
**season** | **float** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**game_type** | **str** |  | 
**play_type** | **str** |  | 
**is_home_team** | **bool** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**opponent_id** | **int** |  | 
**opponent** | **str** |  | 
**opponent_conference** | **str** |  | 
**period** | **int** |  | 
**clock** | **str** |  | 
**seconds_remaining** | **int** |  | 
**home_score** | **int** |  | 
**away_score** | **int** |  | 
**scoring_play** | **bool** |  | 
**shooting_play** | **bool** |  | 
**score_value** | **float** |  | 
**wallclock** | **datetime** |  | 
**play_text** | **str** |  | 
**participants** | [**List[PlayInfoParticipantsInner]**](PlayInfoParticipantsInner.md) |  | 

## Example

```python
from cbbd.models.play_info import PlayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlayInfo from a JSON string
play_info_instance = PlayInfo.from_json(json)
# print the JSON string representation of the object
print PlayInfo.to_json()

# convert the object into a dict
play_info_dict = play_info_instance.to_dict()
# create an instance of PlayInfo from a dict
play_info_from_dict = PlayInfo.from_dict(play_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


