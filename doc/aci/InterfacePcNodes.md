# Node Interface - Port Channel (PC)

## Multiple nodes

```
# iserver get aci intf pc --apic apic11 --node rl

Apic: apic11o.emea-sp.cisco.com
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
    "duration": 2922,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 2318,
        "total_time": 2733
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

True	415	-	connect apic11o.emea-sp.cisco.com
True	325	11	apic11o.emea-sp.cisco.com class fabricNode
True	306	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	299	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	308	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	312	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	331	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	437	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
```

[[Back]](./InterfacePc.md)