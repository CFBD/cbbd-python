# TeamRosterPlayer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_id** | **str** |  | 
**name** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**jersey** | **str** |  | 
**position** | **str** |  | 
**height** | **float** |  | 
**weight** | **float** |  | 
**hometown** | [**TeamRosterPlayerHometown**](TeamRosterPlayerHometown.md) |  | 
**date_of_birth** | **date** |  | 
**start_season** | **float** |  | 
**end_season** | **float** |  | 

## Example

```python
from cbbd.models.team_roster_player import TeamRosterPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRosterPlayer from a JSON string
team_roster_player_instance = TeamRosterPlayer.from_json(json)
# print the JSON string representation of the object
print TeamRosterPlayer.to_json()

# convert the object into a dict
team_roster_player_dict = team_roster_player_instance.to_dict()
# create an instance of TeamRosterPlayer from a dict
team_roster_player_from_dict = TeamRosterPlayer.from_dict(team_roster_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


