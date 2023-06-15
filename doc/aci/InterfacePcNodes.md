# Node Interface - Port Channel (PC)

## Multiple nodes

```
# iserver get aci intf pc --apic apic11 --node rl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-----+------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name                   | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/rl301-eu-spdc | po1 | UCSB1-R3DC-FI-A_PolGrp | up    | enabled   | up    |        | active    | 300        | 1            | 
| pod-1/rl301-eu-spdc | po2 | UCSB1-R3DC-FI-B_PolGrp | up    | enabled   | up    |        | active    | 300        | 1            | 
| pod-1/rl302-eu-spdc | po1 | UCSB1-R3DC-FI-B_PolGrp | up    | enabled   | up    |        | active    | 300        | 1            | 
| pod-1/rl302-eu-spdc | po2 | UCSB1-R3DC-FI-A_PolGrp | up    | enabled   | up    |        | active    | 300        | 1            | 
+---------------------+-----+------------------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node rl

{
    "duration": 2635,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 2110,
        "total_time": 2499
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

True	389	-	connect apic11o.emea-sp.cisco.com
True	318	13	apic11o.emea-sp.cisco.com class fabricNode
True	282	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	288	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	358	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	297	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	284	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	283	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfacePc.md)