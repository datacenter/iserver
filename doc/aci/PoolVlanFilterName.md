# VLAN Pool

## Filter by name

```
# iserver get aci pool vlan --apic apic21 --name HX*

Apic: apic21 (mode:online, cache:off)

Pool VLAN [#1]
--------------

+---------+----------------+-----------------+----------------------+----------+-------------+-----------+
| Faults  | VLAN Pool Name | Allocation Mode | Encapsulation Block  | Role     | Domain      | EPG Usage |
+---------+----------------+-----------------+----------------------+----------+-------------+-----------+
| 0 0 0 0 | HX1_VlanPool   | static          | [70-79] (static)     | external | HX1_PhysDom | 0/3059    | 
|         |                |                 | [1000-4048] (static) | external |             |           | 
+---------+----------------+-----------------+----------------------+----------+-------------+-----------+
```

Developer

```
# iserver get aci pool vlan --apic apic21 --name HX*

{
    "duration": 1402,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 447,
        "disconnect_time": 0,
        "mo_time": 674,
        "total_time": 1121
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

True	447	-	connect apic21o.emea-sp.cisco.com:443
True	355	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	319	32	apic21o.emea-sp.cisco.com:443 class vmmEpPD
```

[[Back]](./PoolVlan.md)