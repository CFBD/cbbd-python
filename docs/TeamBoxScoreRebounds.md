# TeamBoxScoreRebounds


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**defensive** | **float** |  | 
**offensive** | **float** |  | 

## Example

```python
from cbbd.models.team_box_score_rebounds import TeamBoxScoreRebounds

# TODO update the JSON string below
json = "{}"
# create an instance of TeamBoxScoreRebounds from a JSON string
team_box_score_rebounds_instance = TeamBoxScoreRebounds.from_json(json)
# print the JSON string representation of the object
print TeamBoxScoreRebounds.to_json()

# convert the object into a dict
team_box_score_rebounds_dict = team_box_score_rebounds_instance.to_dict()
# create an instance of TeamBoxScoreRebounds from a dict
team_box_score_rebounds_from_dict = TeamBoxScoreRebounds.from_dict(team_box_score_rebounds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


