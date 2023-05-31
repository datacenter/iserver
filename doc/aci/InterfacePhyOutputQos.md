# Node Interface - Physical

## QoS stats focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view ether

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+-------------+-----------+-----------+-------------+-------------+----------------+---------------+---------------+---------------+---------------+----------------+
| Node                | Interface | Oper | Packets     | Broadcast | Multicast | Rx          | Tx          | Size up to 64B | Size 65-1270B | Size 128-255B | Size 256-511B | Size 512-1023 | Size 1024-1518 |
+---------------------+-----------+------+-------------+-----------+-----------+-------------+-------------+----------------+---------------+---------------+---------------+---------------+----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | 48018275942 | 27431390  | 3582991   | 23993788604 | 24016443861 | 52             | 42632836600   | 7175123       | 12259496      | 5740249       | 5356569974     | 
| pod-1/bl205-eu-spdc | 1/2       | up   | 19059940    | 14602862  | 3569999   | 1023172     | 18036768    | 65             | 17683384      | 527212        | 766177        | 24            | 83063          | 
| pod-1/bl205-eu-spdc | 1/3       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/4       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/5       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/6       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/7       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/8       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/9       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/10      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/11      | up   | 1276746     | 115       | 1276631   | 638508      | 638238      | 31             | 106           | 510608        | 766001        | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/12      | up   | 1276737     | 141       | 1276596   | 638500      | 638237      | 42             | 192           | 510578        | 765925        | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/13      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/14      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/15      | up   | 511529      | 0         | 511529    | 256153      | 255376      | 0              | 256201        | 0             | 255328        | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | 104490971   | 10336500  | 515870    | 38792410    | 65698561    | 4611229        | 75666589      | 7645719       | 8921954       | 373           | 462            | 
| pod-1/bl205-eu-spdc | 1/17      | down | 14          | 3         | 11        | 8           | 6           | 1              | 8             | 0             | 5             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/18      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | 8578662     | 8169954   | 408708    | 203024      | 8375638     | 3722732        | 3844513       | 9             | 1011408       | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/20      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/21      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/22      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/23      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/24      | up   | 14334123490 | 29765     | 765996    | 9080174049  | 5253949441  | 4232146        | 4243440027    | 444684286     | 272800921     | 448843881     | 8811227367     | 
| pod-1/bl205-eu-spdc | 1/25      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/26      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/27      | up   | 5090239     | 0         | 5090188   | 4451880     | 638308      | 0              | 3813620       | 510635        | 765971        | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/28      | up   | 8066020380  | 3         | 767250    | 4457567002  | 3608453378  | 556962         | 7118166888    | 7918611       | 12379785      | 6417646       | 916883729      | 
| pod-1/bl205-eu-spdc | 1/29      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/30      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/31      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/32      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/33      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/34      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/35      | up   | 31547151117 | 1         | 296864086 | 14635463973 | 16911687144 | 14281919       | 482136653     | 23163637943   | 171147375     | 214711228     | 7284506877     | 
| pod-1/bl205-eu-spdc | 1/36      | up   | 31333982799 | 12        | 73202392  | 14430748041 | 16903234758 | 19056732       | 354144089     | 23245376273   | 206515227     | 223502875     | 7089039841     | 
+---------------------+-----------+------+-------------+-----------+-----------+-------------+-------------+----------------+---------------+---------------+---------------+---------------+----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view ether

{
    "duration": 13843,
    "apic": {
        "read": true,
        "success": 40,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 39,
        "connect_time": 407,
        "disconnect_time": 0,
        "mo_time": 12811,
        "total_time": 13218
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

True	407	-	connect apic11o.emea-sp.cisco.com
True	323	11	apic11o.emea-sp.cisco.com class fabricNode
True	314	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	332	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	308	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query query-target=children&target-subtree-class=rmonEtherStats
True	388	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query query-target=children&target-subtree-class=rmonEtherStats
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query query-target=children&target-subtree-class=rmonEtherStats
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query query-target=children&target-subtree-class=rmonEtherStats
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query query-target=children&target-subtree-class=rmonEtherStats
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query query-target=children&target-subtree-class=rmonEtherStats
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query query-target=children&target-subtree-class=rmonEtherStats
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query query-target=children&target-subtree-class=rmonEtherStats
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query query-target=children&target-subtree-class=rmonEtherStats
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query query-target=children&target-subtree-class=rmonEtherStats
True	312	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query query-target=children&target-subtree-class=rmonEtherStats
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query query-target=children&target-subtree-class=rmonEtherStats
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query query-target=children&target-subtree-class=rmonEtherStats
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query query-target=children&target-subtree-class=rmonEtherStats
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query query-target=children&target-subtree-class=rmonEtherStats
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query query-target=children&target-subtree-class=rmonEtherStats
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query query-target=children&target-subtree-class=rmonEtherStats
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query query-target=children&target-subtree-class=rmonEtherStats
True	288	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query query-target=children&target-subtree-class=rmonEtherStats
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query query-target=children&target-subtree-class=rmonEtherStats
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query query-target=children&target-subtree-class=rmonEtherStats
True	292	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query query-target=children&target-subtree-class=rmonEtherStats
True	280	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query query-target=children&target-subtree-class=rmonEtherStats
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query query-target=children&target-subtree-class=rmonEtherStats
True	514	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query query-target=children&target-subtree-class=rmonEtherStats
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query query-target=children&target-subtree-class=rmonEtherStats
True	387	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query query-target=children&target-subtree-class=rmonEtherStats
True	507	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query query-target=children&target-subtree-class=rmonEtherStats
True	421	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query query-target=children&target-subtree-class=rmonEtherStats
True	366	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query query-target=children&target-subtree-class=rmonEtherStats
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query query-target=children&target-subtree-class=rmonEtherStats
True	275	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query query-target=children&target-subtree-class=rmonEtherStats
True	282	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query query-target=children&target-subtree-class=rmonEtherStats
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query query-target=children&target-subtree-class=rmonEtherStats
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query query-target=children&target-subtree-class=rmonEtherStats
True	322	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query query-target=children&target-subtree-class=rmonEtherStats
```

[[Back]](./InterfacePhy.md)