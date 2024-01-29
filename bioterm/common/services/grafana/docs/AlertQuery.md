# AlertQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasource_uid** | **str** | Grafana data source unique identifier; it should be &#39;__expr__&#39; for a Server Side Expression operation. | [optional] 
**model** | **object** | JSON is the raw JSON query and includes the above properties as well as custom properties. | [optional] 
**query_type** | **str** | QueryType is an optional identifier for the type of query. It can be used to distinguish different types of queries. | [optional] 
**ref_id** | **str** | RefID is the unique identifier of the query, set by the frontend call. | [optional] 
**relative_time_range** | [**RelativeTimeRange**](RelativeTimeRange.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_query import AlertQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AlertQuery from a JSON string
alert_query_instance = AlertQuery.from_json(json)
# print the JSON string representation of the object
print AlertQuery.to_json()

# convert the object into a dict
alert_query_dict = alert_query_instance.to_dict()
# create an instance of AlertQuery from a dict
alert_query_form_dict = alert_query.from_dict(alert_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


