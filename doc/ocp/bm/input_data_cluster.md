# Cluster.json

cluster.json is the only mandatory file. It may contain all details for fabric, cluster and tasks. It may be also augmented with extra files.

## Base

This is the smallest possible cluster.json file provided that other mandatory details are in different files i.e.
- [server.json](./input_data_server.md)
- [web.json](./input_data_web.md)
- [ssh.pub](./input_data_ssh_pub.md)
- [proxy.json](./input_data_proxy.md)

```
    "name": "bm1",
    "openshift_version": "4.18.9",
    "cpu_architecture": "x86_64",
    "base_dns_domain": "ocp.lan",
    "cluster_network_cidr": "10.128.0.0/14",
    "cluster_network_host_prefix": 23,
    "service_network_cidr": "172.30.0.0/16",
    "olm_operators": [{"name":"cnv"}, {"name":"lvm"}],
    "ntp": "ntp.domain.com",
    "iso": "full",
```

Notes:
- name will be used internally in iserver tool
- name will appear on the list of OpenShift clusters at console.redhat.com
- openshift version is checked against openshift software repository, proper version has to be defined
- in case of no proxy requiremts, skip proxy parameters
- in case of no olm operators requiremts, skip
- iso: minimum or full
- assisted installer supports single ssh key for remote access, you can define extra ssh keys in tasks

## Complete

This is an example of single node openshift (sno) cluster definition that does not require any other files or directories in the context of installation only workflow

```
{
    "name": "bm1",
    "openshift_version": "4.18.9",
    "cpu_architecture": "x86_64",
    "base_dns_domain": "ocp.lan",
    "cluster_network_cidr": "10.128.0.0/14",
    "cluster_network_host_prefix": 23,
    "service_network_cidr": "172.30.0.0/16",
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com",
    "olm_operators": [{"name":"cnv"}, {"name":"lvm"}],
    "network_type": "OVNKubernetes",
    "ssh_public_key": "ssh-ed25519 AAAA...",
    "ntp": "30.30.30.30",
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
            "nmstate": "single.yaml",
            "variables": {
                "IFNAME": "eno5",
                "VLAN": "666",
                "IP": "10.5.5.5",
                "PREFIX": "28",
                "GW": "10.5.5.15",
                "DNS_SEARCH": "domain.com",
                "DNS_IP": "20.20.20.20"
            }
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

[Back](../BareMetalCluster.md)