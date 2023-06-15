# Node Protocol - IS-IS

## Show tunnel endpoints for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tunnel

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Discovered Tunnel Endpoints
---------------------------

+---------------------+---------+-------------+---------------------+-------+--------------------------+
| Node                | Domain  | Id          | Destination         | Role  | Type                     |
+---------------------+---------+-------------+---------------------+-------+--------------------------+
| pod-1/cl201-eu-spdc | overlay | 10.3.136.64 | pod-1/cl209-eu-spdc | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.136.65 | pod-1/cl210-eu-spdc | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.64 | pod-1/bl205-eu-spdc | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.65 | pod-1/s101-eu-spdc  | spine | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.68 | pod-1/cl202-eu-spdc | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.64  | pod-1/bl206-eu-spdc | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.65  | pod-1/s102-eu-spdc  | spine | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.64  |                     | spine | physical,proxy-acast-v4  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.65  |                     | spine | physical,proxy-acast-mac | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.66  |                     | spine | physical,proxy-acast-v6  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.67  |                     | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.48.64  |                     | leaf  | physical                 | 
+---------------------+---------+-------------+---------------------+-------+--------------------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view tunnel

{
    "duration": 2096,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 448,
        "disconnect_time": 0,
        "mo_time": 1379,
        "total_time": 1827
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

True	448	-	connect apic11o.emea-sp.cisco.com
True	338	13	apic11o.emea-sp.cisco.com class fabricNode
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	351	12	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisDTEp
```

[[Back]](./ProtocolIsis.md)