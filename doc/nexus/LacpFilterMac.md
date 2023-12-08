# Link Aggregation Control Protocol (LACP)

## Filter by mac

```
# iserver get nx lacp --device ipn11 --mac 09c8

Device: ipn11

LACP [#4]
---------

+--------+----------------+----------------+-------------------+--------------+---------------+
| Device | Interface      | Port           | Partner MAC       | Partner Port | Partner State |
+--------+----------------+----------------+-------------------+--------------+---------------+
| ipn11  | port-channel11 | Ethernet1/32/1 | d0:09:c8:50:dd:ff | 0x1c9        | 0x3d          | 
| ipn11  | port-channel12 | Ethernet1/32/2 | d0:09:c8:50:b3:3f | 0x1c9        | 0x2065723d    | 
| ipn11  | port-channel13 | Ethernet1/32/3 | d0:09:c8:50:e0:87 | 0x1c9        | 0x3d          | 
| ipn11  | port-channel14 | Ethernet1/32/4 | d0:09:c8:50:ad:0f | 0x1c9        | 0x3d          | 
+--------+----------------+----------------+-------------------+--------------+---------------+

Filter: mac
View:   state (def)
```

Developer

```
# iserver get nx lacp --device ipn11 --mac 09c8

{
    "duration": 6900,
    "nexus": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 2235,
        "disconnect_time": 0,
        "mo_time": 4580,
        "total_time": 6815
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

Log: nexus
-----------

2023-12-08 16:35:48.536739	True	2234	connect ipn11.emea-sp.cisco.com
2023-12-08 16:35:53.120117	True	4580	ipn11.emea-sp.cisco.com show lacp neighbor
2023-12-08 16:35:53.147428	True	1	disconnect ipn11.emea-sp.cisco.com
```

[[Back]](./Lldp.md)