# Node Protocol - LACP

## Verbose output

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

LACP Instance
-------------
- Node                    : pod-1/bl205-eu-spdc
- Admin State             : enabled
- System MAC              : 4C:71:0D:7E:84:C0
- Admin Priority          : 32768
- Oper Priority           : 32768
- Port Channel Interfaces : 5/0/5


+-----+-------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| Id  | Name              | Admin State | Oper State | Interface | Oper Key | Nbr System MAC    | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State                           |
+-----+-------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| po1 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 32769    | 00:3A:9C:C0:04:47 | 32768           | 200          | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| po2 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 32770    | 00:3A:9C:C0:03:E7 | 32768           | 241          | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| po3 | SPN_PolGrp        | up          | up         | eth1/27   | 33112    | E0:0E:DA:A3:38:13 | 32768           | 1            | 337      | 32768         | active,aggregate,collect,distribute,sync | 
| po4 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 33111    | 00:3A:9C:BD:8F:07 | 32768           | 15           | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 32771    | 00:3A:9C:BD:92:07 | 32768           | 14           | 457      | 32768         | active,aggregate,collect,distribute,sync | 
+-----+-------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+

+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| Id  | Name              | Admin State | Oper State | Interface | PDU Sent | PDU Recv | PDU Recv Err | Marker Sent | Marker Recv | Marker Response Sent | Marker Response Recv |
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| po1 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 5534     | 5534     | 0            | 0           | 0           | 0                    | 0                    | 
| po2 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 5534     | 5534     | 0            | 0           | 0           | 0                    | 0                    | 
| po3 | SPN_PolGrp        | up          | up         | eth1/27   | 5533     | 5535     | 0            | 0           | 0           | 0                    | 0                    | 
| po4 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 5534     | 5536     | 0            | 0           | 0           | 0                    | 0                    | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 5534     | 5535     | 0            | 0           | 0           | 0                    | 0                    | 
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc --view verbose

{
    "duration": 2769,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 1676,
        "total_time": 2071
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	334	13	apic11o.emea-sp.cisco.com class fabricNode
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst
True	294	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	324	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	412	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)