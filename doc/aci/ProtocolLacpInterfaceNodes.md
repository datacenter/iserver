# Node Protocol - LACP

## Show LACP interface for selected nodes

```
# iserver get aci proto lacp --apic apic11 --node rl --view intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+-----+------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| Id  | Name                   | Admin State | Oper State | Interface | Oper Key | Nbr System MAC | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State |
+-----+------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| po1 | UCSB1-R3DC-FI-A_PolGrp | up          | up         | eth1/3    | 32776    | None           | None            | None         | None     | None          | None           | 
| po2 | UCSB1-R3DC-FI-B_PolGrp | up          | up         | eth1/4    | 32775    | None           | None            | None         | None     | None          | None           | 
| po1 | UCSB1-R3DC-FI-B_PolGrp | up          | up         | eth1/4    | 32775    | None           | None            | None         | None     | None          | None           | 
| po2 | UCSB1-R3DC-FI-A_PolGrp | up          | up         | eth1/3    | 32776    | None           | None            | None         | None     | None          | None           | 
+-----+------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
```

Developer

```
# iserver get aci proto lacp --apic apic11 --node rl --view intf

{
    "duration": 3996,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 3209,
        "total_time": 3591
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

True	382	-	connect apic11o.emea-sp.cisco.com
True	311	11	apic11o.emea-sp.cisco.com class fabricNode
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst
True	306	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	281	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	272	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	277	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lacp/inst/if-[eth1/3] query query-target=children&target-subtree-class=lacpAdjEp
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst
True	287	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	336	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst/if-[eth1/4] query query-target=children&target-subtree-class=lacpAdjEp
True	285	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lacp/inst/if-[eth1/3] query query-target=children&target-subtree-class=lacpAdjEp
```

[[Back]](./ProtocolLacp.md)