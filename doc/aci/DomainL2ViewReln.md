# L2 Domain

## Reln view

```
# iserver get aci domain l2 --apic apic21 --view reln

Apic: apic21 (mode:online, cache:off)

L2 Domain - Policy Relationships [#2]
-------------------------------------

+---------+-------------+-------------+-------------+
| Faults  | Domain      | Policy Type | Policy Name |
+---------+-------------+-------------+-------------+
| 0 0 0 0 | Infra_L2dom | AAEP        | Infra_AAEP  | 
|         |             | L2 Out      | k8s/Test    | 
+---------+-------------+-------------+-------------+
| 0 0 0 0 | test        | AAEP        | nidemo      | 
+---------+-------------+-------------+-------------+
```

Developer

```
# iserver get aci domain l2 --apic apic21 --view reln

{
    "duration": 992,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 498,
        "disconnect_time": 0,
        "mo_time": 333,
        "total_time": 831
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

True	498	-	connect apic21o.emea-sp.cisco.com:443
True	333	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
```

[[Back]](./DomainL2.md)