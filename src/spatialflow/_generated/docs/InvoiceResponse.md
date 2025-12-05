# InvoiceResponse

Invoice details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**number** | **str** |  | 
**status** | **str** |  | 
**amount_due** | **int** |  | 
**amount_paid** | **int** |  | 
**currency** | **str** |  | 
**period_start** | **int** |  | 
**period_end** | **int** |  | 
**created_at** | **int** |  | 
**invoice_pdf** | **str** |  | [optional] 
**line_items** | [**List[InvoiceLineItem]**](InvoiceLineItem.md) |  | 

## Example

```python
from spatialflow_generated.models.invoice_response import InvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceResponse from a JSON string
invoice_response_instance = InvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceResponse.to_json())

# convert the object into a dict
invoice_response_dict = invoice_response_instance.to_dict()
# create an instance of InvoiceResponse from a dict
invoice_response_from_dict = InvoiceResponse.from_dict(invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


