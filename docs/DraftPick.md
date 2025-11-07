# DraftPick


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**athlete_id** | **int** |  | 
**source_team_id** | **int** |  | 
**source_team_location** | **str** |  | 
**source_team_name** | **str** |  | 
**source_team_league_affiliation** | **str** |  | 
**source_team_college_id** | **float** |  | 
**draft_team_id** | **float** |  | 
**draft_team** | **str** |  | 
**year** | **int** |  | 
**overall** | **int** |  | 
**round** | **int** |  | 
**pick** | **int** |  | 
**name** | **str** |  | 
**overall_rank** | **int** |  | 
**position_rank** | **int** |  | 
**height** | **float** |  | 
**weight** | **int** |  | 

## Example

```python
from cbbd.models.draft_pick import DraftPick

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPick from a JSON string
draft_pick_instance = DraftPick.from_json(json)
# print the JSON string representation of the object
print DraftPick.to_json()

# convert the object into a dict
draft_pick_dict = draft_pick_instance.to_dict()
# create an instance of DraftPick from a dict
draft_pick_from_dict = DraftPick.from_dict(draft_pick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


