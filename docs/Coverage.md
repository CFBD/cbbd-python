# Coverage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**Availability**](Availability.md) |  | 
**reason** | [**Reason**](Reason.md) |  | 
**eligible_games** | **float** |  | 
**covered_games** | **float** |  | 

## Example

```python
from cbbd.models.coverage import Coverage

# TODO update the JSON string below
json = "{}"
# create an instance of Coverage from a JSON string
coverage_instance = Coverage.from_json(json)
# print the JSON string representation of the object
print Coverage.to_json()

# convert the object into a dict
coverage_dict = coverage_instance.to_dict()
# create an instance of Coverage from a dict
coverage_from_dict = Coverage.from_dict(coverage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


