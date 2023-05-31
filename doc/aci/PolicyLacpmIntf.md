# Policy - Port Channel Member

## Interface specific output

```
# iserver get aci policy lacp-m --apic apic11 --name default --view intf

Apic: apic11

+-------------+---------------------+-----------+
| Policy Name | Node                | Interface |
+-------------+---------------------+-----------+
| default     | pod-1/cl201-eu-spdc | eth1/1    | 
|             | pod-1/cl201-eu-spdc | eth1/10   | 
|             | pod-1/cl201-eu-spdc | eth1/11   | 
|             | pod-1/cl201-eu-spdc | eth1/13   | 
|             | pod-1/cl201-eu-spdc | eth1/14   | 
|             | pod-1/cl201-eu-spdc | eth1/2    | 
|             | pod-1/cl201-eu-spdc | eth1/23   | 
|             | pod-1/cl201-eu-spdc | eth1/24   | 
|             | pod-1/cl201-eu-spdc | eth1/27   | 
|             | pod-1/cl201-eu-spdc | eth1/4    | 
|             | pod-1/cl201-eu-spdc | eth1/49   | 
|             | pod-1/cl201-eu-spdc | eth1/5    | 
|             | pod-1/cl201-eu-spdc | eth1/50   | 
|             | pod-1/cl201-eu-spdc | eth1/52   | 
|             | pod-1/cl201-eu-spdc | eth1/53   | 
|             | pod-1/cl201-eu-spdc | eth1/55   | 
|             | pod-1/cl201-eu-spdc | eth1/56   | 
|             | pod-1/cl201-eu-spdc | eth1/58   | 
|             | pod-1/cl201-eu-spdc | eth1/59   | 
|             | pod-1/cl201-eu-spdc | eth1/61   | 
|             | pod-1/cl201-eu-spdc | eth1/62   | 
|             | pod-1/cl201-eu-spdc | eth1/64   | 
|             | pod-1/cl201-eu-spdc | eth1/65   | 
|             | pod-1/cl201-eu-spdc | eth1/67   | 
|             | pod-1/cl201-eu-spdc | eth1/68   | 
|             | pod-1/cl201-eu-spdc | eth1/7    | 
|             | pod-1/cl201-eu-spdc | eth1/8    | 
|             | pod-1/cl201-eu-spdc | eth1/96   | 
|             | pod-1/cl202-eu-spdc | eth1/1    | 
|             | pod-1/cl202-eu-spdc | eth1/10   | 
|             | pod-1/cl202-eu-spdc | eth1/11   | 
|             | pod-1/cl202-eu-spdc | eth1/13   | 
|             | pod-1/cl202-eu-spdc | eth1/14   | 
|             | pod-1/cl202-eu-spdc | eth1/2    | 
|             | pod-1/cl202-eu-spdc | eth1/23   | 
|             | pod-1/cl202-eu-spdc | eth1/24   | 
|             | pod-1/cl202-eu-spdc | eth1/27   | 
|             | pod-1/cl202-eu-spdc | eth1/4    | 
|             | pod-1/cl202-eu-spdc | eth1/49   | 
|             | pod-1/cl202-eu-spdc | eth1/5    | 
|             | pod-1/cl202-eu-spdc | eth1/50   | 
|             | pod-1/cl202-eu-spdc | eth1/52   | 
|             | pod-1/cl202-eu-spdc | eth1/53   | 
|             | pod-1/cl202-eu-spdc | eth1/55   | 
|             | pod-1/cl202-eu-spdc | eth1/56   | 
|             | pod-1/cl202-eu-spdc | eth1/58   | 
|             | pod-1/cl202-eu-spdc | eth1/59   | 
|             | pod-1/cl202-eu-spdc | eth1/61   | 
|             | pod-1/cl202-eu-spdc | eth1/62   | 
|             | pod-1/cl202-eu-spdc | eth1/64   | 
|             | pod-1/cl202-eu-spdc | eth1/65   | 
|             | pod-1/cl202-eu-spdc | eth1/67   | 
|             | pod-1/cl202-eu-spdc | eth1/68   | 
|             | pod-1/cl202-eu-spdc | eth1/7    | 
|             | pod-1/cl202-eu-spdc | eth1/8    | 
|             | pod-1/cl202-eu-spdc | eth1/96   | 
|             | pod-1/bl205-eu-spdc | eth1/1    | 
|             | pod-1/bl205-eu-spdc | eth1/11   | 
|             | pod-1/bl205-eu-spdc | eth1/12   | 
|             | pod-1/bl205-eu-spdc | eth1/2    | 
|             | pod-1/bl205-eu-spdc | eth1/27   | 
|             | pod-1/bl206-eu-spdc | eth1/1    | 
|             | pod-1/bl206-eu-spdc | eth1/11   | 
|             | pod-1/bl206-eu-spdc | eth1/12   | 
|             | pod-1/bl206-eu-spdc | eth1/2    | 
|             | pod-1/bl206-eu-spdc | eth1/27   | 
|             | pod-1/rl301-eu-spdc | eth1/3    | 
|             | pod-1/rl301-eu-spdc | eth1/4    | 
|             | pod-1/rl302-eu-spdc | eth1/3    | 
|             | pod-1/rl302-eu-spdc | eth1/4    | 
+-------------+---------------------+-----------+
Context: phy
```

Developer

```
# iserver get aci policy lacp-m --apic apic11 --name default --view intf

{
    "duration": 1644,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 409,
        "disconnect_time": 0,
        "mo_time": 1000,
        "total_time": 1409
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

True	409	-	connect apic11o.emea-sp.cisco.com
True	338	1	apic11o.emea-sp.cisco.com class lacpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	352	70	apic11o.emea-sp.cisco.com class l1RsLacpIfPolCons
True	310	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacpm.md)