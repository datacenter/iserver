# Get Blade with Power Information

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --power

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


+--------------------+-------+-------+-------+-------+
| Power Statistics   | Value | Min   | Avg   | Max   |
+--------------------+-------+-------+-------+-------+
| Consumed Power (W) | 144.0 | 138.0 | 140.0 | 144.0 | 
| Input Current (A)  | 11.96 | 11.47 | 11.63 | 11.96 | 
| Input Voltage (V)  | 12.04 | 12.04 | 12.04 | 12.04 | 
+--------------------+-------+-------+-------+-------+
```

JSON Output

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --power

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
    "chassis_rn": "chassis-1",
    "power": {
        "Data": {
            "dn": "sys/chassis-1/blade-1/board/power-stats",
            "time_collected": "2022-12-08T10:58:22.884",
            "chassis_rn": "chassis-1",
            "blade_rn": "blade-1",
            "consumed_power": 144.0,
            "input_current": 11.96,
            "input_voltage": 12.04,
            "consumed_power_avg": 140.0,
            "input_current_avg": 11.63,
            "input_voltage_avg": 12.04,
            "consumed_power_min": 138.0,
            "input_current_min": 11.47,
            "input_voltage_min": 12.04,
            "consumed_power_max": 144.0,
            "input_current_max": 11.96,
            "input_voltage_max": 12.04
        },
        "Summary": {
            "Source": "UCSM",
            "PowerNow": 144.0,
            "PowerMin": 138.0,
            "PowerAvg": 140.0,
            "PowerMax": 144.0
        }
    }
}
```

Developer Output

```
# iserver get ucsm blade --manager milan --chassis-id 1 --blade-id 1 --power

Developer output

{
    "duration": 3866,
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
        "success": 5,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 2255,
        "disconnect_time": 0,
        "mo_time": 1481,
        "total_time": 3736
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

2022-12-08 10:59:04.769936	True	1817	connect vip-ucsb1.emea-sp.cisco.com
2022-12-08 10:59:05.262962	True	490	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-08 10:59:05.785229	True	520	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-08 10:59:06.257887	True	471	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-08 10:59:06.728234	True	438	disconnect vip-ucsb1.emea-sp.cisco.com
```
