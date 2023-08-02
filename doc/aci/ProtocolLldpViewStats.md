# Node Protocol - LLDP

## Stats view

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view stats

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol LLDP - Stats [#1]
--------------------------

+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
| Node                | Packets Sent | Packets Received | Packets Discarded | Error Received Packets | Unrecognized TLV | Adjacencies Added | Adjacencies Removed | Entries Aged |
+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
| pod-1/bl205-eu-spdc | 1914417      | 1916515          | 0                 | 0                      | 0                | 17                | 0                   | 0            | 
+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view stats

{
    "duration": 1108,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 589,
        "total_time": 979
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

True	390	-	connect apic11o.emea-sp.cisco.com:443
True	300	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	289	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lldpInstStats
```

[[Back]](./ProtocolLldp.md)