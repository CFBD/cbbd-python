# cbbd.VenuesApi

All URIs are relative to *https://api.collegebasketballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_venues**](VenuesApi.md#get_venues) | **GET** /venues | 


# **get_venues**
> List[VenueInfo] get_venues()



Retrieves list of available venues

### Example

* Bearer Authentication (apiKey):
```python
import time
import os
import cbbd
from cbbd.models.venue_info import VenueInfo
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
    api_instance = cbbd.VenuesApi(api_client)

    try:
        api_response = api_instance.get_venues()
        print("The response of VenuesApi->get_venues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VenuesApi->get_venues: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[VenueInfo]**](VenueInfo.md)

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

