# Fabric checks with no controller configuration

## Input

```
{
    "controller": [
        {
            "type": "aci",
            "apic": "myapic",
            "domain": "management"
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
                    "vlan": 666,
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
                    "vlan": 666,
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
- VLAN [666] match
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
- VLAN [666] match
- Bonding enabled
```

[Back](./fabric_aci_check.md)
