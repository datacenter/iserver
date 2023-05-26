# Get Chassis Information

```
# iserver get ucsm chassis --manager milan --chassis-id 1

Chassis
-------
- Chassis Id    : 1
- Name          : chassis-1
- Model         : UCSB-5108-AC2
- Serial        : FOX2403P669
- Operability   : operable
- Power State   : ok
- Thermal State : ok
```

JSON Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1

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
}
```

Developer Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1

Developer output

{
    "duration": 2841,
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
        "connect_time": 2206,
        "disconnect_time": 0,
        "mo_time": 543,
        "total_time": 2749
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

2022-12-08 11:01:02.284322	True	1767	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:01:02.831968	True	543	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:01:03.286775	True	439	disconnect vip-ucsb1.emea-sp.cisco.com
```
