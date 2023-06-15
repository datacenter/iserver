# Node Protocol - LLDP

## Interface stats output

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view stats

Apic: apic11 (mode:online, cache:on)
Pod: 1
Node: bl205-eu-spdc

+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
| Node                | Packets Sent | Packets Received | Packets Discarded | Error Received Packets | Unrecognized TLV | Adjacencies Added | Adjacencies Removed | Entries Aged |
+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
| pod-1/bl205-eu-spdc | 109389       | 109464           | 0                 | 0                      | 0                | 16                | 0                   | 0            | 
+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
```

Developer

```
# iserver get aci proto lldp --apic apic11 --node bl205-eu-spdc --view stats

{
    "duration": 107,
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
    "cache_hits": 3
}
```

[[Back]](./ProtocolLldp.md)