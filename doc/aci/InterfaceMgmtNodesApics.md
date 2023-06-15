# Node Interface - Management

## Multi-APIC

```
# iserver get aci intf mgmt --apic dom:milan --node any

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
Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Apic   | Node                 | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| apic11 | pod-1/bl205-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:04.036+02:00 | 
| apic11 | pod-1/bl206-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:46.234+02:00 | 
| apic11 | pod-1/cl201-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:02.581+02:00 | 
| apic11 | pod-1/cl202-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:08.264+02:00 | 
| apic11 | pod-1/cl209-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T16:55:12.934+02:00 | 
| apic11 | pod-1/cl210-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T16:55:06.883+02:00 | 
| apic11 | pod-1/rl301-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:13:40.873+02:00 | 
| apic11 | pod-1/rl302-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:13:53.167+02:00 | 
| apic11 | pod-1/s101-eu-spdc   | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:12:56.045+02:00 | 
| apic11 | pod-1/s102-eu-spdc   | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:12:57.357+02:00 | 
| apic21 | pod-1/bl2205-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:52:45.929+02:00 | 
| apic21 | pod-1/bl2206-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:52:46.222+02:00 | 
| apic21 | pod-1/cl2201-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:53:19.031+02:00 | 
| apic21 | pod-1/cl2202-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:53:16.885+02:00 | 
| apic21 | pod-1/cl2207-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:51:52.891+02:00 | 
| apic21 | pod-1/cl2208-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:51:59.278+02:00 | 
| apic21 | pod-1/cl2209-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T16:52:58.547+02:00 | 
| apic21 | pod-1/cl2210-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T16:53:10.455+02:00 | 
| apic21 | pod-1/rl2701-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T10:06:26.091+02:00 | 
| apic21 | pod-1/rl2702-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T10:06:04.714+02:00 | 
| apic21 | pod-1/s2101-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:51:30.452+02:00 | 
| apic21 | pod-1/s2102-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:51:25.329+02:00 | 
+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

Developer

```
# iserver get aci intf mgmt --apic dom:milan --node any

{
    "duration": 21545,
    "apic": {
        "read": true,
        "success": 70,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 68,
        "connect_time": 754,
        "disconnect_time": 0,
        "mo_time": 20119,
        "total_time": 20873
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

True	369	-	connect apic11o.emea-sp.cisco.com
True	298	13	apic11o.emea-sp.cisco.com class fabricNode
True	385	-	connect apic21o.emea-sp.cisco.com
True	306	15	apic21o.emea-sp.cisco.com class fabricNode
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	279	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	271	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	286	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	285	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	350	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/mgmtMgmtIf
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	279	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	282	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/mgmtMgmtIf
True	272	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	285	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	289	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/mgmtMgmtIf
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	307	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	281	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/mgmtMgmtIf
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	298	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/mgmtMgmtIf
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/mgmtMgmtIf
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	294	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/mgmtMgmtIf
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	322	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/mgmtMgmtIf
True	302	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	300	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2205/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	299	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/mgmtMgmtIf
True	297	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2206/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	280	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2206/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	298	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/mgmtMgmtIf
True	282	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2201/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	304	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2201/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	298	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/mgmtMgmtIf
True	289	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2202/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	295	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2202/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	282	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/mgmtMgmtIf
True	293	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2207/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	283	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2207/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	285	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/mgmtMgmtIf
True	332	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2208/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	302	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2208/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	299	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/mgmtMgmtIf
True	288	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2209/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	292	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2209/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	283	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/mgmtMgmtIf
True	287	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2210/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	286	0	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2210/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	291	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/mgmtMgmtIf
True	294	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2701/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	274	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2701/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	285	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/mgmtMgmtIf
True	293	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2702/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	319	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2702/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	289	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/mgmtMgmtIf
True	291	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2101/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	341	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2101/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	321	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/mgmtMgmtIf
True	293	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2102/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	299	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2102/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)