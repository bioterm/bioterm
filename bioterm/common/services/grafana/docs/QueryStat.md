# QueryStat

The embedded FieldConfig's display name must be set. It corresponds to the QueryResultMetaStat on the frontend (https://github.com/grafana/grafana/blob/master/packages/grafana-data/src/types/data.ts#L53).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **object** | Map values to a display color NOTE: this interface is under development in the frontend... so simple map for now | [optional] 
**custom** | **object** | Panel Specific Values | [optional] 
**decimals** | **int** |  | [optional] 
**description** | **str** | Description is human readable field metadata | [optional] 
**display_name** | **str** | DisplayName overrides Grafana default naming, should not be used from a data source | [optional] 
**display_name_from_ds** | **str** | DisplayNameFromDS overrides Grafana default naming strategy. | [optional] 
**filterable** | **bool** | Filterable indicates if the Field&#39;s data can be filtered by additional calls. | [optional] 
**interval** | **float** | Interval indicates the expected regular step between values in the series. When an interval exists, consumers can identify \&quot;missing\&quot; values when the expected value is not present. The grafana timeseries visualization will render disconnected values when missing values are found it the time field. The interval uses the same units as the values.  For time.Time, this is defined in milliseconds. | [optional] 
**links** | [**List[DataLink]**](DataLink.md) | The behavior when clicking on a result | [optional] 
**mappings** | **List[object]** |  | [optional] 
**max** | **float** | ConfFloat64 is a float64. It Marshals float64 values of NaN of Inf to null. | [optional] 
**min** | **float** | ConfFloat64 is a float64. It Marshals float64 values of NaN of Inf to null. | [optional] 
**no_value** | **str** | Alternative to empty string | [optional] 
**path** | **str** | Path is an explicit path to the field in the datasource. When the frame meta includes a path, this will default to &#x60;${frame.meta.path}/${field.name}  When defined, this value can be used as an identifier within the datasource scope, and may be used as an identifier to update values in a subsequent request | [optional] 
**thresholds** | [**ThresholdsConfig**](ThresholdsConfig.md) |  | [optional] 
**type** | [**FieldTypeConfig**](FieldTypeConfig.md) |  | [optional] 
**unit** | **str** | Numeric Options | [optional] 
**value** | **float** |  | [optional] 
**writeable** | **bool** | Writeable indicates that the datasource knows how to update this value | [optional] 

## Example

```python
from grafanaApiClient.models.query_stat import QueryStat

# TODO update the JSON string below
json = "{}"
# create an instance of QueryStat from a JSON string
query_stat_instance = QueryStat.from_json(json)
# print the JSON string representation of the object
print QueryStat.to_json()

# convert the object into a dict
query_stat_dict = query_stat_instance.to_dict()
# create an instance of QueryStat from a dict
query_stat_form_dict = query_stat.from_dict(query_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


