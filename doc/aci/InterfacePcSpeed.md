# Node Interface - Port Channel (PC)

## Filter by port speed

```
# iserver get aci intf pc --apic apic11 --node any --speed 40G

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name              | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/bl205-eu-spdc | po1 | HX1-FI-B_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po3 | UCSB1-FI-B_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po4 | HX1-FI-A_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po5 | UCSB1-FI-A_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po1 | HX1-FI-A_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po2 | HX1-FI-B_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po3 | UCSB1-FI-B_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po4 | UCSB1-FI-A_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node any --speed 40G

{
    "duration": 5213,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 4239,
        "total_time": 4654
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
True	329	11	apic11o.emea-sp.cisco.com class fabricNode
True	311	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	336	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	308	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	342	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	330	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	317	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	395	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	341	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	295	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	348	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	272	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	315	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
```

[[Back]](./InterfacePc.md)