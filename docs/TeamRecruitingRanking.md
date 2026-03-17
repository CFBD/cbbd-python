# TeamRecruitingRanking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** |  | 
**team** | **str** |  | 
**conference** | **str** |  | 
**year** | **int** |  | 
**ranking** | **int** |  | 
**rating** | **float** |  | 

## Example

```python
from cbbd.models.team_recruiting_ranking import TeamRecruitingRanking

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRecruitingRanking from a JSON string
team_recruiting_ranking_instance = TeamRecruitingRanking.from_json(json)
# print the JSON string representation of the object
print TeamRecruitingRanking.to_json()

# convert the object into a dict
team_recruiting_ranking_dict = team_recruiting_ranking_instance.to_dict()
# create an instance of TeamRecruitingRanking from a dict
team_recruiting_ranking_from_dict = TeamRecruitingRanking.from_dict(team_recruiting_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


