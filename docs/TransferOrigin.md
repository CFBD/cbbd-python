# TransferOrigin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | **str** |  | 
**name** | **str** |  | 
**id** | **int** | * | 

## Example

```python
from cbbd.models.transfer_origin import TransferOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOrigin from a JSON string
transfer_origin_instance = TransferOrigin.from_json(json)
# print the JSON string representation of the object
print TransferOrigin.to_json()

# convert the object into a dict
transfer_origin_dict = transfer_origin_instance.to_dict()
# create an instance of TransferOrigin from a dict
transfer_origin_from_dict = TransferOrigin.from_dict(transfer_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


