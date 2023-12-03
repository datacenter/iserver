# Intersight Server

## net view

```
# iserver get server --group test -v net

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Network Adapters [#0]
---------------------
None

External Ethernet (MLOM) [#50]
------------------------------

+----------------------+-------------------------------------------+--------------+-------------------+
| Server               | Adapter Dn                                | Interface ID | MAC Address       |
+----------------------+-------------------------------------------+--------------+-------------------+
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-1/ext-eth-1 | 1            | 3c:57:31:a0:e1:94 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-1/ext-eth-3 | 3            | 3c:57:31:a0:e1:97 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-1/ext-eth-5 | 5            | 3c:57:31:a0:e1:95 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-1/ext-eth-7 | 7            | 3c:57:31:a0:e1:9a | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-2/ext-eth-1 | 1            | 3c:57:31:35:bd:18 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-2/ext-eth-3 | 3            | 3c:57:31:35:bd:1b | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-2/ext-eth-5 | 5            | 3c:57:31:35:bd:19 | 
| FI-ucsb1-eu-spdc-2-4 | sys/chassis-2/blade-4/adaptor-2/ext-eth-7 | 7            | 3c:57:31:35:bd:1e | 
+----------------------+-------------------------------------------+--------------+-------------------+

Host Ethernet [#76]
-------------------

+--------------------------------+--------------+----------------+-------------------+
| Server                         | Adapter Name | Interface Name | MAC Address       |
+--------------------------------+--------------+----------------+-------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter 3    | eth-1          | 3c:fd:fe:ee:2c:30 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter 3    | eth-2          | 3c:fd:fe:ee:2c:31 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter 6    | eth-1          | 3c:fd:fe:ee:2d:60 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter 6    | eth-2          | 3c:fd:fe:ee:2d:61 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter L    | eth-1          | 5c:71:0d:26:37:b2 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter L    | eth-2          | 5c:71:0d:26:37:b3 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | eth0           | 3C:57:31:CC:0E:46 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | eth1           | 3C:57:31:CC:0E:47 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | eth2           | 3C:57:31:CC:0E:48 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | eth3           | 3C:57:31:CC:0E:49 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter 3    | eth-1          | 3c:fd:fe:ee:2a:4c | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter 3    | eth-2          | 3c:fd:fe:ee:2a:4d | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter 6    | eth-1          | 3c:fd:fe:ee:2d:24 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter 6    | eth-2          | 3c:fd:fe:ee:2d:25 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter L    | eth-1          | 5c:71:0d:26:2b:d2 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter L    | eth-2          | 5c:71:0d:26:2b:d3 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | eth0           | 3C:57:31:CC:14:0A | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | eth1           | 3C:57:31:CC:14:0B | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | eth2           | 3C:57:31:CC:14:0C | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | eth3           | 3C:57:31:CC:14:0D | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter 3    | eth-1          | 3c:fd:fe:ee:2d:28 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter 3    | eth-2          | 3c:fd:fe:ee:2d:29 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter 6    | eth-1          | 3c:fd:fe:ee:2a:dc | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter 6    | eth-2          | 3c:fd:fe:ee:2a:dd | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter L    | eth-1          | 5c:71:0d:26:3b:fe | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter L    | eth-2          | 5c:71:0d:26:3b:ff | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | eth0           | 3C:57:31:CC:0E:6A | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | eth1           | 3C:57:31:CC:0E:6B | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | eth2           | 3C:57:31:CC:0E:6C | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | eth3           | 3C:57:31:CC:0E:6D | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | eth0           | 88:FC:5D:45:4E:BC | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | eth1           | 88:FC:5D:45:4E:BD | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | eth2           | 88:FC:5D:45:4E:BE | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | eth3           | 88:FC:5D:45:4E:BF | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | vic1-i0        | 88:FC:5D:45:4E:C6 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | vic1-i1        | 88:FC:5D:45:4E:C7 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | vic1-vs0       | 88:FC:5D:45:4E:C4 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | vic1-vs1       | 88:FC:5D:45:4E:C5 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | eth0           | 04:BD:97:23:32:90 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | eth1           | 04:BD:97:23:32:91 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | i0             | 04:BD:97:23:32:96 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | i1             | 04:BD:97:23:32:97 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | vs0            | 04:BD:97:23:32:94 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | vs1            | 04:BD:97:23:32:95 | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 1    | ESXi-vSwitch0  | 00:25:B5:00:00:04 | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 1    | EU-SPDC-CDC    | 00:25:B5:CD:03:4F | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 1    | EU-SPDC-CDC22  | 00:25:B5:C2:01:CF | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 1    | Infra_DVS      | 00:25:B5:AA:00:4F | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 2    | EU-SPDC-CDC66  | 00:25:B5:6C:01:DF | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 2    | EU-SPDC-R3DC   | 00:25:B5:3D:02:8F | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 2    | EU-SPDC-R4DC   | 00:25:B5:4D:00:DF | 
| FI-ucsb1-eu-spdc-2-1           | Adapter 2    | EU-SPDC-R7DC   | 00:25:B5:7D:03:BF | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 1    | ESXi-vSwitch0  | 00:25:B5:00:00:05 | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 1    | EU-SPDC-CDC    | 00:25:B5:CD:03:5F | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 1    | EU-SPDC-CDC22  | 00:25:B5:C2:01:AF | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 1    | Infra_DVS      | 00:25:B5:AA:00:5F | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 2    | EU-SPDC-CDC66  | 00:25:B5:6C:01:CF | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 2    | EU-SPDC-R3DC   | 00:25:B5:3D:02:9F | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 2    | EU-SPDC-R4DC   | 00:25:B5:4D:00:CF | 
| FI-ucsb1-eu-spdc-2-2           | Adapter 2    | EU-SPDC-R7DC   | 00:25:B5:7D:02:8F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 1    | ESXi-vSwitch0  | 00:25:B5:00:00:06 | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 1    | EU-SPDC-CDC    | 00:25:B5:CD:03:2F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 1    | EU-SPDC-CDC22  | 00:25:B5:C2:00:8F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 1    | Infra_DVS      | 00:25:B5:AA:00:2F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 2    | EU-SPDC-CDC66  | 00:25:B5:6C:01:AF | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 2    | EU-SPDC-R3DC   | 00:25:B5:3D:02:6F | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 2    | EU-SPDC-R4DC   | 00:25:B5:4D:00:AF | 
| FI-ucsb1-eu-spdc-2-3           | Adapter 2    | EU-SPDC-R7DC   | 00:25:B5:7D:02:9F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 1    | ESXi-vSwitch0  | 00:25:B5:00:00:07 | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 1    | EU-SPDC-CDC    | 00:25:B5:CD:03:3F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 1    | EU-SPDC-CDC22  | 00:25:B5:C2:00:9F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 1    | Infra_DVS      | 00:25:B5:AA:00:3F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 2    | EU-SPDC-CDC66  | 00:25:B5:6C:00:8F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 2    | EU-SPDC-R3DC   | 00:25:B5:3D:02:7F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 2    | EU-SPDC-R4DC   | 00:25:B5:4D:01:8F | 
| FI-ucsb1-eu-spdc-2-4           | Adapter 2    | EU-SPDC-R7DC   | 00:25:B5:7D:02:6F | 
+--------------------------------+--------------+----------------+-------------------+

Host FC [#18]
-------------

+--------------------------------+--------------+----------------+-------------------------+-------------------------+
| Server                         | Adapter Name | Interface Name | WWNN                    | WWPN                    |
+--------------------------------+--------------+----------------+-------------------------+-------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | fc0            | 10:00:3C:57:31:CC:0E:4A | 20:00:3C:57:31:CC:0E:4A | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | fc1            | 10:00:3C:57:31:CC:0E:4B | 20:00:3C:57:31:CC:0E:4B | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | fc2            | 10:00:3C:57:31:CC:0E:4C | 20:00:3C:57:31:CC:0E:4C | 
| comp-1-p2b-eu-spdc-WZP23400AJW | Adapter MLOM | fc3            | 10:00:3C:57:31:CC:0E:4D | 20:00:3C:57:31:CC:0E:4D | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | fc0            | 10:00:3C:57:31:CC:14:0E | 20:00:3C:57:31:CC:14:0E | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | fc1            | 10:00:3C:57:31:CC:14:0F | 20:00:3C:57:31:CC:14:0F | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | fc2            | 10:00:3C:57:31:CC:14:10 | 20:00:3C:57:31:CC:14:10 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Adapter MLOM | fc3            | 10:00:3C:57:31:CC:14:11 | 20:00:3C:57:31:CC:14:11 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | fc0            | 10:00:3C:57:31:CC:0E:6E | 20:00:3C:57:31:CC:0E:6E | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | fc1            | 10:00:3C:57:31:CC:0E:6F | 20:00:3C:57:31:CC:0E:6F | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | fc2            | 10:00:3C:57:31:CC:0E:70 | 20:00:3C:57:31:CC:0E:70 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Adapter MLOM | fc3            | 10:00:3C:57:31:CC:0E:71 | 20:00:3C:57:31:CC:0E:71 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | fc0            | 10:00:88:FC:5D:45:4E:C0 | 20:00:88:FC:5D:45:4E:C0 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | fc1            | 10:00:88:FC:5D:45:4E:C1 | 20:00:88:FC:5D:45:4E:C1 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | fc2            | 10:00:88:FC:5D:45:4E:C2 | 20:00:88:FC:5D:45:4E:C2 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter 1    | fc3            | 10:00:88:FC:5D:45:4E:C3 | 20:00:88:FC:5D:45:4E:C3 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | fc0            | 10:00:04:BD:97:23:32:92 | 20:00:04:BD:97:23:32:92 | 
| comp3-p4b-eu-spdc-WZP262207UM  | Adapter MLOM | fc1            | 10:00:04:BD:97:23:32:93 | 20:00:04:BD:97:23:32:93 | 
+--------------------------------+--------------+----------------+-------------------------+-------------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v net

{
    "duration": 14786,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 12475
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
        "lines": 49
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:26:28.362265	True	2735	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:26:32.312492	True	3947	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:26:34.432139	True	2024	12	isctl get compute blade   -o json --top 100
2023-12-03 15:26:36.503795	True	2021	20	isctl get adapter unit --filter "Moid in ('5fdf9bf46176752d35e4426e', '5fdf9c886176752d35e477e4', '5fdf9c886176752d35e477ea', '5fdf9c886176752d35e477f0', '5fdf9c6b6176752d35e46d1c', '5fdf9cfe6176752d35e4aa7f', '5fdf9cfe6176752d35e4aa85', '5fdf9cfe6176752d35e4aa8b', '5fdf9cf56176752d35e4a70f', '5fdf9d896176752d35e4e0b6', '5fdf9d896176752d35e4e0bc', '5fdf9d896176752d35e4e0c2', '6385018c76752d313964b35d', '6385018c76752d313964b35f', '6501db4c76752d3901eb3813', '6501db4c76752d3901eb3864', '6501db4c76752d3901eb381b', '6501db4d76752d3901eb3976', '6501db4e76752d3901eb3b32', '6501db4e76752d3901eb3b59')" --expand "ExtEthIfs,HostEthIfs,HostFcIfs" -o json --top 100
2023-12-03 15:26:38.281587	True	1748	2	isctl get adapter unit --filter "Moid in ('6501db4d76752d3901eb3972', '6501db4f76752d3901eb3c71')" --expand "ExtEthIfs,HostEthIfs,HostFcIfs" -o json --top 100
```

[[Back]](./ServerInventory.md)