# Physical Domain

## Filter by domain name

```
# iserver get aci domain phy --apic apic21 --name UCSB*

Apic: apic21 (mode:online, cache:off)

Physical Domain [#2]
--------------------

+---------+--------------------+-----------------+---------------------+---------+-----------------------+------------+
| Faults  | Domain             | AAEP            | VLAN Pool           | Mode    | Encapsulation Block   | Sec Domain |
+---------+--------------------+-----------------+---------------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom | UCSB1-R7DC_AAEP | UCSB1-R7DC_VlanPool | dynamic | [2-100] (static)      | --         | 
|         |                    |                 |                     |         | [1701-1899] (dynamic) |            | 
+---------+--------------------+-----------------+---------------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1_PhysDom      | UCSB1_AAEP      | UCSB1_VlanPool      | dynamic | [2-100] (static)      | --         | 
|         |                    |                 |                     |         | [3701-4000] (dynamic) |            | 
+---------+--------------------+-----------------+---------------------+---------+-----------------------+------------+
```

Developer

```
# iserver get aci domain phy --apic apic21 --name UCSB*

{
    "duration": 1748,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 564,
        "disconnect_time": 0,
        "mo_time": 911,
        "total_time": 1475
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

True	564	-	connect apic21o.emea-sp.cisco.com:443
True	444	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	467	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainPhy.md)