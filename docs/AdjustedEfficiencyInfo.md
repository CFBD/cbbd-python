# AdjustedEfficiencyInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**offensive_rating** | **float** |  | 
**defensive_rating** | **float** |  | 
**net_rating** | **float** |  | 

## Example

```python
from cbbd.models.adjusted_efficiency_info import AdjustedEfficiencyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedEfficiencyInfo from a JSON string
adjusted_efficiency_info_instance = AdjustedEfficiencyInfo.from_json(json)
# print the JSON string representation of the object
print AdjustedEfficiencyInfo.to_json()

# convert the object into a dict
adjusted_efficiency_info_dict = adjusted_efficiency_info_instance.to_dict()
# create an instance of AdjustedEfficiencyInfo from a dict
adjusted_efficiency_info_from_dict = AdjustedEfficiencyInfo.from_dict(adjusted_efficiency_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


