# Node Interface - Physical

## Ethernet error stats focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view err

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
| Node                | Interface | Oper | Oversize | Undersize | Rx giant | Rx oversize | Tx giant | Tx oversize | Collisions | CRC errors | Drops |
+---------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
| pod-1/bl205-eu-spdc | 1/1       | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/2       | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/3       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/4       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/5       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/6       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/7       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/8       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/9       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/10      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/11      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/12      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/13      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/14      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/15      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/16      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/17      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/18      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/19      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/20      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/21      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/22      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/23      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/24      | up   | 15084    | 0         | 0        | 15076       | 0        | 8           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/25      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/26      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/27      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/28      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/29      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/30      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/31      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/32      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/33      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/34      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/35      | up   | 3238304  | 0         | 0        | 2872656     | 0        | 365648      | 0          | 0          | 0     | 
| pod-1/bl205-eu-spdc | 1/36      | up   | 2012380  | 0         | 0        | 1676792     | 0        | 335588      | 0          | 0          | 0     | 
+---------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view err

{
    "duration": 1837,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 1254,
        "total_time": 1659
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
True	308	13	apic11o.emea-sp.cisco.com class fabricNode
True	311	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	315	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	320	91	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys query query-target=subtree&target-subtree-class=rmonEtherStats
```

[[Back]](./InterfacePhy.md)