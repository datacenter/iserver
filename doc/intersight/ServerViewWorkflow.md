# Intersight Server

## workflow view

```
# iserver get server --group test --days 100 -v workflow

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Workflow [#15]
--------------

+--------------------------------+--------------------------+-----------------------+--------------------------+-----------+----------+
| Server                         | Workflow Moid            | Name                  | Create Time              | Status    | Duration |
+--------------------------------+--------------------------+-----------------------+--------------------------+-----------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | 655227ff696f6e3001621c1d | Turn On Locator       | 2023-11-13T13:43:27.581Z | COMPLETED | 00:00:03 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 6529844a696f6e300147c320 | Deploy Server Profile | 2023-10-13T17:54:18.661Z | COMPLETED | 00:00:20 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 6529840f696f6e300147c0ec | Deploy Server Profile | 2023-10-13T17:53:19.913Z | COMPLETED | 00:00:18 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 6529833f696f6e300147b9e8 | Deploy Server Profile | 2023-10-13T17:49:51.296Z | COMPLETED | 00:01:02 | 
| comp-1-p2b-eu-spdc-WZP23400AJW | 65297f7c696f6e300147afc1 | Deploy Server Profile | 2023-10-13T17:33:48.336Z | FAILED    | 00:00:01 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 656a0d0c696f6e3001d47374 | Deploy Server Profile | 2023-12-01T16:42:52.453Z | COMPLETED | 00:02:23 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 656a0cbb696f6e3001d47265 | Power Cycle           | 2023-12-01T16:41:31.92Z  | COMPLETED | 00:00:05 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 656a0b9e696f6e3001d46b19 | Power On              | 2023-12-01T16:36:46.865Z | COMPLETED | 00:00:07 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 656a021e696f6e3001d4159e | Deploy Server Profile | 2023-12-01T15:56:14.597Z | COMPLETED | 00:23:45 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 65453d01696f6e3001157e79 | Deploy Server Profile | 2023-11-03T18:33:37.562Z | FAILED    | 00:00:03 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 65453cf1696f6e3001157cb8 | Power On              | 2023-11-03T18:33:21.877Z | COMPLETED | 00:00:06 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 65453b00696f6e3001156cb2 | Deploy Server Profile | 2023-11-03T18:25:04.075Z | FAILED    | 00:00:03 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 6543c902696f6e3001839869 | Deploy Server Profile | 2023-11-02T16:06:26.938Z | FAILED    | 00:00:07 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 6543c61d696f6e3001837722 | Deploy Server Profile | 2023-11-02T15:54:05.811Z | FAILED    | 00:00:07 | 
| comp3-p4b-eu-spdc-WZP262207UM  | 6543c24b696f6e300183403e | Deploy Server Profile | 2023-11-02T15:37:47.506Z | COMPLETED | 00:02:04 | 
+--------------------------------+--------------------------+-----------------------+--------------------------+-----------+----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test --days 100 -v workflow

{
    "duration": 14726,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 12577
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

2023-12-03 15:30:08.430844	True	2376	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:30:10.247650	True	1812	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:30:12.205373	True	1899	12	isctl get compute blade   -o json --top 100
2023-12-03 15:30:14.490248	True	2254	100	isctl get workflow workflowinfo --filter "CreateTime gt 2023-08-25T16:30:12.000Z"  -o json --top 100
2023-12-03 15:30:16.804729	True	2196	100	isctl get workflow workflowinfo --filter "CreateTime gt 2023-08-25T16:30:12.000Z"  -o json --top 100 --skip 100
2023-12-03 15:30:18.924492	True	2040	91	isctl get workflow workflowinfo --filter "CreateTime gt 2023-08-25T16:30:12.000Z"  -o json --top 100 --skip 200
```

[[Back]](./ServerInventory.md)