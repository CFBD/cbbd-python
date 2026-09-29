# ShotBucket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**attempts** | **float** |  | 
**made** | **float** |  | 
**attempt_pct** | **float** |  | 
**field_goal_pct** | **float** |  | 

## Example

```python
from cbbd.models.shot_bucket import ShotBucket

# TODO update the JSON string below
json = "{}"
# create an instance of ShotBucket from a JSON string
shot_bucket_instance = ShotBucket.from_json(json)
# print the JSON string representation of the object
print ShotBucket.to_json()

# convert the object into a dict
shot_bucket_dict = shot_bucket_instance.to_dict()
# create an instance of ShotBucket from a dict
shot_bucket_from_dict = ShotBucket.from_dict(shot_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


