# Node Interface - Physical

## Eee focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view eee

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+----------+------------+----------------+
| Node                | Interface | Oper | Eee Lat  | Eee Lpi    | Eee State      |
+---------------------+-----------+------+----------+------------+----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/2       | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/3       | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/4       | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/5       | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/6       | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/7       | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/8       | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/9       | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/10      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/11      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/12      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/13      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/14      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/15      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/16      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/17      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/18      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/19      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/20      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/21      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/22      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/23      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/24      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/25      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/26      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/27      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/28      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/29      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/30      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/31      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/32      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/33      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/34      | down | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/35      | up   | variable | aggressive | not-applicable | 
| pod-1/bl205-eu-spdc | 1/36      | up   | variable | aggressive | not-applicable | 
+---------------------+-----------+------+----------+------------+----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view eee

{
    "duration": 14925,
    "apic": {
        "read": true,
        "success": 40,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 39,
        "connect_time": 568,
        "disconnect_time": 0,
        "mo_time": 13634,
        "total_time": 14202
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

True	568	-	connect apic11o.emea-sp.cisco.com
True	491	11	apic11o.emea-sp.cisco.com class fabricNode
True	479	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	604	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	500	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query query-target=children&target-subtree-class=l1EeeP
True	383	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query query-target=children&target-subtree-class=l1EeeP
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query query-target=children&target-subtree-class=l1EeeP
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query query-target=children&target-subtree-class=l1EeeP
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query query-target=children&target-subtree-class=l1EeeP
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query query-target=children&target-subtree-class=l1EeeP
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query query-target=children&target-subtree-class=l1EeeP
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query query-target=children&target-subtree-class=l1EeeP
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query query-target=children&target-subtree-class=l1EeeP
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query query-target=children&target-subtree-class=l1EeeP
True	348	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query query-target=children&target-subtree-class=l1EeeP
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query query-target=children&target-subtree-class=l1EeeP
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query query-target=children&target-subtree-class=l1EeeP
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query query-target=children&target-subtree-class=l1EeeP
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query query-target=children&target-subtree-class=l1EeeP
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query query-target=children&target-subtree-class=l1EeeP
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query query-target=children&target-subtree-class=l1EeeP
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query query-target=children&target-subtree-class=l1EeeP
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query query-target=children&target-subtree-class=l1EeeP
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query query-target=children&target-subtree-class=l1EeeP
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query query-target=children&target-subtree-class=l1EeeP
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query query-target=children&target-subtree-class=l1EeeP
True	364	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query query-target=children&target-subtree-class=l1EeeP
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query query-target=children&target-subtree-class=l1EeeP
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query query-target=children&target-subtree-class=l1EeeP
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query query-target=children&target-subtree-class=l1EeeP
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query query-target=children&target-subtree-class=l1EeeP
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query query-target=children&target-subtree-class=l1EeeP
True	404	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query query-target=children&target-subtree-class=l1EeeP
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query query-target=children&target-subtree-class=l1EeeP
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query query-target=children&target-subtree-class=l1EeeP
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query query-target=children&target-subtree-class=l1EeeP
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query query-target=children&target-subtree-class=l1EeeP
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query query-target=children&target-subtree-class=l1EeeP
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query query-target=children&target-subtree-class=l1EeeP
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query query-target=children&target-subtree-class=l1EeeP
```

[[Back]](./InterfacePhy.md)