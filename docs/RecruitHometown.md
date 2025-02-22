# RecruitHometown


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**state** | **str** |  | 
**city** | **str** |  | 

## Example

```python
from cbbd.models.recruit_hometown import RecruitHometown

# TODO update the JSON string below
json = "{}"
# create an instance of RecruitHometown from a JSON string
recruit_hometown_instance = RecruitHometown.from_json(json)
# print the JSON string representation of the object
print RecruitHometown.to_json()

# convert the object into a dict
recruit_hometown_dict = recruit_hometown_instance.to_dict()
# create an instance of RecruitHometown from a dict
recruit_hometown_from_dict = RecruitHometown.from_dict(recruit_hometown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


