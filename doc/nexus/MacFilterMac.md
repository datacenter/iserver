# MAC Table

## Filter by mac

```
# iserver get nx mac --device ipn11 --mac 447f

Device: ipn11

MAC [#2]
--------

+--------+------+----------------+--------+-----+-----+------+-------------+
| Device | VLAN | MAC            | Type   | Age | Sec | Ntfy | Port        |
+--------+------+----------------+--------+-----+-----+------+-------------+
| ipn11  | -    | 3c51.0ee0.447f | static | -   | F   | F    | sup-eth1(R) | 
| ipn11  | 3    | 3c51.0ee0.447f | static | -   | F   | F    | sup-eth1(R) | 
+--------+------+----------------+--------+-----+-----+------+-------------+

Filter: mac, vlan
View:   state (def)
```

Developer

```
# iserver get nx mac --device ipn11 --mac 447f

{
    "duration": 2852,
    "nexus": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 2280,
        "disconnect_time": 0,
        "mo_time": 438,
        "total_time": 2718
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

2023-12-08 16:47:09.983519	True	2275	connect ipn11.emea-sp.cisco.com
2023-12-08 16:47:10.425663	True	438	ipn11.emea-sp.cisco.com show mac address-table
2023-12-08 16:47:10.477384	True	5	disconnect ipn11.emea-sp.cisco.com
```

[[Back]](./Mac.md)