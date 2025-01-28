# ConferenceHistoryTeamsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_season** | **int** |  | 
**start_season** | **int** |  | 
**mascot** | **str** |  | 
**school** | **str** |  | 
**source_id** | **str** |  | 
**id** | **int** |  | 

## Example

```python
from cbbd.models.conference_history_teams_inner import ConferenceHistoryTeamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceHistoryTeamsInner from a JSON string
conference_history_teams_inner_instance = ConferenceHistoryTeamsInner.from_json(json)
# print the JSON string representation of the object
print ConferenceHistoryTeamsInner.to_json()

# convert the object into a dict
conference_history_teams_inner_dict = conference_history_teams_inner_instance.to_dict()
# create an instance of ConferenceHistoryTeamsInner from a dict
conference_history_teams_inner_from_dict = ConferenceHistoryTeamsInner.from_dict(conference_history_teams_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


