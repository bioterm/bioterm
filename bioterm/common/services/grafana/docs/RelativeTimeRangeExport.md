# RelativeTimeRangeExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** |  | [optional] 
**to** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.relative_time_range_export import RelativeTimeRangeExport

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeTimeRangeExport from a JSON string
relative_time_range_export_instance = RelativeTimeRangeExport.from_json(json)
# print the JSON string representation of the object
print RelativeTimeRangeExport.to_json()

# convert the object into a dict
relative_time_range_export_dict = relative_time_range_export_instance.to_dict()
# create an instance of RelativeTimeRangeExport from a dict
relative_time_range_export_form_dict = relative_time_range_export.from_dict(relative_time_range_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


