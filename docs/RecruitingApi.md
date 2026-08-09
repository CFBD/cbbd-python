# cbbd.RecruitingApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portal_transfers**](RecruitingApi.md#get_portal_transfers) | **GET** /recruiting/portal | 
[**get_recruits**](RecruitingApi.md#get_recruits) | **GET** /recruiting/players | 
[**get_team_recruiting_rankings**](RecruitingApi.md#get_team_recruiting_rankings) | **GET** /recruiting/teams | 


# **get_portal_transfers**
> List[Transfer] get_portal_transfers(year=year, source_team=source_team, destination_team=destination_team, source_conference=source_conference, destination_conference=destination_conference, position=position)



Returns historical transfer portal activity.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.transfer import Transfer
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
    api_instance = cbbd.RecruitingApi(api_client)
    year = 3.4 # float | Filters results to the specified transfer season. (optional)
    source_team = 'source_team_example' # str | Filters results to the specified source team. (optional)
    destination_team = 'destination_team_example' # str | Filters results to the specified destination team. (optional)
    source_conference = 'source_conference_example' # str | Filters results to the specified source conference abbreviation. (optional)
    destination_conference = 'destination_conference_example' # str | Filters results to the specified destination conference abbreviation. (optional)
    position = 'position_example' # str | Filters results to the specified player position. (optional)

    try:
        api_response = api_instance.get_portal_transfers(year=year, source_team=source_team, destination_team=destination_team, source_conference=source_conference, destination_conference=destination_conference, position=position)
        print("The response of RecruitingApi->get_portal_transfers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecruitingApi->get_portal_transfers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**| Filters results to the specified transfer season. | [optional] 
 **source_team** | **str**| Filters results to the specified source team. | [optional] 
 **destination_team** | **str**| Filters results to the specified destination team. | [optional] 
 **source_conference** | **str**| Filters results to the specified source conference abbreviation. | [optional] 
 **destination_conference** | **str**| Filters results to the specified destination conference abbreviation. | [optional] 
 **position** | **str**| Filters results to the specified player position. | [optional] 

### Return type

[**List[Transfer]**](Transfer.md)

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

# **get_recruits**
> List[Recruit] get_recruits(year=year, team=team, conference=conference, position=position)



Returns historical composite player recruiting rankings and ratings.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.recruit import Recruit
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
    api_instance = cbbd.RecruitingApi(api_client)
    year = 56 # int | Filters results to the specified recruiting year. (optional)
    team = 'team_example' # str | Filters results to the specified college team. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)
    position = 'position_example' # str | Filters results to the specified player position. (optional)

    try:
        api_response = api_instance.get_recruits(year=year, team=team, conference=conference, position=position)
        print("The response of RecruitingApi->get_recruits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecruitingApi->get_recruits: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Filters results to the specified recruiting year. | [optional] 
 **team** | **str**| Filters results to the specified college team. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 
 **position** | **str**| Filters results to the specified player position. | [optional] 

### Return type

[**List[Recruit]**](Recruit.md)

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

# **get_team_recruiting_rankings**
> List[TeamRecruitingRanking] get_team_recruiting_rankings(year=year, team=team, conference=conference)



Returns historical composite team recruiting rankings.

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.team_recruiting_ranking import TeamRecruitingRanking
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
    api_instance = cbbd.RecruitingApi(api_client)
    year = 56 # int | Filters results to the specified recruiting year. (optional)
    team = 'team_example' # str | Filters results to the specified team name. (optional)
    conference = 'conference_example' # str | Filters results to the specified conference abbreviation. (optional)

    try:
        api_response = api_instance.get_team_recruiting_rankings(year=year, team=team, conference=conference)
        print("The response of RecruitingApi->get_team_recruiting_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecruitingApi->get_team_recruiting_rankings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Filters results to the specified recruiting year. | [optional] 
 **team** | **str**| Filters results to the specified team name. | [optional] 
 **conference** | **str**| Filters results to the specified conference abbreviation. | [optional] 

### Return type

[**List[TeamRecruitingRanking]**](TeamRecruitingRanking.md)

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

