# cbbd.GamesApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_broadcasts**](GamesApi.md#get_broadcasts) | **GET** /games/media | 
[**get_game_players**](GamesApi.md#get_game_players) | **GET** /games/players | 
[**get_game_teams**](GamesApi.md#get_game_teams) | **GET** /games/teams | 
[**get_games**](GamesApi.md#get_games) | **GET** /games | 


# **get_broadcasts**
> List[GameMediaInfo] get_broadcasts(start_date_range=start_date_range, end_date_range=end_date_range, team=team, conference=conference, season=season, season_type=season_type, tournament=tournament)



Returns broadcast information on the first 3000 games that match the provided filters, ordered by start date.

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
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional start timestamp in ISO 8601 format (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional end timestamp in ISO 8601 format (optional)
    team = 'team_example' # str | Optional team name filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    season = 3.4 # float | Optional season filter (optional)
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    tournament = 'tournament_example' # str | Optional tournament filter (e.g. NCAA, NIT, etc) (optional)

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
 **start_date_range** | **datetime**| Optional start timestamp in ISO 8601 format | [optional] 
 **end_date_range** | **datetime**| Optional end timestamp in ISO 8601 format | [optional] 
 **team** | **str**| Optional team name filter | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **season** | **float**| Optional season filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **tournament** | **str**| Optional tournament filter (e.g. NCAA, NIT, etc) | [optional] 

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



Returns player box score statistics and metrics on the first 1000 games that match the provided filters, ordered by start date.

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
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional start timestamp in ISO 8601 format (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional end timestamp in ISO 8601 format (optional)
    team = 'team_example' # str | Optional team name filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    season = 3.4 # float | Optional season filter (optional)
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    tournament = 'tournament_example' # str | Optional tournament filter (e.g. NCAA, NIT, etc) (optional)

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
 **start_date_range** | **datetime**| Optional start timestamp in ISO 8601 format | [optional] 
 **end_date_range** | **datetime**| Optional end timestamp in ISO 8601 format | [optional] 
 **team** | **str**| Optional team name filter | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **season** | **float**| Optional season filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **tournament** | **str**| Optional tournament filter (e.g. NCAA, NIT, etc) | [optional] 

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



Returns team box score statistics and metrics on the first 3000 games that match the provided filters, ordered by start date.

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
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional start timestamp in ISO 8601 format (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional end timestamp in ISO 8601 format (optional)
    team = 'team_example' # str | Optional team name filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    season = 3.4 # float | Optional season filter (optional)
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    tournament = 'tournament_example' # str | Optional tournament filter (e.g. NCAA, NIT, etc) (optional)

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
 **start_date_range** | **datetime**| Optional start timestamp in ISO 8601 format | [optional] 
 **end_date_range** | **datetime**| Optional end timestamp in ISO 8601 format | [optional] 
 **team** | **str**| Optional team name filter | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **season** | **float**| Optional season filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **tournament** | **str**| Optional tournament filter (e.g. NCAA, NIT, etc) | [optional] 

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



Returns information on the first 3000 games that match the provided filters, ordered by start date.

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
    start_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional start timestamp in ISO 8601 format (optional)
    end_date_range = '2013-10-20T19:20:30+01:00' # datetime | Optional end timestamp in ISO 8601 format (optional)
    team = 'team_example' # str | Optional team name filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    season = 56 # int | Optional season filter (optional)
    season_type = cbbd.SeasonType() # SeasonType | Optional season type filter (optional)
    status = cbbd.GameStatus() # GameStatus | Optional game status filter (optional)
    tournament = 'tournament_example' # str | Optional tournament filter (e.g. NCAA, NIT, etc) (optional)

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
 **start_date_range** | **datetime**| Optional start timestamp in ISO 8601 format | [optional] 
 **end_date_range** | **datetime**| Optional end timestamp in ISO 8601 format | [optional] 
 **team** | **str**| Optional team name filter | [optional] 
 **conference** | **str**| Optional conference abbreviation filter | [optional] 
 **season** | **int**| Optional season filter | [optional] 
 **season_type** | [**SeasonType**](.md)| Optional season type filter | [optional] 
 **status** | [**GameStatus**](.md)| Optional game status filter | [optional] 
 **tournament** | **str**| Optional tournament filter (e.g. NCAA, NIT, etc) | [optional] 

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

