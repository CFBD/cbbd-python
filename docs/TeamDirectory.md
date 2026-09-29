# TeamDirectory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **float** |  | 
**season_label** | **str** |  | 
**teams** | [**List[DirectoryTeam]**](DirectoryTeam.md) |  | 
**conferences** | [**List[Conference]**](Conference.md) |  | 

## Example

```python
from cbbd.models.team_directory import TeamDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDirectory from a JSON string
team_directory_instance = TeamDirectory.from_json(json)
# print the JSON string representation of the object
print TeamDirectory.to_json()

# convert the object into a dict
team_directory_dict = team_directory_instance.to_dict()
# create an instance of TeamDirectory from a dict
team_directory_from_dict = TeamDirectory.from_dict(team_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


