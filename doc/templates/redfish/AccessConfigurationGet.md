# Get Redfish Access Configuration

- get all configured redfish endpoints access details
- use supported filtering options for subset of configured endpoints
- use verify flag to check Redfish authentication

## Example

```
# iserver get redfish access --ip 10.58.50.0/24

+-------------+----------------+--------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
| S/N         | Product        | Name                           | Type | IP          | Port | Username | Password | FI Inventory Type | FI Inventory ID |
+-------------+----------------+--------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
| WZP23440N1P | UCSC-C220-M5SX | esx21-eu-spdc-WZP23440N1P      | ucsc | 10.58.50.38 | 443  | admin    | ******   |                   |                 |
| WZP2343171Y | UCSC-C220-M5SX | esx22-eu-spdc-WZP2343171Y      | ucsc | 10.58.50.39 | 443  | admin    | ******   |                   |                 |
| WMP24040053 | UCSC-C220-M5SX | esx20-eu-spdc-WMP24040053      | ucsc | 10.58.50.40 | 443  | admin    | ******   |                   |                 |
| WZP23400AJW | UCSC-C240-M5SN | comp-1-p2b-eu-spdc-WZP23400AJW | ucsc | 10.58.50.41 | 443  | admin    | ******   |                   |                 |
| WZP23400AK4 | UCSC-C240-M5SN | comp-2-p2b-eu-spdc-WZP23400AK4 | ucsc | 10.58.50.42 | 443  | admin    | ******   |                   |                 |
| WZP23400AKL | UCSC-C240-M5SN | comp-3-p2b-eu-spdc-WZP23400AKL | ucsc | 10.58.50.43 | 443  | admin    | ******   |                   |                 |
| WMP240400FM | UCSC-C220-M5SX | comp-4-p2b-eu-spdc-WMP240400FM | ucsc | 10.58.50.44 | 443  | admin    | ******   |                   |                 |
| WMP2404000R | UCSC-C220-M5SX | comp-5-p2b-eu-spdc-WMP2404000R | ucsc | 10.58.50.45 | 443  | admin    | ******   |                   |                 |
| WMP24040059 | UCSC-C220-M5SX | comp-6-p2b-eu-spdc-WMP24040059 | ucsc | 10.58.50.46 | 443  | admin    | ******   |                   |                 |
| WMP24040061 | UCSC-C220-M5SX | comp-7-p2b-eu-spdc-WMP24040061 | ucsc | 10.58.50.47 | 443  | admin    | ******   |                   |                 |
| FCH2017V1J7 | UCS C240 M4SX  | comp1-p3b-eu-spdc-FCH2017V1J7  | ucsc | 10.58.50.48 | 443  | admin    | ******   |                   |                 |
| WZP23450C8K | UCSC-C240-M5SX | aio3-p5g-eu-spdc-WZP23450C8K   | ucsc | 10.58.50.51 | 443  | admin    | ******   |                   |                 |
| FCH2017V24J | UCS C220 M4S   | comp6-p3b-eu-spdc-FCH2017V24J  | ucsc | 10.58.50.59 | 443  | admin    | ******   |                   |                 |
| FCH2023V2A4 | UCS C220 M4S   | comp7-p3b-eu-spdc-FCH2023V2A4  | ucsc | 10.58.50.60 | 443  | admin    | ******   |                   |                 |
+-------------+----------------+--------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
```