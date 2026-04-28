# RunIt - RedHat Console API Body Generation

[[Back]](../BareMetalCluster.md) [[Next]](./example_create_cluster.md) [[Prev]](./example_variables_check.md)

```
Cluster Data
------------
{
    "name": "bm1",
    "openshift_version": "4.21.4",
    "base_dns_domain": "ocp.domain.com",
    ...

Infra Data
----------
{
    "cpu_architecture": "x86_64",
    "openshift_version": "4.21.4",
    "proxy": {
        "http_proxy": "http://proxy.domain.com:80",
        "https_proxy": "http://proxy.domain.com:80",
        "no_proxy": "domain.com"
    },

All checks passed
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_create_cluster.md) [[Prev]](./example_variables_check.md)