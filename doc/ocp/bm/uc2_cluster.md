# OpenShift Cluster with Cilium CNI

## IP addressing

- Bare metal management subnet (IMC): 10.5.5.0/24 gw .254
- Machine network (Cluster Node): 10.6.6.0/24 gw. 254
  - server connect to machine network with two interfaces
  - vlan 666
- API IP: 10.6.6.1 (the same as node machine network)
- Ingress IP: 10.6.6.1 (the same as node machine network)
- DNS server: 10.7.7.7
- Web server: 10.8.8.8

Node | BMC Network | Machine Network
--- | --- | ---
sno | 10.5.5.1 | 10.6.6.1

## cluster.json

Custom file used by OpenShift bare metal installation workflow that defined the cluster settings

```
{
    "name": "my-cluster",
    "openshift_version": "4.18.9",
    "cpu_architecture": "x86_64",
    "base_dns_domain": "pod.domain.com",
    "cluster_network_cidr": "10.128.0.0/14",
    "cluster_network_host_prefix": 23,
    "service_network_cidr": "172.30.0.0/16",
    "olm_operators": [
        {
            "name": "lvm"
        }
    ],
    "network_type": "Cilium",
    "ssh_public_key": "ssh-ed25519 ...",
    "ntp": "ntp.domain.com",
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com"
    "api": "10.6.6.10",
    "ingress": "10.6.6.11",
    "server": [
        {
            "hostname": "sno",
            "kube": true,
            "redfish": {
                "endpoint_ip": "10.5.5.1",
                "username": "user",
                "password": "pass"
            },
            "ssh": {
                "ip": "10.6.6.1"
            },
            "interface": [
                {
                    "name": "eno5",
                    "mac": "11:11:11:11:11:11"
                },
                {
                    "name": "eno6",
                    "mac": "22:22:22:22:22:22"
                }
            ],
            "nmstate": "bonding.yaml",
            "variables": {
                "BOND": "bond0",
                "BOND_MEMBER_1": "eno5",
                "BOND_MEMBER_2": "eno6",
                "VLAN": "666",
                "IP": "10.6.6.1",
                "PREFIX": "24",
                "GW": "10.6.6.254",
                "DNS_SEARCH": "pod.domain.com",
                "DNS_IP": "10.7.7.7"
            }
        }
    ],
    "web_server": {
        "ip": "10.8.8.8",
        "username": "user",
        "password": "pass",
        "image_base_url": "http://10.8.8.8/repo",
        "image_upload_directory": "/var/www/html/repo"
    },
    "tasks": [
        {
            "cli": {
                "bashrc": true,
                "helm": true,
                "cilium": true,
                "hubble": true,
                "virtctl": true
            }
        }
    ]
}
```

[Back](./uc2.md)