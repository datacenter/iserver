# Node Interface - Physical

## Ethernet error stats focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view err

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+-----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
| Node                | Interface | Oper | Oversize  | Undersize | Rx giant | Rx oversize | Tx giant | Tx oversize | Collisions | CRC errors | Drops |
+---------------------+-----------+------+-----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
| pod-1/bl205-eu-spdc | 1/1       | up   | 3694448   | 0         | 0        | 127256      | 0        | 3567192     | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/2       | up   | 15        | 0         | 0        | 15          | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/3       | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/4       | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/5       | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/6       | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/7       | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/8       | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/9       | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/10      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/11      | up   | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/12      | up   | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/13      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/14      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/15      | up   | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/16      | up   | 7644673   | 0         | 0        | 7644673     | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/17      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/18      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/19      | up   | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/20      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/21      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/22      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/23      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/24      | up   | 108895836 | 0         | 0        | 103531454   | 0        | 5364382     | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/25      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/26      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/27      | up   | 13        | 0         | 13       | 13          | 0        | 0           | 0          | 38         | 0     | 
| pod-1/bl205-eu-spdc | 1/28      | up   | 3696759   | 0         | 0        | 128102      | 0        | 3568657     | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/29      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/30      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/31      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/32      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/33      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/34      | down | 0         | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/35      | up   | 216730344 | 0         | 0        | 75444889    | 0        | 141285455   | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/36      | up   | 196349344 | 0         | 0        | 84577410    | 0        | 111771934   | 0          | 0          | 0     | 
+---------------------+-----------+------+-----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view err

{
    "duration": 13814,
    "apic": {
        "read": true,
        "success": 40,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 39,
        "connect_time": 458,
        "disconnect_time": 0,
        "mo_time": 12672,
        "total_time": 13130
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

True	458	-	connect apic11o.emea-sp.cisco.com
True	310	11	apic11o.emea-sp.cisco.com class fabricNode
True	329	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	294	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	295	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query query-target=children&target-subtree-class=rmonEtherStats
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query query-target=children&target-subtree-class=rmonEtherStats
True	359	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query query-target=children&target-subtree-class=rmonEtherStats
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query query-target=children&target-subtree-class=rmonEtherStats
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query query-target=children&target-subtree-class=rmonEtherStats
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query query-target=children&target-subtree-class=rmonEtherStats
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query query-target=children&target-subtree-class=rmonEtherStats
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query query-target=children&target-subtree-class=rmonEtherStats
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query query-target=children&target-subtree-class=rmonEtherStats
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query query-target=children&target-subtree-class=rmonEtherStats
True	305	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query query-target=children&target-subtree-class=rmonEtherStats
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query query-target=children&target-subtree-class=rmonEtherStats
True	278	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query query-target=children&target-subtree-class=rmonEtherStats
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query query-target=children&target-subtree-class=rmonEtherStats
True	283	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query query-target=children&target-subtree-class=rmonEtherStats
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query query-target=children&target-subtree-class=rmonEtherStats
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query query-target=children&target-subtree-class=rmonEtherStats
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query query-target=children&target-subtree-class=rmonEtherStats
True	397	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query query-target=children&target-subtree-class=rmonEtherStats
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query query-target=children&target-subtree-class=rmonEtherStats
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query query-target=children&target-subtree-class=rmonEtherStats
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query query-target=children&target-subtree-class=rmonEtherStats
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query query-target=children&target-subtree-class=rmonEtherStats
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query query-target=children&target-subtree-class=rmonEtherStats
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query query-target=children&target-subtree-class=rmonEtherStats
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query query-target=children&target-subtree-class=rmonEtherStats
True	382	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query query-target=children&target-subtree-class=rmonEtherStats
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query query-target=children&target-subtree-class=rmonEtherStats
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query query-target=children&target-subtree-class=rmonEtherStats
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query query-target=children&target-subtree-class=rmonEtherStats
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query query-target=children&target-subtree-class=rmonEtherStats
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query query-target=children&target-subtree-class=rmonEtherStats
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query query-target=children&target-subtree-class=rmonEtherStats
True	350	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query query-target=children&target-subtree-class=rmonEtherStats
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query query-target=children&target-subtree-class=rmonEtherStats
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query query-target=children&target-subtree-class=rmonEtherStats
```

[[Back]](./InterfacePhy.md)