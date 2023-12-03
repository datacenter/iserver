# Intersight Server

## Filter by fan

```
# iserver get server --fan

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
# iserver get server --fan

{
    "duration": 14229,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6126
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
        "lines": 612
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:12:20.347960	True	3041	100	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100
2023-12-03 15:12:21.825206	True	1474	9	isctl get compute rackunit  --expand "LocatorLed,RegisteredDevice" -o json --top 100 --skip 100
2023-12-03 15:12:23.546320	True	1611	12	isctl get compute blade  --expand "LocatorLed,RegisteredDevice" -o json --top 100
```

[[Back]](./ServerInventory.md)