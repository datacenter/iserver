# Node Interface - Physical

## Ethernet error stats focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view err

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
| Node                 | Interface | Oper | Oversize | Undersize | Rx giant | Rx oversize | Tx giant | Tx oversize | Collisions | CRC errors | Drops |
+----------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/3       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/4       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/5       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/6       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/7       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/8       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/9       | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/10      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/13      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/14      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/15      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/16      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/17      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/18      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/20      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/21      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/22      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/23      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/24      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | 18031891 | 0         | 0        | 16371547    | 0        | 1660344     | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/26      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/28      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/29      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/30      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/31      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/32      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/33      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/34      | down | 0        | 0         | 0        | 0           | 0        | 0           | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/35      | up   | 23603704 | 0         | 0        | 91082       | 0        | 23512622    | 0          | 0          | 0     | 
| pod-1/bl2205-eu-spdc | 1/36      | up   | 41932389 | 0         | 0        | 34105117    | 0        | 7827272     | 0          | 0          | 0     | 
+----------------------+-----------+------+----------+-----------+----------+-------------+----------+-------------+------------+------------+-------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view err

{
    "duration": 2786,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 1849,
        "total_time": 2231
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

True	382	-	connect apic21o.emea-sp.cisco.com:443
True	317	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	943	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	300	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	289	58	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=rmonEtherStats
```

[[Back]](./InterfacePhy.md)