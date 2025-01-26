# VenueInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**source_id** | **str** |  | 
**name** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 
**country** | **str** |  | 

## Example

```python
from cbbd.models.venue_info import VenueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VenueInfo from a JSON string
venue_info_instance = VenueInfo.from_json(json)
# print the JSON string representation of the object
print VenueInfo.to_json()

# convert the object into a dict
venue_info_dict = venue_info_instance.to_dict()
# create an instance of VenueInfo from a dict
venue_info_from_dict = VenueInfo.from_dict(venue_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


