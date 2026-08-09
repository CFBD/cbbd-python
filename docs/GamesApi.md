# cbbd.GamesApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_broadcasts**](GamesApi.md#get_broadcasts) | **GET** /games/media | 
[**get_game_players**](GamesApi.md#get_game_players) | **GET** /games/players | 
[**get_game_teams**](GamesApi.md#get_game_teams) | **GET** /games/teams | 
[**get_games**](GamesApi.md#get_games) | **GET** /games | 
[**get_scoreboard**](GamesApi.md#get_scoreboard) | **GET** /scoreboard | 


# **get_broadcasts**
> List[GameMediaInfo] get_broadcasts(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, tournament=tournament)



Returns broadcast records for up to 3,000 games that match the filters, ordered by start date.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.game_media_info import GameMediaInfo
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
    api_instance = cbbd.GamesApi(api_client)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)
    season = 3.4 # float | Filters results to the specified season. (optional)
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    tournament = 'tournament_example' # str | Filters results to the specified tournament, such as NCAA or NIT. (optional)

    try:
        api_response = api_instance.get_broadcasts(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, tournament=tournament)
        print("The response of GamesApi->get_broadcasts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_broadcasts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 
 **season** | **float**| Filters results to the specified season. | [optional] 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **tournament** | **str**| Filters results to the specified tournament, such as NCAA or NIT. | [optional] 

### Return type

[**List[GameMediaInfo]**](GameMediaInfo.md)

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

# **get_game_players**
> List[GameBoxScorePlayers] get_game_players(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, tournament=tournament)



Returns player box scores and advanced metrics for up to 1,000 games that match the filters, ordered by start date.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.game_box_score_players import GameBoxScorePlayers
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
    api_instance = cbbd.GamesApi(api_client)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)
    season = 3.4 # float | Filters results to the specified season. (optional)
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    tournament = 'tournament_example' # str | Filters results to the specified tournament, such as NCAA or NIT. (optional)

    try:
        api_response = api_instance.get_game_players(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, tournament=tournament)
        print("The response of GamesApi->get_game_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_game_players: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 
 **season** | **float**| Filters results to the specified season. | [optional] 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **tournament** | **str**| Filters results to the specified tournament, such as NCAA or NIT. | [optional] 

### Return type

[**List[GameBoxScorePlayers]**](GameBoxScorePlayers.md)

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

# **get_game_teams**
> List[GameBoxScoreTeam] get_game_teams(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, tournament=tournament)



Returns team box scores and advanced metrics for up to 3,000 games that match the filters, ordered by start date.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.game_box_score_team import GameBoxScoreTeam
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
    api_instance = cbbd.GamesApi(api_client)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)
    season = 3.4 # float | Filters results to the specified season. (optional)
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    tournament = 'tournament_example' # str | Filters results to the specified tournament, such as NCAA or NIT. (optional)

    try:
        api_response = api_instance.get_game_teams(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, tournament=tournament)
        print("The response of GamesApi->get_game_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_game_teams: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 
 **season** | **float**| Filters results to the specified season. | [optional] 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **tournament** | **str**| Filters results to the specified tournament, such as NCAA or NIT. | [optional] 

### Return type

[**List[GameBoxScoreTeam]**](GameBoxScoreTeam.md)

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

# **get_games**
> List[GameInfo] get_games(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, status=status, tournament=tournament)



Returns up to 3,000 games that match the filters, ordered by start date.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.game_info import GameInfo
from cbbd.models.game_status import GameStatus
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
    api_instance = cbbd.GamesApi(api_client)
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or after this ISO 8601 timestamp. (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Includes games starting at or before this ISO 8601 timestamp. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)
    season = 56 # int | Filters results to the specified season. (optional)
    season_type = cbbd.SeasonType() # SeasonType | Filters results to the specified season type. (optional)
    status = cbbd.GameStatus() # GameStatus | Filters results to the specified game status. (optional)
    tournament = 'tournament_example' # str | Filters results to the specified tournament, such as NCAA or NIT. (optional)

    try:
        api_response = api_instance.get_games(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, status=status, tournament=tournament)
        print("The response of GamesApi->get_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_games: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date_range** | **datetime**| Includes games starting at or after this ISO 8601 timestamp. | [optional] 
 **end_date_range** | **datetime**| Includes games starting at or before this ISO 8601 timestamp. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 
 **season** | **int**| Filters results to the specified season. | [optional] 
 **season_type** | [**SeasonType**](.md)| Filters results to the specified season type. | [optional] 
 **status** | [**GameStatus**](.md)| Filters results to the specified game status. | [optional] 
 **tournament** | **str**| Filters results to the specified tournament, such as NCAA or NIT. | [optional] 

### Return type

[**List[GameInfo]**](GameInfo.md)

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

# **get_scoreboard**
> List[ScoreboardGame] get_scoreboard(conference=conference)



Returns live scoreboard data. This endpoint requires Patreon Tier 1 access or higher.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.scoreboard_game import ScoreboardGame
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
    api_instance = cbbd.GamesApi(api_client)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)

    try:
        api_response = api_instance.get_scoreboard(conference=conference)
        print("The response of GamesApi->get_scoreboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GamesApi->get_scoreboard: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 

### Return type

[**List[ScoreboardGame]**](ScoreboardGame.md)

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

