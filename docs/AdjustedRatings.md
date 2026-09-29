# AdjustedRatings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offense** | [**RatedValue**](RatedValue.md) |  | 
**defense** | [**RatedValue**](RatedValue.md) |  | 
**net** | [**RatedValue**](RatedValue.md) |  | 
**population** | **float** |  | 

## Example

```python
from cbbd.models.adjusted_ratings import AdjustedRatings

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustedRatings from a JSON string
adjusted_ratings_instance = AdjustedRatings.from_json(json)
# print the JSON string representation of the object
print AdjustedRatings.to_json()

# convert the object into a dict
adjusted_ratings_dict = adjusted_ratings_instance.to_dict()
# create an instance of AdjustedRatings from a dict
adjusted_ratings_from_dict = AdjustedRatings.from_dict(adjusted_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


