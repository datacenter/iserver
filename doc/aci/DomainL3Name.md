# L3 Domain

## Filter by name

```
# iserver get aci domain l3 --apic apic11 --name UCSB*

Apic: apic11

+-------------+------------+----------------+-----------------------+-----------+
| Domain Name | AAEP       | VLAN Pool      | Encapsulation Block   | EPG Usage |
+-------------+------------+----------------+-----------------------+-----------+
| UCSB1_L3Dom | UCSB1_AAEP | UCSB1_VlanPool | [2-100] (static)      | 0/1999    | 
|             |            |                | [101-1000] (inherit)  |           | 
|             |            |                | [2001-2500] (inherit) |           | 
|             |            |                | [3001-3500] (inherit) |           | 
+-------------+------------+----------------+-----------------------+-----------+
```

Developer

```
# iserver get aci domain l3 --apic apic11 --name UCSB*

{
    "duration": 1610,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 1053,
        "total_time": 1448
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
    }
}

Log: apic
----------

True	395	-	connect apic11o.emea-sp.cisco.com
True	327	18	apic11o.emea-sp.cisco.com class l3extDomP query rsp-subtree=children&rsp-subtree-class=infraRsVlanNs,infraRtDomP,aaaDomain
True	375	25	apic11o.emea-sp.cisco.com class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	351	39	apic11o.emea-sp.cisco.com class vmmEpPD
```

[[Back]](./DomainL3.md)