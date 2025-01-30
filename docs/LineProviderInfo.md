# LineProviderInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from cbbd.models.line_provider_info import LineProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LineProviderInfo from a JSON string
line_provider_info_instance = LineProviderInfo.from_json(json)
# print the JSON string representation of the object
print LineProviderInfo.to_json()

# convert the object into a dict
line_provider_info_dict = line_provider_info_instance.to_dict()
# create an instance of LineProviderInfo from a dict
line_provider_info_from_dict = LineProviderInfo.from_dict(line_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


