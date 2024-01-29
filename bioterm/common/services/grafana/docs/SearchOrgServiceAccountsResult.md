# SearchOrgServiceAccountsResult

swagger: model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**service_accounts** | [**List[ServiceAccountDTO]**](ServiceAccountDTO.md) |  | [optional] 
**total_count** | **int** | It can be used for pagination of the user list E.g. if totalCount is equal to 100 users and the perpage parameter is set to 10 then there are 10 pages of users. | [optional] 

## Example

```python
from grafanaApiClient.models.search_org_service_accounts_result import SearchOrgServiceAccountsResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOrgServiceAccountsResult from a JSON string
search_org_service_accounts_result_instance = SearchOrgServiceAccountsResult.from_json(json)
# print the JSON string representation of the object
print SearchOrgServiceAccountsResult.to_json()

# convert the object into a dict
search_org_service_accounts_result_dict = search_org_service_accounts_result_instance.to_dict()
# create an instance of SearchOrgServiceAccountsResult from a dict
search_org_service_accounts_result_form_dict = search_org_service_accounts_result.from_dict(search_org_service_accounts_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


