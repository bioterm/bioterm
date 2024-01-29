# BacktestConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**condition** | **str** |  | [optional] 
**data** | [**List[AlertQuery]**](AlertQuery.md) |  | [optional] 
**var_for** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**var_from** | **datetime** |  | [optional] 
**interval** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**no_data_state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**to** | **datetime** |  | [optional] 

## Example

```python
from grafanaApiClient.models.backtest_config import BacktestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BacktestConfig from a JSON string
backtest_config_instance = BacktestConfig.from_json(json)
# print the JSON string representation of the object
print BacktestConfig.to_json()

# convert the object into a dict
backtest_config_dict = backtest_config_instance.to_dict()
# create an instance of BacktestConfig from a dict
backtest_config_form_dict = backtest_config.from_dict(backtest_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


