# cbbd.LineupsApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lineup_stats_by_game**](LineupsApi.md#get_lineup_stats_by_game) | **GET** /lineups/game/{gameId} | 
[**get_substitutions_by_game**](LineupsApi.md#get_substitutions_by_game) | **GET** /lineups/team | 


# **get_lineup_stats_by_game**
> List[LineupStats] get_lineup_stats_by_game(game_id)



Queries lineup statistics for a specific game

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.lineup_stats import LineupStats
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
    api_instance = cbbd.LineupsApi(api_client)
    game_id = 56 # int | Required game id filter

    try:
        api_response = api_instance.get_lineup_stats_by_game(game_id)
        print("The response of LineupsApi->get_lineup_stats_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LineupsApi->get_lineup_stats_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| Required game id filter | 

### Return type

[**List[LineupStats]**](LineupStats.md)

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

# **get_substitutions_by_game**
> List[LineupStats] get_substitutions_by_game(season, team, start_date_range=start_date_range, end_date_range=end_date_range)



Queries lineup statistics for a given team and season

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.lineup_stats import LineupStats
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
    api_instance = cbbd.LineupsApi(api_client)
    season = 56 # int | Required season filter
    team = 'team_example' # str | Required team filter
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional start date range filter (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional end date range filter (optional)

    try:
        api_response = api_instance.get_substitutions_by_game(season, team, start_date_range=start_date_range, end_date_range=end_date_range)
        print("The response of LineupsApi->get_substitutions_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LineupsApi->get_substitutions_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Required season filter | 
 **team** | **str**| Required team filter | 
 **start_date_range** | **datetime**| Optional start date range filter | [optional] 
 **end_date_range** | **datetime**| Optional end date range filter | [optional] 

### Return type

[**List[LineupStats]**](LineupStats.md)

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

