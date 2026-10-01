# Proxy settings

[[Back]](../README.md)

In case of http proxy, make sure bmc and os address range is in **noProxy**, otherwise the node may hang in registering or provisioning phase for quite a while and eventually fail.

```
2026-08-20 08:19:07.591 47 WARNING sushy.connector [None req-4a66ade3-d92f-4a37-a0ac-e079d799a7ba - - - - - -] Transient error during Redfish request to https:/10.10.10.10//redfish/v1/ (attempt 1/10): HTTPSConnectionPool(host='10.10.10.10', port=443): Max retries exceeded with url: /redfish/v1/ (Caused by ProxyError('Cannot connect to proxy.', TimeoutError('timed out'))): requests.exceptions.ProxyError: HTTPSConnectionPool(host='10.10.10.10', port=443): Max retries exceeded with url: /redfish/v1/ (Caused by ProxyError('Cannot connect to proxy.', TimeoutError('timed out')))
```

>[!CAUTION]
>Any chance in proxy/cluster settings will trigger redeployment of most of deployments/pods in `openshift-machine-api` namespace

[[Back]](../README.md)