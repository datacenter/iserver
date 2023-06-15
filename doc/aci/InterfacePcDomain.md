# Node Interface - Port Channel (PC)

## Filter by port channel's vpc domain

```
# iserver get aci intf pc --apic apic11 --node any --domain 105

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| Node                | Id  | Name              | Admin | Switching | State | Reason | Oper Mode | VPC Domain | Active Links |
+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
| pod-1/bl205-eu-spdc | po1 | HX1-FI-A_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po2 | HX1-FI-B_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po3 | SPN_PolGrp        | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po4 | UCSB1-FI-B_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po5 | UCSB1-FI-A_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po1 | HX1-FI-B_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po2 | UCSB1-FI-B_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po3 | HX1-FI-A_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po4 | UCSB1-FI-A_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po5 | SPN_PolGrp        | up    | enabled   | up    |        | active    | 105        | 1            | 
+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node any --domain 105

{
    "duration": 7653,
    "apic": {
        "read": true,
        "success": 24,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 23,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 6920,
        "total_time": 7311
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

True	391	-	connect apic11o.emea-sp.cisco.com
True	299	13	apic11o.emea-sp.cisco.com class fabricNode
True	335	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	279	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	281	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	309	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	285	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	286	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	352	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	277	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	308	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	330	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	296	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	290	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	348	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	289	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	289	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	316	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	300	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	320	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	281	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	283	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
```

[[Back]](./InterfacePc.md)