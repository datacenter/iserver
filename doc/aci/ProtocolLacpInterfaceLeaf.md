# Node Protocol - LACP

## Show LACP interfaces for all leaf nodes

```
# iserver get aci proto lacp --apic apic11 --role leaf --view intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+------+--------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| Id   | Name                     | Admin State | Oper State | Interface | Oper Key | Nbr System MAC | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State |
+------+--------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| po1  | HX1-FI-B_PolGrp          | up          | up         | eth1/12   | 32770    | None           | None            | None         | None     | None          | None           | 
| po2  | SPN_PolGrp               | up          | up         | eth1/27   | 33112    | None           | None            | None         | None     | None          | None           | 
| po3  | UCSB1-FI-B_PolGrp        | up          | up         | eth1/2    | 33111    | None           | None            | None         | None     | None          | None           | 
| po4  | HX1-FI-A_PolGrp          | up          | up         | eth1/11   | 32769    | None           | None            | None         | None     | None          | None           | 
| po5  | UCSB1-FI-A_PolGrp        | up          | up         | eth1/1    | 32771    | None           | None            | None         | None     | None          | None           | 
| po1  | HX1-FI-A_PolGrp          | up          | up         | eth1/11   | 32769    | None           | None            | None         | None     | None          | None           | 
| po2  | HX1-FI-B_PolGrp          | up          | up         | eth1/12   | 32770    | None           | None            | None         | None     | None          | None           | 
| po3  | UCSB1-FI-B_PolGrp        | up          | up         | eth1/2    | 33111    | None           | None            | None         | None     | None          | None           | 
| po4  | UCSB1-FI-A_PolGrp        | up          | up         | eth1/1    | 32771    | None           | None            | None         | None     | None          | None           | 
| po5  | SPN_PolGrp               | up          | up         | eth1/27   | 33112    | None           | None            | None         | None     | None          | None           | 
| po1  | pod-4a-br-API            | up          | up         | eth1/68   | 33119    | None           | None            | None         | None     | None          | None           | 
| po2  | Infra_PolGrp             | up          | up         | eth1/96   | 33111    | None           | None            | None         | None     | None          | None           | 
| po3  | pod4a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/55   | 32789    | None           | None            | None         | None     | None          | None           | 
| po4  | pod1a-MX_PolGrp          | up          | up         | eth1/23   | 33454    | None           | None            | None         | None     | None          | None           | 
| po5  | pod1a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/1    | 32794    | None           | None            | None         | None     | None          | None           | 
| po6  | pod4a-COMP-1-PET_PolGrp  | up          | up         | eth1/59   | 32791    | None           | None            | None         | None     | None          | None           | 
| po7  | pod4a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/49   | 32782    | None           | None            | None         | None     | None          | None           | 
| po8  | pod1a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/7    | 33121    | None           | None            | None         | None     | None          | None           | 
| po9  | pod1a-AIO-2-PET_PolGrp   | up          | up         | eth1/5    | 32795    | None           | None            | None         | None     | None          | None           | 
| po10 | pod1a-COMP-1-SAMX_PolGrp | up          | up         | eth1/10   | 33457    | None           | None            | None         | None     | None          | None           | 
| po11 | pod4a-COMP-2-PET_PolGrp  | up          | up         | eth1/62   | 32793    | None           | None            | None         | None     | None          | None           | 
| po12 | pod1a-NVBench_PolGrp     | up          | down       |           |          |                |                 |              |          |               |                | 
| po13 | pod1a-AIO-1-PET_PolGrp   | up          | up         | eth1/2    | 33120    | None           | None            | None         | None     | None          | None           | 
| po14 | pod4a-COMP-2-SAMX_PolGrp | up          | up         | eth1/61   | 32792    | None           | None            | None         | None     | None          | None           | 
| po15 | pod1a-API_PolGrp         | up          | up         | eth1/24   | 33453    | None           | None            | None         | None     | None          | None           | 
| po16 | pod1a-COMP-2-PET_PolGrp  | up          | up         | eth1/14   | 33124    | None           | None            | None         | None     | None          | None           | 
| po17 | pod1a-COMP-2-SAMX_PolGrp | up          | up         | eth1/13   | 32796    | None           | None            | None         | None     | None          | None           | 
| po18 | pod4a-AIO-1-PET_PolGrp   | up          | up         | eth1/50   | 32783    | None           | None            | None         | None     | None          | None           | 
| po19 | pod1a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/4    | 33456    | None           | None            | None         | None     | None          | None           | 
| po20 | pod4a-COMP-1-SAMX_PolGrp | up          | up         | eth1/58   | 33465    | None           | None            | None         | None     | None          | None           | 
| po21 | pod4a-AIO-2-PET_PolGrp   | up          | up         | eth1/53   | 33464    | None           | None            | None         | None     | None          | None           | 
| po22 | pod1a-AIO-3-PET_PolGrp   | up          | up         | eth1/8    | 33122    | None           | None            | None         | None     | None          | None           | 
| po23 | pod4a-MX_PolGrp          | up          | up         | eth1/67   | 33452    | None           | None            | None         | None     | None          | None           | 
| po24 | pod4a-COMP-3-SAMX_PolGrp | up          | up         | eth1/64   | 33463    | None           | None            | None         | None     | None          | None           | 
| po25 | pod4a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/52   | 32784    | None           | None            | None         | None     | None          | None           | 
| po26 | pod4a-COMP-3-PET_PolGrp  | up          | up         | eth1/65   | 32781    | None           | None            | None         | None     | None          | None           | 
| po27 | pod1a-COMP-1-PET_PolGrp  | up          | up         | eth1/11   | 33123    | None           | None            | None         | None     | None          | None           | 
| po28 | pod4a-AIO-3-PET_PolGrp   | up          | up         | eth1/56   | 32790    | None           | None            | None         | None     | None          | None           | 
| po1  | pod4a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/55   | 32789    | None           | None            | None         | None     | None          | None           | 
| po2  | pod4a-AIO-1-PET_PolGrp   | up          | up         | eth1/50   | 32783    | None           | None            | None         | None     | None          | None           | 
| po3  | pod4a-COMP-3-PET_PolGrp  | up          | up         | eth1/65   | 32781    | None           | None            | None         | None     | None          | None           | 
| po4  | pod4a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/52   | 32784    | None           | None            | None         | None     | None          | None           | 
| po5  | pod4a-COMP-2-SAMX_PolGrp | up          | up         | eth1/61   | 32792    | None           | None            | None         | None     | None          | None           | 
| po6  | pod4a-COMP-2-PET_PolGrp  | up          | up         | eth1/62   | 32793    | None           | None            | None         | None     | None          | None           | 
| po7  | pod4a-AIO-2-PET_PolGrp   | up          | up         | eth1/53   | 33464    | None           | None            | None         | None     | None          | None           | 
| po8  | pod4a-COMP-3-SAMX_PolGrp | up          | up         | eth1/64   | 33463    | None           | None            | None         | None     | None          | None           | 
| po9  | Infra_PolGrp             | up          | up         | eth1/96   | 33111    | None           | None            | None         | None     | None          | None           | 
| po10 | pod4a-COMP-1-PET_PolGrp  | up          | up         | eth1/59   | 32791    | None           | None            | None         | None     | None          | None           | 
| po11 | pod4a-AIO-3-PET_PolGrp   | up          | up         | eth1/56   | 32790    | None           | None            | None         | None     | None          | None           | 
| po12 | pod4a-COMP-1-SAMX_PolGrp | up          | up         | eth1/58   | 33465    | None           | None            | None         | None     | None          | None           | 
| po13 | pod4a-MX_PolGrp          | up          | down       |           |          |                |                 |              |          |               |                | 
| po14 | pod-4a-br-API            | up          | up         | eth1/68   | 33119    | None           | None            | None         | None     | None          | None           | 
| po15 | pod4a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/49   | 32782    | None           | None            | None         | None     | None          | None           | 
| po16 | pod1a-AIO-3-PET_PolGrp   | up          | up         | eth1/8    | 33122    | None           | None            | None         | None     | None          | None           | 
| po17 | pod1a-COMP-2-PET_PolGrp  | up          | up         | eth1/14   | 33124    | None           | None            | None         | None     | None          | None           | 
| po18 | pod1a-COMP-1-PET_PolGrp  | up          | up         | eth1/11   | 33123    | None           | None            | None         | None     | None          | None           | 
| po19 | pod1a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/1    | 32794    | None           | None            | None         | None     | None          | None           | 
| po20 | pod1a-AIO-1-PET_PolGrp   | up          | up         | eth1/2    | 33120    | None           | None            | None         | None     | None          | None           | 
| po21 | pod1a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/7    | 33121    | None           | None            | None         | None     | None          | None           | 
| po22 | pod1a-AIO-2-PET_PolGrp   | up          | up         | eth1/5    | 32795    | None           | None            | None         | None     | None          | None           | 
| po23 | pod1a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/4    | 33456    | None           | None            | None         | None     | None          | None           | 
| po24 | pod1a-MX_PolGrp          | up          | down       |           |          |                |                 |              |          |               |                | 
| po25 | pod1a-NVBench_PolGrp     | up          | down       |           |          |                |                 |              |          |               |                | 
| po26 | pod1a-API_PolGrp         | up          | up         | eth1/24   | 33453    | None           | None            | None         | None     | None          | None           | 
| po27 | pod1a-COMP-1-SAMX_PolGrp | up          | up         | eth1/10   | 33457    | None           | None            | None         | None     | None          | None           | 
| po28 | pod1a-COMP-2-SAMX_PolGrp | up          | up         | eth1/13   | 32796    | None           | None            | None         | None     | None          | None           | 
| po1  | UCSB1-R3DC-FI-A_PolGrp   | up          | up         | eth1/3    | 32776    | None           | None            | None         | None     | None          | None           | 
| po2  | UCSB1-R3DC-FI-B_PolGrp   | up          | up         | eth1/4    | 32775    | None           | None            | None         | None     | None          | None           | 
| po1  | UCSB1-R3DC-FI-B_PolGrp   | up          | up         | eth1/4    | 32775    | None           | None            | None         | None     | None          | None           | 
| po2  | UCSB1-R3DC-FI-A_PolGrp   | up          | up         | eth1/3    | 32776    | None           | None            | None         | None     | None          | None           | 
+------+--------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --role leaf --view intf

{
    "duration": 34554,
    "apic": {
        "read": true,
        "success": 90,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 89,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 28642,
        "total_time": 29041
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
    }
}

Log: apic
----------

True	399	-	connect apic11o.emea-sp.cisco.com
True	318	11	apic11o.emea-sp.cisco.com class fabricNode
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	296	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	323	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/12] query query-target=children&target-subtree-class=lacpAdjEp
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	365	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst
True	361	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	364	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/12] query query-target=children&target-subtree-class=lacpAdjEp
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst
True	386	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	334	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/96] query query-target=children&target-subtree-class=lacpAdjEp
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/68] query query-target=children&target-subtree-class=lacpAdjEp
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/65] query query-target=children&target-subtree-class=lacpAdjEp
True	308	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/52] query query-target=children&target-subtree-class=lacpAdjEp
True	383	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/67] query query-target=children&target-subtree-class=lacpAdjEp
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/5] query query-target=children&target-subtree-class=lacpAdjEp
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/59] query query-target=children&target-subtree-class=lacpAdjEp
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/7] query query-target=children&target-subtree-class=lacpAdjEp
True	349	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/64] query query-target=children&target-subtree-class=lacpAdjEp
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/23] query query-target=children&target-subtree-class=lacpAdjEp
True	285	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/55] query query-target=children&target-subtree-class=lacpAdjEp
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/8] query query-target=children&target-subtree-class=lacpAdjEp
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/13] query query-target=children&target-subtree-class=lacpAdjEp
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/49] query query-target=children&target-subtree-class=lacpAdjEp
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/53] query query-target=children&target-subtree-class=lacpAdjEp
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/56] query query-target=children&target-subtree-class=lacpAdjEp
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/10] query query-target=children&target-subtree-class=lacpAdjEp
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/62] query query-target=children&target-subtree-class=lacpAdjEp
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/61] query query-target=children&target-subtree-class=lacpAdjEp
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/24] query query-target=children&target-subtree-class=lacpAdjEp
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/14] query query-target=children&target-subtree-class=lacpAdjEp
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/50] query query-target=children&target-subtree-class=lacpAdjEp
True	365	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/58] query query-target=children&target-subtree-class=lacpAdjEp
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst
True	369	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	411	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/50] query query-target=children&target-subtree-class=lacpAdjEp
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/55] query query-target=children&target-subtree-class=lacpAdjEp
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/62] query query-target=children&target-subtree-class=lacpAdjEp
True	319	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/67] query query-target=children&target-subtree-class=lacpAdjEp
True	357	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/49] query query-target=children&target-subtree-class=lacpAdjEp
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/65] query query-target=children&target-subtree-class=lacpAdjEp
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/52] query query-target=children&target-subtree-class=lacpAdjEp
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/61] query query-target=children&target-subtree-class=lacpAdjEp
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/64] query query-target=children&target-subtree-class=lacpAdjEp
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/53] query query-target=children&target-subtree-class=lacpAdjEp
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/59] query query-target=children&target-subtree-class=lacpAdjEp
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/96] query query-target=children&target-subtree-class=lacpAdjEp
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/56] query query-target=children&target-subtree-class=lacpAdjEp
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/58] query query-target=children&target-subtree-class=lacpAdjEp
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/68] query query-target=children&target-subtree-class=lacpAdjEp
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/13] query query-target=children&target-subtree-class=lacpAdjEp
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/10] query query-target=children&target-subtree-class=lacpAdjEp
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/24] query query-target=children&target-subtree-class=lacpAdjEp
True	336	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	289	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/23] query query-target=children&target-subtree-class=lacpAdjEp
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/5] query query-target=children&target-subtree-class=lacpAdjEp
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/14] query query-target=children&target-subtree-class=lacpAdjEp
True	369	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/8] query query-target=children&target-subtree-class=lacpAdjEp
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/7] query query-target=children&target-subtree-class=lacpAdjEp
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst
True	301	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	318	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst/if-[eth1/3] query query-target=children&target-subtree-class=lacpAdjEp
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst
True	301	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	388	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	360	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst/if-[eth1/3] query query-target=children&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)