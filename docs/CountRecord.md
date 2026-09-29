# CountRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**games** | **float** |  | 
**wins** | **float** |  | 
**losses** | **float** |  | 
**unresolved** | **float** |  | 

## Example

```python
from cbbd.models.count_record import CountRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CountRecord from a JSON string
count_record_instance = CountRecord.from_json(json)
# print the JSON string representation of the object
print CountRecord.to_json()

# convert the object into a dict
count_record_dict = count_record_instance.to_dict()
# create an instance of CountRecord from a dict
count_record_from_dict = CountRecord.from_dict(count_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


