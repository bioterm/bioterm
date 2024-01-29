# AlertingFileExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **int** |  | [optional] 
**contact_points** | [**List[ContactPointExport]**](ContactPointExport.md) |  | [optional] 
**groups** | [**List[AlertRuleGroupExport]**](AlertRuleGroupExport.md) |  | [optional] 
**policies** | [**List[NotificationPolicyExport]**](NotificationPolicyExport.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.alerting_file_export import AlertingFileExport

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingFileExport from a JSON string
alerting_file_export_instance = AlertingFileExport.from_json(json)
# print the JSON string representation of the object
print AlertingFileExport.to_json()

# convert the object into a dict
alerting_file_export_dict = alerting_file_export_instance.to_dict()
# create an instance of AlertingFileExport from a dict
alerting_file_export_form_dict = alerting_file_export.from_dict(alerting_file_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


