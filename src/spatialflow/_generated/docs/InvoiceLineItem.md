# InvoiceLineItem

Invoice line item details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**quantity** | **int** |  | 
**unit_amount** | **int** |  | 
**amount** | **int** |  | 

## Example

```python
from spatialflow_generated.models.invoice_line_item import InvoiceLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineItem from a JSON string
invoice_line_item_instance = InvoiceLineItem.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineItem.to_json())

# convert the object into a dict
invoice_line_item_dict = invoice_line_item_instance.to_dict()
# create an instance of InvoiceLineItem from a dict
invoice_line_item_from_dict = InvoiceLineItem.from_dict(invoice_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


