# TestReceiversConfigAlertParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | A LabelSet is a collection of LabelName and LabelValue pairs.  The LabelSet may be fully-qualified down to the point where it may resolve to a single Metric in the data store or not.  All operations that occur within the realm of a LabelSet can emit a vector of Metric entities to which the LabelSet may match. | [optional] 
**labels** | **Dict[str, str]** | A LabelSet is a collection of LabelName and LabelValue pairs.  The LabelSet may be fully-qualified down to the point where it may resolve to a single Metric in the data store or not.  All operations that occur within the realm of a LabelSet can emit a vector of Metric entities to which the LabelSet may match. | [optional] 

## Example

```python
from grafanaApiClient.models.test_receivers_config_alert_params import TestReceiversConfigAlertParams

# TODO update the JSON string below
json = "{}"
# create an instance of TestReceiversConfigAlertParams from a JSON string
test_receivers_config_alert_params_instance = TestReceiversConfigAlertParams.from_json(json)
# print the JSON string representation of the object
print TestReceiversConfigAlertParams.to_json()

# convert the object into a dict
test_receivers_config_alert_params_dict = test_receivers_config_alert_params_instance.to_dict()
# create an instance of TestReceiversConfigAlertParams from a dict
test_receivers_config_alert_params_form_dict = test_receivers_config_alert_params.from_dict(test_receivers_config_alert_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


