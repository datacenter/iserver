# Policy - Port Channel Member

## Verbose output

```
# iserver get aci policy lacp-m --apic apic11 --name default --view verbose

Apic: apic11 (mode:online, cache:off)

Port Channel Member Policy Properties
-------------------------------------
- Policy Name   : default
- TF            : False
- Priority      : 32768
- Transmit Rate : normal
- Interfaces    : 70
- Ref Policies  : 1


+---------------------+-----------+
| Node                | Interface |
+---------------------+-----------+
| pod-1/cl201-eu-spdc | eth1/1    | 
| pod-1/cl201-eu-spdc | eth1/10   | 
| pod-1/cl201-eu-spdc | eth1/11   | 
| pod-1/cl201-eu-spdc | eth1/13   | 
| pod-1/cl201-eu-spdc | eth1/14   | 
| pod-1/cl201-eu-spdc | eth1/2    | 
| pod-1/cl201-eu-spdc | eth1/23   | 
| pod-1/cl201-eu-spdc | eth1/24   | 
| pod-1/cl201-eu-spdc | eth1/27   | 
| pod-1/cl201-eu-spdc | eth1/4    | 
| pod-1/cl201-eu-spdc | eth1/49   | 
| pod-1/cl201-eu-spdc | eth1/5    | 
| pod-1/cl201-eu-spdc | eth1/50   | 
| pod-1/cl201-eu-spdc | eth1/52   | 
| pod-1/cl201-eu-spdc | eth1/53   | 
| pod-1/cl201-eu-spdc | eth1/55   | 
| pod-1/cl201-eu-spdc | eth1/56   | 
| pod-1/cl201-eu-spdc | eth1/58   | 
| pod-1/cl201-eu-spdc | eth1/59   | 
| pod-1/cl201-eu-spdc | eth1/61   | 
| pod-1/cl201-eu-spdc | eth1/62   | 
| pod-1/cl201-eu-spdc | eth1/64   | 
| pod-1/cl201-eu-spdc | eth1/65   | 
| pod-1/cl201-eu-spdc | eth1/67   | 
| pod-1/cl201-eu-spdc | eth1/68   | 
| pod-1/cl201-eu-spdc | eth1/7    | 
| pod-1/cl201-eu-spdc | eth1/8    | 
| pod-1/cl201-eu-spdc | eth1/96   | 
| pod-1/cl202-eu-spdc | eth1/1    | 
| pod-1/cl202-eu-spdc | eth1/10   | 
| pod-1/cl202-eu-spdc | eth1/11   | 
| pod-1/cl202-eu-spdc | eth1/13   | 
| pod-1/cl202-eu-spdc | eth1/14   | 
| pod-1/cl202-eu-spdc | eth1/2    | 
| pod-1/cl202-eu-spdc | eth1/23   | 
| pod-1/cl202-eu-spdc | eth1/24   | 
| pod-1/cl202-eu-spdc | eth1/27   | 
| pod-1/cl202-eu-spdc | eth1/4    | 
| pod-1/cl202-eu-spdc | eth1/49   | 
| pod-1/cl202-eu-spdc | eth1/5    | 
| pod-1/cl202-eu-spdc | eth1/50   | 
| pod-1/cl202-eu-spdc | eth1/52   | 
| pod-1/cl202-eu-spdc | eth1/53   | 
| pod-1/cl202-eu-spdc | eth1/55   | 
| pod-1/cl202-eu-spdc | eth1/56   | 
| pod-1/cl202-eu-spdc | eth1/58   | 
| pod-1/cl202-eu-spdc | eth1/59   | 
| pod-1/cl202-eu-spdc | eth1/61   | 
| pod-1/cl202-eu-spdc | eth1/62   | 
| pod-1/cl202-eu-spdc | eth1/64   | 
| pod-1/cl202-eu-spdc | eth1/65   | 
| pod-1/cl202-eu-spdc | eth1/67   | 
| pod-1/cl202-eu-spdc | eth1/68   | 
| pod-1/cl202-eu-spdc | eth1/7    | 
| pod-1/cl202-eu-spdc | eth1/8    | 
| pod-1/cl202-eu-spdc | eth1/96   | 
| pod-1/bl205-eu-spdc | eth1/1    | 
| pod-1/bl205-eu-spdc | eth1/11   | 
| pod-1/bl205-eu-spdc | eth1/12   | 
| pod-1/bl205-eu-spdc | eth1/2    | 
| pod-1/bl205-eu-spdc | eth1/27   | 
| pod-1/bl206-eu-spdc | eth1/1    | 
| pod-1/bl206-eu-spdc | eth1/11   | 
| pod-1/bl206-eu-spdc | eth1/12   | 
| pod-1/bl206-eu-spdc | eth1/2    | 
| pod-1/bl206-eu-spdc | eth1/27   | 
| pod-1/rl301-eu-spdc | eth1/3    | 
| pod-1/rl301-eu-spdc | eth1/4    | 
| pod-1/rl302-eu-spdc | eth1/3    | 
| pod-1/rl302-eu-spdc | eth1/4    | 
+---------------------+-----------+

+-------------+--------------+--------------+
| Policy Name | Policy Type  | Policy Class |
+-------------+--------------+--------------+
| infra       | Access Infra | infraInfra   | 
+-------------+--------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy lacp-m --apic apic11 --name default --view verbose

{
    "duration": 1845,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 425,
        "disconnect_time": 0,
        "mo_time": 959,
        "total_time": 1384
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

True	425	-	connect apic11o.emea-sp.cisco.com
True	315	1	apic11o.emea-sp.cisco.com class lacpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	341	70	apic11o.emea-sp.cisco.com class l1RsLacpIfPolCons
True	303	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacpm.md)