# Node Protocol - LACP

## Show LACP interface for selected nodes

```
# iserver get aci proto lacp --apic apic11 --node rl --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+-----+------------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| Id  | Name                   | Admin State | Oper State | Interface | Oper Key | Nbr System MAC    | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State                           |
+-----+------------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| po1 | UCSB1-R3DC-FI-A_PolGrp | up          | up         | eth1/3    | 32776    | 00:3A:9C:BD:8F:07 | 32768           | 17           | 437      | 32768         | active,aggregate,collect,distribute,sync | 
| po2 | UCSB1-R3DC-FI-B_PolGrp | up          | up         | eth1/4    | 32775    | 00:3A:9C:BD:92:07 | 32768           | 16           | 437      | 32768         | active,aggregate,collect,distribute,sync | 
| po1 | UCSB1-R3DC-FI-B_PolGrp | up          | up         | eth1/4    | 32775    | 00:3A:9C:BD:92:07 | 32768           | 16           | 433      | 32768         | active,aggregate,collect,distribute,sync | 
| po2 | UCSB1-R3DC-FI-A_PolGrp | up          | up         | eth1/3    | 32776    | 00:3A:9C:BD:8F:07 | 32768           | 17           | 433      | 32768         | active,aggregate,collect,distribute,sync | 
+-----+------------------------+-------------+------------+-----------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node rl --view intf

{
    "duration": 3616,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 465,
        "disconnect_time": 0,
        "mo_time": 2813,
        "total_time": 3278
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

True	465	-	connect apic11o.emea-sp.cisco.com
True	330	13	apic11o.emea-sp.cisco.com class fabricNode
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst
True	309	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	281	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	311	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst
True	300	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	328	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	342	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)