# Node Protocol - LLDP

## Interface stats output

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view stats

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
| Node                | Packets Sent | Packets Received | Packets Discarded | Error Received Packets | Unrecognized TLV | Adjacencies Added | Adjacencies Removed | Entries Aged |
+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
| pod-1/bl205-eu-spdc | 120218       | 120308           | 0                 | 0                      | 0                | 16                | 0                   | 0            | 
+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view stats

{
    "duration": 1055,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 572,
        "total_time": 961
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

True	389	-	connect apic11o.emea-sp.cisco.com:443
True	299	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	273	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lldpInstStats
```

[[Back]](./ProtocolLldp.md)