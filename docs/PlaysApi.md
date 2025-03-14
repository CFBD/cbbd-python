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



Retrieve list of play types

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



Returns all plays for a given game

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
    game_id = 56 # int | Game id filter
    shooting_plays_only = True # bool | Optional filter to only return shooting plays (optional)

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
 **game_id** | **int**| Game id filter | 
 **shooting_plays_only** | **bool**| Optional filter to only return shooting plays | [optional] 

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
> List[PlayInfo] get_plays_by_date(var_date, shooting_plays_only=shooting_plays_only)



Retrieve all plays for a given UTC date

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
    var_date = '2013-10-20T19:20:30+01:00' # datetime | Required date filter in ISO 8601 format (YYYY-MM-DD)
    shooting_plays_only = True # bool | Optional filter to only return shooting plays (optional)

    try:
        api_response = api_instance.get_plays_by_date(var_date, shooting_plays_only=shooting_plays_only)
        print("The response of PlaysApi->get_plays_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlaysApi->get_plays_by_date: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**| Required date filter in ISO 8601 format (YYYY-MM-DD) | 
 **shooting_plays_only** | **bool**| Optional filter to only return shooting plays | [optional] 

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



Retrieve all plays for a given player and season

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
    player_id = 56 # int | Required player id filter
    season = 56 # int | Required season filter
    shooting_plays_only = True # bool | Optional filter to only return shooting plays (optional)

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
 **player_id** | **int**| Required player id filter | 
 **season** | **int**| Required season filter | 
 **shooting_plays_only** | **bool**| Optional filter to only return shooting plays | [optional] 

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



Retrieve all plays for a given team and season

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
    season = 56 # int | Required season filter
    team = 'team_example' # str | Required team filter
    shooting_plays_only = True # bool | Optional filter to only return shooting plays (optional)

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
 **season** | **int**| Required season filter | 
 **team** | **str**| Required team filter | 
 **shooting_plays_only** | **bool**| Optional filter to only return shooting plays | [optional] 

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



Retrieve all plays for a given tournament and season

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
    tournament = 'tournament_example' # str | Required tournament filter (e.g. NCAA, NIT, etc)
    season = 3.4 # float | Required season filter
    shooting_plays_only = True # bool | Optional filter to only return shooting plays (optional)

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
 **tournament** | **str**| Required tournament filter (e.g. NCAA, NIT, etc) | 
 **season** | **float**| Required season filter | 
 **shooting_plays_only** | **bool**| Optional filter to only return shooting plays | [optional] 

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



Returns all player substitutions for a given game

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
    game_id = 56 # int | Game id filter

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
 **game_id** | **int**| Game id filter | 

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



Retrieve all player substitutions for a given player and season

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
    player_id = 56 # int | Required player id filter
    season = 56 # int | Required season filter

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
 **player_id** | **int**| Required player id filter | 
 **season** | **int**| Required season filter | 

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



Retrieve all player substitutions for a given team and season

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
    season = 56 # int | Required season filter
    team = 'team_example' # str | Required team filter

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
 **season** | **int**| Required season filter | 
 **team** | **str**| Required team filter | 

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

