# L2 Domain

## Default output

```
# iserver get aci domain l2 --apic apic21

Apic: apic21 (mode:online, cache:off)

L2 Domain [#2]
--------------

+---------+-------------+------------+------------------+--------+----------------------+--------------+
| Faults  | Domain      | AAEP       | VLAN Pool        | Mode   | Encapsulation Block  | Sec Domain   |
+---------+-------------+------------+------------------+--------+----------------------+--------------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool   | static | [1-1000] (static)    | --           | 
+---------+-------------+------------+------------------+--------+----------------------+--------------+
| 0 0 0 0 | test        | nidemo     | nidemo-3000-3001 | static | [3000-3001] (static) | UCSB1_SecDom | 
+---------+-------------+------------+------------------+--------+----------------------+--------------+
```

Developer

```
# iserver get aci domain l2 --apic apic21

{
    "duration": 1529,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 488,
        "disconnect_time": 0,
        "mo_time": 762,
        "total_time": 1250
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

True	488	-	connect apic21o.emea-sp.cisco.com:443
True	369	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	393	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
```

[[Back]](./DomainL2.md)