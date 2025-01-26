# PlayTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from cbbd.models.play_type_info import PlayTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlayTypeInfo from a JSON string
play_type_info_instance = PlayTypeInfo.from_json(json)
# print the JSON string representation of the object
print PlayTypeInfo.to_json()

# convert the object into a dict
play_type_info_dict = play_type_info_instance.to_dict()
# create an instance of PlayTypeInfo from a dict
play_type_info_from_dict = PlayTypeInfo.from_dict(play_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


