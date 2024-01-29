# MetricRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug** | **bool** |  | [optional] 
**var_from** | **str** | From Start time in epoch timestamps in milliseconds or relative using Grafana time units. | 
**queries** | **List[object]** | queries.refId – Specifies an identifier of the query. Is optional and default to “A”. queries.datasourceId – Specifies the data source to be queried. Each query in the request must have an unique datasourceId. queries.maxDataPoints - Species maximum amount of data points that dashboard panel can render. Is optional and default to 100. queries.intervalMs - Specifies the time interval in milliseconds of time series. Is optional and defaults to 1000. | 
**to** | **str** | To End time in epoch timestamps in milliseconds or relative using Grafana time units. | 

## Example

```python
from grafanaApiClient.models.metric_request import MetricRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetricRequest from a JSON string
metric_request_instance = MetricRequest.from_json(json)
# print the JSON string representation of the object
print MetricRequest.to_json()

# convert the object into a dict
metric_request_dict = metric_request_instance.to_dict()
# create an instance of MetricRequest from a dict
metric_request_form_dict = metric_request.from_dict(metric_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


