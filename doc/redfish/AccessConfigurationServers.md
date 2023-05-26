# Redfish Access Configuration - Standalone Servers

- servers in Intersight inventory selected using group name, IP address or subnet, name (loose match) or model (loose match)
- Redfish API enabled via management interface discovered via Intersight API
- option to define Redfish endpoint IP address and port (useful for redfish emulated servers)
- IPv4-only
- Redfish access is verified for every select servers
- configuration entry is added only upon successfull authentication

## Example: IP address based selection

```
# iserver set redfish access servers --ip 10.58.50.41 --type ucsc --username admin --password ********
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | Cri |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
Continue [Y/N]?
Server |################################| 1/1
```

## Example: IP subnet based selection

Note: some servers in the subnet have different Redfish credentials or Redfish disabled

```
# iserver.py set redfish access servers --ip 10.58.50.0/24 --type ucsc --username admin --password ********
|
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H    | Cri |    | aio3-p5g-eu-spdc-WZP23450C8K   | (R) UCSC-C240-M5SX | WZP23450C8K | 10.58.50.51 | 2S 48C 96T | 384 [GiB] |
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cri |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] |
| P- H    | Cri |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43 | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cri |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cri |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cri |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cri |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] |
| P- H    | Cri |    | comp1-p3b-eu-spdc-FCH2017V1J7  | (R) UCSC-C240-M4SX | FCH2017V1J7 | 10.58.50.48 | 2S 16C 32T | 128 [GiB] |
| P- H    | Cri |    | comp2-p3b-eu-spdc-FCH2017V1J8  | (R) UCSC-C240-M4SX | FCH2017V1J8 | 10.58.50.49 | 2S 16C 32T | 128 [GiB] |
| P- H    | Cri |    | comp3-p3b-eu-spdc-FCH2017V1J5  | (R) UCSC-C240-M4SX | FCH2017V1J5 | 10.58.50.50 | 2S 16C 32T | 128 [GiB] |
| P- H    | Cri |    | comp4-p3b-eu-spdc-FCH2108V1FC  | (R) UCSC-C220-M4S  | FCH2108V1FC | 10.58.50.57 | 2S 28C 56T | 256 [GiB] |
| P- H    | Cri |    | comp5-p3b-eu-spdc-FCH2017V1Y6  | (R) UCSC-C220-M4S  | FCH2017V1Y6 | 10.58.50.58 | 2S 28C 56T | 256 [GiB] |
| P- H    | Cri |    | comp6-p3b-eu-spdc-FCH2017V24J  | (R) UCSC-C220-M4S  | FCH2017V24J | 10.58.50.59 | 2S 28C 56T | 256 [GiB] |
| P+ C(1) | Cri |    | comp7-p3b-eu-spdc-FCH2023V2A4  | (R) UCSC-C220-M4S  | FCH2023V2A4 | 10.58.50.60 | 2S 28C 56T | 256 [GiB] |
| P+ H    | Cri |    | esx20-eu-spdc-WMP24040053      | (R) UCSC-C220-M5SX | WMP24040053 | 10.58.50.40 | 2S 40C 80T | 384 [GiB] |
| P+ H    | Cri |    | esx21-eu-spdc-WZP23440N1P      | (R) UCSC-C220-M5SX | WZP23440N1P | 10.58.50.38 | 2S 48C 96T | 512 [GiB] |
| P- H    | Cri |    | esx22-eu-spdc-WZP2343171Y      | (R) UCSC-C220-M5SX | WZP2343171Y | 10.58.50.39 | 2S 48C 96T | 512 [GiB] |
+---------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
Continue [Y/N]?
Server |################################| 18/18
[ERROR] Not all redfish endpoints settings saved
- comp2-p3b-eu-spdc-FCH2017V1J8: Redfish authentication failed
- comp3-p3b-eu-spdc-FCH2017V1J5: Redfish authentication failed
- comp4-p3b-eu-spdc-FCH2108V1FC: Redfish authentication failed
- comp5-p3b-eu-spdc-FCH2017V1Y6: Redfish authentication failed
```

## Example: multiple filtering criteria

```
# iserver set redfish access servers --ip 10.58.50.0/24 --name comp --model m5sx --type ucsc --username admin --password ********
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44 | 2S 40C 80T | 384 [GiB] |
| P+ H | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] |
| P+ H | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46 | 2S 40C 80T | 384 [GiB] |
| P+ H | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47 | 2S 40C 80T | 384 [GiB] |
+------+-----+----+--------------------------------+--------------------+-------------+-------------+------------+-----------+
Continue [Y/N]?
Server |################################| 4/4
```