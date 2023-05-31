# Node Protocol - LACP

## Show instance summary for all leaf nodes

```
# iserver get aci proto lacp --apic apic11 --role leaf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| Node                | Admin State | System MAC        | Admin Priority | Oper Priority | Port Channel Interfaces |
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| pod-1/bl205-eu-spdc | enabled     | 4C:71:0D:7E:84:C0 | 32768          | 32768         | 5/0/5                   | 
| pod-1/bl206-eu-spdc | enabled     | 3C:13:CC:C9:ED:80 | 32768          | 32768         | 5/0/5                   | 
| pod-1/cl201-eu-spdc | enabled     | 4C:71:0D:23:FA:E3 | 32768          | 32768         | 27/1/28                 | 
| pod-1/cl202-eu-spdc | enabled     | 10:B3:D5:B5:62:C7 | 32768          | 32768         | 25/3/28                 | 
| pod-1/rl301-eu-spdc | enabled     | A0:B4:39:4A:2B:DF | 32768          | 32768         | 2/0/2                   | 
| pod-1/rl302-eu-spdc | enabled     | A0:B4:39:4A:2D:B3 | 32768          | 32768         | 2/0/2                   | 
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --role leaf

{
    "duration": 33910,
    "apic": {
        "read": true,
        "success": 90,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 89,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 28056,
        "total_time": 28451
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	322	11	apic11o.emea-sp.cisco.com class fabricNode
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	299	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	291	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/12] query query-target=children&target-subtree-class=lacpAdjEp
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	403	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst
True	315	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	362	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	293	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/12] query query-target=children&target-subtree-class=lacpAdjEp
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst
True	363	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	347	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/96] query query-target=children&target-subtree-class=lacpAdjEp
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/68] query query-target=children&target-subtree-class=lacpAdjEp
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/65] query query-target=children&target-subtree-class=lacpAdjEp
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/52] query query-target=children&target-subtree-class=lacpAdjEp
True	394	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/67] query query-target=children&target-subtree-class=lacpAdjEp
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/5] query query-target=children&target-subtree-class=lacpAdjEp
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/59] query query-target=children&target-subtree-class=lacpAdjEp
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	308	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/7] query query-target=children&target-subtree-class=lacpAdjEp
True	284	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/64] query query-target=children&target-subtree-class=lacpAdjEp
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/23] query query-target=children&target-subtree-class=lacpAdjEp
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/55] query query-target=children&target-subtree-class=lacpAdjEp
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/8] query query-target=children&target-subtree-class=lacpAdjEp
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/13] query query-target=children&target-subtree-class=lacpAdjEp
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/49] query query-target=children&target-subtree-class=lacpAdjEp
True	369	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/53] query query-target=children&target-subtree-class=lacpAdjEp
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/56] query query-target=children&target-subtree-class=lacpAdjEp
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/10] query query-target=children&target-subtree-class=lacpAdjEp
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/62] query query-target=children&target-subtree-class=lacpAdjEp
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/61] query query-target=children&target-subtree-class=lacpAdjEp
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/24] query query-target=children&target-subtree-class=lacpAdjEp
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/14] query query-target=children&target-subtree-class=lacpAdjEp
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/50] query query-target=children&target-subtree-class=lacpAdjEp
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst/if-[eth1/58] query query-target=children&target-subtree-class=lacpAdjEp
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst
True	373	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	356	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/50] query query-target=children&target-subtree-class=lacpAdjEp
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/55] query query-target=children&target-subtree-class=lacpAdjEp
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/62] query query-target=children&target-subtree-class=lacpAdjEp
True	294	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/67] query query-target=children&target-subtree-class=lacpAdjEp
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/49] query query-target=children&target-subtree-class=lacpAdjEp
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/65] query query-target=children&target-subtree-class=lacpAdjEp
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/52] query query-target=children&target-subtree-class=lacpAdjEp
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/61] query query-target=children&target-subtree-class=lacpAdjEp
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/64] query query-target=children&target-subtree-class=lacpAdjEp
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/53] query query-target=children&target-subtree-class=lacpAdjEp
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/59] query query-target=children&target-subtree-class=lacpAdjEp
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/96] query query-target=children&target-subtree-class=lacpAdjEp
True	365	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/56] query query-target=children&target-subtree-class=lacpAdjEp
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/58] query query-target=children&target-subtree-class=lacpAdjEp
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/68] query query-target=children&target-subtree-class=lacpAdjEp
True	347	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/13] query query-target=children&target-subtree-class=lacpAdjEp
True	350	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/10] query query-target=children&target-subtree-class=lacpAdjEp
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/24] query query-target=children&target-subtree-class=lacpAdjEp
True	335	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	300	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/23] query query-target=children&target-subtree-class=lacpAdjEp
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/5] query query-target=children&target-subtree-class=lacpAdjEp
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/14] query query-target=children&target-subtree-class=lacpAdjEp
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/8] query query-target=children&target-subtree-class=lacpAdjEp
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst/if-[eth1/7] query query-target=children&target-subtree-class=lacpAdjEp
True	280	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst
True	326	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	299	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst/if-[eth1/3] query query-target=children&target-subtree-class=lacpAdjEp
True	308	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst
True	314	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	318	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst/if-[eth1/3] query query-target=children&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)