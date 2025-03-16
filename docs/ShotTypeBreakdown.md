# ShotTypeBreakdown


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**made** | **int** |  | 
**attempted** | **int** |  | 
**pct** | **float** |  | 

## Example

```python
from cbbd.models.shot_type_breakdown import ShotTypeBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ShotTypeBreakdown from a JSON string
shot_type_breakdown_instance = ShotTypeBreakdown.from_json(json)
# print the JSON string representation of the object
print ShotTypeBreakdown.to_json()

# convert the object into a dict
shot_type_breakdown_dict = shot_type_breakdown_instance.to_dict()
# create an instance of ShotTypeBreakdown from a dict
shot_type_breakdown_from_dict = ShotTypeBreakdown.from_dict(shot_type_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


