# Node Protocol - ND

## Single node adjacencies

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------+----------------+----------------+------------------------+
| Node                | Admin State | Aging Interval | Neighbor Count | Active Interface Count |
+---------------------+-------------+----------------+----------------+------------------------+
| pod-1/bl205-eu-spdc | enabled     | 1380           | 0              | 0                      | 
+---------------------+-------------+----------------+----------------+------------------------+
```

Developer

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc

{
    "duration": 2229,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 447,
        "disconnect_time": 0,
        "mo_time": 1677,
        "total_time": 2124
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

True	447	-	connect apic11o.emea-sp.cisco.com
True	339	11	apic11o.emea-sp.cisco.com class fabricNode
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/nd/inst
True	311	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ndDom
True	326	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	392	35	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolNd.md)