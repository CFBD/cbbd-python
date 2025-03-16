# cbbd.StatsApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_season_shooting_stats**](StatsApi.md#get_player_season_shooting_stats) | **GET** /stats/player/shooting/season | 
[**get_player_season_stats**](StatsApi.md#get_player_season_stats) | **GET** /stats/player/season | 
[**get_team_season_shooting_stats**](StatsApi.md#get_team_season_shooting_stats) | **GET** /stats/team/shooting/season | 
[**get_team_season_stats**](StatsApi.md#get_team_season_stats) | **GET** /stats/team/season | 


# **get_player_season_shooting_stats**
> List[PlayerSeasonShootingStats] get_player_season_shooting_stats(season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)



Retrieves player season shooting statistics

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.player_season_shooting_stats import PlayerSeasonShootingStats
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
    api_instance = cbbd.StatsApi(api_client)
    season = 56 # int | Required season filter
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    team = 'team_example' # str | Team filter, required if conference is not provided (optional)
    conference = 'conference_example' # str | Conference abbreviation filter, required if team is not provided (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional start date range filter (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional end date range filter (optional)

    try:
        api_response = api_instance.get_player_season_shooting_stats(season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)
        print("The response of StatsApi->get_player_season_shooting_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_player_season_shooting_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Required season filter | 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **team** | **str**| Team filter, required if conference is not provided | [optional] 
 **conference** | **str**| Conference abbreviation filter, required if team is not provided | [optional] 
 **start_date_range** | **datetime**| Optional start date range filter | [optional] 
 **end_date_range** | **datetime**| Optional end date range filter | [optional] 

### Return type

[**List[PlayerSeasonShootingStats]**](PlayerSeasonShootingStats.md)

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

# **get_player_season_stats**
> List[PlayerSeasonStats] get_player_season_stats(season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)



Returns player statistics by season

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.player_season_stats import PlayerSeasonStats
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
    api_instance = cbbd.StatsApi(api_client)
    season = 3.4 # float | Required season filter
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    team = 'team_example' # str | Optional team name filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_player_season_stats(season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)
        print("The response of StatsApi->get_player_season_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_player_season_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **float**| Required season filter | 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **team** | **str**| Optional team name filter | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **start_date_range** | **datetime**|  | [optional] 
 **end_date_range** | **datetime**|  | [optional] 

### Return type

[**List[PlayerSeasonStats]**](PlayerSeasonStats.md)

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

# **get_team_season_shooting_stats**
> List[SeasonShootingStats] get_team_season_shooting_stats(season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)



Retrieves team season shooting statistics

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.season_shooting_stats import SeasonShootingStats
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
    api_instance = cbbd.StatsApi(api_client)
    season = 56 # int | Required season filter
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    team = 'team_example' # str | Team filter, required if conference is not provided (optional)
    conference = 'conference_example' # str | Conference abbreviation filter, required if team is not provided (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional start date range filter (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional end date range filter (optional)

    try:
        api_response = api_instance.get_team_season_shooting_stats(season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)
        print("The response of StatsApi->get_team_season_shooting_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_team_season_shooting_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Required season filter | 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **team** | **str**| Team filter, required if conference is not provided | [optional] 
 **conference** | **str**| Conference abbreviation filter, required if team is not provided | [optional] 
 **start_date_range** | **datetime**| Optional start date range filter | [optional] 
 **end_date_range** | **datetime**| Optional end date range filter | [optional] 

### Return type

[**List[SeasonShootingStats]**](SeasonShootingStats.md)

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

# **get_team_season_stats**
> List[TeamSeasonStats] get_team_season_stats(season=season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)



Returns team season statistics by year or team

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.season_type import SeasonType
from cbbd.models.team_season_stats import TeamSeasonStats
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
    api_instance = cbbd.StatsApi(api_client)
    season = 3.4 # float | Optional season filter, required if team is not provided (optional)
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    team = 'team_example' # str | Optional team name filter, required if season is not provided (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_team_season_stats(season=season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)
        print("The response of StatsApi->get_team_season_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_team_season_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **float**| Optional season filter, required if team is not provided | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **team** | **str**| Optional team name filter, required if season is not provided | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **start_date_range** | **datetime**|  | [optional] 
 **end_date_range** | **datetime**|  | [optional] 

### Return type

[**List[TeamSeasonStats]**](TeamSeasonStats.md)

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

