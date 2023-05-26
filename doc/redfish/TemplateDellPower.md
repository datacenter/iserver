# Dell Power Templates

```
# iserver get redfish endpoint
    --type dell
    --ip 10.58.24.210
    --port 49153
    --username administrator
    --password ******
    --template power

Power Consumption (Watt)
------------------------
- Current      : 396
- Min          : 393
- Average      : 395
- Max          : 399
- Limit action : HardPowerOff


+--------------------------------+----------+---------+--------+------------------+
| Name                           | State    | Health  | Volts  | Upper Threshold  |
+--------------------------------+----------+---------+--------+------------------+
| PS1 Voltage 1                  | Enabled  | OK      | 208.0  | None             | 
| PS2 Voltage 2                  | Enabled  | OK      | 208.0  | None             | 
| System Board Pfault Fail Safe  | Enabled  | OK      | None   | None             | 
| System Board DIMM VSHORT       | Enabled  | OK      | None   | None             | 
| System Board PS1 PG FAIL       | Enabled  | OK      | None   | None             | 
| System Board PS2 PG FAIL       | Enabled  | OK      | None   | None             | 
| CPU1 MEMABCD VDD PG            | Enabled  | OK      | None   | None             | 
| CPU1 MEMABCD VPP PG            | Enabled  | OK      | None   | None             | 
| CPU1 MEMABCD VTT PG            | Enabled  | OK      | None   | None             | 
| CPU1 MEMEFGH VDD PG            | Enabled  | OK      | None   | None             | 
| CPU1 MEMEFGH VPP PG            | Enabled  | OK      | None   | None             | 
| CPU1 MEMEFGH VTT PG            | Enabled  | OK      | None   | None             | 
| CPU1 1P8 PG                    | Enabled  | OK      | None   | None             | 
| CPU1 ANA PG                    | Enabled  | OK      | None   | None             | 
| CPU1 VCCIN PG                  | Enabled  | OK      | None   | None             | 
| CPU1 VCCIO PG                  | Enabled  | OK      | None   | None             | 
| CPU1 VSA PG                    | Enabled  | OK      | None   | None             | 
| CPU1 FIVR PG                   | Enabled  | OK      | None   | None             | 
| CPU2 MEMABCD VDD PG            | Enabled  | OK      | None   | None             | 
| CPU2 MEMABCD VPP PG            | Enabled  | OK      | None   | None             | 
| CPU2 MEMABCD VTT PG            | Enabled  | OK      | None   | None             | 
| CPU2 MEMEFGH VDD PG            | Enabled  | OK      | None   | None             | 
| CPU2 MEMEFGH VPP PG            | Enabled  | OK      | None   | None             | 
| CPU2 MEMEFGH VTT PG            | Enabled  | OK      | None   | None             | 
| CPU2 1P8 PG                    | Enabled  | OK      | None   | None             | 
| CPU2 ANA PG                    | Enabled  | OK      | None   | None             | 
| CPU2 VCCIN PG                  | Enabled  | OK      | None   | None             | 
| CPU2 VCCIO PG                  | Enabled  | OK      | None   | None             | 
| CPU2 VSA PG                    | Enabled  | OK      | None   | None             | 
| CPU2 FIVR PG                   | Enabled  | OK      | None   | None             | 
| System Board BP0 PG            | Enabled  | OK      | None   | None             | 
| System Board BP1 PG            | Enabled  | OK      | None   | None             | 
| System Board BP3 PG            | Enabled  | OK      | None   | None             | 
| System Board BP4 PG            | Enabled  | OK      | None   | None             | 
| System Board 1V05 SW PG        | Enabled  | OK      | None   | None             | 
| System Board 3.3V A PG         | Enabled  | OK      | None   | None             | 
| System Board 5V SW PG          | Enabled  | OK      | None   | None             | 
| System Board BMC SW PG         | Enabled  | OK      | None   | None             | 
| System Board OCP1 PG           | Enabled  | OK      | None   | None             | 
| System Board OCP1 HP SW PG     | Enabled  | OK      | None   | None             | 
| System Board BATT PG           | Enabled  | OK      | None   | None             | 
| System Board PVNN SW PG        | Enabled  | OK      | None   | None             | 
| CPU1 VCORE VR                  | Enabled  | OK      | 1.79   | None             | 
| CPU2 VCORE VR                  | Enabled  | OK      | 1.79   | None             | 
| CPU1 MEM0123 VR                | Enabled  | OK      | 1.22   | None             | 
| CPU1 MEM4567 VR                | Enabled  | OK      | 1.22   | None             | 
| CPU2 MEM0123 VR                | Enabled  | OK      | 1.22   | None             | 
| CPU2 MEM4567 VR                | Enabled  | OK      | 1.22   | None             | 
+--------------------------------+----------+---------+--------+------------------+

+-------------+----------+---------+-----------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| Name        | State    | Health  | Serial          | Firmware  | Output (Watt)  | Input (Watt)  | Max (V)  | Min (V)  | Max (Hz)  | Min (Hz)  |
+-------------+----------+---------+-----------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
| PS1 Status  | Enabled  | OK      | CNLOD001262D5D  | 00.17.28  | 363.0          | 393.0         | 14       | 132      | 35        | 40        | 
| PS2 Status  | Enabled  | OK      | CNLOD001262DF2  | 00.17.28  | 0.0            | 5.0           | 14       | 132      | 35        | 40        | 
+-------------+----------+---------+-----------------+-----------+----------------+---------------+----------+----------+-----------+-----------+
```

