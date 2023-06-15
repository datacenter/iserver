# Policy - CDP

## Filter by node

```
# iserver get aci policy cdp --apic apic11 --node bl205* --view intf

Apic: apic11 (mode:online, cache:off)

+-------------+---------------------+-----------+
| Policy Name | Node                | Interface |
+-------------+---------------------+-----------+
| cdp-enabled | pod-1/bl205-eu-spdc | eth1/28   | 
| CDP_enable  | pod-1/bl205-eu-spdc | eth1/1    | 
|             | pod-1/bl205-eu-spdc | eth1/11   | 
|             | pod-1/bl205-eu-spdc | eth1/12   | 
|             | pod-1/bl205-eu-spdc | eth1/2    | 
|             | pod-1/bl205-eu-spdc | eth1/24   | 
|             | pod-1/bl205-eu-spdc | eth1/27   | 
| default     | pod-1/bl205-eu-spdc | eth1/10   | 
|             | pod-1/bl205-eu-spdc | eth1/13   | 
|             | pod-1/bl205-eu-spdc | eth1/14   | 
|             | pod-1/bl205-eu-spdc | eth1/15   | 
|             | pod-1/bl205-eu-spdc | eth1/16   | 
|             | pod-1/bl205-eu-spdc | eth1/17   | 
|             | pod-1/bl205-eu-spdc | eth1/18   | 
|             | pod-1/bl205-eu-spdc | eth1/19   | 
|             | pod-1/bl205-eu-spdc | eth1/20   | 
|             | pod-1/bl205-eu-spdc | eth1/21   | 
|             | pod-1/bl205-eu-spdc | eth1/22   | 
|             | pod-1/bl205-eu-spdc | eth1/23   | 
|             | pod-1/bl205-eu-spdc | eth1/25   | 
|             | pod-1/bl205-eu-spdc | eth1/26   | 
|             | pod-1/bl205-eu-spdc | eth1/3    | 
|             | pod-1/bl205-eu-spdc | eth1/4    | 
|             | pod-1/bl205-eu-spdc | eth1/5    | 
|             | pod-1/bl205-eu-spdc | eth1/6    | 
|             | pod-1/bl205-eu-spdc | eth1/7    | 
|             | pod-1/bl205-eu-spdc | eth1/8    | 
|             | pod-1/bl205-eu-spdc | eth1/9    | 
+-------------+---------------------+-----------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11 --node bl205* --view intf

{
    "duration": 1940,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 432,
        "disconnect_time": 0,
        "mo_time": 1066,
        "total_time": 1498
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

True	432	-	connect apic11o.emea-sp.cisco.com
True	322	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	409	426	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	335	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)