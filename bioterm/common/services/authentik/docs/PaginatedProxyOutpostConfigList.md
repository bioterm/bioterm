# PaginatedProxyOutpostConfigList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedApplicationListPagination**](PaginatedApplicationListPagination.md) |  | 
**results** | [**List[ProxyOutpostConfig]**](ProxyOutpostConfig.md) |  | 

## Example

```python
from authentikApiClient.models.paginated_proxy_outpost_config_list import PaginatedProxyOutpostConfigList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProxyOutpostConfigList from a JSON string
paginated_proxy_outpost_config_list_instance = PaginatedProxyOutpostConfigList.from_json(json)
# print the JSON string representation of the object
print PaginatedProxyOutpostConfigList.to_json()

# convert the object into a dict
paginated_proxy_outpost_config_list_dict = paginated_proxy_outpost_config_list_instance.to_dict()
# create an instance of PaginatedProxyOutpostConfigList from a dict
paginated_proxy_outpost_config_list_form_dict = paginated_proxy_outpost_config_list.from_dict(paginated_proxy_outpost_config_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


