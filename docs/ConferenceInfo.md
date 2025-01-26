# ConferenceInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_id** | **str** |  | 
**name** | **str** |  | 
**abbreviation** | **str** |  | 
**short_name** | **str** |  | 

## Example

```python
from cbbd.models.conference_info import ConferenceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceInfo from a JSON string
conference_info_instance = ConferenceInfo.from_json(json)
# print the JSON string representation of the object
print ConferenceInfo.to_json()

# convert the object into a dict
conference_info_dict = conference_info_instance.to_dict()
# create an instance of ConferenceInfo from a dict
conference_info_from_dict = ConferenceInfo.from_dict(conference_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


