# Node Interface - Management

## All nodes

```
# iserver get aci intf mgmt --apic apic11 --node any

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

+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Node                | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:13:34.502+02:00 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:37:10.362+02:00 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:15:14.143+02:00 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:39:11.176+02:00 | 
| pod-1/rl301-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:10:01.724+02:00 | 
| pod-1/rl302-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:33:50.626+02:00 | 
| pod-1/s101-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:12:44.643+02:00 | 
| pod-1/s102-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-04-28T11:27:42.302+02:00 | 
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic11 --node any

{
    "duration": 8583,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 482,
        "disconnect_time": 0,
        "mo_time": 7750,
        "total_time": 8232
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

True	482	-	connect apic11o.emea-sp.cisco.com
True	317	11	apic11o.emea-sp.cisco.com class fabricNode
True	321	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	310	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	294	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	285	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	290	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/mgmtMgmtIf
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	291	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/mgmtMgmtIf
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	302	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/mgmtMgmtIf
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	305	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/mgmtMgmtIf
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	294	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/mgmtMgmtIf
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)