# Correlation

Correlation is the model for correlations definitions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**CorrelationConfig**](CorrelationConfig.md) |  | [optional] 
**description** | **str** | Description of the correlation | [optional] 
**label** | **str** | Label identifying the correlation | [optional] 
**org_id** | **int** | OrgID of the data source the correlation originates from | [optional] 
**provisioned** | **bool** | Provisioned True if the correlation was created during provisioning | [optional] 
**source_uid** | **str** | UID of the data source the correlation originates from | [optional] 
**target_uid** | **str** | UID of the data source the correlation points to | [optional] 
**uid** | **str** | Unique identifier of the correlation | [optional] 

## Example

```python
from grafanaApiClient.models.correlation import Correlation

# TODO update the JSON string below
json = "{}"
# create an instance of Correlation from a JSON string
correlation_instance = Correlation.from_json(json)
# print the JSON string representation of the object
print Correlation.to_json()

# convert the object into a dict
correlation_dict = correlation_instance.to_dict()
# create an instance of Correlation from a dict
correlation_form_dict = correlation.from_dict(correlation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


