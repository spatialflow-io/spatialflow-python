# spatialflow_generated.PublicLocationIngestApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_public_locations_api_get_ingest_stats**](PublicLocationIngestApi.md#apps_public_locations_api_get_ingest_stats) | **GET** /api/v1/v1/locations/stats | Get Ingest Stats
[**apps_public_locations_api_ingest_location**](PublicLocationIngestApi.md#apps_public_locations_api_ingest_location) | **POST** /api/v1/v1/locations | Ingest Location
[**apps_public_locations_api_ingest_location_batch**](PublicLocationIngestApi.md#apps_public_locations_api_ingest_location_batch) | **POST** /api/v1/v1/locations/batch | Ingest Location Batch


# **apps_public_locations_api_get_ingest_stats**
> Dict[str, object] apps_public_locations_api_get_ingest_stats()

Get Ingest Stats

Get location ingestion statistics for the authenticated organization.  Authentication: API Key (Bearer token)  Returns:     - total_ingested_today: Total locations ingested today     - total_ingested_week: Total locations ingested this week     - devices_active: Number of active devices     - last_ingest: Timestamp of last location ingestion  Example:     ```bash     curl -X GET https://api.spatialflow.io/api/v1/locations/stats \\       -H \"Authorization: Bearer sf_live_abc123...\"     ```

### Example

* Api Key Authentication (APIKeyBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicLocationIngestApi(api_client)

    try:
        # Get Ingest Stats
        api_response = await api_instance.apps_public_locations_api_get_ingest_stats()
        print("The response of PublicLocationIngestApi->apps_public_locations_api_get_ingest_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLocationIngestApi->apps_public_locations_api_get_ingest_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_locations_api_ingest_location**
> LocationIngestResponse apps_public_locations_api_ingest_location(location_point_in)

Ingest Location

Ingest a single location point.  This endpoint accepts location updates from external systems and queues them for asynchronous processing with GPS jitter reduction filters.  Authentication: API Key (Bearer token) Rate Limit: 1000 requests/minute per API key  PRD Reference: §3.4 Public Ingest API  Returns:     202 Accepted: Location queued for processing     400 Bad Request: Invalid location data     401 Unauthorized: Missing or invalid API key     429 Too Many Requests: Rate limit exceeded  Example:     ```bash     curl -X POST https://api.spatialflow.io/api/v1/locations \\       -H \"Authorization: Bearer sf_live_abc123...\" \\       -H \"Content-Type: application/json\" \\       -d '{         \"device_id\": \"truck-005\",         \"lat\": 40.7589,         \"lon\": -73.9851,         \"ts\": \"2025-10-01T14:30:00Z\",         \"accuracy\": 8.5       }'     ```

### Example

* Api Key Authentication (APIKeyBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.location_ingest_response import LocationIngestResponse
from spatialflow_generated.models.location_point_in import LocationPointIn
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicLocationIngestApi(api_client)
    location_point_in = spatialflow_generated.LocationPointIn() # LocationPointIn | 

    try:
        # Ingest Location
        api_response = await api_instance.apps_public_locations_api_ingest_location(location_point_in)
        print("The response of PublicLocationIngestApi->apps_public_locations_api_ingest_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLocationIngestApi->apps_public_locations_api_ingest_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_point_in** | [**LocationPointIn**](LocationPointIn.md)|  | 

### Return type

[**LocationIngestResponse**](LocationIngestResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_locations_api_ingest_location_batch**
> LocationIngestResponse apps_public_locations_api_ingest_location_batch(location_batch_in)

Ingest Location Batch

Ingest a batch of location points.  Accepts up to 5000 locations per batch (PRD §3.4). Each location is validated and processed asynchronously as a single batch task.  **Idempotency:** If `idempotency_key` is provided, duplicate requests with the same key within 24 hours will return the original response without reprocessing.  Authentication: API Key (Bearer token) Rate Limit: 100 batches/minute per API key  PRD Reference: §3.4 Public Ingest API  Returns:     202 Accepted: Locations queued (includes counts of accepted/rejected)     400 Bad Request: Invalid batch data     401 Unauthorized: Missing or invalid API key     429 Too Many Requests: Rate limit exceeded  Example:     ```bash     curl -X POST https://api.spatialflow.io/api/v1/locations/batch \\       -H \"Authorization: Bearer sf_live_abc123...\" \\       -H \"Content-Type: application/json\" \\       -d '{         \"locations\": [           {\"device_id\": \"truck-005\", \"lat\": 40.7589, \"lon\": -73.9851, \"ts\": \"2025-10-01T14:30:00Z\"},           {\"device_id\": \"truck-005\", \"lat\": 40.7590, \"lon\": -73.9850, \"ts\": \"2025-10-01T14:31:00Z\"}         ],         \"idempotency_key\": \"batch-20251001-001\"       }'     ```

### Example

* Api Key Authentication (APIKeyBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.location_batch_in import LocationBatchIn
from spatialflow_generated.models.location_ingest_response import LocationIngestResponse
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicLocationIngestApi(api_client)
    location_batch_in = spatialflow_generated.LocationBatchIn() # LocationBatchIn | 

    try:
        # Ingest Location Batch
        api_response = await api_instance.apps_public_locations_api_ingest_location_batch(location_batch_in)
        print("The response of PublicLocationIngestApi->apps_public_locations_api_ingest_location_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicLocationIngestApi->apps_public_locations_api_ingest_location_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_batch_in** | [**LocationBatchIn**](LocationBatchIn.md)|  | 

### Return type

[**LocationIngestResponse**](LocationIngestResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

