# Node Protocol - LACP

## Interface stats output

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view stats

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| Id  | Name              | Admin State | Oper State | Interface | PDU Sent | PDU Recv | PDU Recv Err | Marker Sent | Marker Recv | Marker Response Sent | Marker Response Recv |
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| po1 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 5534     | 5534     | 0            | 0           | 0           | 0                    | 0                    | 
| po2 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 5534     | 5534     | 0            | 0           | 0           | 0                    | 0                    | 
| po3 | SPN_PolGrp        | up          | up         | eth1/27   | 5533     | 5535     | 0            | 0           | 0           | 0                    | 0                    | 
| po4 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 5534     | 5535     | 0            | 0           | 0           | 0                    | 0                    | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 5533     | 5534     | 0            | 0           | 0           | 0                    | 0                    | 
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view stats

{
    "duration": 2432,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 478,
        "disconnect_time": 0,
        "mo_time": 1644,
        "total_time": 2122
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

True	478	-	connect apic11o.emea-sp.cisco.com
True	330	13	apic11o.emea-sp.cisco.com class fabricNode
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	357	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	319	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	323	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)