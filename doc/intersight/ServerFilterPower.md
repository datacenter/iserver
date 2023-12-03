# Intersight Server

## Filter by power state

```
# iserver get server --power off

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#8]
-------------------

+---------+-----+-------------------------------+-------------+--------------------+-------------+---------------+-------------+-----------+
| SF      | MF  | Name                          | Tag         | Model              | Serial      | IP            | CPU         | Memory    |
+---------+-----+-------------------------------+-------------+--------------------+-------------+---------------+-------------+-----------+
| P- H    | CRi | aio3-p5g-eu-spdc-WZP23450C8K  | LAB-ID:DMZ  | (R) UCSC-C240-M5SX | WZP23450C8K | 10.58.29.44   | 2S 48C 96T  | 384 [GiB] | 
| P- H    | Cu  | berlin-ucsm-7                 |             | (R) UCSC-C240-M4S  | FCH1930V1LA | 10.49.234.205 | 2S 28C 56T  | 768 [GiB] | 
| P- C(1) | Cu  | berlin-ucsm-8                 |             | (R) UCSC-C220-M4S  | FCH1849V26H | 10.49.234.194 | 2S 24C 48T  | 256 [GiB] | 
| P- H    | CRi | comp1-p3c-eu-spdc-WZP26510CZ6 | psirt:ready | (R) UCSC-C240-M6SN | WZP26510CZ6 | 10.58.53.47   | 2S 64C 128T | 512 [GiB] | 
| P- H    | Cri | comp2-p1z-eu-spdc-WZP26510CZ9 | psirt:ready | (R) UCSC-C240-M6SN | WZP26510CZ9 | 10.58.26.162  | 2S 64C 128T | 512 [GiB] | 
| P- H    | CRi | comp2-p3c-eu-spdc-WZP26510CZC | psirt:ready | (R) UCSC-C240-M6SN | WZP26510CZC | 10.58.53.48   | 2S 64C 128T | 512 [GiB] | 
| P- H    | CRi | comp3-p3c-eu-spdc-WZP26510CZD | psirt:ready | (R) UCSC-C240-M6SN | WZP26510CZD | 10.58.53.49   | 2S 64C 128T | 512 [GiB] | 
| P- H    | Cri | wnas-eu-spdc-FCH2008V230      | psirt:ready | (R) UCSC-C240-M4SX | FCH2008V230 | 10.58.28.55   | 2S 16C 32T  | 128 [GiB] | 
+---------+-----+-------------------------------+-------------+--------------------+-------------+---------------+-------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --power off

{
    "duration": 14162,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6103
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
        "lines": 604
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:14:40.457225	True	2868	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:14:41.881188	True	1421	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:14:43.779687	True	1814	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)