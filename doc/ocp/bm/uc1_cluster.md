# OpenShift Cluster on UCSX with NVIDIA GPU

## IP addressing

Bare metal management subnet (IMC): 10.5.5.0/24 gw .254
Machine network (Cluster Node): 10.6.6.0/24 gw. 254
- server connect to machine network with single interface
- vlan 666
API IP: 10.6.6.10
Ingress IP: 10.6.6.11
DNS server: 10.7.7.7
Web server: 10.8.8.8
NFS server: 10.9.9.9

Node | BMC Network | Machine Network
--- | --- | ---
cp1 | 10.5.5.1 | 10.6.6.1
cp2 | 10.5.5.2 | 10.6.6.2
cp3 | 10.5.5.3 | 10.6.6.3
wk1 | 10.5.5.4 | 10.6.6.4
wk2 | 10.5.5.5 | 10.6.6.5
wk3 | 10.5.5.6 | 10.6.6.6

## cluster.json

Custom file used by OpenShift bare metal installation workflow that defines the cluster settings

```
{
    "name": "my-cluster",
    "openshift_version": "4.17.30",
    "cpu_architecture": "x86_64",
    "base_dns_domain": "ai-pod.domain.com",
    "cluster_network_cidr": "10.128.0.0/14",
    "cluster_network_host_prefix": 23,
    "service_network_cidr": "172.30.0.0/16",
    "olm_operators": [
        {
            "name": "lvm"
        }
    ],
    "network_type": "OVNKubernetes",
    "ssh_public_key": "ssh-ed25519 ...",
    "ntp": "ntp.domain.com",
    "api": "10.6.6.10",
    "ingress": "10.6.6.11",
    "server": [
        {
            "hostname": "cp1",
            "role": "master",
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
                }
            ],
            "nmstate": "single.yaml",
            "variables": {
                "INTF": "eno5",
                "VLAN": "666",
                "IP": "10.6.6.1",
                "PREFIX": "24",
                "GW": "10.6.6.254",
                "DNS_SEARCH": "ai-pod.domain.com",
                "DNS_IP": "10.7.7.7"
            }
        },
        {
            "hostname": "cp2",
            "role": "master",
            "kube": false,
            "redfish": {
                "endpoint_ip": "10.5.5.2",
                "username": "user",
                "password": "pass"
            },
            "ssh": {
                "ip": "10.6.6.2"
            },
            "interface": [
                {
                    "name": "eno5",
                    "mac": "22:22:22:22:22:22"
                }
            ],
            "nmstate": "single.yaml",
            "variables": {
                "INTF": "eno5",
                "VLAN": "666",
                "IP": "10.6.6.2",
                "PREFIX": "24",
                "GW": "10.6.6.254",
                "DNS_SEARCH": "ai-pod.domain.com",
                "DNS_IP": "10.7.7.7"
            }
        },
        {
            "hostname": "cp3",
            "role": "master",
            "kube": false,
            "redfish": {
                "endpoint_ip": "10.5.5.3",
                "username": "user",
                "password": "pass"
            },
            "ssh": {
                "ip": "10.6.6.3"
            },
            "interface": [
                {
                    "name": "eno5",
                    "mac": "33:33:33:33:33:33"
                }
            ],
            "nmstate": "single.yaml",
            "variables": {
                "INTF": "eno5",
                "VLAN": "666",
                "IP": "10.6.6.3",
                "PREFIX": "24",
                "GW": "10.6.6.254",
                "DNS_SEARCH": "ai-pod.domain.com",
                "DNS_IP": "10.7.7.7"
            }
        },
        {
            "hostname": "wk1",
            "role": "worker",
            "kube": false,
            "redfish": {
                "endpoint_ip": "10.5.5.4",
                "username": "user",
                "password": "pass"
            },
            "ssh": {
                "ip": "10.6.6.4"
            },
            "interface": [
                {
                    "name": "eno5",
                    "mac": "44:44:44:44:44:44"
                }
            ],
            "nmstate": "single.yaml",
            "variables": {
                "INTF": "eno5",
                "VLAN": "666",
                "IP": "10.6.6.4",
                "PREFIX": "24",
                "GW": "10.6.6.254",
                "DNS_SEARCH": "ai-pod.domain.com",
                "DNS_IP": "10.7.7.7"
            }
        },
        {
            "hostname": "wk2",
            "role": "worker",
            "kube": false,
            "redfish": {
                "endpoint_ip": "10.5.5.5",
                "username": "user",
                "password": "pass"
            },
            "ssh": {
                "ip": "10.6.6.5"
            },
            "interface": [
                {
                    "name": "eno5",
                    "mac": "55:55:55:55:55:55"
                }
            ],
            "nmstate": "single.yaml",
            "variables": {
                "INTF": "eno5",
                "VLAN": "666",
                "IP": "10.6.6.5",
                "PREFIX": "24",
                "GW": "10.6.6.254",
                "DNS_SEARCH": "ai-pod.domain.com",
                "DNS_IP": "10.7.7.7"
            }
        },
        {
            "hostname": "wk3",
            "role": "worker",
            "kube": false,
            "redfish": {
                "endpoint_ip": "10.5.5.6",
                "username": "user",
                "password": "pass"
            },
            "ssh": {
                "ip": "10.6.6.6"
            },
            "interface": [
                {
                    "name": "eno5",
                    "mac": "66:66:66:66:66:66"
                }
            ],
            "nmstate": "single.yaml",
            "variables": {
                "INTF": "eno5",
                "VLAN": "666",
                "IP": "10.6.6.6",
                "PREFIX": "24",
                "GW": "10.6.6.254",
                "DNS_SEARCH": "ai-pod.domain.com",
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
                "helm": true
            },
            "identity": {
                "provider": "htpasswd",
                "filename": "htpasswd",
                "admin": [
                    "__ALL__"
                ]
            },
            "nfd": {},
            "gpu": {
                "monitoring": {}
            },
            "server": {
                "power-management": {},
                "node-annotation": true
            },
            "storage": {
                "nfs": {
                    "server": "10.9.9.9",
                    "share": "/export/nfs-share",
                    "dir": "${pvc.metadata.namespace}-${pvc.metadata.name}",
                    "default": true
                }
            }
        }
    ]
}
```

[Back](./uc1.md)