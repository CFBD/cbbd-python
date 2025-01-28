# TeamRoster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**team_source_id** | **str** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**season** | **float** |  | 
**players** | [**List[TeamRosterPlayer]**](TeamRosterPlayer.md) |  | 

## Example

```python
from cbbd.models.team_roster import TeamRoster

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRoster from a JSON string
team_roster_instance = TeamRoster.from_json(json)
# print the JSON string representation of the object
print TeamRoster.to_json()

# convert the object into a dict
team_roster_dict = team_roster_instance.to_dict()
# create an instance of TeamRoster from a dict
team_roster_from_dict = TeamRoster.from_dict(team_roster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


