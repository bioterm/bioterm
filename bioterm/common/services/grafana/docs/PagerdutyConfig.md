# PagerdutyConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** |  | [optional] 
**client** | **str** |  | [optional] 
**client_url** | **str** |  | [optional] 
**component** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**details** | **Dict[str, str]** |  | [optional] 
**group** | **str** |  | [optional] 
**http_config** | [**HTTPClientConfig**](HTTPClientConfig.md) |  | [optional] 
**images** | [**List[PagerdutyImage]**](PagerdutyImage.md) |  | [optional] 
**links** | [**List[PagerdutyLink]**](PagerdutyLink.md) |  | [optional] 
**routing_key** | **str** |  | [optional] 
**routing_key_file** | **str** |  | [optional] 
**send_resolved** | **bool** |  | [optional] 
**service_key** | **str** |  | [optional] 
**service_key_file** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**url** | [**URL**](URL.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.pagerduty_config import PagerdutyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PagerdutyConfig from a JSON string
pagerduty_config_instance = PagerdutyConfig.from_json(json)
# print the JSON string representation of the object
print PagerdutyConfig.to_json()

# convert the object into a dict
pagerduty_config_dict = pagerduty_config_instance.to_dict()
# create an instance of PagerdutyConfig from a dict
pagerduty_config_form_dict = pagerduty_config.from_dict(pagerduty_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


