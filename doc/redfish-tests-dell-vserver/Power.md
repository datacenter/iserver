# Redfish Template Power

Vendor | Model
--- | ---
Dell | vServer

```
# iserver get redfish endpoint
    --cache dell-poweredge-r650-ygfcbtjso8womr-5.10.00.00-on
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