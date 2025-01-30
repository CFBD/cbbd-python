# SrsInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**rating** | **float** |  | 

## Example

```python
from cbbd.models.srs_info import SrsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SrsInfo from a JSON string
srs_info_instance = SrsInfo.from_json(json)
# print the JSON string representation of the object
print SrsInfo.to_json()

# convert the object into a dict
srs_info_dict = srs_info_instance.to_dict()
# create an instance of SrsInfo from a dict
srs_info_from_dict = SrsInfo.from_dict(srs_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


