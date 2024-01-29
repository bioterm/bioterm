# Certificate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority_key_id** | **List[int]** |  | [optional] 
**basic_constraints_valid** | **bool** | BasicConstraintsValid indicates whether IsCA, MaxPathLen, and MaxPathLenZero are valid. | [optional] 
**crl_distribution_points** | **List[str]** | CRL Distribution Points | [optional] 
**dns_names** | **List[str]** | Subject Alternate Name values. (Note that these values may not be valid if invalid values were contained within a parsed certificate. For example, an element of DNSNames may not be a valid DNS domain name.) | [optional] 
**email_addresses** | **List[str]** |  | [optional] 
**excluded_dns_domains** | **List[str]** |  | [optional] 
**excluded_email_addresses** | **List[str]** |  | [optional] 
**excluded_ip_ranges** | [**List[IPNet]**](IPNet.md) |  | [optional] 
**excluded_uri_domains** | **List[str]** |  | [optional] 
**ext_key_usage** | **List[int]** |  | [optional] 
**extensions** | [**List[Extension]**](Extension.md) | Extensions contains raw X.509 extensions. When parsing certificates, this can be used to extract non-critical extensions that are not parsed by this package. When marshaling certificates, the Extensions field is ignored, see ExtraExtensions. | [optional] 
**extra_extensions** | [**List[Extension]**](Extension.md) | ExtraExtensions contains extensions to be copied, raw, into any marshaled certificates. Values override any extensions that would otherwise be produced based on the other fields. The ExtraExtensions field is not populated when parsing certificates, see Extensions. | [optional] 
**ip_addresses** | **List[str]** |  | [optional] 
**is_ca** | **bool** |  | [optional] 
**issuer** | [**Name**](Name.md) |  | [optional] 
**issuing_certificate_url** | **List[str]** |  | [optional] 
**key_usage** | **int** | KeyUsage represents the set of actions that are valid for a given key. It&#39;s a bitmap of the KeyUsage* constants. | [optional] 
**max_path_len** | **int** | MaxPathLen and MaxPathLenZero indicate the presence and value of the BasicConstraints&#39; \&quot;pathLenConstraint\&quot;.  When parsing a certificate, a positive non-zero MaxPathLen means that the field was specified, -1 means it was unset, and MaxPathLenZero being true mean that the field was explicitly set to zero. The case of MaxPathLen&#x3D;&#x3D;0 with MaxPathLenZero&#x3D;&#x3D;false should be treated equivalent to -1 (unset).  When generating a certificate, an unset pathLenConstraint can be requested with either MaxPathLen &#x3D;&#x3D; -1 or using the zero value for both MaxPathLen and MaxPathLenZero. | [optional] 
**max_path_len_zero** | **bool** | MaxPathLenZero indicates that BasicConstraintsValid&#x3D;&#x3D;true and MaxPathLen&#x3D;&#x3D;0 should be interpreted as an actual maximum path length of zero. Otherwise, that combination is interpreted as MaxPathLen not being set. | [optional] 
**not_before** | **datetime** |  | [optional] 
**ocsp_server** | **List[str]** | RFC 5280, 4.2.2.1 (Authority Information Access) | [optional] 
**permitted_dns_domains** | **List[str]** |  | [optional] 
**permitted_dns_domains_critical** | **bool** | Name constraints | [optional] 
**permitted_email_addresses** | **List[str]** |  | [optional] 
**permitted_ip_ranges** | [**List[IPNet]**](IPNet.md) |  | [optional] 
**permitted_uri_domains** | **List[str]** |  | [optional] 
**policy_identifiers** | **List[List[int]]** |  | [optional] 
**public_key** | **object** |  | [optional] 
**public_key_algorithm** | **int** |  | [optional] 
**raw** | **List[int]** |  | [optional] 
**raw_issuer** | **List[int]** |  | [optional] 
**raw_subject** | **List[int]** |  | [optional] 
**raw_subject_public_key_info** | **List[int]** |  | [optional] 
**raw_tbs_certificate** | **List[int]** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**signature** | **List[int]** |  | [optional] 
**signature_algorithm** | **int** |  | [optional] 
**subject** | [**Name**](Name.md) |  | [optional] 
**subject_key_id** | **List[int]** |  | [optional] 
**uris** | [**List[URL]**](URL.md) |  | [optional] 
**unhandled_critical_extensions** | **List[List[int]]** | UnhandledCriticalExtensions contains a list of extension IDs that were not (fully) processed when parsing. Verify will fail if this slice is non-empty, unless verification is delegated to an OS library which understands all the critical extensions.  Users can access these extensions using Extensions and can remove elements from this slice if they believe that they have been handled. | [optional] 
**unknown_ext_key_usage** | **List[List[int]]** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.certificate import Certificate

# TODO update the JSON string below
json = "{}"
# create an instance of Certificate from a JSON string
certificate_instance = Certificate.from_json(json)
# print the JSON string representation of the object
print Certificate.to_json()

# convert the object into a dict
certificate_dict = certificate_instance.to_dict()
# create an instance of Certificate from a dict
certificate_form_dict = certificate.from_dict(certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


