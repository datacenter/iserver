# Node Protocol - LACP

## Intf view

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol LACP - Port Channels [#5]
----------------------------------

+---------------------+---------+-------------------+-------+------+---------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| Node                | Intf Id | Name              | Admin | Oper | Member  | Oper Key | Nbr System MAC    | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State                           |
+---------------------+---------+-------------------+-------+------+---------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| pod-1/bl205-eu-spdc | po1     | HX1-FI-A_PolGrp   | up    | up   | eth1/11 | 32769    | 00:3A:9C:C0:04:47 | 32768           | 200          | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| pod-1/bl205-eu-spdc | po2     | HX1-FI-B_PolGrp   | up    | up   | eth1/12 | 32770    | 00:3A:9C:C0:03:E7 | 32768           | 241          | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| pod-1/bl205-eu-spdc | po3     | SPN_PolGrp        | up    | up   | eth1/27 | 33112    | E0:0E:DA:A3:38:13 | 32768           | 1            | 337      | 32768         | active,aggregate,collect,distribute,sync | 
| pod-1/bl205-eu-spdc | po4     | UCSB1-FI-B_PolGrp | up    | up   | eth1/2  | 33111    | 00:3A:9C:BD:8F:07 | 32768           | 15           | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| pod-1/bl205-eu-spdc | po5     | UCSB1-FI-A_PolGrp | up    | up   | eth1/1  | 32771    | 00:3A:9C:BD:92:07 | 32768           | 14           | 457      | 32768         | active,aggregate,collect,distribute,sync | 
+---------------------+---------+-------------------+-------+------+---------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view intf

{
    "duration": 2141,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 385,
        "disconnect_time": 0,
        "mo_time": 1569,
        "total_time": 1954
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

True	385	-	connect apic11o.emea-sp.cisco.com:443
True	295	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	278	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst
True	423	5	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	291	5	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	282	5	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp&rsp-subtree-include=fault-count
```

[[Back]](./ProtocolLacp.md)