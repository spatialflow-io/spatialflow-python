# ConfigurationItem

Single configuration item with resolved value and metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**category** | **str** |  | 
**value_type** | **str** |  | 
**value** | [**AnyOf**](AnyOf.md) |  | [optional] 
**source** | **str** |  | 
**requires_restart** | **bool** |  | 
**is_sensitive** | **bool** |  | 
**is_readonly** | **bool** |  | 
**is_write_only** | **bool** |  | 
**allow_empty** | **bool** |  | [optional] [default to False]
**validation_rules** | **Dict[str, object]** |  | 
**updated_at** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.configuration_item import ConfigurationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationItem from a JSON string
configuration_item_instance = ConfigurationItem.from_json(json)
# print the JSON string representation of the object
print(ConfigurationItem.to_json())

# convert the object into a dict
configuration_item_dict = configuration_item_instance.to_dict()
# create an instance of ConfigurationItem from a dict
configuration_item_from_dict = ConfigurationItem.from_dict(configuration_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


