# Node Interface - Management

## Address focused view

```
# iserver get aci intf mgmt --apic apic11 --node any --view addr

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

+---------------------+-------+-------------+-----------+-------------------+-----------------+-------------------+
| Node                | Name  | Admin State | OperState | MAC Address       | IP Address      | Router MAC        |
+---------------------+-------+-------------+-----------+-------------------+-----------------+-------------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | up        | 4C:71:0D:7E:83:F0 | 10.58.28.145/27 | 4C:71:0D:7E:83:F0 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | up        | 3C:13:CC:C9:EC:B0 | 10.58.28.146/27 | 3C:13:CC:C9:EC:B0 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | up        | 4C:71:0D:23:FA:38 | 10.58.28.141/27 | 4C:71:0D:23:FA:38 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | up        | 10:B3:D5:B5:62:1C | 10.58.28.142/27 | 10:B3:D5:B5:62:1C | 
| pod-1/cl209-eu-spdc | mgmt0 | up          | up        | C0:F8:7F:FE:0F:E0 |                 | C0:F8:7F:FE:0F:E0 | 
| pod-1/cl210-eu-spdc | mgmt0 | up          | up        | C0:F8:7F:FE:10:B0 |                 | C0:F8:7F:FE:10:B0 | 
| pod-1/rl301-eu-spdc | mgmt0 | up          | up        | A0:B4:39:4A:2B:44 | 10.58.28.135/27 | A0:B4:39:4A:2B:44 | 
| pod-1/rl302-eu-spdc | mgmt0 | up          | up        | A0:B4:39:4A:2D:18 | 10.58.28.136/27 | A0:B4:39:4A:2D:18 | 
| pod-1/s101-eu-spdc  | mgmt0 | up          | up        | 4C:71:0D:55:D1:CC | 10.58.28.151/27 | 4C:71:0D:55:D1:CC | 
| pod-1/s102-eu-spdc  | mgmt0 | up          | up        | 8C:94:1F:FA:54:20 | 10.58.28.152/27 | 8C:94:1F:FA:54:20 | 
+---------------------+-------+-------------+-----------+-------------------+-----------------+-------------------+
```

Developer

```
# iserver get aci intf mgmt --apic apic11 --node any --view addr

{
    "duration": 9942,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 9251,
        "total_time": 9656
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

True	405	-	connect apic11o.emea-sp.cisco.com
True	336	13	apic11o.emea-sp.cisco.com class fabricNode
True	283	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	284	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	281	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	290	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	385	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	290	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/mgmtMgmtIf
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	286	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/mgmtMgmtIf
True	285	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	340	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	282	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/mgmtMgmtIf
True	290	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	308	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	303	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/mgmtMgmtIf
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	281	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	298	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/mgmtMgmtIf
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	291	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/mgmtMgmtIf
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	283	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/mgmtMgmtIf
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)