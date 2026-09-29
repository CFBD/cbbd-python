# DirectoryTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**source_id** | **str** |  | 
**school** | **str** |  | 
**mascot** | **str** |  | 
**abbreviation** | **str** |  | 
**display_name** | **str** |  | 
**short_display_name** | **str** |  | 
**conference_id** | **float** |  | 

## Example

```python
from cbbd.models.directory_team import DirectoryTeam

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoryTeam from a JSON string
directory_team_instance = DirectoryTeam.from_json(json)
# print the JSON string representation of the object
print DirectoryTeam.to_json()

# convert the object into a dict
directory_team_dict = directory_team_instance.to_dict()
# create an instance of DirectoryTeam from a dict
directory_team_from_dict = DirectoryTeam.from_dict(directory_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


