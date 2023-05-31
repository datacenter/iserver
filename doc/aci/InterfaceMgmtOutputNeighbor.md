# Node Interface - Management

## Neighbor (cdp/lldp) focused view

```
# iserver get aci intf mgmt --apic apic11 --node any --view nei

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

+---------------------+-------+-------------+-----------+----------------+-------------------+--------------+-------------------------------+--------------+
| Node                | Name  | Admin State | OperState | CDP - Platform | CDP - System Name | CDP - Port   | LLDP - System Name            | LLDP - Port  |
+---------------------+-------+-------------+-----------+----------------+-------------------+--------------+-------------------------------+--------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/27 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/27 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/28 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/28 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/25 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/25 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | up        | N9K-C92348GC-X | r22-eu-spdc       | Ethernet1/26 | r22-eu-spdc.emea-sp.cisco.com | Ethernet1/26 | 
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
    "duration": 14336,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 490,
        "disconnect_time": 0,
        "mo_time": 13322,
        "total_time": 13812
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

True	490	-	connect apic11o.emea-sp.cisco.com
True	323	11	apic11o.emea-sp.cisco.com class fabricNode
True	303	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	301	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	307	13	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	316	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	305	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	308	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	367	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	300	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	306	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	362	43	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	306	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/mgmtMgmtIf
True	325	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	347	43	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	360	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	303	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/mgmtMgmtIf
True	335	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	311	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	354	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	353	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/mgmtMgmtIf
True	317	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	380	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	360	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	348	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/mgmtMgmtIf
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	327	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	348	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/mgmtMgmtIf
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	341	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)