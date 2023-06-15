# Policy - CDP

## Interface specific output

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled --view intf

Apic: apic11 (mode:online, cache:off)

+-------------+---------------------+-----------+
| Policy Name | Node                | Interface |
+-------------+---------------------+-----------+
| cdp-enabled | pod-1/bl205-eu-spdc | eth1/28   | 
|             | pod-1/bl206-eu-spdc | eth1/28   | 
|             | pod-1/rl301-eu-spdc | eth1/29   | 
|             | pod-1/rl302-eu-spdc | eth1/29   | 
+-------------+---------------------+-----------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled --view intf

{
    "duration": 1892,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 446,
        "disconnect_time": 0,
        "mo_time": 1155,
        "total_time": 1601
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

True	446	-	connect apic11o.emea-sp.cisco.com
True	353	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	434	426	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	368	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)