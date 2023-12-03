# Intersight Server

## contract view

```
# iserver get server --group test -v contract

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Contract [#8]
-------------

+--------------------------------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+
| Server                         | Contract Status | Start Date           | End Date             | Last Updated             | Service Description                                          | Purchase Order Number | Sales Order Number |
+--------------------------------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-02T11:39:03.345Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | 6710008753            | 110208990          | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-02T10:29:21.56Z  | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | 6710008753            | 110208990          | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-02T23:39:15.269Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | 6710008753            | 110208990          | 
| comp3-p4b-eu-spdc-WZP262207UM  | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-02T18:48:58.573Z | UCS C225 M6 Rack w/o CPU, mem, drv, 1U wSFF 10HDD backplane  | PR616717              | 114132936          | 
| FI-ucsb1-eu-spdc-2-1           | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-03T02:08:58.181Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | 6710008742            | 110341108          | 
| FI-ucsb1-eu-spdc-2-2           | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-03T02:08:58.181Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | 6710008742            | 110341108          | 
| FI-ucsb1-eu-spdc-2-3           | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-03T02:08:58.181Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | 6710008742            | 110341108          | 
| FI-ucsb1-eu-spdc-2-4           | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-03T02:08:58.181Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | 6710008742            | 110341108          | 
+--------------------------------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v contract

{
    "duration": 8616,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 7085
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
        "lines": 24
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:20:50.020824	True	2239	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:20:51.582192	True	1560	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:20:53.073520	True	1427	12	isctl get compute blade   -o json --top 100
2023-12-03 15:20:54.958862	True	1859	8	isctl get asset devicecontractinformation --filter "DeviceId in ('WZP23400AJW', 'WZP23400AK4', 'WZP23400AKL', 'WZP262207UM', 'FLM24140BJB', 'FLM24140B0B', 'FLM241501FB', 'FLM241501CT')"  -o json --top 100
```

[[Back]](./ServerInventory.md)