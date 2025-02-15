# ShotInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shooter** | [**ShotInfoShooter**](ShotInfoShooter.md) |  | 
**made** | **bool** |  | 
**range** | **str** |  | 
**assisted** | **bool** |  | 
**assisted_by** | [**ShotInfoShooter**](ShotInfoShooter.md) |  | 
**location** | [**ShotInfoLocation**](ShotInfoLocation.md) |  | 

## Example

```python
from cbbd.models.shot_info import ShotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShotInfo from a JSON string
shot_info_instance = ShotInfo.from_json(json)
# print the JSON string representation of the object
print ShotInfo.to_json()

# convert the object into a dict
shot_info_dict = shot_info_instance.to_dict()
# create an instance of ShotInfo from a dict
shot_info_from_dict = ShotInfo.from_dict(shot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


