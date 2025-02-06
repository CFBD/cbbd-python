# PollTeamInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**season_type** | [**SeasonType**](SeasonType.md) |  | 
**week** | **int** |  | 
**poll_date** | **datetime** |  | 
**poll_type** | **str** |  | 
**team_id** | **float** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**ranking** | **float** |  | 
**points** | **float** |  | 
**first_place_votes** | **float** |  | 

## Example

```python
from cbbd.models.poll_team_info import PollTeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PollTeamInfo from a JSON string
poll_team_info_instance = PollTeamInfo.from_json(json)
# print the JSON string representation of the object
print PollTeamInfo.to_json()

# convert the object into a dict
poll_team_info_dict = poll_team_info_instance.to_dict()
# create an instance of PollTeamInfo from a dict
poll_team_info_from_dict = PollTeamInfo.from_dict(poll_team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


