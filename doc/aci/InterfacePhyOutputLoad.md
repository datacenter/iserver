# Node Interface - Physical

## Load interval focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view load

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+-----------------+-----------------+-----------------+
| Node                | Interface | Oper | Load Interval 1 | Load Interval 2 | Load Interval 3 |
+---------------------+-----------+------+-----------------+-----------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/2       | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/3       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/4       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/5       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/6       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/7       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/8       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/9       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/10      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/11      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/12      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/13      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/14      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/15      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/16      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/17      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/18      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/19      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/20      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/21      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/22      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/23      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/24      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/25      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/26      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/27      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/28      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/29      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/30      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/31      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/32      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/33      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/34      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/35      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/36      | up   | 30              | 300             | 0               | 
+---------------------+-----------+------+-----------------+-----------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view load

{
    "duration": 13887,
    "apic": {
        "read": true,
        "success": 40,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 39,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 12854,
        "total_time": 13264
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

True	410	-	connect apic11o.emea-sp.cisco.com
True	303	11	apic11o.emea-sp.cisco.com class fabricNode
True	318	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	303	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query query-target=children&target-subtree-class=l1LoadP
True	409	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query query-target=children&target-subtree-class=l1LoadP
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query query-target=children&target-subtree-class=l1LoadP
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query query-target=children&target-subtree-class=l1LoadP
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query query-target=children&target-subtree-class=l1LoadP
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query query-target=children&target-subtree-class=l1LoadP
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query query-target=children&target-subtree-class=l1LoadP
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query query-target=children&target-subtree-class=l1LoadP
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query query-target=children&target-subtree-class=l1LoadP
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query query-target=children&target-subtree-class=l1LoadP
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query query-target=children&target-subtree-class=l1LoadP
True	385	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query query-target=children&target-subtree-class=l1LoadP
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query query-target=children&target-subtree-class=l1LoadP
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query query-target=children&target-subtree-class=l1LoadP
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query query-target=children&target-subtree-class=l1LoadP
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query query-target=children&target-subtree-class=l1LoadP
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query query-target=children&target-subtree-class=l1LoadP
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query query-target=children&target-subtree-class=l1LoadP
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query query-target=children&target-subtree-class=l1LoadP
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query query-target=children&target-subtree-class=l1LoadP
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query query-target=children&target-subtree-class=l1LoadP
True	319	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query query-target=children&target-subtree-class=l1LoadP
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query query-target=children&target-subtree-class=l1LoadP
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query query-target=children&target-subtree-class=l1LoadP
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query query-target=children&target-subtree-class=l1LoadP
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query query-target=children&target-subtree-class=l1LoadP
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query query-target=children&target-subtree-class=l1LoadP
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query query-target=children&target-subtree-class=l1LoadP
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query query-target=children&target-subtree-class=l1LoadP
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query query-target=children&target-subtree-class=l1LoadP
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query query-target=children&target-subtree-class=l1LoadP
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query query-target=children&target-subtree-class=l1LoadP
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query query-target=children&target-subtree-class=l1LoadP
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query query-target=children&target-subtree-class=l1LoadP
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query query-target=children&target-subtree-class=l1LoadP
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query query-target=children&target-subtree-class=l1LoadP
```

[[Back]](./InterfacePhy.md)