# Link Layer Discovery Protocol (LLDP)

## Filter by mac

```
# iserver get nx lldp --device ipn11 --mac a0ec

Device: ipn11

LLDP [#1]
---------

+--------+-----------------+----------------+----------------+-----------+------------+
| Device | Local Interface | Device ID      | Port ID        | Hold Time | Capability |
+--------+-----------------+----------------+----------------+-----------+------------+
| ipn11  | Eth1/5          | 14a2.a0ec.7468 | 14a2.a0ec.746c | 120       | --         | 
+--------+-----------------+----------------+----------------+-----------+------------+

Filter: id, mac
View:   state (def)
```

Developer

```
# iserver get nx lldp --device ipn11 --mac a0ec

{
    "duration": 2525,
    "nexus": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 2248,
        "disconnect_time": 0,
        "mo_time": 172,
        "total_time": 2420
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

2023-12-08 16:36:59.606153	True	2246	connect ipn11.emea-sp.cisco.com
2023-12-08 16:36:59.782014	True	172	ipn11.emea-sp.cisco.com show lldp neighbors
2023-12-08 16:36:59.797929	True	2	disconnect ipn11.emea-sp.cisco.com
```

[[Back]](./Lldp.md)