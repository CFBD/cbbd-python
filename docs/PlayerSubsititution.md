# PlayerSubsititution


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_id** | **int** |  | 
**start_date** | **datetime** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**athlete_id** | **int** |  | 
**athlete** | **str** |  | 
**position** | **str** |  | 
**opponent_id** | **int** |  | 
**opponent** | **str** |  | 
**opponent_conference** | **str** |  | 
**sub_in** | [**PlayerSubsititutionSubIn**](PlayerSubsititutionSubIn.md) |  | 
**sub_out** | [**PlayerSubsititutionSubIn**](PlayerSubsititutionSubIn.md) |  | 

## Example

```python
from cbbd.models.player_subsititution import PlayerSubsititution

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSubsititution from a JSON string
player_subsititution_instance = PlayerSubsititution.from_json(json)
# print the JSON string representation of the object
print PlayerSubsititution.to_json()

# convert the object into a dict
player_subsititution_dict = player_subsititution_instance.to_dict()
# create an instance of PlayerSubsititution from a dict
player_subsititution_from_dict = PlayerSubsititution.from_dict(player_subsititution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


