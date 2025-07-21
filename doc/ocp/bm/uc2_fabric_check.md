# OpenShift Cluster with Cilium CNI

## Fabric Check

Overview
- OpenShift cluster node connects to ACI fabric via two physical interfaces that are configured in bonding mode with VLAN encapsulation
- this intent is defined in [cluster](./uc2_cluster.md) input file
- extra fabric.json file or 'fabric' JSON structure in cluster.json is required
- while it follows own data model, it essentially adds connectivity information of physical interfaces to ACI nodes on top of information already present in server section of cluster

ACI Check Workflow
- validate node and interface input
- check interface state with expectations
  - operational up
  - switching enabled
  - configured with epg
  - trunk mode
  - vlan enabled
  - bonding enabled
- validate cluster node IP endpoint
  - expected to be either not found
  - or found on the same interface (reinstallation)
  - otherwise it is identified as IP collision scenario

Check the details in outputs below.

## Input Data Example

```
{
    "controller": [
        {
            "type": "aci",
            "apic": "my-apic",
            "domain": "main",
            "tenant": "k8s",
            "l3out": "MyL3out",
	          "vrf": "MyVrf"
        }
    ],
    "server": [
        {
            "hostname": "bm",
            "interface": [
                {
                    "domain": "main",
                    "ip": "10.6.6.1",
                    "gateway": "10.6.6.254/24",
                    "mac": "11:11:11:11:11:11",
                    "bond": true,
                    "trunk": true,
                    "vlan": 666,
                    "node": "100",
                    "port": "1/1/1"
                },
                {
                    "domain": "main",
                    "ip": "10.6.6.1",
                    "gateway": "10.6.6.254/24",
                    "mac": "22:22:22:22:22:22",
                    "bond": true,
                    "trunk": true,
                    "vlan": 666,
                    "node": "200",
                    "port": "1/1/1"
                }
            ]
        }
    ]
}
```

## Output Example

```
Apic [my-apic] domain [main] configuration
------------------------------------------

Validated and resolved fabric configuration intent
{
    "type": "aci",
    "apic": "my-apic",
    "domain": "main",
    "tenant": "k8s",
    "l3out": "MyL3out",
    "vrf": "MyVrf",
    "check_mode": "full",
    "mo_name": null,
    "l3_domain": {
        "enabled": false
    },
    "bgp": {
        "enabled": false
    },
    "vlan_pool": null,
    "physical_domain": null,
    "aaep": null,
    "policy_group": null,
    "ap": null,
    "epg": null,
    "bd": null,
    "cdp": null,
    "lldp": null,
    "link_level": null,
    "l2": null,
    "port_channel": null
}

Validated and resolved servers connectivity layout
[
    {
        "hostname": "bm",
        "interface": [
            {
                "domain": "main",
                "ip": "10.6.6.1",
                "gateway": "10.6.6.254/24",
                "mac": "11:11:11:11:11:11",
                "bond": true,
                "trunk": true,
                "vlan": "666",
                "node": "100",
                "port": "1/1/1",
                "mtu": "1500",
                "pod": "1"
            },
            {
                "domain": "main",
                "ip": "10.6.6.1",
                "gateway": "10.6.6.254/24",
                "mac": "22:22:22:22:22:22",
                "bond": true,
                "trunk": true,
                "vlan": "666",
                "node": "200",
                "port": "1/1/1",
                "mtu": "1500",
                "pod": "1"
            }
        ]
    }
]
- Tenant [k8s] found
- VLAN pool not defined
- phys domain not defined
- l3 domain not enabled
- aaep not defined
- Policy group not defined
- Application profile not defined
- epg not defined
- bridge domain not defined

Server [bm] interfaces in domain [main]
---------------------------------------

Interface pod-1:node-100:1/1/1
- Interface found
        Operational State up
        Switching State enabled
        Usage epg
        Operational Mode trunk
        Operational Speed 10G
        IP endpoint [10.6.6.1] found
        - k8s/bm/main
                pod-1:node-200:eth1/1/1 (k8s-bm-main)
                pod-1:node-100:eth1/1/1 (k8s-bm-main)
        IP endpoint found on the server interface (reinstallation)
        MAC endpoint [11:11:11:11:11:11] found
        - k8s/bm/main
                pod-1:node-200:eth1/1/1 (k8s-bm-main)
                pod-1:node-100:eth1/1/1 (k8s-bm-main)
        MAC endpoint found on the server interface (reinstallation)
- Trunk mode match
- VLAN [666] match
- Bonding enabled

Interface pod-1:node-200:1/1/1
- Interface found
        Operational State up
        Switching State enabled
        Usage epg
        Operational Mode trunk
        Operational Speed 10G
        IP endpoint [10.6.6.1] found
        - k8s/bm/main
                pod-1:node-200:eth1/1/1 (k8s-bm-main)
                pod-1:node-100:eth1/1/1 (k8s-bm-main)
        IP endpoint found on the server interface (reinstallation)
        MAC endpoint [22:22:22:22:22:22] not found
- Trunk mode match
- VLAN [666] match
- Bonding enabled
```

[Back](./uc2.md)