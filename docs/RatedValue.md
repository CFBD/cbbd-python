# RatedValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 
**rank** | **float** |  | 

## Example

```python
from cbbd.models.rated_value import RatedValue

# TODO update the JSON string below
json = "{}"
# create an instance of RatedValue from a JSON string
rated_value_instance = RatedValue.from_json(json)
# print the JSON string representation of the object
print RatedValue.to_json()

# convert the object into a dict
rated_value_dict = rated_value_instance.to_dict()
# create an instance of RatedValue from a dict
rated_value_from_dict = RatedValue.from_dict(rated_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


