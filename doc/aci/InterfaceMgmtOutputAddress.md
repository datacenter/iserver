# Node Interface - Management

## Address focused view

```
# iserver get aci intf mgmt --apic apic11 --node any --view addr

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

+---------------------+-------+-------------+-----------+-------------------+-----------------+-------------------+
| Node                | Name  | Admin State | OperState | MAC Address       | IP Address      | Router MAC        |
+---------------------+-------+-------------+-----------+-------------------+-----------------+-------------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | up        | 4C:71:0D:7E:83:F0 | 10.58.28.145/27 | 4C:71:0D:7E:83:F0 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | up        | 3C:13:CC:C9:EC:B0 | 10.58.28.146/27 | 3C:13:CC:C9:EC:B0 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | up        | 4C:71:0D:23:FA:38 | 10.58.28.141/27 | 4C:71:0D:23:FA:38 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | up        | 10:B3:D5:B5:62:1C | 10.58.28.142/27 | 10:B3:D5:B5:62:1C | 
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
    "duration": 9453,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 440,
        "disconnect_time": 0,
        "mo_time": 8644,
        "total_time": 9084
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

True	440	-	connect apic11o.emea-sp.cisco.com
True	304	11	apic11o.emea-sp.cisco.com class fabricNode
True	297	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/mgmtMgmtIf
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	355	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/mgmtMgmtIf
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	314	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	452	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/mgmtMgmtIf
True	405	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	312	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/mgmtMgmtIf
True	455	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	373	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	476	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/mgmtMgmtIf
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	352	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/mgmtMgmtIf
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	295	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/mgmtMgmtIf
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
True	369	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/mgmtMgmtIf
True	343	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/mgmt-[mgmt0] query query-target=children&target-subtree-class=imMgmtIf
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/ipv4/inst/dom-management/if-[mgmt0] query query-target=children&target-subtree-class=ipv4Addr
```

[[Back]](./InterfaceMgmt.md)