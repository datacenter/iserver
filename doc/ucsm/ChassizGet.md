# Get Chassis' Information

```
# iserver get ucsm chassiz --manager milan

+------------+-----------+---------------+-------------+-------------+-------------+---------------+
| Chassis Id | Name      | Model         | Serial      | Operability | Power State | Thermal State |
+------------+-----------+---------------+-------------+-------------+-------------+---------------+
| 1          | chassis-1 | UCSB-5108-AC2 | FOX2403P669 | operable    | ok          | ok            | 
| 2          | chassis-2 | UCSB-5108-AC2 | FOX2403P2Z9 | operable    | ok          | ok            | 
+------------+-----------+---------------+-------------+-------------+-------------+---------------+
```

JSON Output

```
# iserver get ucsm chassiz --manager milan

[
    {
        "mo_type": "chassis",
        "dn": "sys/chassis-1",
        "rn": "chassis-1",
        "id": "1",
        "model": "UCSB-5108-AC2",
        "oper_state": "operable",
        "part_number": "68-5091-06",
        "power": "ok",
        "serial": "FOX2403P669",
        "service_state": "in-service",
        "thermal": "ok",
        "vendor": "Cisco Systems Inc"
    },
    {
        "mo_type": "chassis",
        "dn": "sys/chassis-2",
        "rn": "chassis-2",
        "id": "2",
        "model": "UCSB-5108-AC2",
        "oper_state": "operable",
        "part_number": "68-5091-06",
        "power": "ok",
        "serial": "FOX2403P2Z9",
        "service_state": "in-service",
        "thermal": "ok",
        "vendor": "Cisco Systems Inc"
    }
]
```

Developer Output

```
# iserver get ucsm chassiz --manager milan

Developer output

{
    "duration": 3022,
    "isctl": {
        "read": false,
        "calls": 0,
        "success": 0,
        "failed": 0,
        "total_time": 0
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 2277,
        "disconnect_time": 0,
        "mo_time": 588,
        "total_time": 2865
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
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

Log: ucsm
----------

2022-12-08 11:03:02.914528	True	1798	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:03:03.506069	True	588	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:03:04.035668	True	479	disconnect vip-ucsb1.emea-sp.cisco.com
```
