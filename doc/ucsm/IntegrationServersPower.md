# Get Intersight Servers with Power Information

```
# iserver get servers --group ucsm -c power

+---------+----+----+----------------------+------------------+-------------+-------------+--------------+---------+---------+---------+
| SF      | MF | WF | Name                 | Model            | Serial      | IP          | Consumed [W] | Min [W] | Avg [W] | Max [W] |
+---------+----+----+----------------------+------------------+-------------+-------------+--------------+---------+---------+---------+
| P+ C(9) | CU |    | FI-ucsb1-eu-spdc-1-1 | (B) UCSB-B200-M4 | FCH205371PZ | 10.58.52.33 | 144.0        | 138.0   | 142.8   | 144.0   | 
| P+ C(9) | CU |    | FI-ucsb1-eu-spdc-1-2 | (B) UCSB-B200-M4 | FCH20527XXD | 10.58.52.34 | 138.0        | 138.0   | 138.0   | 138.0   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-1-3 | (B) UCSB-B200-M4 | FCH20437VXH | 10.58.52.35 | 126.0        | 126.0   | 126.0   | 126.0   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-1-4 | (B) UCSB-B200-M4 | FCH205371UU | 10.58.52.36 | 126.0        | 126.0   | 126.0   | 126.0   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-1 | (B) UCSB-B200-M5 | FLM241501FB | 10.58.52.41 | 249.6        | 237.9   | 242.58  | 249.6   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-2 | (B) UCSB-B200-M5 | FLM24140BJB | 10.58.52.42 | 202.8        | 202.8   | 202.8   | 202.8   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-3 | (B) UCSB-B200-M5 | FLM241501CT | 10.58.52.43 | 195.0        | 195.0   | 196.06  | 198.9   | 
| P+ H    | CU |    | FI-ucsb1-eu-spdc-2-4 | (B) UCSB-B200-M5 | FLM24140B0B | 10.58.52.44 | 237.9        | 234.0   | 235.3   | 237.9   | 
+---------+----+----+----------------------+------------------+-------------+-------------+--------------+---------+---------+---------+
```

JSON Output

