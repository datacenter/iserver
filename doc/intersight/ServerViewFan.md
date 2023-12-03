# Intersight Server

## fan view

```
# iserver get server --group test -v fan

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Fan Module [#29]
----------------

+--------------------------------+-------+--------------+-----------+----------+
| Server                         | State | Fan Module   | OperState | Presence |
+--------------------------------+-------+--------------+-----------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 3 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 4 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 5 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 6 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | Fan Module 7 | unknown   | missing  | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 3 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 4 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 5 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 6 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | Fan Module 7 | unknown   | missing  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 3 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 4 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 5 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 6 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | Fan Module 7 | unknown   | missing  | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 3 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 4 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 5 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 6 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 7 | unknown   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 8 | unknown   | equipped | 
+--------------------------------+-------+--------------+-----------+----------+

Fan [#58]
---------

+--------------------------------+-------+----------------------+-----------+----------+
| Server                         | State | Fan                  | OperState | Presence |
+--------------------------------+-------+----------------------+-----------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 1 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 1 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 2 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 2 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 3 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 3 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 4 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 4 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 5 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 5 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 6 - Fan 1 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | V     | Fan Module 6 - Fan 2 | operable  | equipped | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | Fan Module 7 - Fan 1 | unknown   | missing  | 
| comp-1-p2b-eu-spdc-WZP23400AJW | X     | Fan Module 7 - Fan 2 | unknown   | missing  | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 1 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 1 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 2 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 2 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 3 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 3 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 4 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 4 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 5 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 5 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 6 - Fan 1 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | V     | Fan Module 6 - Fan 2 | operable  | equipped | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | Fan Module 7 - Fan 1 | unknown   | missing  | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | X     | Fan Module 7 - Fan 2 | unknown   | missing  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 1 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 1 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 2 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 2 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 3 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 3 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 4 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 4 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 5 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 5 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 6 - Fan 1 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | V     | Fan Module 6 - Fan 2 | operable  | equipped | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | Fan Module 7 - Fan 1 | unknown   | missing  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | X     | Fan Module 7 - Fan 2 | unknown   | missing  | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 1 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 1 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 2 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 2 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 3 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 3 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 4 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 4 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 5 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 5 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 6 - Fan 1 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | V     | Fan Module 6 - Fan 2 | operable  | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 7 - Fan 1 | unknown   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 7 - Fan 2 | unknown   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 8 - Fan 1 | unknown   | equipped | 
| comp3-p4b-eu-spdc-WZP262207UM  | X     | Fan Module 8 - Fan 2 | unknown   | equipped | 
+--------------------------------+-------+----------------------+-----------+----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v fan

{
    "duration": 11140,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 9465
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
        "lines": 25
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:21:47.621186	True	3893	100	isctl get compute rackunit  --expand "Fanmodules" -o json --top 100
2023-12-03 15:21:49.126162	True	1501	9	isctl get compute rackunit  --expand "Fanmodules" -o json --top 100 --skip 100
2023-12-03 15:21:50.698111	True	1415	12	isctl get compute blade   -o json --top 100
2023-12-03 15:21:52.090056	True	1358	40	isctl get equipment fan --filter "Parent/Moid in ('5fdf9c106176752d35e44d71', '5fdf9c106176752d35e44d73', '5fdf9c106176752d35e44d75', '5fdf9c106176752d35e44d77', '5fdf9c106176752d35e44d79', '5fdf9c106176752d35e44d7b', '5fdf9c106176752d35e44d7d', '5fdf9c876176752d35e4777c', '5fdf9c876176752d35e4777e', '5fdf9c876176752d35e47780', '5fdf9c876176752d35e47782', '5fdf9c876176752d35e47784', '5fdf9c876176752d35e47786', '5fdf9c876176752d35e47788', '5fdf9d116176752d35e4b355', '5fdf9d116176752d35e4b357', '5fdf9d116176752d35e4b359', '5fdf9d116176752d35e4b35b', '5fdf9d116176752d35e4b35d', '5fdf9d116176752d35e4b35f')"  -o json --top 100
2023-12-03 15:21:53.400245	True	1298	18	isctl get equipment fan --filter "Parent/Moid in ('5fdf9d116176752d35e4b361', '638501f176752d313964c5c6', '638501f176752d313964c5c8', '638501f176752d313964c5ca', '638501f176752d313964c5cc', '638501f176752d313964c5ce', '638501f176752d313964c5d0', '638501f176752d313964c5d2', '638501f176752d313964c5d4')"  -o json --top 100
```

[[Back]](./ServerInventory.md)