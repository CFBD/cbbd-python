# ProfileGame


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**opponent_id** | **float** |  | 
**opponent** | **str** |  | 
**opponent_has_profile** | **bool** |  | 
**start_date** | **str** |  | 
**calendar_date** | **str** |  | 
**start_time_tbd** | **bool** |  | 
**location** | **str** |  | 
**status** | **str** |  | 
**season_type** | **str** |  | 
**game_type** | **str** |  | 
**eligibility** | **str** |  | 
**conference_game** | **bool** |  | 
**team_points** | **float** |  | 
**opponent_points** | **float** |  | 
**result** | **str** |  | 
**venue** | **str** |  | 

## Example

```python
from cbbd.models.profile_game import ProfileGame

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileGame from a JSON string
profile_game_instance = ProfileGame.from_json(json)
# print the JSON string representation of the object
print ProfileGame.to_json()

# convert the object into a dict
profile_game_dict = profile_game_instance.to_dict()
# create an instance of ProfileGame from a dict
profile_game_from_dict = ProfileGame.from_dict(profile_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


