# L3 Out

## Filter PIM-enabled L3 outs

```
# iserver get aci l3out --apic apic11 --pim --empty

Apic: apic11
```

Developer

```
# iserver get aci l3out --apic apic11 --pim --empty

{
    "duration": 1526,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 624,
        "disconnect_time": 0,
        "mo_time": 783,
        "total_time": 1407
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

True	624	-	connect apic11o.emea-sp.cisco.com
True	445	46	apic11o.emea-sp.cisco.com class l3extOut query rsp-subtree=children&rsp-subtree-class=l3extLNodeP,l3extInstP,bgpExtP,ospfExtP,eigrpExtP,pimExtP,l3extRsEctx,l3extRsL3DomAtt
True	338	43	apic11o.emea-sp.cisco.com class l3extLNodeP query rsp-subtree=children&rsp-subtree-class=l3extRsNodeL3OutAtt
```

[[Back]](./L3Out.md)