# Policy - CDP

## Interface specific output

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled --view intf

Apic: apic11

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
    "duration": 1583,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 1078,
        "total_time": 1460
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

True	382	-	connect apic11o.emea-sp.cisco.com
True	313	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	440	370	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	325	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)