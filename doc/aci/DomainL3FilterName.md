# L3 Domain

## Filter by domain name

```
# iserver get aci domain l3 --apic apic21 --name UCSB*

Apic: apic21 (mode:online, cache:off)

L3 Domain [#1]
--------------

+---------+-------------+------------+----------------+---------+-----------------------+------------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Mode    | Encapsulation Block   | Sec Domain |
+---------+-------------+------------+----------------+---------+-----------------------+------------+
| 0 0 0 0 | UCSB1_L3Dom | UCSB1_AAEP | UCSB1_VlanPool | dynamic | [2-100] (static)      | --         | 
|         |             |            |                |         | [3701-4000] (dynamic) |            | 
+---------+-------------+------------+----------------+---------+-----------------------+------------+
```

Developer

```
# iserver get aci domain l3 --apic apic21 --name UCSB*

{
    "duration": 1516,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 779,
        "total_time": 1225
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

True	446	-	connect apic21o.emea-sp.cisco.com:443
True	391	7	apic21o.emea-sp.cisco.com:443 class l3extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,extnwRtL3DomAtt,aaaDomainRef
True	388	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainL3.md)