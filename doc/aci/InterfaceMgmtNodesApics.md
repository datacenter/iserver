# Node Interface - Management

## Multi-APIC

```
# iserver get aci intf mgmt --apic dom:milan --node any

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
Apic: apic21o.emea-sp.cisco.com
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Apic   | Node                 | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| apic11 | pod-1/bl205-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:13:34.502+02:00 | 
| apic11 | pod-1/bl206-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:37:10.362+02:00 | 
| apic11 | pod-1/cl201-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:15:14.143+02:00 | 
| apic11 | pod-1/cl202-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:39:11.176+02:00 | 
| apic11 | pod-1/rl301-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:10:01.724+02:00 | 
| apic11 | pod-1/rl302-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:33:50.626+02:00 | 
| apic11 | pod-1/s101-eu-spdc   | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:12:44.643+02:00 | 
| apic11 | pod-1/s102-eu-spdc   | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-04-28T11:27:42.302+02:00 | 
| apic21 | pod-1/bl2205-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:42:07.364+02:00 | 
| apic21 | pod-1/bl2206-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:20:58.587+02:00 | 
| apic21 | pod-1/cl2201-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:40:11.007+02:00 | 
| apic21 | pod-1/cl2202-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:18:48.158+02:00 | 
| apic21 | pod-1/cl2207-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:39:24.929+02:00 | 
| apic21 | pod-1/cl2208-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:18:36.886+02:00 | 
| apic21 | pod-1/rl2701-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:44:47.287+02:00 | 
| apic21 | pod-1/rl2702-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:18:07.223+02:00 | 
| apic21 | pod-1/s2101-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:35:07.559+02:00 | 
| apic21 | pod-1/s2102-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:14:04.440+02:00 | 
+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

Developer

```
# iserver get aci intf mgmt --apic dom:milan --node any

{
    "duration": 19594,
    "apic": {
        "read": true,
        "success": 58,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 56,
        "connect_time": 777,
        "disconnect_time": 0,
        "mo_time": 18097,
        "total_time": 18874
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

True	388	-	connect apic11o.emea-sp.cisco.com
True	389	-	connect apic21o.emea-sp.cisco.com
True	368	11	apic11o.emea-sp.cisco.com class fabricNode
True	335	13	apic21o.emea-sp.cisco.com class fabricNode
True	301	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	293	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	359	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	304	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/mgmtMgmtIf
True	394	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	401	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/mgmtMgmtIf
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	315	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/mgmtMgmtIf
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	299	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/mgmtMgmtIf
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	308	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/mgmtMgmtIf
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	353	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/mgmtMgmtIf
True	315	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2205/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	354	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2205/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	319	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/mgmtMgmtIf
True	324	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2206/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	335	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2206/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	315	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/mgmtMgmtIf
True	305	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2201/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	355	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2201/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	318	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/mgmtMgmtIf
True	323	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2202/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	319	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2202/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	357	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/mgmtMgmtIf
True	330	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2207/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	326	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2207/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	341	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/mgmtMgmtIf
True	280	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2208/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	330	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2208/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	342	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/mgmtMgmtIf
True	319	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2701/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	332	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2701/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	297	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/mgmtMgmtIf
True	329	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2702/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	312	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2702/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	326	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/mgmtMgmtIf
True	308	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2101/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	310	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2101/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	303	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/mgmtMgmtIf
True	312	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2102/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	294	1	apic21o.emea-sp.cisco.com mo topology/pod-1/node-2102/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)