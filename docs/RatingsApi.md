# cbbd.RatingsApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_srs**](RatingsApi.md#get_srs) | **GET** /ratings/srs | 


# **get_srs**
> List[SrsInfo] get_srs(season=season, team=team, conference=conference)



Retrieves SRS ratings for the provided season, team, or conference.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.srs_info import SrsInfo
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
    api_instance = cbbd.RatingsApi(api_client)
    season = 56 # int | Optional season filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)

    try:
        api_response = api_instance.get_srs(season=season, team=team, conference=conference)
        print("The response of RatingsApi->get_srs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingsApi->get_srs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Optional season filter | [optional] 
 **team** | **str**| Optional team filter | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 

### Return type

[**List[SrsInfo]**](SrsInfo.md)

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

