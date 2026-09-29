# TeamBoxScore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_goals** | [**ShootingLine**](ShootingLine.md) |  | 
**two_point_field_goals** | [**ShootingLine**](ShootingLine.md) |  | 
**three_point_field_goals** | [**ShootingLine**](ShootingLine.md) |  | 
**free_throws** | [**ShootingLine**](ShootingLine.md) |  | 
**rebounds** | [**TeamBoxScoreRebounds**](TeamBoxScoreRebounds.md) |  | 
**assists** | **float** |  | 
**steals** | **float** |  | 
**blocks** | **float** |  | 
**turnovers** | **float** |  | 
**fouls** | **float** |  | 
**minutes** | **float** |  | 
**team_turnovers** | **float** |  | 
**technical_fouls** | **float** |  | 
**flagrant_fouls** | **float** |  | 
**points_in_paint** | **float** |  | 
**points_off_turnovers** | **float** |  | 
**fast_break_points** | **float** |  | 
**true_shooting_pct** | **float** |  | 

## Example

```python
from cbbd.models.team_box_score import TeamBoxScore

# TODO update the JSON string below
json = "{}"
# create an instance of TeamBoxScore from a JSON string
team_box_score_instance = TeamBoxScore.from_json(json)
# print the JSON string representation of the object
print TeamBoxScore.to_json()

# convert the object into a dict
team_box_score_dict = team_box_score_instance.to_dict()
# create an instance of TeamBoxScore from a dict
team_box_score_from_dict = TeamBoxScore.from_dict(team_box_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


