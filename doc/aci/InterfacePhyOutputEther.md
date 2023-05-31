# Node Interface - Physical

## Ethernet stats focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view ether

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+-------------+-----------+-----------+-------------+-------------+----------------+---------------+---------------+---------------+---------------+----------------+
| Node                | Interface | Oper | Packets     | Broadcast | Multicast | Rx          | Tx          | Size up to 64B | Size 65-1270B | Size 128-255B | Size 256-511B | Size 512-1023 | Size 1024-1518 |
+---------------------+-----------+------+-------------+-----------+-----------+-------------+-------------+----------------+---------------+---------------+---------------+---------------+----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | 48018401836 | 27431450  | 3582998   | 23993851624 | 24016506735 | 52             | 42632948632   | 7175131       | 12259504      | 5740256       | 5356583813     | 
| pod-1/bl205-eu-spdc | 1/2       | up   | 19059965    | 14602879  | 3570007   | 1023174     | 18036791    | 65             | 17683405      | 527214        | 766179        | 24            | 83063          | 
| pod-1/bl205-eu-spdc | 1/3       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/4       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/5       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/6       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/7       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/8       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/9       | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/10      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/11      | up   | 1276750     | 115       | 1276635   | 638510      | 638240      | 31             | 106           | 510610        | 766003        | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/12      | up   | 1276740     | 141       | 1276599   | 638501      | 638239      | 42             | 192           | 510580        | 765926        | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/13      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/14      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/15      | up   | 511531      | 0         | 511531    | 256154      | 255377      | 0              | 256202        | 0             | 255329        | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | 104491231   | 10336526  | 515872    | 38792506    | 65698725    | 4611241        | 75666777      | 7645738       | 8921976       | 373           | 462            | 
| pod-1/bl205-eu-spdc | 1/17      | down | 14          | 3         | 11        | 8           | 6           | 1              | 8             | 0             | 5             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/18      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | 8578690     | 8169980   | 408710    | 203025      | 8375665     | 3722744        | 3844526       | 9             | 1011411       | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/20      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/21      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/22      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/23      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/24      | up   | 14334132698 | 29765     | 765999    | 9080178474  | 5253954224  | 4232153        | 4243444706    | 444686432     | 272801158     | 448844043     | 8811228727     | 
| pod-1/bl205-eu-spdc | 1/25      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/26      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/27      | up   | 5090253     | 0         | 5090202   | 4451892     | 638310      | 0              | 3813630       | 510637        | 765973        | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/28      | up   | 8066041245  | 3         | 767252    | 4457578394  | 3608462851  | 556964         | 7118185471    | 7918617       | 12379787      | 6417648       | 916885999      | 
| pod-1/bl205-eu-spdc | 1/29      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/30      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/31      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/32      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/33      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/34      | down | 0           | 0         | 0         | 0           | 0           | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/35      | up   | 31547221024 | 1         | 296864842 | 14635498982 | 16911722042 | 14281945       | 482139273     | 23163695765   | 171147649     | 214711354     | 7284515299     | 
| pod-1/bl205-eu-spdc | 1/36      | up   | 31334054210 | 12        | 73202609  | 14430783319 | 16903270891 | 19056865       | 354145926     | 23245435352   | 206516191     | 223503084     | 7089048244     | 
+---------------------+-----------+------+-------------+-----------+-----------+-------------+-------------+----------------+---------------+---------------+---------------+---------------+----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view ether

{
    "duration": 13737,
    "apic": {
        "read": true,
        "success": 40,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 39,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 12712,
        "total_time": 13111
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

True	399	-	connect apic11o.emea-sp.cisco.com
True	319	11	apic11o.emea-sp.cisco.com class fabricNode
True	312	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	320	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query query-target=children&target-subtree-class=rmonEtherStats
True	455	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query query-target=children&target-subtree-class=rmonEtherStats
True	313	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query query-target=children&target-subtree-class=rmonEtherStats
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query query-target=children&target-subtree-class=rmonEtherStats
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query query-target=children&target-subtree-class=rmonEtherStats
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query query-target=children&target-subtree-class=rmonEtherStats
True	311	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query query-target=children&target-subtree-class=rmonEtherStats
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query query-target=children&target-subtree-class=rmonEtherStats
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query query-target=children&target-subtree-class=rmonEtherStats
True	358	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query query-target=children&target-subtree-class=rmonEtherStats
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query query-target=children&target-subtree-class=rmonEtherStats
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query query-target=children&target-subtree-class=rmonEtherStats
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query query-target=children&target-subtree-class=rmonEtherStats
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query query-target=children&target-subtree-class=rmonEtherStats
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query query-target=children&target-subtree-class=rmonEtherStats
True	300	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query query-target=children&target-subtree-class=rmonEtherStats
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query query-target=children&target-subtree-class=rmonEtherStats
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query query-target=children&target-subtree-class=rmonEtherStats
True	380	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query query-target=children&target-subtree-class=rmonEtherStats
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query query-target=children&target-subtree-class=rmonEtherStats
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query query-target=children&target-subtree-class=rmonEtherStats
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query query-target=children&target-subtree-class=rmonEtherStats
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query query-target=children&target-subtree-class=rmonEtherStats
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query query-target=children&target-subtree-class=rmonEtherStats
True	382	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query query-target=children&target-subtree-class=rmonEtherStats
True	309	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query query-target=children&target-subtree-class=rmonEtherStats
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query query-target=children&target-subtree-class=rmonEtherStats
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query query-target=children&target-subtree-class=rmonEtherStats
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query query-target=children&target-subtree-class=rmonEtherStats
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query query-target=children&target-subtree-class=rmonEtherStats
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query query-target=children&target-subtree-class=rmonEtherStats
True	310	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query query-target=children&target-subtree-class=rmonEtherStats
True	306	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query query-target=children&target-subtree-class=rmonEtherStats
True	304	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query query-target=children&target-subtree-class=rmonEtherStats
True	294	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query query-target=children&target-subtree-class=rmonEtherStats
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query query-target=children&target-subtree-class=rmonEtherStats
```

[[Back]](./InterfacePhy.md)