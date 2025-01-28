# cbbd.ConferencesApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conference_history**](ConferencesApi.md#get_conference_history) | **GET** /conferences/history | 
[**get_conferences**](ConferencesApi.md#get_conferences) | **GET** /conferences | 


# **get_conference_history**
> List[ConferenceHistory] get_conference_history(conference=conference)



Retrieves historical conference membership information

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.conference_history import ConferenceHistory
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
    api_instance = cbbd.ConferencesApi(api_client)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)

    try:
        api_response = api_instance.get_conference_history(conference=conference)
        print("The response of ConferencesApi->get_conference_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_conference_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conference** | **str**| Optional conference abbreviation filter | [optional] 

### Return type

[**List[ConferenceHistory]**](ConferenceHistory.md)

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

# **get_conferences**
> List[ConferenceInfo] get_conferences()



Retrieves list of available conferences

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.conference_info import ConferenceInfo
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
    api_instance = cbbd.ConferencesApi(api_client)

    try:
        api_response = api_instance.get_conferences()
        print("The response of ConferencesApi->get_conferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_conferences: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ConferenceInfo]**](ConferenceInfo.md)

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

