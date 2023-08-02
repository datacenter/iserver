# VLAN Pool

## Filter by vlan

```
# iserver get aci pool vlan --apic apic21 --vlan 2501

Apic: apic21 (mode:online, cache:off)

Pool VLAN [#3]
--------------

+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| Faults  | VLAN Pool Name         | Allocation Mode | Encapsulation Block   | Role     | Domain                | EPG Usage |
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | ESX-CDC-22_VlanPool    | dynamic         | [2501-2502] (static)  | external | ESX-CDC-22_PhysDom    | 11/309    | 
|         |                        |                 | [2503-2509] (static)  | external | EU-SPDC-CDC-22        |           | 
|         |                        |                 | [2700-2999] (dynamic) | external | vEPC_ESX              |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | HX1_VlanPool           | static          | [70-79] (static)      | external | HX1_PhysDom           | 0/3059    | 
|         |                        |                 | [1000-4048] (static)  | external |                       |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
| 0 0 0 0 | vEPC-ESX21-22_VlanPool | dynamic         | [2501-2509] (static)  | external | vEPC-Dataplane        | 4/309     | 
|         |                        |                 | [2700-2999] (dynamic) | external | vEPC-ESX20_PhysDom    |           | 
|         |                        |                 |                       |          | vEPC-ESX21-22_PhysDom |           | 
+---------+------------------------+-----------------+-----------------------+----------+-----------------------+-----------+
```

Developer

```
# iserver get aci pool vlan --apic apic21 --vlan 2501

{
    "duration": 1463,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 420,
        "disconnect_time": 0,
        "mo_time": 687,
        "total_time": 1107
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

True	420	-	connect apic21o.emea-sp.cisco.com:443
True	340	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	347	32	apic21o.emea-sp.cisco.com:443 class vmmEpPD
```

[[Back]](./PoolVlan.md)