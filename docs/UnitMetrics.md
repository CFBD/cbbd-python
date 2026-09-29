# UnitMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_score** | [**TeamBoxScore**](TeamBoxScore.md) |  | [optional] 
**points** | **float** |  | 
**possessions** | **float** |  | 
**raw_rating** | **float** |  | 
**effective_field_goal_pct** | **float** |  | 
**turnover_pct** | **float** |  | 
**offensive_rebound_pct** | **float** |  | 
**free_throw_rate** | **float** |  | 

## Example

```python
from cbbd.models.unit_metrics import UnitMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of UnitMetrics from a JSON string
unit_metrics_instance = UnitMetrics.from_json(json)
# print the JSON string representation of the object
print UnitMetrics.to_json()

# convert the object into a dict
unit_metrics_dict = unit_metrics_instance.to_dict()
# create an instance of UnitMetrics from a dict
unit_metrics_from_dict = UnitMetrics.from_dict(unit_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


