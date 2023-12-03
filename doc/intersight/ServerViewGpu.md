# Intersight Server

## gpu view

```
# iserver get server --group test -v gpu

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


GPU [#1]
--------

+-------------------------------+-------------------------+----------------+--------+--------+----------+---------------------------------+
| Server                        | GPU Device Model        | Pid            | SlotId | Vendor | Firmware | Dn                              |
+-------------------------------+-------------------------+----------------+--------+--------+----------+---------------------------------+
| comp3-p4b-eu-spdc-WZP262207UM | NVIDIA T4 PCIe 16GB 70W | UCSC-GPU-T4-16 | 3      | 0x10de | N/A      | sys/rack-unit-1/equipped-slot-3 | 
+-------------------------------+-------------------------+----------------+--------+--------+----------+---------------------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v gpu

{
    "duration": 9265,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 7219
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
        "lines": 31
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:22:21.446408	True	3786	100	isctl get compute rackunit  --expand "PciDevices" -o json --top 100
2023-12-03 15:22:23.289654	True	1838	9	isctl get compute rackunit  --expand "PciDevices" -o json --top 100 --skip 100
2023-12-03 15:22:25.029821	True	1595	12	isctl get compute blade  --expand "PciDevices" -o json --top 100
```

[[Back]](./ServerInventory.md)