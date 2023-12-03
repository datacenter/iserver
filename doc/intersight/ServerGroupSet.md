# Intersight Server

## Create servers group

```
# iserver get server --serial WZP23400AJW --serial WZP23400AK4 --set self-test

iaccount isctl (cache: off)
Select servers...
Selected servers: 2
Collect server api objects...


Server Summary [#2]
-------------------

+------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Tag         | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | comp-1-p2b-eu-spdc-WZP23400AJW | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
| P+ H | CRi | comp-2-p2b-eu-spdc-WZP23400AK4 | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 
+------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+
Group configured with selected servers: self-test
```
