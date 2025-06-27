# HTTP Proxy

Redfish Console prepares ISO that may be configured with HTTP Proxy settings. HTTP Proxy definition in iserver can be in cluster.json or proxy.json file.

Note: http proxy authentication is not supported

## cluster.json

```
{
    "name": "bm1",
    "openshift_version": "4.17.2",
    "cpu_architecture": "x86_64",
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com",
    ...
}
```

## proxy.json

```
{
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com",

}
```

[Back](../BareMetalCluster.md)
