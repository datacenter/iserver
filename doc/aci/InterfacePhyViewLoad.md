# Node Interface - Physical

## Load interval focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view load

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+-----------------+-----------------+-----------------+
| Node                 | Interface | Oper | Load Interval 1 | Load Interval 2 | Load Interval 3 |
+----------------------+-----------+------+-----------------+-----------------+-----------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/3       | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/4       | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/5       | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/6       | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/7       | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/8       | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/9       | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/10      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/13      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/14      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/15      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/16      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/17      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/18      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/20      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/21      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/22      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/23      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/24      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/26      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/28      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/29      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/30      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/31      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/32      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/33      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/34      | down | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/35      | up   | 30              | 300             | 0               | 
| pod-1/bl2205-eu-spdc | 1/36      | up   | 30              | 300             | 0               | 
+----------------------+-----------+------+-----------------+-----------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view load

{
    "duration": 2853,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 1922,
        "total_time": 2336
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

True	414	-	connect apic21o.emea-sp.cisco.com:443
True	320	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	947	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	333	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	322	42	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=l1LoadP
```

[[Back]](./InterfacePhy.md)