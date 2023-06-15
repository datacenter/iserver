# VLAN Pool

## Filter by name

```
# iserver get aci pool vlan --apic apic21 --name HX*

Apic: apic21 (mode:online, cache:off)

+----------------+-----------------+----------------------+----------+-------------+-----------+
| VLAN Pool Name | Allocation Mode | Encapsulation Block  | Role     | Domain      | EPG Usage |
+----------------+-----------------+----------------------+----------+-------------+-----------+
| HX1_VlanPool   | static          | [70-79] (static)     | external | HX1_PhysDom | 0/3059    | 
|                |                 | [1000-4048] (static) | external |             |           | 
+----------------+-----------------+----------------------+----------+-------------+-----------+
```

Developer

```
# iserver get aci pool vlan --apic apic21 --name HX*

{
    "duration": 1400,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 449,
        "disconnect_time": 0,
        "mo_time": 741,
        "total_time": 1190
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

True	449	-	connect apic21o.emea-sp.cisco.com
True	375	13	apic21o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	366	32	apic21o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./PoolVlan.md)