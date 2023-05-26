# Redfish Access Configuration - Fabric Interconnect attached servers

- servers and chassis connected to Fabric Interconnect and discovered via Redfish
- all FI connected devices are added to configuration database upon successful Redfish access verification
- Redfish endpoint type enforced to [fi](./EndpointFi.md)

## Example

```
# iserver set redfish access fi --ip 10.90.90.13 --username admin --password ********

Redfish authentication successful


+----------------+------------+---------------------+---------------------+--------------+---------------+----------------+
| Inventory Type | Chassis Id | Inventory Id (IOM1) | Inventory Id (IOM2) | Chassis Name | Chassis Model | Chassis Serial |
+----------------+------------+---------------------+---------------------+--------------+---------------+----------------+
| Chassis        | chassis-1  | ucsX-1-1            | ucsX-1-2            | ucsX-1       | UCSX-9508     | FOX2611PPHP    |
| Chassis        | chassis-2  | ucsX-2-1            | ucsX-2-2            | ucsX-2       | UCSX-9508     | FOX2615P18G    |
+----------------+------------+---------------------+---------------------+--------------+---------------+----------------+

+----------------+--------------+-------------+----------------+---------------+
| Inventory Type | Inventory Id | Chassis Id  | Server Model   | Server Serial |
+----------------+--------------+-------------+----------------+---------------+
| Server         | ucsX-1-1     | chassis-1   | UCSX-210C-M6   | FCH26167MMZ   |
| Server         | ucsX-1-2     | chassis-1   | UCSX-210C-M6   | FCH26167L94   |
| Server         | ucsX-1-3     | chassis-1   | UCSX-210C-M6   | FCH26167MQK   |
| Server         | ucsX-1-4     | chassis-1   | UCSX-210C-M6   | FCH26167MHB   |
| Server         | ucsX-2-1     | chassis-2   | UCSX-210C-M6   | FCH262373DD   |
| Server         | ucsX-2-2     | chassis-2   | UCSX-210C-M6   | FCH262373D7   |
| Server         | ucsX-2-3     | chassis-2   | UCSX-210C-M6   | FCH2623746B   |
| Server         | ucsX-1       | rack-unit-1 | UCSC-C245-M6SX | WZP26360D3N   |
| Server         | ucsX-2       | rack-unit-2 | UCSC-C245-M6SX | WZP26360D2S   |
| Server         | ucsX-3       | rack-unit-3 | UCSC-C245-M6SX | WZP26370B3V   |
| Server         | ucsX-4       | rack-unit-4 | UCSC-C245-M6SX | WZP26360D2P   |
| Server         | ucsX-5       | rack-unit-5 | UCSC-C245-M6SX | WZP26360D40   |
| Server         | ucsX-6       | rack-unit-6 | UCSC-C245-M6SX | WZP26360D2T   |
+----------------+--------------+-------------+----------------+---------------+

Continue [Y/N]? y
Chassis |################################| 2/2
Server |################################| 14/14
All FI-attached redfish endpoints settings saved
```
