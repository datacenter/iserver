# Node Protocol - LLDP

## Interface stats output

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view stats

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------+--------------+------------------+-------------------+---------------+-------------------+---------------------+--------------+
| Node                | Admin State | Packets Sent | Packets Received | Packets Discarded | Error Packets | Adjacencies Added | Adjacencies Removed | Entries Aged |
+---------------------+-------------+--------------+------------------+-------------------+---------------+-------------------+---------------------+--------------+
| pod-1/bl205-eu-spdc | enabled     | 3273968      | 3277656          | 0                 | 0             | 26                | 0                   | 0            | 
+---------------------+-------------+--------------+------------------+-------------------+---------------+-------------------+---------------------+--------------+
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view stats

{
    "duration": 1863,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 423,
        "disconnect_time": 0,
        "mo_time": 1276,
        "total_time": 1699
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

True	423	-	connect apic11o.emea-sp.cisco.com
True	311	11	apic11o.emea-sp.cisco.com class fabricNode
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst
True	314	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lldpInstStats
True	309	13	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back]](./ProtocolLldp.md)