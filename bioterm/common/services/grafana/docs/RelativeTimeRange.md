# RelativeTimeRange

RelativeTimeRange is the per query start and end time for requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**to** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 

## Example

```python
from grafanaApiClient.models.relative_time_range import RelativeTimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeTimeRange from a JSON string
relative_time_range_instance = RelativeTimeRange.from_json(json)
# print the JSON string representation of the object
print RelativeTimeRange.to_json()

# convert the object into a dict
relative_time_range_dict = relative_time_range_instance.to_dict()
# create an instance of RelativeTimeRange from a dict
relative_time_range_form_dict = relative_time_range.from_dict(relative_time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


