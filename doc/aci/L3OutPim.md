# L3 Out

## Filter PIM-enabled L3 outs

```
# iserver get aci l3out --apic apic11 --pim

Apic: apic11 (mode:online, cache:off)
```

Developer

```
# iserver get aci l3out --apic apic11 --pim

{
    "duration": 1498,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 808,
        "total_time": 1222
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

True	414	-	connect apic11o.emea-sp.cisco.com
True	396	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	412	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)