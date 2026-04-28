# cluster.json (aio)

[[Back]](../BareMetalCluster.md) [[base]](./input_data_cluster_base.md)

**mandatory** file

## Example

```json
{
    "name": "bm1",
    "openshift_version": "4.18.9",
    "cpu_architecture": "x86_64",
    "base_dns_domain": "ocp.lan",
    "cluster_network_cidr": "10.128.0.0/14",
    "cluster_network_host_prefix": 23,
    "service_network_cidr": "172.30.0.0/16",
    "machine_network_gateway": "10.5.5.15/28",
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com",
    "network_type": "OVNKubernetes",
    "ssh_public_key": "ssh-ed25519 AAAA...",
    "ntp": "30.30.30.30",
    "dns_ip": "40.40.40.40",
    "dns_search": "domain.com",
    "iso": "full",
    "server": [
        {
            "hostname": "bm1",
            "kube": true,
            "redfish": {
                "endpoint_type": "ucsc",
                "endpoint_ip": "10.4.4.1",
                "endpoint_port": "443",
                "username": "user",
                "password": "pass"
            },
            "vlan": 666,
            "ssh": {
                "ip": "10.5.5.5",
                "username": "core"
            },
            "interface": [
                {
                    "name": "eno5",
                    "mac": "aa:aa:aa:aa:aa:aa"
                }
            ],
            "nmstate": "single.yaml"
        }
    ],
    "web_server": {
        "ip": "10.6.6.6",
        "username": "user",
        "password": null,
        "ssh_public_key": "ssh-ed25519 AAAA...",
        "image_base_url": "http://10.6.6.6:8080",
        "image_upload_directory": "./image"
    }
}
```

[[Back]](../BareMetalCluster.md) [[base]](./input_data_cluster_base.md)