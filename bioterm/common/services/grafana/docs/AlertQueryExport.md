# AlertQueryExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_uid** | **str** |  | [optional] 
**model** | **object** |  | [optional] 
**query_type** | **str** |  | [optional] 
**ref_id** | **str** |  | [optional] 
**relative_time_range** | [**RelativeTimeRangeExport**](RelativeTimeRangeExport.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_query_export import AlertQueryExport

# TODO update the JSON string below
json = "{}"
# create an instance of AlertQueryExport from a JSON string
alert_query_export_instance = AlertQueryExport.from_json(json)
# print the JSON string representation of the object
print AlertQueryExport.to_json()

# convert the object into a dict
alert_query_export_dict = alert_query_export_instance.to_dict()
# create an instance of AlertQueryExport from a dict
alert_query_export_form_dict = alert_query_export.from_dict(alert_query_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


