# Recruit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_id** | **str** |  | 
**position** | **str** |  | 
**school_id** | **int** |  | 
**school** | **str** |  | 
**hometown** | [**RecruitHometown**](RecruitHometown.md) |  | 
**committed_to** | [**RecruitCommittedTo**](RecruitCommittedTo.md) |  | 
**athlete_id** | **int** |  | 
**year** | **int** |  | 
**name** | **str** |  | 
**height_inches** | **int** |  | 
**weight_pounds** | **int** |  | 
**stars** | **int** |  | 
**rating** | **float** |  | 
**ranking** | **int** |  | 

## Example

```python
from cbbd.models.recruit import Recruit

# TODO update the JSON string below
json = "{}"
# create an instance of Recruit from a JSON string
recruit_instance = Recruit.from_json(json)
# print the JSON string representation of the object
print Recruit.to_json()

# convert the object into a dict
recruit_dict = recruit_instance.to_dict()
# create an instance of Recruit from a dict
recruit_from_dict = Recruit.from_dict(recruit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