```
# iserver get redfish endpoint
    --type dell
    --ip 10.58.24.210
    --port 49153
    --username administrator
    --password ******
    --template power
    --output json

{
    "PowerControl": {
        "PowerConsumedWatts": 396,
        "LimitException": "HardPowerOff",
        "AverageConsumedWatts": 395,
        "IntervalInMin": 1,
        "MaxConsumedWatts": 399,
        "MinConsumedWatts": 393
    },
    "Voltage": [
        {
            "Name": "PS1 Voltage 1",
            "ReadingVolts": 208.0,
            "UpperThresholdCritical": null,
            "PhysicalContext": "PowerSupply",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "PS2 Voltage 2",
            "ReadingVolts": 208.0,
            "UpperThresholdCritical": null,
            "PhysicalContext": "PowerSupply",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board Pfault Fail Safe",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board DIMM VSHORT",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board PS1 PG FAIL",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board PS2 PG FAIL",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 MEMABCD VDD PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 MEMABCD VPP PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 MEMABCD VTT PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 MEMEFGH VDD PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 MEMEFGH VPP PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 MEMEFGH VTT PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 1P8 PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 ANA PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 VCCIN PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 VCCIO PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 VSA PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 FIVR PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 MEMABCD VDD PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 MEMABCD VPP PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 MEMABCD VTT PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 MEMEFGH VDD PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 MEMEFGH VPP PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 MEMEFGH VTT PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 1P8 PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 ANA PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 VCCIN PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 VCCIO PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 VSA PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 FIVR PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board BP0 PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board BP1 PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board BP3 PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board BP4 PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board 1V05 SW PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board 3.3V A PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board 5V SW PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board BMC SW PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board OCP1 PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board OCP1 HP SW PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board BATT PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "System Board PVNN SW PG",
            "ReadingVolts": null,
            "UpperThresholdCritical": null,
            "PhysicalContext": "SystemBoard",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 VCORE VR",
            "ReadingVolts": 1.79,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 VCORE VR",
            "ReadingVolts": 1.79,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 MEM0123 VR",
            "ReadingVolts": 1.22,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU1 MEM4567 VR",
            "ReadingVolts": 1.22,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 MEM0123 VR",
            "ReadingVolts": 1.22,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        },
        {
            "Name": "CPU2 MEM4567 VR",
            "ReadingVolts": 1.22,
            "UpperThresholdCritical": null,
            "PhysicalContext": "CPU",
            "State": "Enabled",
            "Health": "OK"
        }
    ],
    "PowerSupply": [
        {
            "Name": "PS1 Status",
            "Model": "PWR SPLY,1400W,RDNT,LTON",
            "SerialNumber": "CNLOD001262D5D",
            "PartNumber": "01CW9GA03",
            "SparePartNumber": "01CW9GA03",
            "Manufacturer": "DELL",
            "FirmwareVersion": "00.17.28",
            "State": "Enabled",
            "Health": "OK",
            "PowerSupplyType": "AC",
            "PowerOutputWatts": 363.0,
            "LastPowerOutputWatts": null,
            "PowerInputWatts": 393.0,
            "MaximumFrequencyHz": 35,
            "MaximumVoltage": 14,
            "MinimumFrequencyHz": 40,
            "MinimumVoltage": 132,
            "OutputWattage": 1400
        },
        {
            "Name": "PS2 Status",
            "Model": "PWR SPLY,1400W,RDNT,LTON",
            "SerialNumber": "CNLOD001262DF2",
            "PartNumber": "01CW9GA03",
            "SparePartNumber": "01CW9GA03",
            "Manufacturer": "DELL",
            "FirmwareVersion": "00.17.28",
            "State": "Enabled",
            "Health": "OK",
            "PowerSupplyType": "AC",
            "PowerOutputWatts": 0.0,
            "LastPowerOutputWatts": null,
            "PowerInputWatts": 5.0,
            "MaximumFrequencyHz": 35,
            "MaximumVoltage": 14,
            "MinimumFrequencyHz": 40,
            "MinimumVoltage": 132,
            "OutputWattage": 1400
        }
    ]
}
```
