# Intersight Server

## connector view

```
# iserver get server --group test -v connector

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Connector [#8]
--------------

+--------------------------------+-------------------+-------------------+--------------------+--------------------------+-------------------------------+---------------+----------------------------+
| Server                         | Connection Status | Connector Version | Claimed By         | Claimed Time             | Connection Status Last Update | Platform Type | Device External IP Address |
+--------------------------------+-------------------+-------------------+--------------------+--------------------------+-------------------------------+---------------+----------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Connected         | 1.0.11-3136       | ttrabatt@cisco.com | 2020-12-20T18:46:00.104Z | 2023-12-01T05:12:39.272Z      | IMCM5         | 173.38.209.7               | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Connected         | 1.0.11-3136       | ttrabatt@cisco.com | 2020-12-20T18:48:08.061Z | 2023-12-01T20:29:26.594Z      | IMCM5         | 173.38.209.6               | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Connected         | 1.0.11-3136       | ttrabatt@cisco.com | 2020-12-20T18:50:26.206Z | 2023-12-01T22:41:35.389Z      | IMCM5         | 173.38.209.11              | 
| comp3-p4b-eu-spdc-WZP262207UM  | Connected         | 1.0.11-3273       | ttrabatt@cisco.com | 2022-11-28T18:44:17.856Z | 2023-12-03T00:26:24.649Z      | IMCRack       | 64.103.36.135              | 
| FI-ucsb1-eu-spdc-2-1           | Connected         | 1.0.11-4665       | ttrabatt@cisco.com | 2023-09-13T15:54:45.974Z | 2023-12-01T19:41:43.272Z      | UCSFI         | 10.0.169.80                | 
| FI-ucsb1-eu-spdc-2-2           | Connected         | 1.0.11-4665       | ttrabatt@cisco.com | 2023-09-13T15:54:45.974Z | 2023-12-01T19:41:43.272Z      | UCSFI         | 10.0.169.80                | 
| FI-ucsb1-eu-spdc-2-3           | Connected         | 1.0.11-4665       | ttrabatt@cisco.com | 2023-09-13T15:54:45.974Z | 2023-12-01T19:41:43.272Z      | UCSFI         | 10.0.169.80                | 
| FI-ucsb1-eu-spdc-2-4           | Connected         | 1.0.11-4665       | ttrabatt@cisco.com | 2023-09-13T15:54:45.974Z | 2023-12-01T19:41:43.272Z      | UCSFI         | 10.0.169.80                | 
+--------------------------------+-------------------+-------------------+--------------------+--------------------------+-------------------------------+---------------+----------------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v connector

{
    "duration": 8736,
    "isctl": {
        "read": true,
        "calls": 4,
        "success": 4,
        "failed": 0,
        "total_time": 7229
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

2023-12-03 15:20:35.745583	True	2381	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:20:37.321355	True	1573	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:20:38.938120	True	1559	12	isctl get compute blade   -o json --top 100
2023-12-03 15:20:40.679683	True	1716	5	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '638501816f72612d317dabd7', '6501db456f726131016b7aea', '6501db456f726131016b7aea', '6501db456f726131016b7aea', '6501db456f726131016b7aea')"  -o json --top 100
```

[[Back]](./ServerInventory.md)