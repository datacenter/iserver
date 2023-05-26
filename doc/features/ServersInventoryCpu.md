# Filter by CPU cores

Use --cpu option to select servers based on CPU cores count. Supported values by example:
- "--cpu 28" will select servers with 28 CPU cores
- "--cpu gt28" will select servers with >28 CPU cores
- "--cpu ge28" will select servers with >=28 CPU cores
- "--cpu le28" will select servers with <=28 CPU cores
- "--cpu lt28" will select servers with <28 CPU cores
- "--cpu ne28" will select servers with !=28 CPU cores

Add any extra filtering options following logical AND rule. Use -o|--output for desired output format.

## Equal

```
# iserver get servers --cpu 40

+---------+-----+----+--------------------------------+--------------------+-------------+---------------+------------+-----------+
| SF      | MF  | WF | Name                           | Model              | Serial      | IP            | CPU        | Memory    |
+---------+-----+----+--------------------------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cri |    |  C220-WZP23350ZAQ              | (R) UCSC-C220-M5SX | WZP23350ZAQ | 10.58.244.186 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri |    |  C220-WZP23360FH9              | (R) UCSC-C220-M5SX | WZP23360FH9 | 10.58.244.70  | 2S 40C 80T | 384 [GiB] | 
| P+ C(1) | Cri |    | C220-231                       | (R) UCSC-C220-M5SX | WZP23240NNZ | 10.58.250.241 | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-1           | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-2           | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-3           | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43   | 2S 40C 80T | 192 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-4           | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44   | 2S 40C 80T | 192 [GiB] | 
| P- C(2) | Cu  |    | HX1-eu-spdc-1                  | (R) HXAF220C-M5SN  | WZP24100SMV | 10.58.24.56   | 2S 40C 80T | 384 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-2                  | (R) HXAF220C-M5SN  | WZP24100SN0 | 10.58.24.55   | 2S 40C 80T | 384 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-3                  | (R) HXAF220C-M5SN  | WZP24100SML | 10.58.24.53   | 2S 40C 80T | 384 [GiB] | 
| P+ C(3) | Cu  |    | HX1-eu-spdc-4                  | (R) HXAF220C-M5SN  | WZP24100SMP | 10.58.24.57   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri |    | POD-4A-AIO-1-WZP23400AK9       | (R) UCSC-C240-M5SN | WZP23400AK9 | 10.58.29.55   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri |    | POD-4A-AIO-2-WZP23400AK7       | (R) UCSC-C240-M5SN | WZP23400AK7 | 10.58.29.56   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri |    | POD-4A-AIO-3-WZP23400AM2       | (R) UCSC-C240-M5SN | WZP23400AM2 | 10.58.29.57   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4 | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43   | 2S 40C 80T | 384 [GiB] | 
| P- H    | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44   | 2S 40C 80T | 384 [GiB] | 
| P- H    | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45   | 2S 40C 80T | 384 [GiB] | 
| P- H    | CRi |    | comp-6-p2b-eu-spdc-WMP24040059 | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | comp-7-p2b-eu-spdc-WMP24040061 | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | Cri |    | comp1-p4A-eu-spdc              | (R) UCSC-C220-M5SX | WMP24040045 | 10.58.29.54   | 2S 40C 80T | 384 [GiB] | 
| P+ H    | CRi |    | esx20-eu-spdc-WMP24040053      | (R) UCSC-C220-M5SX | WMP24040053 | 10.58.50.40   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+----+--------------------------------+--------------------+-------------+---------------+------------+-----------+
```

## Lower or Equal

```
# iserver get servers --cpu 30

+----+----+----+------+-------+--------+----+-----+--------+
| SF | MF | WF | Name | Model | Serial | IP | CPU | Memory |
+----+----+----+------+-------+--------+----+-----+--------+
+----+----+----+------+-------+--------+----+-----+--------+
```

## Greater or Equal

```
# iserver get servers --cpu 100

+----+----+----+------+-------+--------+----+-----+--------+
| SF | MF | WF | Name | Model | Serial | IP | CPU | Memory |
+----+----+----+------+-------+--------+----+-----+--------+
+----+----+----+------+-------+--------+----+-----+--------+
```
