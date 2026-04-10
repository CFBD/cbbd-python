# Transfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_id** | **str** |  | 
**year** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**position** | **str** |  | 
**origin** | [**TransferOrigin**](TransferOrigin.md) |  | 
**destination** | [**RecruitCommittedTo**](RecruitCommittedTo.md) |  | 
**eligibility** | [**TransferEligibility**](TransferEligibility.md) |  | 
**years_remaining** | **int** |  | 
**stars** | **int** |  | 
**rating** | **float** |  | 

## Example

```python
from cbbd.models.transfer import Transfer

# TODO update the JSON string below
json = "{}"
# create an instance of Transfer from a JSON string
transfer_instance = Transfer.from_json(json)
# print the JSON string representation of the object
print Transfer.to_json()

# convert the object into a dict
transfer_dict = transfer_instance.to_dict()
# create an instance of Transfer from a dict
transfer_from_dict = Transfer.from_dict(transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


