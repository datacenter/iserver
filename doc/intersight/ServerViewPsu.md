# Intersight Server

## Psu view

```
# iserver get server --group test -v psu

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


PSU [#8]
--------

+--------------------------------+--------+-------+---------+---------+---------------+-------------+-------------------+
| Server                         | Name   | State | Present | Voltage | Model         | Serial      | Vendor            |
+--------------------------------+--------+-------+---------+---------+---------------+-------------+-------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | LIT241244MU | Cisco Systems Inc | 
| comp-1-p2b-eu-spdc-WZP23400AJW | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | LIT241244Z5 | Cisco Systems Inc | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | LIT241244RQ | Cisco Systems Inc | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | LIT241242TS | Cisco Systems Inc | 
| comp-3-p2b-eu-spdc-WZP23400AKL | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | LIT241244NV | Cisco Systems Inc | 
| comp-3-p2b-eu-spdc-WZP23400AKL | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | LIT241244UN | Cisco Systems Inc | 
| comp3-p4b-eu-spdc-WZP262207UM  | PSU #1 | V     | V       | ok      | PS-2112-9S-LF | LIT2625AJTW | Cisco Systems Inc | 
| comp3-p4b-eu-spdc-WZP262207UM  | PSU #2 | V     | V       | ok      | PS-2112-9S-LF | LIT2625AHMD | Cisco Systems Inc | 
+--------------------------------+--------+-------+---------+---------+---------------+-------------+-------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v psu

{
    "duration": 8288,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 6425
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
        "lines": 23
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:27:56.579725	True	2969	100	isctl get compute rackunit  --expand "Psus" -o json --top 100
2023-12-03 15:27:58.447915	True	1861	9	isctl get compute rackunit  --expand "Psus" -o json --top 100 --skip 100
2023-12-03 15:28:00.128266	True	1595	12	isctl get compute blade   -o json --top 100
```

[[Back]](./ServerInventory.md)