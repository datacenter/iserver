# Link Layer Discovery Protocol (LLDP)

## Filter by id

```
# iserver get nx lldp --device ipn11 --id r11*

Device: ipn11

LLDP [#1]
---------

+--------+-----------------+-------------------------------+--------------+-----------+------------+
| Device | Local Interface | Device ID                     | Port ID      | Hold Time | Capability |
+--------+-----------------+-------------------------------+--------------+-----------+------------+
| ipn11  | Eth1/32/1       | r11-eu-spdc.emea-sp.cisco.com | Ethernet1/51 | 120       | BR         | 
+--------+-----------------+-------------------------------+--------------+-----------+------------+

Filter: id, mac
View:   state (def)
```

Developer

```
# iserver get nx lldp --device ipn11 --id r11*

{
    "duration": 2504,
    "nexus": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 2261,
        "disconnect_time": 0,
        "mo_time": 133,
        "total_time": 2394
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

2023-12-08 16:36:46.437810	True	2259	connect ipn11.emea-sp.cisco.com
2023-12-08 16:36:46.581357	True	133	ipn11.emea-sp.cisco.com show lldp neighbors
2023-12-08 16:36:46.605856	True	2	disconnect ipn11.emea-sp.cisco.com
```

[[Back]](./Lldp.md)