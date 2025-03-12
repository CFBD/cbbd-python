# ShootingStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**made** | **int** |  | 
**attempted** | **int** |  | 
**pct** | **float** |  | 

## Example

```python
from cbbd.models.shooting_stats import ShootingStats

# TODO update the JSON string below
json = "{}"
# create an instance of ShootingStats from a JSON string
shooting_stats_instance = ShootingStats.from_json(json)
# print the JSON string representation of the object
print ShootingStats.to_json()

# convert the object into a dict
shooting_stats_dict = shooting_stats_instance.to_dict()
# create an instance of ShootingStats from a dict
shooting_stats_from_dict = ShootingStats.from_dict(shooting_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


