# L3Out

## Fault view

```
# iserver get aci l3out --apic apic11 --view fault

Apic: apic11 (mode:online, cache:off)

L3Out - Faults [#1]
-------------------

+---------------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| L3Out               | Sev  | Code  | Cause             | Created Time                  | Lifecycle | Description                                                                     |
+---------------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
| infra/RDC-3_SRL3out | Warn | F1021 | resolution-failed | 2023-06-12T10:38:35.195+02:00 | raised    | Failed to form relation to MO uni/l3dom-SR-Infra-RDC-3_L3dom of class extnwDomP | 
+---------------------+------+-------+-------------------+-------------------------------+-----------+---------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci l3out --apic apic11 --view fault

{
    "duration": 1831,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 467,
        "disconnect_time": 0,
        "mo_time": 1189,
        "total_time": 1656
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

True	467	-	connect apic11o.emea-sp.cisco.com:443
True	435	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	400	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
True	354	1	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./L3Out.md)