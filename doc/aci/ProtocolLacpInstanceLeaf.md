# Node Protocol - LACP

## Show instance summary for all leaf nodes

```
# iserver get aci proto lacp --apic apic11 --role leaf

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

+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| Node                | Admin State | System MAC        | Admin Priority | Oper Priority | Port Channel Interfaces |
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
| pod-1/bl205-eu-spdc | enabled     | 4C:71:0D:7E:84:C0 | 32768          | 32768         | 5/0/5                   | 
| pod-1/bl206-eu-spdc | enabled     | 3C:13:CC:C9:ED:80 | 32768          | 32768         | 5/0/5                   | 
| pod-1/cl201-eu-spdc | enabled     | 4C:71:0D:23:FA:E3 | 32768          | 32768         | 27/1/28                 | 
| pod-1/cl202-eu-spdc | enabled     | 10:B3:D5:B5:62:C7 | 32768          | 32768         | 25/3/28                 | 
| pod-1/cl209-eu-spdc | enabled     | C0:F8:7F:FE:10:B0 | 32768          | 32768         | 0/0/0                   | 
| pod-1/cl210-eu-spdc | enabled     | C0:F8:7F:FE:11:80 | 32768          | 32768         | 0/0/0                   | 
| pod-1/rl301-eu-spdc | enabled     | A0:B4:39:4A:2B:DF | 32768          | 32768         | 2/0/2                   | 
| pod-1/rl302-eu-spdc | enabled     | A0:B4:39:4A:2D:B3 | 32768          | 32768         | 2/0/2                   | 
+---------------------+-------------+-------------------+----------------+---------------+-------------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --role leaf

{
    "duration": 12026,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 10638,
        "total_time": 11075
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

True	437	-	connect apic11o.emea-sp.cisco.com
True	336	13	apic11o.emea-sp.cisco.com class fabricNode
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	391	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	342	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	341	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst
True	358	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	307	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	324	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst
True	390	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	345	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	326	27	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst
True	386	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	353	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	337	25	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/lacp/inst
True	322	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	336	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/lacp/inst
True	334	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	383	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst
True	379	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	311	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	331	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	429	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst
True	337	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	328	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	331	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)