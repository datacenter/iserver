# L3 Out

## Filter EIGRP-enabled L3 outs

```
# iserver get aci l3out --apic apic11 --eigrp

Apic: apic11 (mode:online, cache:off)

L3Out - EIGRP [#0]
------------------
None
```

Developer

```
# iserver get aci l3out --apic apic11 --eigrp

{
    "duration": 1444,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 463,
        "disconnect_time": 0,
        "mo_time": 834,
        "total_time": 1297
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

True	463	-	connect apic11o.emea-sp.cisco.com:443
True	445	46	apic11o.emea-sp.cisco.com:443 class l3extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	389	43	apic11o.emea-sp.cisco.com:443 class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)