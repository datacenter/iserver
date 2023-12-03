# Intersight Server

## Filter by cpu

Use --cpu option to select servers based on CPU cores count. Supported values by example:
- "--cpu 28" will select servers with 28 CPU cores
- "--cpu gt28" will select servers with >28 CPU cores
- "--cpu ge28" will select servers with >=28 CPU cores
- "--cpu le28" will select servers with <=28 CPU cores
- "--cpu lt28" will select servers with <28 CPU cores
- "--cpu ne28" will select servers with !=28 CPU cores

Equal

```
# iserver get server --cpu 40

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#23]
--------------------

+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| SF      | MF  | Name                           | Tag          | Model              | Serial      | IP            | CPU        | Memory    |
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ W(2) | Cri |  C220-WZP23350ZAQ              | psirt:manual | (R) UCSC-C220-M5SX | WZP23350ZAQ | 10.58.244.186 | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cri |  C220-WZP23360FH9              | psirt:manual | (R) UCSC-C220-M5SX | WZP23360FH9 | 10.58.244.70  | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cri | C220-231                       | psirt:manual | (R) UCSC-C220-M5SX | WZP23240NNZ | 10.58.250.241 | 2S 40C 80T | 352 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | CRi | comp-1-p2b-eu-spdc-WZP23400AJW | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | CRi | comp-2-p2b-eu-spdc-WZP23400AK4 | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H L  | CRi | comp-3-p2b-eu-spdc-WZP23400AKL | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AKL | 10.58.50.43   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H L  | CRi | comp-4-p2b-eu-spdc-WMP240400FM | psirt:ready  | (R) UCSC-C220-M5SX | WMP240400FM | 10.58.50.44   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | CRi | comp-5-p2b-eu-spdc-WMP2404000R | User:vanniew | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45   | 2S 40C 80T | 384 [GiB] | 
|         |     |                                | psirt:ready  |                    |             |               |            |           | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | CRi | comp-6-p2b-eu-spdc-WMP24040059 | psirt:ready  | (R) UCSC-C220-M5SX | WMP24040059 | 10.58.50.46   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H L  | CRi | comp-7-p2b-eu-spdc-WMP24040061 | psirt:ready  | (R) UCSC-C220-M5SX | WMP24040061 | 10.58.50.47   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | CRi | comp1-p4A-eu-spdc              | psirt:ready  | (R) UCSC-C220-M5SX | WMP24040045 | 10.58.29.54   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | CRi | esx20-eu-spdc-WMP24040053      | psirt:ready  | (R) UCSC-C220-M5SX | WMP24040053 | 10.58.50.40   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cu  | FI-ucsb1-eu-spdc-2-1           |              | (B) UCSB-B200-M5   | FLM241501FB | 10.58.52.41   | 2S 40C 80T | 512 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cu  | FI-ucsb1-eu-spdc-2-2           |              | (B) UCSB-B200-M5   | FLM24140BJB | 10.58.52.42   | 2S 40C 80T | 512 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cu  | FI-ucsb1-eu-spdc-2-3           |              | (B) UCSB-B200-M5   | FLM241501CT | 10.58.52.43   | 2S 40C 80T | 512 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cu  | FI-ucsb1-eu-spdc-2-4           |              | (B) UCSB-B200-M5   | FLM24140B0B | 10.58.52.44   | 2S 40C 80T | 512 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cri | NX1-S1-eu-spdc-WZP24100SMV     |              | (R) HXAF220C-M5SN  | WZP24100SMV | 10.58.50.51   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cri | NX1-S2-eu-spdc-WZP24100SN0     |              | (R) HXAF220C-M5SN  | WZP24100SN0 | 10.58.50.52   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cri | NX1-S3-eu-spdc-WZP24100SML     |              | (R) HXAF220C-M5SN  | WZP24100SML | 10.58.50.53   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | Cri | NX1-S4-eu-spdc-WZP24100SMP     |              | (R) HXAF220C-M5SN  | WZP24100SMP | 10.58.50.54   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ C(1) | CRi | POD-4A-AIO-1-WZP23400AK9       | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AK9 | 10.58.29.55   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | CRi | POD-4A-AIO-2-WZP23400AK7       | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AK7 | 10.58.29.56   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+
| P+ H    | CRi | POD-4A-AIO-3-WZP23400AM2       | psirt:ready  | (R) UCSC-C240-M5SN | WZP23400AM2 | 10.58.29.57   | 2S 40C 80T | 384 [GiB] | 
+---------+-----+--------------------------------+--------------+--------------------+-------------+---------------+------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Lower or Equal

```
# iserver get server --cpu 30

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#0]
-------------------
None

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Greater or Equal

```
# iserver get server --cpu 100

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#0]
-------------------
None

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --cpu 40

{
    "duration": 18783,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 8011
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
        "lines": 589
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:10:58.222532	True	3933	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:11:00.206773	True	1980	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:11:02.406679	True	2098	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)