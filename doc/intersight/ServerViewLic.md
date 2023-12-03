# Intersight Server

## lic view

```
# iserver get server --group test -v lic

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


License [#8]
------------

+--------------------------------+-----------+
| Server                         | License   |
+--------------------------------+-----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Advantage | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Advantage | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Advantage | 
| comp3-p4b-eu-spdc-WZP262207UM  | Advantage | 
| FI-ucsb1-eu-spdc-2-1           | Advantage | 
| FI-ucsb1-eu-spdc-2-2           | Advantage | 
| FI-ucsb1-eu-spdc-2-3           | Advantage | 
| FI-ucsb1-eu-spdc-2-4           | Advantage | 
+--------------------------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v lic

{
    "duration": 8256,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6411
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
        "lines": 15
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:25:42.629677	True	2888	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:25:44.440929	True	1808	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:25:46.228699	True	1715	12	isctl get compute blade   -o json --top 100
```

[[Back]](./ServerInventory.md)