```
# iserver get servers --group ucsm -c power

[
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6335c26e76752d3139b9694c",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-1",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM241501FB",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 393216,
        "TotalMemory": 393216,
        "UsedMemory": 0,
        "TotalMemoryUnit": "384 [GiB]",
        "TotalMemoryGB": 384,
        "AvailableMemoryUnit": "384 [GiB]",
        "AvailableMemoryGB": 384,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.41",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-1/board/power-stats",
                "time_collected": "2022-12-13T18:00:43.794",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-1",
                "consumed_power": 249.6,
                "input_current": 20.64,
                "input_voltage": 12.1,
                "consumed_power_avg": 242.58,
                "input_current_avg": 20.11,
                "input_voltage_avg": 12.06,
                "consumed_power_min": 237.9,
                "input_current_min": 19.77,
                "input_voltage_min": 12.04,
                "consumed_power_max": 249.6,
                "input_current_max": 20.64,
                "input_voltage_max": 12.1
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 249.6,
                "PowerMin": 237.9,
                "PowerAvg": 242.58,
                "PowerMax": 249.6
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6335c45976752d3139b9bf94",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-2",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM24140BJB",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 393216,
        "TotalMemory": 393216,
        "UsedMemory": 0,
        "TotalMemoryUnit": "384 [GiB]",
        "TotalMemoryGB": 384,
        "AvailableMemoryUnit": "384 [GiB]",
        "AvailableMemoryGB": 384,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.42",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-2/board/power-stats",
                "time_collected": "2022-12-13T18:00:59.870",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-2",
                "consumed_power": 202.8,
                "input_current": 16.69,
                "input_voltage": 12.15,
                "consumed_power_avg": 202.8,
                "input_current_avg": 16.69,
                "input_voltage_avg": 12.15,
                "consumed_power_min": 202.8,
                "input_current_min": 16.69,
                "input_voltage_min": 12.15,
                "consumed_power_max": 202.8,
                "input_current_max": 16.69,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 202.8,
                "PowerMin": 202.8,
                "PowerAvg": 202.8,
                "PowerMax": 202.8
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "6335e1f376752d3139bf12b8",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-1",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH205371PZ",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.33",
        "AlarmSummary": {
            "Critical": 9,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Critical (9)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-1/board/power-stats",
                "time_collected": "2022-12-13T18:00:56.196",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-1",
                "consumed_power": 144.0,
                "input_current": 11.96,
                "input_voltage": 12.04,
                "consumed_power_avg": 142.8,
                "input_current_avg": 11.86,
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
                "PowerAvg": 142.8,
                "PowerMax": 144.0
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ C(9)",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.RRRR"
        },
        "Moid": "6337014c76752d3139f2f459",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-2",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH20527XXD",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
        "AvailableMemory": 524288,
        "TotalMemory": 524288,
        "UsedMemory": 0,
        "TotalMemoryUnit": "512 [GiB]",
        "TotalMemoryGB": 512,
        "AvailableMemoryUnit": "512 [GiB]",
        "AvailableMemoryGB": 512,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.34",
        "AlarmSummary": {
            "Critical": 9,
            "Warning": 0,
            "Info": 1
        },
        "Health": "Critical (9)",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-2/board/power-stats",
                "time_collected": "2022-12-13T18:00:57.110",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-2",
                "consumed_power": 138.0,
                "input_current": 11.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 138.0,
                "input_current_avg": 11.52,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 138.0,
                "input_current_min": 11.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 138.0,
                "input_current_max": 11.52,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 138.0,
                "PowerMin": 138.0,
                "PowerAvg": 138.0,
                "PowerMax": 138.0
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ C(9)",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "6337063276752d3139f3cc83",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-3",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH20437VXH",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
        "AvailableMemory": 262144,
        "TotalMemory": 262144,
        "UsedMemory": 0,
        "TotalMemoryUnit": "256 [GiB]",
        "TotalMemoryGB": 256,
        "AvailableMemoryUnit": "256 [GiB]",
        "AvailableMemoryGB": 256,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.35",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-3/board/power-stats",
                "time_collected": "2022-12-13T18:01:21.944",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-3",
                "consumed_power": 126.0,
                "input_current": 10.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 126.0,
                "input_current_avg": 10.52,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 126.0,
                "input_current_min": 10.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 126.0,
                "input_current_max": 10.52,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 126.0,
                "PowerMin": 126.0,
                "PowerAvg": 126.0,
                "PowerMax": 126.0
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "63371c9176752d3139f7da74",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-1-4",
        "Model": "UCSB-B200-M4",
        "Serial": "FCH205371UU",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 24,
        "NumThreads": 48,
        "Cpu": "2S 24C 48T",
        "AvailableMemory": 262144,
        "TotalMemory": 262144,
        "UsedMemory": 0,
        "TotalMemoryUnit": "256 [GiB]",
        "TotalMemoryGB": 256,
        "AvailableMemoryUnit": "256 [GiB]",
        "AvailableMemoryGB": 256,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.36",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Power": {
            "Data": {
                "dn": "sys/chassis-1/blade-4/board/power-stats",
                "time_collected": "2022-12-13T18:01:02.071",
                "chassis_rn": "chassis-1",
                "blade_rn": "blade-4",
                "consumed_power": 126.0,
                "input_current": 10.52,
                "input_voltage": 11.98,
                "consumed_power_avg": 126.0,
                "input_current_avg": 10.52,
                "input_voltage_avg": 11.98,
                "consumed_power_min": 126.0,
                "input_current_min": 10.52,
                "input_voltage_min": 11.98,
                "consumed_power_max": 126.0,
                "input_current_max": 10.52,
                "input_voltage_max": 11.98
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 126.0,
                "PowerMin": 126.0,
                "PowerAvg": 126.0,
                "PowerMax": 126.0
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M4",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "63371c9176752d3139f7da78",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-4",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM24140B0B",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 196608,
        "TotalMemory": 196608,
        "UsedMemory": 0,
        "TotalMemoryUnit": "192 [GiB]",
        "TotalMemoryGB": 192,
        "AvailableMemoryUnit": "192 [GiB]",
        "AvailableMemoryGB": 192,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.44",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-4/board/power-stats",
                "time_collected": "2022-12-13T18:00:51.827",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-4",
                "consumed_power": 237.9,
                "input_current": 19.67,
                "input_voltage": 12.1,
                "consumed_power_avg": 235.3,
                "input_current_avg": 19.45,
                "input_voltage_avg": 12.1,
                "consumed_power_min": 234.0,
                "input_current_min": 19.35,
                "input_voltage_min": 12.1,
                "consumed_power_max": 237.9,
                "input_current_max": 19.67,
                "input_voltage_max": 12.1
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 237.9,
                "PowerMin": 234.0,
                "PowerAvg": 235.3,
                "PowerMax": 237.9
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    },
    {
        "__Output": {
            "FlagState": ":GG.G"
        },
        "Moid": "63371c9176752d3139f7da82",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Name": "FI-ucsb1-eu-spdc-2-3",
        "Model": "UCSB-B200-M5",
        "Serial": "FLM241501CT",
        "ManagementMode": "UCSM",
        "OperPowerState": "on",
        "NumCpus": 2,
        "NumCpuCores": 40,
        "NumThreads": 80,
        "Cpu": "2S 40C 80T",
        "AvailableMemory": 196608,
        "TotalMemory": 196608,
        "UsedMemory": 0,
        "TotalMemoryUnit": "192 [GiB]",
        "TotalMemoryGB": 192,
        "AvailableMemoryUnit": "192 [GiB]",
        "AvailableMemoryGB": 192,
        "UsedMemoryUnit": "0 [KiB]",
        "UsedMemoryGB": 0,
        "UsedMemoryPct": 0,
        "UsedMemoryPctUnit": "0%",
        "ManagementIp": "10.58.52.43",
        "AlarmSummary": {
            "Critical": 0,
            "Warning": 0,
            "Info": 0
        },
        "Health": "Healthy",
        "Connected": true,
        "Workflow": {
            "Running": null,
            "LatestMoid": null,
            "Last": []
        },
        "Groups": "power,ucsm",
        "Redfish": {
            "Capable": false,
            "Enabled": false
        },
        "UCSM": {
            "Capable": true,
            "Enabled": true
        },
        "IMC": {
            "Capable": false,
            "Enabled": false
        },
        "Power": {
            "Data": {
                "dn": "sys/chassis-2/blade-3/board/power-stats",
                "time_collected": "2022-12-13T18:00:54.854",
                "chassis_rn": "chassis-2",
                "blade_rn": "blade-3",
                "consumed_power": 195.0,
                "input_current": 16.04,
                "input_voltage": 12.15,
                "consumed_power_avg": 196.06,
                "input_current_avg": 16.17,
                "input_voltage_avg": 12.12,
                "consumed_power_min": 195.0,
                "input_current_min": 16.04,
                "input_voltage_min": 12.1,
                "consumed_power_max": 198.9,
                "input_current_max": 16.44,
                "input_voltage_max": 12.15
            },
            "Summary": {
                "Source": "UCSM",
                "PowerNow": 195.0,
                "PowerMin": 195.0,
                "PowerAvg": 196.06,
                "PowerMax": 198.9
            }
        },
        "Type": "Blade",
        "TypeModel": "(B) UCSB-B200-M5",
        "LocatorLedOn": false,
        "FlagState": "P+ H",
        "FlagManagement": "CU",
        "FlagWorkflow": ""
    }
]
```

