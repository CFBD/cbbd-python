# ProfilePlayer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_stats** | [**PlayerSeasonDetails**](PlayerSeasonDetails.md) |  | [optional] 
**athlete_id** | **float** |  | 
**name** | **str** |  | 
**position** | **str** |  | 
**on_roster** | **bool** |  | 
**has_stats** | **bool** |  | 
**games** | **float** |  | 
**minutes** | **float** |  | 
**points** | **float** |  | 
**rebounds** | **float** |  | 
**assists** | **float** |  | 
**minutes_per_game** | **float** |  | 
**points_per_game** | **float** |  | 
**usage_pct** | **float** |  | 
**true_shooting_pct** | **float** |  | 
**effective_field_goal_pct** | **float** |  | 
**usage_games** | **float** |  | 
**complete** | **bool** |  | 

## Example

```python
from cbbd.models.profile_player import ProfilePlayer

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePlayer from a JSON string
profile_player_instance = ProfilePlayer.from_json(json)
# print the JSON string representation of the object
print ProfilePlayer.to_json()

# convert the object into a dict
profile_player_dict = profile_player_instance.to_dict()
# create an instance of ProfilePlayer from a dict
profile_player_from_dict = ProfilePlayer.from_dict(profile_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


