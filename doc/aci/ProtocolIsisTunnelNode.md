# Node Protocol - IS-IS

## Show tunnel endpoints for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tunnel

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+---------+-------------+-------+--------------------------+
| Node                | Domain  | Id          | Role  | Type                     |
+---------------------+---------+-------------+-------+--------------------------+
| pod-1/cl201-eu-spdc | overlay | 10.3.192.64 | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.65 | spine | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.68 | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.64  | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.65  | spine | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.64  | spine | physical,proxy-acast-v4  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.65  | spine | physical,proxy-acast-mac | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.66  | spine | physical,proxy-acast-v6  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.67  | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.48.64  | leaf  | physical                 | 
+---------------------+---------+-------------+-------+--------------------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tunnel

{
    "duration": 1976,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 1364,
        "total_time": 1781
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

True	417	-	connect apic11o.emea-sp.cisco.com
True	343	11	apic11o.emea-sp.cisco.com class fabricNode
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	379	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisDTEp
```

[[Back]](./ProtocolIsis.md)