# Get Chassis and Blades Information

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade

Chassis
-------
- Chassis Id    : 1
- Name          : chassis-1
- Model         : UCSB-5108-AC2
- Serial        : FOX2403P669
- Operability   : operable
- Power State   : ok
- Thermal State : ok


+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| Blade   | Model        | Serial      | Overal Status | Operability | Power State | Assoc State |
+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| blade-1 | UCSB-B200-M4 | FCH205371PZ | ok            | operable    | on          | associated  | 
| blade-2 | UCSB-B200-M4 | FCH20527XXD | ok            | operable    | on          | associated  | 
| blade-3 | UCSB-B200-M4 | FCH20437VXH | ok            | operable    | on          | associated  | 
| blade-4 | UCSB-B200-M4 | FCH205371UU | ok            | operable    | on          | associated  | 
+---------+--------------+-------------+---------------+-------------+-------------+-------------+
```

JSON Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade

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
    "vendor": "Cisco Systems Inc",
    "blade": [
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
        },
        {
            "mo_type": "blade",
            "association": "associated",
            "chassis_id": "1",
            "available_memory": "524288",
            "assigned_to_dn": "org-root/org-EU-SPN/ls-esx42-eu-spdc",
            "admin_state": "in-service",
            "dn": "sys/chassis-1/blade-2",
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
            "rn": "blade-2",
            "serial": "FCH20527XXD",
            "server_id": "1/2",
            "slot_id": "2",
            "total_memory": "524288",
            "uuid": "315220a5-2121-4e5b-0101-e1dc0000015f",
            "vendor": "Cisco Systems Inc",
            "id": "2",
            "chassis_rn": "chassis-1"
        },
        {
            "mo_type": "blade",
            "association": "associated",
            "chassis_id": "1",
            "available_memory": "262144",
            "assigned_to_dn": "org-root/org-EU-SPN/ls-esx43-eu-spdc",
            "admin_state": "in-service",
            "dn": "sys/chassis-1/blade-3",
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
            "rn": "blade-3",
            "serial": "FCH20437VXH",
            "server_id": "1/3",
            "slot_id": "3",
            "total_memory": "262144",
            "uuid": "315220a5-2121-4e5b-0101-e1dc0000012f",
            "vendor": "Cisco Systems Inc",
            "id": "3",
            "chassis_rn": "chassis-1"
        },
        {
            "mo_type": "blade",
            "association": "associated",
            "chassis_id": "1",
            "available_memory": "262144",
            "assigned_to_dn": "org-root/org-EU-SPN/ls-esx44-eu-spdc",
            "admin_state": "in-service",
            "dn": "sys/chassis-1/blade-4",
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
            "rn": "blade-4",
            "serial": "FCH205371UU",
            "server_id": "1/4",
            "slot_id": "4",
            "total_memory": "262144",
            "uuid": "315220a5-2121-4e5b-0101-e1dc0000013f",
            "vendor": "Cisco Systems Inc",
            "id": "4",
            "chassis_rn": "chassis-1"
        }
    ]
}
```

Developer Output

```
# iserver get ucsm chassis --manager milan --chassis-id 1 --blade

Developer output

{
    "duration": 3294,
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
        "connect_time": 2108,
        "disconnect_time": 0,
        "mo_time": 1065,
        "total_time": 3173
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

2022-12-08 11:01:56.820987	True	1656	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 11:01:57.327398	True	505	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 11:01:57.889362	True	560	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 11:01:58.398163	True	452	disconnect vip-ucsb1.emea-sp.cisco.com
```
