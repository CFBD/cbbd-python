# PlayerSeasonDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_goals** | [**ShootingLine**](ShootingLine.md) |  | 
**two_point_field_goals** | [**ShootingLine**](ShootingLine.md) |  | 
**three_point_field_goals** | [**ShootingLine**](ShootingLine.md) |  | 
**free_throws** | [**ShootingLine**](ShootingLine.md) |  | 
**rebounds** | [**TeamBoxScoreRebounds**](TeamBoxScoreRebounds.md) |  | 
**assists** | **float** |  | 
**steals** | **float** |  | 
**blocks** | **float** |  | 
**turnovers** | **float** |  | 
**fouls** | **float** |  | 
**starts** | **float** |  | 
**assist_turnover_ratio** | **float** |  | 
**free_throw_rate** | **float** |  | 
**offensive_rebound_pct** | **float** |  | 
**advanced** | [**PlayerSeasonDetailsAdvanced**](PlayerSeasonDetailsAdvanced.md) |  | 

## Example

```python
from cbbd.models.player_season_details import PlayerSeasonDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSeasonDetails from a JSON string
player_season_details_instance = PlayerSeasonDetails.from_json(json)
# print the JSON string representation of the object
print PlayerSeasonDetails.to_json()

# convert the object into a dict
player_season_details_dict = player_season_details_instance.to_dict()
# create an instance of PlayerSeasonDetails from a dict
player_season_details_from_dict = PlayerSeasonDetails.from_dict(player_season_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


