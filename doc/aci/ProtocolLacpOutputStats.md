# Node Protocol - LACP

## Interface stats output

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view stats

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| Id  | Name              | Admin State | Oper State | Interface | PDU Sent | PDU Recv | PDU Recv Err | Marker Sent | Marker Recv | Marker Response Sent | Marker Response Recv |
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| po1 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 255889   | 255884   | 0            | 0           | 0           | 0                    | 0                    | 
| po2 | SPN_PolGrp        | up          | up         | eth1/27   | 255914   | 255911   | 0            | 0           | 0           | 0                    | 0                    | 
| po3 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 255899   | 255912   | 0            | 0           | 0           | 0                    | 0                    | 
| po4 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 255892   | 255909   | 0            | 0           | 0           | 0                    | 0                    | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 255908   | 255897   | 0            | 0           | 0           | 0                    | 0                    | 
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view stats

{
    "duration": 3788,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 2810,
        "total_time": 3231
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

True	421	-	connect apic11o.emea-sp.cisco.com
True	332	11	apic11o.emea-sp.cisco.com class fabricNode
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	294	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	292	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/2] query query-target=children&target-subtree-class=lacpAdjEp
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/27] query query-target=children&target-subtree-class=lacpAdjEp
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/12] query query-target=children&target-subtree-class=lacpAdjEp
True	360	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/11] query query-target=children&target-subtree-class=lacpAdjEp
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst/if-[eth1/1] query query-target=children&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)