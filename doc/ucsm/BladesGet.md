# Get Blades Information

```
# iserver get ucsm blades --manager milan --chassis-id 1

+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| Chassis   | Blade   | Model        | Serial      | Overal Status | Operability | Power State | Assoc State |
+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+
| chassis-1 | blade-1 | UCSB-B200-M4 | FCH205371PZ | ok            | operable    | on          | associated  | 
| chassis-1 | blade-2 | UCSB-B200-M4 | FCH20527XXD | ok            | operable    | on          | associated  | 
| chassis-1 | blade-3 | UCSB-B200-M4 | FCH20437VXH | ok            | operable    | on          | associated  | 
| chassis-1 | blade-4 | UCSB-B200-M4 | FCH205371UU | ok            | operable    | on          | associated  | 
+-----------+---------+--------------+-------------+---------------+-------------+-------------+-------------+
```

JSON Output

```
# iserver get ucsm blades --manager milan --chassis-id 1

[
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
```

Developer Output

```
# iserver get ucsm blades --manager milan --chassis-id 1

Developer output

{
    "duration": 3830,
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
        "connect_time": 2351,
        "disconnect_time": 0,
        "mo_time": 1315,
        "total_time": 3666
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

2022-12-08 10:59:46.880162	True	1802	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 10:59:47.522074	True	639	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 10:59:48.202053	True	676	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 10:59:48.820197	True	549	disconnect vip-ucsb1.emea-sp.cisco.com
```
