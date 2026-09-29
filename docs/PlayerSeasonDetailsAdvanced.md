# PlayerSeasonDetailsAdvanced


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**win_shares** | [**PlayerSeasonDetailsAdvancedWinShares**](PlayerSeasonDetailsAdvancedWinShares.md) |  | 
**porpag** | **float** |  | 
**net_rating** | **float** |  | 
**defensive_rating** | **float** |  | 
**offensive_rating** | **float** |  | 
**games** | **float** |  | 

## Example

```python
from cbbd.models.player_season_details_advanced import PlayerSeasonDetailsAdvanced

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonDetailsAdvanced from a JSON string
player_season_details_advanced_instance = PlayerSeasonDetailsAdvanced.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonDetailsAdvanced.to_json()

# convert the object into a dict
player_season_details_advanced_dict = player_season_details_advanced_instance.to_dict()
# create an instance of PlayerSeasonDetailsAdvanced from a dict
player_season_details_advanced_from_dict = PlayerSeasonDetailsAdvanced.from_dict(player_season_details_advanced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


