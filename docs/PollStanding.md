# PollStanding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**var_date** | **str** |  | 
**week** | **float** |  | 
**season_type** | **str** |  | 
**rank** | **float** |  | 

## Example

```python
from cbbd.models.poll_standing import PollStanding

# TODO update the JSON string below
json = "{}"
# create an instance of PollStanding from a JSON string
poll_standing_instance = PollStanding.from_json(json)
# print the JSON string representation of the object
print PollStanding.to_json()

# convert the object into a dict
poll_standing_dict = poll_standing_instance.to_dict()
# create an instance of PollStanding from a dict
poll_standing_from_dict = PollStanding.from_dict(poll_standing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


