# Node Interface - Management

## Neighbor (cdp/lldp) focused view

```
# iserver get aci intf mgmt --apic apic11 --node any --view nei

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

+---------------------+-------+-------------+-----------+----------------+-------------------+--------------+-------------------------------+--------------+
| Node                | Name  | Admin State | OperState | CDP - Platform | CDP - System Name | CDP - Port   | LLDP - System Name            | LLDP - Port  |
+---------------------+-------+-------------+-----------+----------------+-------------------+--------------+-------------------------------+--------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/27 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/27 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/28 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/28 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/25 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/25 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/26 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/26 | 
| pod-1/cl209-eu-spdc | mgmt0 | up          | up        |                |                   |              |                               |              | 
| pod-1/cl210-eu-spdc | mgmt0 | up          | up        |                |                   |              |                               |              | 
| pod-1/rl301-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r23-eu-spdc       | Ethernet1/41 | r23-eu-spdc.emea-sp.cisco.com | Ethernet1/41 | 
| pod-1/rl302-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r23-eu-spdc       | Ethernet1/42 | r23-eu-spdc.emea-sp.cisco.com | Ethernet1/42 | 
| pod-1/s101-eu-spdc  | mgmt0 | up          | up        | N9K-C92348GC-X | r23-eu-spdc       | Ethernet1/39 | r23-eu-spdc.emea-sp.cisco.com | Ethernet1/39 | 
| pod-1/s102-eu-spdc  | mgmt0 | up          | up        | N9K-C92348GC-X | r23-eu-spdc       | Ethernet1/40 | r23-eu-spdc.emea-sp.cisco.com | Ethernet1/40 | 
+---------------------+-------+-------------+-----------+----------------+-------------------+--------------+-------------------------------+--------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic11 --node any --view nei

{
    "duration": 16286,
    "apic": {
        "read": true,
        "success": 52,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 51,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 15393,
        "total_time": 15810
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

True	417	-	connect apic11o.emea-sp.cisco.com
True	328	13	apic11o.emea-sp.cisco.com class fabricNode
True	307	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	285	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	299	13	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	298	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	290	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	283	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	299	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	279	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	279	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	286	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	310	43	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	282	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/mgmtMgmtIf
True	295	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	323	43	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	308	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/mgmtMgmtIf
True	298	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	281	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	291	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	287	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/mgmtMgmtIf
True	302	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	338	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	321	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/mgmtMgmtIf
True	299	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	299	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	319	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/mgmtMgmtIf
True	295	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	297	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	289	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/mgmtMgmtIf
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	318	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	279	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/mgmtMgmtIf
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	316	7	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)