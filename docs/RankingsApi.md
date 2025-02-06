# cbbd.RankingsApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rankings**](RankingsApi.md#get_rankings) | **GET** /rankings | 


# **get_rankings**
> List[PollTeamInfo] get_rankings(season=season, season_type=season_type, week=week, poll_type=poll_type, team=team, conference=conference)



Retrieves historical poll data

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
    season = 56 # int | Optional season filter (optional)
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    week = 56 # int | Optional week filter (optional)
    poll_type = 'poll_type_example' # str | Optional poll type filter (\"ap\" or \"coaches\") (optional)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference filter (optional)

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
 **season** | **int**| Optional season filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **week** | **int**| Optional week filter | [optional] 
 **poll_type** | **str**| Optional poll type filter (\&quot;ap\&quot; or \&quot;coaches\&quot;) | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **conference** | **str**| Optional conference filter | [optional] 

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

