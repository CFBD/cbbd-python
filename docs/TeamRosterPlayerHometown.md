# TeamRosterPlayerHometown


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**state** | **str** |  | 
**city** | **str** |  | 

## Example

```python
from cbbd.models.team_roster_player_hometown import TeamRosterPlayerHometown

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRosterPlayerHometown from a JSON string
team_roster_player_hometown_instance = TeamRosterPlayerHometown.from_json(json)
# print the JSON string representation of the object
print TeamRosterPlayerHometown.to_json()

# convert the object into a dict
team_roster_player_hometown_dict = team_roster_player_hometown_instance.to_dict()
# create an instance of TeamRosterPlayerHometown from a dict
team_roster_player_hometown_from_dict = TeamRosterPlayerHometown.from_dict(team_roster_player_hometown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


