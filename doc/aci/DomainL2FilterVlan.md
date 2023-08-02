# L2 Domain

## Filter by vlan id

```
# iserver get aci domain l2 --apic apic21 --vlan 801

Apic: apic21 (mode:online, cache:off)

L2 Domain [#1]
--------------

+---------+-------------+------------+----------------+--------+---------------------+------------+
| Faults  | Domain      | AAEP       | VLAN Pool      | Mode   | Encapsulation Block | Sec Domain |
+---------+-------------+------------+----------------+--------+---------------------+------------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool | static | [1-1000] (static)   | --         | 
+---------+-------------+------------+----------------+--------+---------------------+------------+
```

Developer

```
# iserver get aci domain l2 --apic apic21 --vlan 801

{
    "duration": 1459,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 464,
        "disconnect_time": 0,
        "mo_time": 728,
        "total_time": 1192
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

True	464	-	connect apic21o.emea-sp.cisco.com:443
True	374	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	354	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainL2.md)