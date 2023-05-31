# Node Interface - Port Channel (PC)

## Filter by port channel's vpc domain

```
# iserver get aci intf pc --apic apic11 --node any --domain 105

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
| pod-1/bl205-eu-spdc | po2 | SPN_PolGrp        | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po3 | UCSB1-FI-B_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po4 | HX1-FI-A_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl205-eu-spdc | po5 | UCSB1-FI-A_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po1 | HX1-FI-A_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po2 | HX1-FI-B_PolGrp   | up    | disabled  | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po3 | UCSB1-FI-B_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po4 | UCSB1-FI-A_PolGrp | up    | enabled   | up    |        | active    | 105        | 1            | 
| pod-1/bl206-eu-spdc | po5 | SPN_PolGrp        | up    | enabled   | up    |        | active    | 105        | 1            | 
+---------------------+-----+-------------------+-------+-----------+-------+--------+-----------+------------+--------------+
```

Developer

```
# iserver get aci intf pc --apic apic11 --node any --domain 105

{
    "duration": 7791,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 6893,
        "total_time": 7283
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

True	390	-	connect apic11o.emea-sp.cisco.com
True	326	11	apic11o.emea-sp.cisco.com class fabricNode
True	385	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vpcDom
True	345	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	302	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	326	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/vpcDom
True	327	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/vpc/inst/dom-105 query query-target=children&target-subtree-class=vpcIf
True	390	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	309	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/vpcDom
True	315	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	372	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	310	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/vpcDom
True	326	28	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/vpc/inst/dom-100 query query-target=children&target-subtree-class=vpcIf
True	432	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	303	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/vpcDom
True	337	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	308	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	295	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/vpcDom
True	289	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/vpc/inst/dom-300 query query-target=children&target-subtree-class=vpcIf
True	311	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
True	305	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/pcAggrIf query rsp-subtree=children&rsp-subtree-class=ethpmAggrIf
```

[[Back]](./InterfacePc.md)