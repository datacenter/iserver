# VLAN Pool

## Filter by vlan

```
# iserver get aci pool vlan --apic apic21 --vlan 2501

Apic: apic21 (mode:online, cache:off)

+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| VLAN Pool Name         | Allocation Mode | Encapsulation Block   | Role     | Domain                | EPG Usage |
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| ESX-CDC-22_VlanPool    | dynamic         | [2501-2502] (static)  | external | ESX-CDC-22_PhysDom    | 11/309    | 
|                        |                 | [2503-2509] (static)  | external | vEPC_ESX              |           | 
|                        |                 | [2700-2999] (dynamic) | external | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| HX1_VlanPool           | static          | [70-79] (static)      | external | HX1_PhysDom           | 0/3059    | 
|                        |                 | [1000-4048] (static)  | external |                       |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| vEPC-ESX21-22_VlanPool | dynamic         | [2501-2509] (static)  | external | vEPC-ESX20_PhysDom    | 4/309     | 
|                        |                 | [2700-2999] (dynamic) | external | vEPC-ESX21-22_PhysDom |           | 
|                        |                 |                       |          | VMware                |           | 
+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
```

Developer

```
# iserver get aci pool vlan --apic apic21 --vlan 2501

{
    "duration": 1416,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 453,
        "disconnect_time": 0,
        "mo_time": 703,
        "total_time": 1156
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	453	-	connect apic21o.emea-sp.cisco.com
True	345	13	apic21o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	358	32	apic21o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./PoolVlan.md)