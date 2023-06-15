# Node Protocol - LACP

## Show LACP interfaces for all leaf nodes

```
# iserver get aci proto lacp --apic apic11 --role leaf --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+------+--------------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| Id   | Name                     | Admin State | Oper State | Interface | Oper Key | Nbr System MAC    | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State                           |
+------+--------------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| po1  | HX1-FI-A_PolGrp          | up          | up         | eth1/11   | 32769    | 00:3A:9C:C0:04:47 | 32768           | 200          | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| po2  | HX1-FI-B_PolGrp          | up          | up         | eth1/12   | 32770    | 00:3A:9C:C0:03:E7 | 32768           | 241          | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| po3  | SPN_PolGrp               | up          | up         | eth1/27   | 33112    | E0:0E:DA:A3:38:13 | 32768           | 1            | 337      | 32768         | active,aggregate,collect,distribute,sync | 
| po4  | UCSB1-FI-B_PolGrp        | up          | up         | eth1/2    | 33111    | 00:3A:9C:BD:8F:07 | 32768           | 15           | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| po5  | UCSB1-FI-A_PolGrp        | up          | up         | eth1/1    | 32771    | 00:3A:9C:BD:92:07 | 32768           | 14           | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| po1  | HX1-FI-B_PolGrp          | up          | up         | eth1/12   | 32770    | 00:3A:9C:C0:03:E7 | 32768           | 241          | 461      | 32768         | active,aggregate,collect,distribute,sync | 
| po2  | UCSB1-FI-B_PolGrp        | up          | up         | eth1/2    | 33111    | 00:3A:9C:BD:8F:07 | 32768           | 15           | 461      | 32768         | active,aggregate,collect,distribute,sync | 
| po3  | HX1-FI-A_PolGrp          | up          | up         | eth1/11   | 32769    | 00:3A:9C:C0:04:47 | 32768           | 200          | 461      | 32768         | active,aggregate,collect,distribute,sync | 
| po4  | UCSB1-FI-A_PolGrp        | up          | up         | eth1/1    | 32771    | 00:3A:9C:BD:92:07 | 32768           | 14           | 461      | 32768         | active,aggregate,collect,distribute,sync | 
| po5  | SPN_PolGrp               | up          | up         | eth1/27   | 33112    | E0:0E:DA:A3:38:13 | 32768           | 1            | 333      | 32768         | active,aggregate,collect,distribute,sync | 
| po1  | pod1a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/4    | 33456    | 3C:FD:FE:CB:F5:B0 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po2  | pod1a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/7    | 33121    | 3C:FD:FE:CE:16:40 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po3  | pod1a-NVBench_PolGrp     | up          | down       |           |          |                   |                 |              |          |               |                                          | 
| po4  | pod1a-COMP-2-PET_PolGrp  | up          | up         | eth1/14   | 33124    | 3C:FD:FE:CB:ED:71 | 65535           | 1            | 4        | 255           | active,aggregate,collect,distribute,sync | 
| po5  | pod1a-COMP-2-SAMX_PolGrp | up          | up         | eth1/13   | 32796    | 3C:FD:FE:CB:ED:70 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po6  | pod1a-AIO-2-PET_PolGrp   | up          | up         | eth1/5    | 32795    | 3C:FD:FE:CB:F5:B1 | 65535           | 1            | 4        | 255           | active,aggregate,collect,distribute,sync | 
| po7  | pod1a-AIO-1-PET_PolGrp   | up          | up         | eth1/2    | 33120    | 3C:FD:FE:CE:13:A9 | 65535           | 1            | 3        | 255           | active,aggregate,collect,distribute,sync | 
| po8  | pod1a-COMP-1-PET_PolGrp  | up          | up         | eth1/11   | 33123    | 3C:FD:FE:CE:1A:61 | 65535           | 1            | 3        | 255           | active,aggregate,collect,distribute,sync | 
| po9  | pod1a-COMP-1-SAMX_PolGrp | up          | up         | eth1/10   | 33457    | 3C:FD:FE:CE:1A:60 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po10 | pod1a-AIO-3-PET_PolGrp   | up          | up         | eth1/8    | 33122    | 3C:FD:FE:CE:16:41 | 65535           | 1            | 3        | 255           | active,aggregate,collect,distribute,sync | 
| po11 | pod1a-MX_PolGrp          | up          | up         | eth1/23   | 33454    | 3C:FD:FE:CE:0E:40 | 65535           | 1            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po12 | pod1a-API_PolGrp         | up          | up         | eth1/24   | 33453    | 70:EA:1A:FC:42:1E | 65535           | 2            | 4        | 255           | active,aggregate,collect,distribute,sync | 
| po13 | pod-4a-br-API            | up          | up         | eth1/68   | 33119    | 70:EA:1A:FC:23:06 | 65535           | 2            | 6        | 255           | active,aggregate,collect,distribute,sync | 
| po14 | pod1a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/1    | 32794    | 3C:FD:FE:CE:13:A8 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po15 | pod4a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/55   | 32789    | 40:A6:B7:08:FC:28 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po16 | pod4a-COMP-2-SAMX_PolGrp | up          | up         | eth1/61   | 32792    | 3C:FD:FE:CB:F5:18 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po17 | pod4a-AIO-2-PET_PolGrp   | up          | up         | eth1/53   | 33464    | 40:A6:B7:08:FC:21 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po18 | pod4a-COMP-1-PET_PolGrp  | up          | up         | eth1/59   | 32791    | 3C:FD:FE:F0:15:69 | 65535           | 1            | 3        | 255           | active,aggregate,collect,distribute,sync | 
| po19 | pod4a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/49   | 32782    | 3C:FD:FE:F0:15:10 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po20 | pod4a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/52   | 32784    | 40:A6:B7:08:FC:20 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po21 | pod4a-AIO-1-PET_PolGrp   | up          | up         | eth1/50   | 32783    | 3C:FD:FE:F0:15:11 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po22 | pod4a-MX_PolGrp          | up          | up         | eth1/67   | 33452    | 3C:FD:FE:EF:6F:48 | 65535           | 1            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po23 | pod4a-COMP-3-SAMX_PolGrp | up          | up         | eth1/64   | 33463    | 3C:FD:FE:CE:C4:28 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po24 | pod4a-COMP-3-PET_PolGrp  | up          | up         | eth1/65   | 32781    | 3C:FD:FE:CE:C4:29 | 65535           | 1            | 3        | 255           | active,aggregate,collect,distribute,sync | 
| po25 | pod4a-AIO-3-PET_PolGrp   | up          | up         | eth1/56   | 32790    | 40:A6:B7:08:FC:29 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po26 | Infra_PolGrp             | up          | up         | eth1/96   | 33111    | 00:23:04:EE:BE:65 | 32667           | 32769        | 16829    | 32768         | active,aggregate,collect,distribute,sync | 
| po27 | pod4a-COMP-2-PET_PolGrp  | up          | up         | eth1/62   | 32793    | 3C:FD:FE:CB:F5:19 | 65535           | 1            | 4        | 255           | active,aggregate,collect,distribute,sync | 
| po28 | pod4a-COMP-1-SAMX_PolGrp | up          | up         | eth1/58   | 33465    | 3C:FD:FE:F0:15:68 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po1  | pod1a-NVBench_PolGrp     | up          | down       |           |          |                   |                 |              |          |               |                                          | 
| po2  | pod1a-AIO-1-PET_PolGrp   | up          | up         | eth1/2    | 33120    | 3C:FD:FE:CE:13:A9 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po3  | pod1a-COMP-1-SAMX_PolGrp | up          | up         | eth1/10   | 33457    | 3C:FD:FE:CE:1A:60 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po4  | pod1a-AIO-3-PET_PolGrp   | up          | up         | eth1/8    | 33122    | 3C:FD:FE:CE:16:41 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po5  | pod1a-COMP-2-PET_PolGrp  | up          | up         | eth1/14   | 33124    | 3C:FD:FE:CB:ED:71 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po6  | Infra_PolGrp             | up          | up         | eth1/96   | 33111    | 00:23:04:EE:BE:65 | 32667           | 32769        | 445      | 32768         | active,aggregate,collect,distribute,sync | 
| po7  | pod1a-COMP-1-PET_PolGrp  | up          | up         | eth1/11   | 33123    | 3C:FD:FE:CE:1A:61 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po8  | pod1a-MX_PolGrp          | up          | down       |           |          |                   |                 |              |          |               |                                          | 
| po9  | pod1a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/4    | 33456    | 3C:FD:FE:CB:F5:B0 | 65535           | 2            | 8        | 255           | active,aggregate,collect,distribute,sync | 
| po10 | pod1a-COMP-2-SAMX_PolGrp | up          | up         | eth1/13   | 32796    | 3C:FD:FE:CB:ED:70 | 65535           | 2            | 8        | 255           | active,aggregate,collect,distribute,sync | 
| po11 | pod1a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/1    | 32794    | 3C:FD:FE:CE:13:A8 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po12 | pod1a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/7    | 33121    | 3C:FD:FE:CE:16:40 | 65535           | 2            | 8        | 255           | active,aggregate,collect,distribute,sync | 
| po13 | pod1a-AIO-2-PET_PolGrp   | up          | up         | eth1/5    | 32795    | 3C:FD:FE:CB:F5:B1 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po14 | pod4a-AIO-3-PET_PolGrp   | up          | up         | eth1/56   | 32790    | 40:A6:B7:08:FC:29 | 65535           | 1            | 3        | 255           | active,aggregate,collect,distribute,sync | 
| po15 | pod4a-COMP-1-SAMX_PolGrp | up          | up         | eth1/58   | 33465    | 3C:FD:FE:F0:15:68 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po16 | pod4a-MX_PolGrp          | up          | down       |           |          |                   |                 |              |          |               |                                          | 
| po17 | pod4a-COMP-3-PET_PolGrp  | up          | up         | eth1/65   | 32781    | 3C:FD:FE:CE:C4:29 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po18 | pod4a-COMP-1-PET_PolGrp  | up          | up         | eth1/59   | 32791    | 3C:FD:FE:F0:15:69 | 65535           | 1            | 8        | 255           | active,aggregate,collect,distribute,sync | 
| po19 | pod4a-COMP-2-SAMX_PolGrp | up          | up         | eth1/61   | 32792    | 3C:FD:FE:CB:F5:18 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po20 | pod4a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/49   | 32782    | 3C:FD:FE:F0:15:10 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po21 | pod4a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/52   | 32784    | 40:A6:B7:08:FC:20 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po22 | pod4a-COMP-2-PET_PolGrp  | up          | up         | eth1/62   | 32793    | 3C:FD:FE:CB:F5:19 | 65535           | 1            | 9        | 255           | active,aggregate,collect,distribute,sync | 
| po23 | pod4a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/55   | 32789    | 40:A6:B7:08:FC:28 | 65535           | 2            | 2        | 255           | active,aggregate,collect,distribute,sync | 
| po24 | pod4a-AIO-1-PET_PolGrp   | up          | up         | eth1/50   | 32783    | 3C:FD:FE:F0:15:11 | 65535           | 1            | 3        | 255           | active,aggregate,collect,distribute,sync | 
| po25 | pod1a-API_PolGrp         | up          | up         | eth1/24   | 33453    | 70:EA:1A:FC:42:1E | 65535           | 2            | 8        | 255           | active,aggregate,collect,distribute,sync | 
| po26 | pod4a-AIO-2-PET_PolGrp   | up          | up         | eth1/53   | 33464    | 40:A6:B7:08:FC:21 | 65535           | 1            | 3        | 255           | active,aggregate,collect,distribute,sync | 
| po27 | pod4a-COMP-3-SAMX_PolGrp | up          | up         | eth1/64   | 33463    | 3C:FD:FE:CE:C4:28 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po28 | pod-4a-br-API            | up          | up         | eth1/68   | 33119    | 70:EA:1A:FC:23:06 | 65535           | 2            | 7        | 255           | active,aggregate,collect,distribute,sync | 
| po1  | UCSB1-R3DC-FI-A_PolGrp   | up          | up         | eth1/3    | 32776    | 00:3A:9C:BD:8F:07 | 32768           | 17           | 437      | 32768         | active,aggregate,collect,distribute,sync | 
| po2  | UCSB1-R3DC-FI-B_PolGrp   | up          | up         | eth1/4    | 32775    | 00:3A:9C:BD:92:07 | 32768           | 16           | 437      | 32768         | active,aggregate,collect,distribute,sync | 
| po1  | UCSB1-R3DC-FI-B_PolGrp   | up          | up         | eth1/4    | 32775    | 00:3A:9C:BD:92:07 | 32768           | 16           | 433      | 32768         | active,aggregate,collect,distribute,sync | 
| po2  | UCSB1-R3DC-FI-A_PolGrp   | up          | up         | eth1/3    | 32776    | 00:3A:9C:BD:8F:07 | 32768           | 17           | 433      | 32768         | active,aggregate,collect,distribute,sync | 
+------+--------------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --role leaf --view intf

{
    "duration": 11764,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 737,
        "disconnect_time": 0,
        "mo_time": 9868,
        "total_time": 10605
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
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	737	-	connect apic11o.emea-sp.cisco.com
True	347	13	apic11o.emea-sp.cisco.com class fabricNode
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	358	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	328	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	300	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst
True	305	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	287	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	288	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst
True	349	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	324	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	385	27	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst
True	361	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	322	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	311	25	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/lacp/inst
True	341	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	309	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/lacp/inst
True	363	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	323	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst
True	305	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	292	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	303	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst
True	284	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	297	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	301	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)