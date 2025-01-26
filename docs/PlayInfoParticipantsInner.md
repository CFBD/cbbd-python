# PlayInfoParticipantsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**id** | **int** |  | 

## Example

```python
from cbbd.models.play_info_participants_inner import PlayInfoParticipantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PlayInfoParticipantsInner from a JSON string
play_info_participants_inner_instance = PlayInfoParticipantsInner.from_json(json)
# print the JSON string representation of the object
print PlayInfoParticipantsInner.to_json()

# convert the object into a dict
play_info_participants_inner_dict = play_info_participants_inner_instance.to_dict()
# create an instance of PlayInfoParticipantsInner from a dict
play_info_participants_inner_from_dict = PlayInfoParticipantsInner.from_dict(play_info_participants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


