# Get Blade Information

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1

Blade
-----
- Chassis       : chassis-1
- Blade         : blade-1
- Model         : UCSB-B200-M4
- Serial        : FCH205371PZ
- Overal Status : ok
- Operability   : operable
- Power State   : on
- Assoc State   : associated
```

JSON Output

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1

{
    "mo_type": "blade",
    "association": "associated",
    "chassis_id": "1",
    "available_memory": "524288",
    "assigned_to_dn": "org-root/org-EU-SPN/ls-esx41-eu-spdc",
    "admin_state": "in-service",
    "dn": "sys/chassis-1/blade-1",
    "model": "UCSB-B200-M4",
    "num_of_adaptors": "1",
    "num_of_cores": "24",
    "num_of_cores_enabled": "24",
    "num_of_cpus": "2",
    "num_of_eth_host_ifs": "8",
    "num_of_fc_host_ifs": "0",
    "num_of_threads": "48",
    "oper_power": "on",
    "oper_state": "ok",
    "operability": "operable",
    "part_number": "73-15862-04",
    "rn": "blade-1",
    "serial": "FCH205371PZ",
    "server_id": "1/1",
    "slot_id": "1",
    "total_memory": "524288",
    "uuid": "315220a5-2121-4e5b-0101-e1dc0000014f",
    "vendor": "Cisco Systems Inc",
    "id": "1",
    "chassis_rn": "chassis-1"
}
```

Developer Output

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1

Developer output

{
    "duration": 3121,
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
        "success": 4,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 2017,
        "disconnect_time": 0,
        "mo_time": 1061,
        "total_time": 3078
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

2022-12-08 10:58:52.465544	True	1556	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 10:58:52.976657	True	508	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 10:58:53.530907	True	553	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 10:58:54.003721	True	461	disconnect vip-ucsb1.emea-sp.cisco.com
```
