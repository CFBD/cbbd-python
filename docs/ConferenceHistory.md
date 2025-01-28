# ConferenceHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_id** | **str** |  | 
**name** | **str** |  | 
**abbreviation** | **str** |  | 
**short_name** | **str** |  | 
**teams** | [**List[ConferenceHistoryTeamsInner]**](ConferenceHistoryTeamsInner.md) |  | 

## Example

```python
from cbbd.models.conference_history import ConferenceHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceHistory from a JSON string
conference_history_instance = ConferenceHistory.from_json(json)
# print the JSON string representation of the object
print ConferenceHistory.to_json()

# convert the object into a dict
conference_history_dict = conference_history_instance.to_dict()
# create an instance of ConferenceHistory from a dict
conference_history_from_dict = ConferenceHistory.from_dict(conference_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


