# cbbd.TeamsApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_teams**](TeamsApi.md#get_teams) | **GET** /teams | 


# **get_teams**
> List[TeamInfo] get_teams(conference=conference, season=season)



Retrieves historical team information

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.team_info import TeamInfo
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
    api_instance = cbbd.TeamsApi(api_client)
    conference = 'conference_example' # str | Optional conference filter (optional)
    season = 56 # int | Optional season filter (optional)

    try:
        api_response = api_instance.get_teams(conference=conference, season=season)
        print("The response of TeamsApi->get_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conference** | **str**| Optional conference filter | [optional] 
 **season** | **int**| Optional season filter | [optional] 

### Return type

[**List[TeamInfo]**](TeamInfo.md)

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

