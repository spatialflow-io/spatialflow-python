# spatialflow_generated.TilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_tiles_api_get_raster_tile**](TilesApi.md#apps_tiles_api_get_raster_tile) | **GET** /api/v1/tiles/{z}/{x}/{y}.png | Get Raster Tile
[**apps_tiles_api_get_tile**](TilesApi.md#apps_tiles_api_get_tile) | **GET** /api/v1/tiles/{z}/{x}/{y}.mvt | Get Tile
[**apps_tiles_api_get_tile_metadata**](TilesApi.md#apps_tiles_api_get_tile_metadata) | **GET** /api/v1/tiles/metadata | Get Tile Metadata
[**apps_tiles_api_get_tile_style**](TilesApi.md#apps_tiles_api_get_tile_style) | **GET** /api/v1/tiles/style/{style_id} | Get Tile Style
[**apps_tiles_api_health_check**](TilesApi.md#apps_tiles_api_health_check) | **GET** /api/v1/tiles/health | Health Check
[**apps_tiles_api_invalidate_tiles**](TilesApi.md#apps_tiles_api_invalidate_tiles) | **POST** /api/v1/tiles/invalidate | Invalidate Tiles


# **apps_tiles_api_get_raster_tile**
> apps_tiles_api_get_raster_tile(z, x, y)

Get Raster Tile

Placeholder for raster tile support.
Currently returns 404 as we only support vector tiles.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.TilesApi(api_client)
    z = 56 # int | 
    x = 56 # int | 
    y = 56 # int | 

    try:
        # Get Raster Tile
        await api_instance.apps_tiles_api_get_raster_tile(z, x, y)
    except Exception as e:
        print("Exception when calling TilesApi->apps_tiles_api_get_raster_tile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **z** | **int**|  | 
 **x** | **int**|  | 
 **y** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_tiles_api_get_tile**
> bytearray apps_tiles_api_get_tile(z, x, y)

Get Tile

Generate MVT tile for geofences.

Args:
    z: Zoom level (0-16)
    x: Tile X coordinate
    y: Tile Y coordinate

Returns:
    MVT tile binary data or 204 No Content for empty tiles

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.TilesApi(api_client)
    z = 56 # int | 
    x = 56 # int | 
    y = 56 # int | 

    try:
        # Get Tile
        api_response = await api_instance.apps_tiles_api_get_tile(z, x, y)
        print("The response of TilesApi->apps_tiles_api_get_tile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TilesApi->apps_tiles_api_get_tile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **z** | **int**|  | 
 **x** | **int**|  | 
 **y** | **int**|  | 

### Return type

**bytearray**

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_tiles_api_get_tile_metadata**
> TileMetadata apps_tiles_api_get_tile_metadata()

Get Tile Metadata

Get metadata about available tiles.

Returns information about zoom levels, bounds, and layer details.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.tile_metadata import TileMetadata
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.TilesApi(api_client)

    try:
        # Get Tile Metadata
        api_response = await api_instance.apps_tiles_api_get_tile_metadata()
        print("The response of TilesApi->apps_tiles_api_get_tile_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TilesApi->apps_tiles_api_get_tile_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TileMetadata**](TileMetadata.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_tiles_api_get_tile_style**
> apps_tiles_api_get_tile_style(style_id)

Get Tile Style

Get a custom tile style configuration.

Future endpoint for custom map styles.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.TilesApi(api_client)
    style_id = 'style_id_example' # str | 

    try:
        # Get Tile Style
        await api_instance.apps_tiles_api_get_tile_style(style_id)
    except Exception as e:
        print("Exception when calling TilesApi->apps_tiles_api_get_tile_style: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **style_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**501** | Not Implemented |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_tiles_api_health_check**
> apps_tiles_api_health_check()

Health Check

Health check endpoint for tiles service.

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.TilesApi(api_client)

    try:
        # Health Check
        await api_instance.apps_tiles_api_health_check()
    except Exception as e:
        print("Exception when calling TilesApi->apps_tiles_api_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_tiles_api_invalidate_tiles**
> Dict[str, object] apps_tiles_api_invalidate_tiles()

Invalidate Tiles

Invalidate all cached tiles for the current workspace.

This should be called when geofences are modified.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.TilesApi(api_client)

    try:
        # Invalidate Tiles
        api_response = await api_instance.apps_tiles_api_invalidate_tiles()
        print("The response of TilesApi->apps_tiles_api_invalidate_tiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TilesApi->apps_tiles_api_invalidate_tiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

