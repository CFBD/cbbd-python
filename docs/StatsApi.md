# cbbd.StatsApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_season_shooting_stats**](StatsApi.md#get_player_season_shooting_stats) | **GET** /stats/player/shooting/season | 
[**get_player_season_stats**](StatsApi.md#get_player_season_stats) | **GET** /stats/player/season | 
[**get_team_leaderboard_stats**](StatsApi.md#get_team_leaderboard_stats) | **GET** /stats/team/leaderboard | 
[**get_team_season_shooting_stats**](StatsApi.md#get_team_season_shooting_stats) | **GET** /stats/team/shooting/season | 
[**get_team_season_stats**](StatsApi.md#get_team_season_stats) | **GET** /stats/team/season | 


# **get_player_season_shooting_stats**
> List[PlayerSeasonShootingStats] get_player_season_shooting_stats(season, season_type=season_type, team=team, conference=conference, start_date_range=start_date_range, end_date_range=end_date_range)



Returns player shooting statistics for a season. Provide a team or conference.

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
    season = 56 # int | The season to return.
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    team = 'team_example' # str | Filters results to the specified team name. Required when conference is not provided. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. Required when team is not provided. (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)

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
 **season** | **int**| The season to return. | 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **team** | **str**| Filters results to the specified team name. Required when conference is not provided. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. Required when team is not provided. | [optional] 
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 

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



Returns player statistics for a season.

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
    season = 3.4 # float | The season to return.
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)

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
 **season** | **float**| The season to return. | 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 

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

# **get_team_leaderboard_stats**
> List[TeamStatsLeaderboardRecord] get_team_leaderboard_stats(season=season, team=team, conference=conference)



Returns team leaderboard statistics. This endpoint requires Patreon Tier 2 access or higher.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.team_stats_leaderboard_record import TeamStatsLeaderboardRecord
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
    season = 3.4 # float | Filters results to the specified season. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)

    try:
        api_response = api_instance.get_team_leaderboard_stats(season=season, team=team, conference=conference)
        print("The response of StatsApi->get_team_leaderboard_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->get_team_leaderboard_stats: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **float**| Filters results to the specified season. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 

### Return type

[**List[TeamStatsLeaderboardRecord]**](TeamStatsLeaderboardRecord.md)

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



Returns team shooting statistics for a season. Provide a team or conference.

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
    season = 56 # int | The season to return.
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    team = 'team_example' # str | Filters results to the specified team name. Required when conference is not provided. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. Required when team is not provided. (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)

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
 **season** | **int**| The season to return. | 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **team** | **str**| Filters results to the specified team name. Required when conference is not provided. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. Required when team is not provided. | [optional] 
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 

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



Returns team season statistics. Provide at least a season or team.

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
    season = 3.4 # float | Filters results to the specified season. Required when team is not provided. (optional)
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    team = 'team_example' # str | Filters results to the specified team name. Required when season is not provided. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)

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
 **season** | **float**| Filters results to the specified season. Required when team is not provided. | [optional] 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **team** | **str**| Filters results to the specified team name. Required when season is not provided. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 

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

