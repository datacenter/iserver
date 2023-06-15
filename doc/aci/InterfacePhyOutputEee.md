# Node Interface - Physical

## Eee focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view eee

Apic: apic11 (mode:online, cache:off)
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
    "duration": 1746,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 385,
        "disconnect_time": 0,
        "mo_time": 1212,
        "total_time": 1597
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

True	385	-	connect apic11o.emea-sp.cisco.com
True	298	13	apic11o.emea-sp.cisco.com class fabricNode
True	306	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	311	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	297	41	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys query query-target=subtree&target-subtree-class=l1EeeP
```

[[Back]](./InterfacePhy.md)