Developer Output

```
# iserver get servers --group ucsm -c power

Developer output

{
    "duration": 7983,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 4721
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
        "success": 40,
        "failed": 0,
        "connect": 16,
        "disconnect": 0,
        "mo": 24,
        "connect_time": 9293,
        "disconnect_time": 0,
        "mo_time": 4524,
        "total_time": 13817
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
        "read": true,
        "lines": 57
    }
}

Log: isctl
-----------

2022-12-13 17:01:32.422279	True	2511	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:01:33.035533	True	612	10	isctl get compute blade   -o json --top 100
2022-12-13 17:01:33.482014	True	405	1	isctl get asset deviceregistration --filter "Moid in ('618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1', '618942976f72612d309dfbe1')"  -o json --top 100
2022-12-13 17:01:33.667279	True	591	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 17:01:33.686570	True	602	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T17:01:33.000Z"  -o json --top 100


Log: ucsm
----------

2022-12-13 17:01:34.477112	True	726	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:34.680314	True	203	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:01:34.800090	True	1068	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:34.923417	True	243	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:01:34.997769	True	197	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:01:35.089054	True	166	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:01:35.211927	True	1481	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:35.241990	True	243	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:01:35.242080	True	152	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:35.405098	True	163	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:01:35.405676	True	193	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:01:35.453278	True	1693	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:35.558891	True	152	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:35.633730	True	228	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:01:35.650124	True	197	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:01:35.846387	True	213	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:01:35.870551	True	220	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:01:36.002084	True	155	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:36.053762	True	183	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:01:36.076957	True	718	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:36.212158	True	157	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:36.259586	True	182	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:01:36.416721	True	837	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:36.446984	True	187	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:01:36.587470	True	171	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:01:36.614253	True	167	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:01:36.731563	True	713	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:36.757783	True	170	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:01:36.771994	True	156	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:36.890872	True	158	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:01:36.917395	True	160	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:01:37.048123	True	822	connect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:37.071908	True	153	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:37.078640	True	187	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:01:37.211364	True	163	vip-ucsb1.emea-sp.cisco.com:EquipmentChassis
2022-12-13 17:01:37.248582	True	170	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:01:37.401304	True	190	vip-ucsb1.emea-sp.cisco.com:ComputeBlade
2022-12-13 17:01:37.402066	True	153	disconnect vip-ucsb1.emea-sp.cisco.com
2022-12-13 17:01:37.571133	True	170	vip-ucsb1.emea-sp.cisco.com:ComputeMbPowerStats
2022-12-13 17:01:37.729022	True	157	disconnect vip-ucsb1.emea-sp.cisco.com
```
