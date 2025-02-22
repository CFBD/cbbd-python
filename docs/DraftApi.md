# cbbd.DraftApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_draft_picks**](DraftApi.md#get_draft_picks) | **GET** /draft/picks | 
[**get_draft_positions**](DraftApi.md#get_draft_positions) | **GET** /draft/positions | 
[**get_draft_teams**](DraftApi.md#get_draft_teams) | **GET** /draft/teams | 


# **get_draft_picks**
> List[DraftPick] get_draft_picks(year=year, draft_team=draft_team, source_team=source_team, position=position)



Retrieves historical NBA draft picks

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.draft_pick import DraftPick
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
    api_instance = cbbd.DraftApi(api_client)
    year = 56 # int | Optional draft year filter (optional)
    draft_team = 'draft_team_example' # str | Optional NBA team filter (optional)
    source_team = 'source_team_example' # str | Optional source team (e.g. NCAA) filter (optional)
    position = 'position_example' # str | Optional player position abbreviation filter (optional)

    try:
        api_response = api_instance.get_draft_picks(year=year, draft_team=draft_team, source_team=source_team, position=position)
        print("The response of DraftApi->get_draft_picks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_picks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Optional draft year filter | [optional] 
 **draft_team** | **str**| Optional NBA team filter | [optional] 
 **source_team** | **str**| Optional source team (e.g. NCAA) filter | [optional] 
 **position** | **str**| Optional player position abbreviation filter | [optional] 

### Return type

[**List[DraftPick]**](DraftPick.md)

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

# **get_draft_positions**
> List[DraftPosition] get_draft_positions()



Retrieves list of position names for NBA draft prospects

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.draft_position import DraftPosition
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
    api_instance = cbbd.DraftApi(api_client)

    try:
        api_response = api_instance.get_draft_positions()
        print("The response of DraftApi->get_draft_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_positions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DraftPosition]**](DraftPosition.md)

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

# **get_draft_teams**
> List[DraftTeam] get_draft_teams()



Retrieves list of NBA teams

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.draft_team import DraftTeam
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
    api_instance = cbbd.DraftApi(api_client)

    try:
        api_response = api_instance.get_draft_teams()
        print("The response of DraftApi->get_draft_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DraftApi->get_draft_teams: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[DraftTeam]**](DraftTeam.md)

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

