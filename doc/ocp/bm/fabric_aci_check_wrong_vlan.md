# Fabric checks with VLAN mismatch

## Input

```
{
    "mode": "check",
    "controller": [
        {
            "type": "aci",
            "apic": "myapic",
            "domain": "management",
            "tenant": {
                "name": "my_tenant"
            },
            "vlan_pool": {
                "name": "my_vlan_pool",
                "vlan": "666"
            },
            "physical_domain": {
                "name": "my_phys_dom"
            },
            "aaep": {
                "name": "my_aaep"
            },
            "policy_group": {
                "name": "my_pg",
                "type": "vpc",
                "cdp": {
                    "name": "my_cdp"
                },
                "lldp": {
                    "name": "my_lldp"
                },
                "link_level": {
                    "name": "my_link_level"
                },
                "port_channel": {
                    "name": "my_lacp"
                },
                "l2": {
                    "name": "my_l2"
                }
            },
            "ap": {
                "name": "my_anp"
            },
            "epg": {
                "name": "my_epg"
            },
            "bd": {
                "name": "my_bd",
                "gateway": "10.4.4.15/28",
                "l3out": "my_l3out"
            }
        }
    ],
    "server": [
        {
            "hostname": "bm1",
            "interface": [
                {
                    "domain": "management",
                    "ip": "10.4.4.1",
                    "mac": "aa:aa:aa:aa:aa:aa",
                    "bond": true,
                    "trunk": true,
                    "vlan": 703,
                    "pod": "1",
                    "node": "100",
                    "port": "1/1/1"
                },
                {
                    "domain": "management",
                    "ip": "10.4.4.1",
                    "mac": "bb:bb:bb:bb:bb:bb",
                    "bond": true,
                    "trunk": true,
                    "vlan": 703,
                    "pod": "1",
                    "node": "200",
                    "port": "1/1/1"
                }
            ]
        }
    ]
}
```

## Output

```
Apic [myapic] domain [management] configuration
------------------------------------------------
- Tenant [my_tenant] found
- VLAN pool [my_vlan_pool] found
        Vlans [666] match
- AAEP [my_aaep] found
- Physical domain [my_phys_dom] found
        VLAN pool [my_vlan_pool] match
        AAEP [my_aaep] match
- PolicyGroup [my_pg]
        CDP policy [my_cdp] match
        LLDP policy [my_lldp] match
        Link level policy [my_link_level] match
        Port channel policy [my_lacp] match
        L2 policy [my_l2] match
        Deployed on pod-1:node-100:eth1/1/1
        Server [bm1] interface mac [aa:aa:aa:aa:aa:aa]
        Deployed on pod-1:node-200:eth1/1/1
        Server [bm1] interface mac [bb:bb:bb:bb:bb:bb]
- Application profile [my_anp] found
        Tenant [my_tenant] match
- EPG [my_epg]
        Tenant [my_tenant] match
        Application profile [my_anp] match
        Bridge Domain [my_bd] match
        Static port [my_pg] match
- Bridge Domain [my_bd] found
        Tenant [my_tenant] match
        Gateway [10.4.4.15/28] match
        L3out [my_l3out] match

Server [bm1] interfaces in domain [management]
---------------------------------------------------

Interface pod-1:node-100:1/1/1
- Interface found
        Operational State up
        Switching State enabled
        Usage epg
        Operational Mode trunk
        Operational Speed 10G
        IP endpoint [10.4.4.1] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        IP endpoint with EPG match
        IP endpoint found on the server interface (reinstallation)
        MAC endpoint [aa:aa:aa:aa:aa:aa] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        MAC endpoint with EPG match
        MAC endpoint found on the server interface (reinstallation)
- EPG [my_tenant/my_anp/my_epg] match
- Bridge Domain [my_tenant/my_bd] match
        Bridge domain subnet [10.4.4.0/28] match
- Trunk mode match
[ERROR] VLAN [703] may not be enabled
- PolicyGroup [my_pg] match
- Bonding enabled

Interface pod-1:node-200:1/1/1
- Interface found
        Operational State up
        Switching State enabled
        Usage epg
        Operational Mode trunk
        Operational Speed 10G
        IP endpoint [10.4.4.1] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        IP endpoint with EPG match
        IP endpoint found on the server interface (reinstallation)
        MAC endpoint [bb:bb:bb:bb:bb:bb] not found
- EPG [my_tenant/my_anp/my_epg] match
- Bridge Domain [my_tenant/my_bd] match
        Bridge domain subnet [10.4.4.0/28] match
- Trunk mode match
[ERROR] VLAN [666] may not be enabled
- PolicyGroup [my_pg] match
- Bonding enabled
```

## Output with no policy

```
Apic [myapic] domain [management] configuration
------------------------------------------------

Server [bm1] interfaces in domain [management]
---------------------------------------------------

Interface pod-1:node-100:1/1/1
- Interface found
        Operational State up
        Switching State enabled
        Usage epg
        Operational Mode trunk
        Operational Speed 10G
        IP endpoint [10.4.4.1] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        IP endpoint found on the server interface (reinstallation)
        MAC endpoint [aa:aa:aa:aa:aa:aa] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        MAC endpoint found on the server interface (reinstallation)
- Trunk mode match
[ERROR] VLAN [703] may not be enabled
- Bonding enabled

Interface pod-1:node-200:1/1/1
- Interface found
        Operational State up
        Switching State enabled
        Usage epg
        Operational Mode trunk
        Operational Speed 10G
        IP endpoint [10.4.4.1] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        IP endpoint found on the server interface (reinstallation)
        MAC endpoint [bb:bb:bb:bb:bb:bb] not found
- Trunk mode match
[ERROR] VLAN [666] may not be enabled
- Bonding enabled
```

[Back](./fabric_aci_check.md)
