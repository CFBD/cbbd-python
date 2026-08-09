# cbbd.PlaysApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_play_types**](PlaysApi.md#get_play_types) | **GET** /plays/types | 
[**get_plays**](PlaysApi.md#get_plays) | **GET** /plays/game/{gameId} | 
[**get_plays_by_date**](PlaysApi.md#get_plays_by_date) | **GET** /plays/date | 
[**get_plays_by_player_id**](PlaysApi.md#get_plays_by_player_id) | **GET** /plays/player/{playerId} | 
[**get_plays_by_team**](PlaysApi.md#get_plays_by_team) | **GET** /plays/team | 
[**get_plays_by_tournament**](PlaysApi.md#get_plays_by_tournament) | **GET** /plays/tournament | 
[**get_substitutions_by_game**](PlaysApi.md#get_substitutions_by_game) | **GET** /substitutions/game/{gameId} | 
[**get_substitutions_by_player_id**](PlaysApi.md#get_substitutions_by_player_id) | **GET** /substitutions/player/{playerId} | 
[**get_substitutions_by_team**](PlaysApi.md#get_substitutions_by_team) | **GET** /substitutions/team | 


# **get_play_types**
> List[PlayTypeInfo] get_play_types()



Returns available play types and their identifiers.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.play_type_info import PlayTypeInfo
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
    api_instance = cbbd.PlaysApi(api_client)

    try:
        api_response = api_instance.get_play_types()
        print("The response of PlaysApi->get_play_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_play_types: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[PlayTypeInfo]**](PlayTypeInfo.md)

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

# **get_plays**
> List[PlayInfo] get_plays(game_id, shooting_plays_only=shooting_plays_only)



Returns all recorded plays for a game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.play_info import PlayInfo
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
    api_instance = cbbd.PlaysApi(api_client)
    game_id = 56 # int | The game ID.
    shooting_plays_only = True # bool | When true, returns only shooting plays. (optional)

    try:
        api_response = api_instance.get_plays(game_id, shooting_plays_only=shooting_plays_only)
        print("The response of PlaysApi->get_plays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_plays: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| The game ID. | 
 **shooting_plays_only** | **bool**| When true, returns only shooting plays. | [optional] 

### Return type

[**List[PlayInfo]**](PlayInfo.md)

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

# **get_plays_by_date**
> List[PlayInfo] get_plays_by_date(var_date, shooting_plays_only=shooting_plays_only, utc_offset=utc_offset)



Returns all recorded plays for a UTC date.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.play_info import PlayInfo
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
    api_instance = cbbd.PlaysApi(api_client)
    var_date = '2013-10-20T19:20:30+01:00' # datetime | The date to return in ISO 8601 format (YYYY-MM-DD).
    shooting_plays_only = True # bool | When true, returns only shooting plays. (optional)
    utc_offset = 3.4 # float | Shifts the date range by this number of hours from UTC. (optional)

    try:
        api_response = api_instance.get_plays_by_date(var_date, shooting_plays_only=shooting_plays_only, utc_offset=utc_offset)
        print("The response of PlaysApi->get_plays_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_plays_by_date: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**| The date to return in ISO 8601 format (YYYY-MM-DD). | 
 **shooting_plays_only** | **bool**| When true, returns only shooting plays. | [optional] 
 **utc_offset** | **float**| Shifts the date range by this number of hours from UTC. | [optional] 

### Return type

[**List[PlayInfo]**](PlayInfo.md)

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

# **get_plays_by_player_id**
> List[PlayInfo] get_plays_by_player_id(player_id, season, shooting_plays_only=shooting_plays_only)



Returns all recorded plays for a player and season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.play_info import PlayInfo
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
    api_instance = cbbd.PlaysApi(api_client)
    player_id = 56 # int | The player ID.
    season = 56 # int | The season to return.
    shooting_plays_only = True # bool | When true, returns only shooting plays. (optional)

    try:
        api_response = api_instance.get_plays_by_player_id(player_id, season, shooting_plays_only=shooting_plays_only)
        print("The response of PlaysApi->get_plays_by_player_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_plays_by_player_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **int**| The player ID. | 
 **season** | **int**| The season to return. | 
 **shooting_plays_only** | **bool**| When true, returns only shooting plays. | [optional] 

### Return type

[**List[PlayInfo]**](PlayInfo.md)

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

# **get_plays_by_team**
> List[PlayInfo] get_plays_by_team(season, team, shooting_plays_only=shooting_plays_only)



Returns all recorded plays for a team and season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.play_info import PlayInfo
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
    api_instance = cbbd.PlaysApi(api_client)
    season = 56 # int | The season to return.
    team = 'team_example' # str | The team name to return.
    shooting_plays_only = True # bool | When true, returns only shooting plays. (optional)

    try:
        api_response = api_instance.get_plays_by_team(season, team, shooting_plays_only=shooting_plays_only)
        print("The response of PlaysApi->get_plays_by_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_plays_by_team: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| The season to return. | 
 **team** | **str**| The team name to return. | 
 **shooting_plays_only** | **bool**| When true, returns only shooting plays. | [optional] 

### Return type

[**List[PlayInfo]**](PlayInfo.md)

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

# **get_plays_by_tournament**
> List[PlayInfo] get_plays_by_tournament(tournament, season, shooting_plays_only=shooting_plays_only)



Returns all recorded plays for a tournament and season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.play_info import PlayInfo
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
    api_instance = cbbd.PlaysApi(api_client)
    tournament = 'tournament_example' # str | The tournament to return, such as NCAA or NIT.
    season = 3.4 # float | The season to return.
    shooting_plays_only = True # bool | When true, returns only shooting plays. (optional)

    try:
        api_response = api_instance.get_plays_by_tournament(tournament, season, shooting_plays_only=shooting_plays_only)
        print("The response of PlaysApi->get_plays_by_tournament:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_plays_by_tournament: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament** | **str**| The tournament to return, such as NCAA or NIT. | 
 **season** | **float**| The season to return. | 
 **shooting_plays_only** | **bool**| When true, returns only shooting plays. | [optional] 

### Return type

[**List[PlayInfo]**](PlayInfo.md)

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
> List[PlayerSubsititution] get_substitutions_by_game(game_id)



Returns all recorded player substitutions for a game.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.player_subsititution import PlayerSubsititution
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
    api_instance = cbbd.PlaysApi(api_client)
    game_id = 56 # int | The game ID.

    try:
        api_response = api_instance.get_substitutions_by_game(game_id)
        print("The response of PlaysApi->get_substitutions_by_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_substitutions_by_game: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| The game ID. | 

### Return type

[**List[PlayerSubsititution]**](PlayerSubsititution.md)

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

# **get_substitutions_by_player_id**
> List[PlayerSubsititution] get_substitutions_by_player_id(player_id, season)



Returns all recorded player substitutions for a player and season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.player_subsititution import PlayerSubsititution
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
    api_instance = cbbd.PlaysApi(api_client)
    player_id = 56 # int | The player ID.
    season = 56 # int | The season to return.

    try:
        api_response = api_instance.get_substitutions_by_player_id(player_id, season)
        print("The response of PlaysApi->get_substitutions_by_player_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_substitutions_by_player_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **int**| The player ID. | 
 **season** | **int**| The season to return. | 

### Return type

[**List[PlayerSubsititution]**](PlayerSubsititution.md)

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

# **get_substitutions_by_team**
> List[PlayerSubsititution] get_substitutions_by_team(season, team)



Returns all recorded player substitutions for a team and season.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.player_subsititution import PlayerSubsititution
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
    api_instance = cbbd.PlaysApi(api_client)
    season = 56 # int | The season to return.
    team = 'team_example' # str | The team name to return.

    try:
        api_response = api_instance.get_substitutions_by_team(season, team)
        print("The response of PlaysApi->get_substitutions_by_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_substitutions_by_team: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| The season to return. | 
 **team** | **str**| The team name to return. | 

### Return type

[**List[PlayerSubsititution]**](PlayerSubsititution.md)

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

