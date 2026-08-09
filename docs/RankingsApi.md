# cbbd.RankingsApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rankings**](RankingsApi.md#get_rankings) | **GET** /rankings | 


# **get_rankings**
> List[PollTeamInfo] get_rankings(season=season, season_type=season_type, week=week, poll_type=poll_type, team=team, conference=conference)



Returns historical poll rankings.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.poll_team_info import PollTeamInfo
from cbbd.models.season_type import SeasonType
from cbbd.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collegebasketballdata.com
# See configuration.py for a list of all supported configuration parameters.
configuration = cbbd.Configuration(
    host = "https://api.collegebasketballdata.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiKey
configuration = cbbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with cbbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cbbd.RankingsApi(api_client)
    season = 56 # int | Filters results to the specified season. (optional)
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    week = 56 # int | Filters results to the specified week. (optional)
    poll_type = 'poll_type_example' # str | Filters results to the AP or Coaches Poll. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)

    try:
        api_response = api_instance.get_rankings(season=season, season_type=season_type, week=week, poll_type=poll_type, team=team, conference=conference)
        print("The response of RankingsApi->get_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RankingsApi->get_rankings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Filters results to the specified season. | [optional] 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **week** | **int**| Filters results to the specified week. | [optional] 
 **poll_type** | **str**| Filters results to the AP or Coaches Poll. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 

### Return type

[**List[PollTeamInfo]**](PollTeamInfo.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

