# L2 Domain

## All domains

```
# iserver get aci domain l2 --apic apic11

Apic: apic11 (mode:online, cache:off)

+----------------+------------+----------------+-----------------------+-----------+
| Domain Name    | AAEP       | VLAN Pool      | Encapsulation Block   | EPG Usage |
+----------------+------------+----------------+-----------------------+-----------+
| VNF-mgmt_L2Dom | Infra_AAEP | Infra_VlanPool | [1-1000] (inherit)    | 0/1001    | 
|                |            |                | [2000-2000] (inherit) |           | 
+----------------+------------+----------------+-----------------------+-----------+
```

Developer

```
# iserver get aci domain l2 --apic apic11

{
    "duration": 1549,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 409,
        "disconnect_time": 0,
        "mo_time": 1023,
        "total_time": 1432
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

True	409	-	connect apic11o.emea-sp.cisco.com
True	325	1	apic11o.emea-sp.cisco.com class l2extDomP query rsp-subtree=children&rsp-subtree-class=infraRsVlanNs,infraRtDomP,aaaDomain
True	371	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	327	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainL2.md)