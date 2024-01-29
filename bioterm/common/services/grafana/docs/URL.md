# URL

The general form represented is:  [scheme:][//[userinfo@]host][/]path[?query][#fragment]  URLs that do not start with a slash after the scheme are interpreted as:  scheme:opaque[?query][#fragment]  Note that the Path field is stored in decoded form: /%47%6f%2f becomes /Go/. A consequence is that it is impossible to tell which slashes in the Path were slashes in the raw URL and which were %2f. This distinction is rarely important, but when it is, the code should use the EscapedPath method, which preserves the original encoding of Path.  The RawPath field is an optional field which is only set when the default encoding of Path is different from the escaped path. See the EscapedPath method for more details.  URL's String method uses the EscapedPath method to obtain the path.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_query** | **bool** |  | [optional] 
**fragment** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**omit_host** | **bool** |  | [optional] 
**opaque** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**raw_fragment** | **str** |  | [optional] 
**raw_path** | **str** |  | [optional] 
**raw_query** | **str** |  | [optional] 
**scheme** | **str** |  | [optional] 
**user** | **object** | The Userinfo type is an immutable encapsulation of username and password details for a URL. An existing Userinfo value is guaranteed to have a username set (potentially empty, as allowed by RFC 2396), and optionally a password. | [optional] 

## Example

```python
from grafanaApiClient.models.url import URL

# TODO update the JSON string below
json = "{}"
# create an instance of URL from a JSON string
url_instance = URL.from_json(json)
# print the JSON string representation of the object
print URL.to_json()

# convert the object into a dict
url_dict = url_instance.to_dict()
# create an instance of URL from a dict
url_form_dict = url.from_dict(url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


