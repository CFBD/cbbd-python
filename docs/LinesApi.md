# cbbd.LinesApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lines**](LinesApi.md#get_lines) | **GET** /lines | 
[**get_providers**](LinesApi.md#get_providers) | **GET** /lines/providers | 


# **get_lines**
> List[GameLines] get_lines(season=season, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)



Returns betting lines for up to 3,000 games that match the filters, ordered by start date.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.game_lines import GameLines
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
    api_instance = cbbd.LinesApi(api_client)
    season = 56 # int | Filters results to the specified season. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)

    try:
        api_response = api_instance.get_lines(season=season, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)
        print("The response of LinesApi->get_lines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinesApi->get_lines: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Filters results to the specified season. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 

### Return type

[**List[GameLines]**](GameLines.md)

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

# **get_providers**
> List[LineProviderInfo] get_providers()



Returns available betting line providers.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.line_provider_info import LineProviderInfo
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
    api_instance = cbbd.LinesApi(api_client)

    try:
        api_response = api_instance.get_providers()
        print("The response of LinesApi->get_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinesApi->get_providers: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[LineProviderInfo]**](LineProviderInfo.md)

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

