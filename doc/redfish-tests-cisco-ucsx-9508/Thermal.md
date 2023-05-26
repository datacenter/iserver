# Redfish Template Thermal

Vendor | Model
--- | ---
Cisco | UCSX-9508

```
# iserver get redfish endpoint
    --cache chassis-UCSX-9508-fox2521p34m
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1
    --template thermal

+-----------------------------+----------+------------------+
| Name                        | State    | Value (Celcius)  |
+-----------------------------+----------+------------------+
| ASIC_INLET_TEMP             | Enabled  | 27               | 
| ASIC_OUTLET_TEMP            | Enabled  | 42               | 
| ASIC_TEMP_A                 | Enabled  | 50               | 
| ASIC_TEMP_B                 | Enabled  | 50               | 
| FAN1_HOTSWAP_TEMP           | Absent   |                  | 
| FAN2_HOTSWAP_TEMP           | Absent   |                  | 
| FAN3_HOTSWAP_TEMP           | Absent   |                  | 
| FAN4_HOTSWAP_TEMP           | Absent   |                  | 
| FEM1_HOTSWAP_TEMP           | Absent   |                  | 
| FEM1_INLET_TEMP             | Absent   |                  | 
| FEM2_HOTSWAP_TEMP           | Absent   |                  | 
| FEM2_INLET_TEMP             | Absent   |                  | 
| IFM_HOTSWAP_TEMP            | Enabled  | 18               | 
| IFM_INLET_TEMP              | Enabled  | 20               | 
| IFM_OUTLET_TEMP             | Enabled  | 44               | 
| P1_TEMP                     | Enabled  | 26               | 
| PEER_SLOT_FEM_HOTSWAP_TEMP  | Absent   |                  | 
| PEER_SLOT_FEM_INLET_TEMP    | Absent   |                  | 
| PS1_TEMP1                   | Absent   |                  | 
| PS1_TEMP2                   | Absent   |                  | 
| PS1_TEMP3                   | Absent   |                  | 
| PS2_TEMP1                   | Absent   |                  | 
| PS2_TEMP2                   | Absent   |                  | 
| PS2_TEMP3                   | Absent   |                  | 
| PS3_TEMP1                   | Absent   |                  | 
| PS3_TEMP2                   | Absent   |                  | 
| PS3_TEMP3                   | Absent   |                  | 
| PS4_TEMP1                   | Absent   |                  | 
| PS4_TEMP2                   | Absent   |                  | 
| PS4_TEMP3                   | Absent   |                  | 
| PS5_TEMP1                   | Absent   |                  | 
| PS5_TEMP2                   | Absent   |                  | 
| PS5_TEMP3                   | Absent   |                  | 
| PS6_TEMP1                   | Absent   |                  | 
| PS6_TEMP2                   | Absent   |                  | 
| PS6_TEMP3                   | Absent   |                  | 
| PWR_BRICK_TEMP1             | Enabled  | 40               | 
| PWR_BRICK_TEMP2             | Enabled  | 40               | 
+-----------------------------+----------+------------------+

+---------------------+----------+----------------+---------------+
| Name                | State    | Model          | SerialNumber  |
+---------------------+----------+----------------+---------------+
| Fan Module 1 Fan 1  | Enabled  | UCSX-9508-FAN  | FCH2517709V   | 
| Fan Module 1 Fan 2  | Enabled  | UCSX-9508-FAN  | FCH2517709V   | 
| Fan Module 2 Fan 1  | Enabled  | UCSX-9508-FAN  | FCH2517701J   | 
| Fan Module 2 Fan 2  | Enabled  | UCSX-9508-FAN  | FCH2517701J   | 
| Fan Module 3 Fan 1  | Enabled  | UCSX-9508-FAN  | FCH2517704C   | 
| Fan Module 3 Fan 2  | Enabled  | UCSX-9508-FAN  | FCH2517704C   | 
| Fan Module 4 Fan 1  | Enabled  | UCSX-9508-FAN  | FCH2517701L   | 
| Fan Module 4 Fan 2  | Enabled  | UCSX-9508-FAN  | FCH2517701L   | 
+---------------------+----------+----------------+---------------+
```