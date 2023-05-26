# Check Redfish Access Configuration for Intersight Managed Servers

- select Intersight servers using supported filtering options i.e. group, IP address or subnet, name (loose match), serial, model (loose match)
- use verify flag to check Redfish authentication

## Example

```
# iserver get redfish servers --group p2b --verify
Progress |################################| 7/7

+--------------------------------+----------------+-------------+-------------+-----------------+----------------+------+-------------+------+----------+----------+----------------+--------------+---------------+
| Name                           | Model          | Serial      | IP          | Redfish Support | Redfish Access | Type | IP          | Port | Username | Password | Inventory Type | Inventory ID | Authenticated |
+--------------------------------+----------------+-------------+-------------+-----------------+----------------+------+-------------+------+----------+----------+----------------+--------------+---------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | True            | True           | ucsc | 10.58.50.41 | 443  | admin    | ******   |                |              | True          |
| comp-2-p2b-eu-spdc-WZP23400AK4 | UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | True            | True           | ucsc | 10.58.50.42 | 443  | admin    | ******   |                |              | True          |
| comp-3-p2b-eu-spdc-WZP23400AKL | UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | True            | True           | ucsc | 10.58.50.43 | 443  | admin    | ******   |                |              | True          |
| comp-4-p2b-eu-spdc-WMP240400FM | UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | True            | True           | ucsc | 10.58.50.44 | 443  | admin    | ******   |                |              | True          |
| comp-5-p2b-eu-spdc-WMP2404000R | UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | True            | True           | ucsc | 10.58.50.45 | 443  | admin    | ******   |                |              | True          |
| comp-6-p2b-eu-spdc-WMP24040059 | UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | True            | True           | ucsc | 10.58.50.46 | 443  | admin    | ******   |                |              | True          |
| comp-7-p2b-eu-spdc-WMP24040061 | UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | True            | True           | ucsc | 10.58.50.47 | 443  | admin    | ******   |                |              | True          |
+--------------------------------+----------------+-------------+-------------+-----------------+----------------+------+-------------+------+----------+----------+----------------+--------------+---------------+
```

## Example: summary information

Note: Redfish authentication verification increases command execution time

```
# iserver.py get redfish summary --verify
Progress |################################| 103/103

Intersight Servers - Redfish Access Summary
-------------------------------------------
- Servers Count            : 103
- Redfish Support          : 80
- Redfish Configured       : 14
- Redfish Access Verified  : 14
- Endpoint Type - standard : 0
- Endpoint Type - ucsc     : 14
- Endpoint Type - fi       : 0
- Endpoint Type - dell     : 0
- Endpoint Type - hpe      : 0
```