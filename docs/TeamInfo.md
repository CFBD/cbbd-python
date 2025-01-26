# TeamInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_id** | **str** |  | 
**school** | **str** |  | 
**mascot** | **str** |  | 
**abbreviation** | **str** |  | 
**display_name** | **str** |  | 
**short_display_name** | **str** |  | 
**primary_color** | **str** |  | 
**secondary_color** | **str** |  | 
**current_venue_id** | **int** |  | 
**current_venue** | **str** |  | 
**current_city** | **str** |  | 
**current_state** | **str** |  | 
**conference_id** | **int** |  | 
**conference** | **str** |  | 

## Example

```python
from cbbd.models.team_info import TeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TeamInfo from a JSON string
team_info_instance = TeamInfo.from_json(json)
# print the JSON string representation of the object
print TeamInfo.to_json()

# convert the object into a dict
team_info_dict = team_info_instance.to_dict()
# create an instance of TeamInfo from a dict
team_info_from_dict = TeamInfo.from_dict(team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


