# IPReservationPutRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | &lt;p&gt;The three-part name of the object (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;). | 
**parentpool** | **str** | &lt;code&gt;/oracle/public/ippool&lt;/code&gt;&lt;p&gt;Pool of public IP addresses | 
**permanent** | **bool** | &lt;code&gt;true&lt;/code&gt; indicates that the IP reservation has a persistent public IP address. You can associate either a temporary or a persistent public IP address with an instance when you create the instance.&lt;p&gt;Temporary public IP addresses are assigned dynamically from a pool of public IP addresses. When you associate a temporary public IP address with an instance, if the instance is restarted or is deleted and created again later, its public IP address might change. | 
**tags** | **list[str]** | A comma-separated list of strings which helps you to identify IP reservations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


