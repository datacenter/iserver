# Node Interface - Management

## All nodes

```
# iserver get aci intf mgmt --apic apic11 --node any

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

+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Node                | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:04.036+02:00 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:46.234+02:00 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:02.581+02:00 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:08.264+02:00 | 
| pod-1/cl209-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T16:55:12.934+02:00 | 
| pod-1/cl210-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T16:55:06.883+02:00 | 
| pod-1/rl301-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:13:40.873+02:00 | 
| pod-1/rl302-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:13:53.167+02:00 | 
| pod-1/s101-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:12:56.045+02:00 | 
| pod-1/s102-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:12:57.357+02:00 | 
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic11 --node any

{
    "duration": 9775,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 9080,
        "total_time": 9468
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

True	388	-	connect apic11o.emea-sp.cisco.com
True	306	13	apic11o.emea-sp.cisco.com class fabricNode
True	293	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	273	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	321	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	293	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	272	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/mgmtMgmtIf
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	281	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/mgmtMgmtIf
True	285	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	290	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	321	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/mgmtMgmtIf
True	286	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	284	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	319	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/mgmtMgmtIf
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/mgmtMgmtIf
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	282	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/mgmtMgmtIf
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	288	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/mgmtMgmtIf
True	279	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)