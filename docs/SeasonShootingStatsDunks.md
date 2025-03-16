# SeasonShootingStatsDunks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**made** | **int** |  | 
**attempted** | **int** |  | 
**pct** | **float** |  | 
**assisted_pct** | **float** |  | 
**assisted** | **int** |  | 

## Example

```python
from cbbd.models.season_shooting_stats_dunks import SeasonShootingStatsDunks

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonShootingStatsDunks from a JSON string
season_shooting_stats_dunks_instance = SeasonShootingStatsDunks.from_json(json)
# print the JSON string representation of the object
print SeasonShootingStatsDunks.to_json()

# convert the object into a dict
season_shooting_stats_dunks_dict = season_shooting_stats_dunks_instance.to_dict()
# create an instance of SeasonShootingStatsDunks from a dict
season_shooting_stats_dunks_from_dict = SeasonShootingStatsDunks.from_dict(season_shooting_stats_dunks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


