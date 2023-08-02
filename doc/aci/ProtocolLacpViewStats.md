# Node Protocol - LACP

## Nei view

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view stats

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol LACP - Interface Stats [#5]
------------------------------------

+---------------------+---------+-------------------+-------+------+---------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| Node                | Intf Id | Name              | Admin | Oper | Member  | PDU Sent | PDU Recv | PDU Recv Err | Marker Sent | Marker Recv | Marker Response Sent | Marker Response Recv |
+---------------------+---------+-------------------+-------+------+---------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| pod-1/bl205-eu-spdc | po1     | HX1-FI-A_PolGrp   | up    | up   | eth1/11 | 147397   | 147398   | 0            | 0           | 0           | 0                    | 0                    | 
| pod-1/bl205-eu-spdc | po2     | HX1-FI-B_PolGrp   | up    | up   | eth1/12 | 147397   | 147396   | 0            | 0           | 0           | 0                    | 0                    | 
| pod-1/bl205-eu-spdc | po3     | SPN_PolGrp        | up    | up   | eth1/27 | 147396   | 147398   | 0            | 0           | 0           | 0                    | 0                    | 
| pod-1/bl205-eu-spdc | po4     | UCSB1-FI-B_PolGrp | up    | up   | eth1/2  | 147397   | 147399   | 0            | 0           | 0           | 0                    | 0                    | 
| pod-1/bl205-eu-spdc | po5     | UCSB1-FI-A_PolGrp | up    | up   | eth1/1  | 147402   | 147406   | 0            | 0           | 0           | 0                    | 0                    | 
+---------------------+---------+-------------------+-------+------+---------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view stats

{
    "duration": 2220,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 422,
        "disconnect_time": 0,
        "mo_time": 1577,
        "total_time": 1999
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

True	422	-	connect apic11o.emea-sp.cisco.com:443
True	297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	288	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst
True	430	5	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	282	5	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	280	5	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp&rsp-subtree-include=fault-count
```

[[Back]](./ProtocolLacp.md)