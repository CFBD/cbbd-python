# TeamSeasonOverviewRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unknown_conference_games** | **float** |  | 
**unknown_eligibility_games** | **float** |  | 
**complete** | **bool** |  | 
**conference** | [**CountRecord**](CountRecord.md) |  | 
**overall** | [**CountRecord**](CountRecord.md) |  | 

## Example

```python
from cbbd.models.team_season_overview_record import TeamSeasonOverviewRecord

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonOverviewRecord from a JSON string
team_season_overview_record_instance = TeamSeasonOverviewRecord.from_json(json)
# print the JSON string representation of the object
print TeamSeasonOverviewRecord.to_json()

# convert the object into a dict
team_season_overview_record_dict = team_season_overview_record_instance.to_dict()
# create an instance of TeamSeasonOverviewRecord from a dict
team_season_overview_record_from_dict = TeamSeasonOverviewRecord.from_dict(team_season_overview_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


