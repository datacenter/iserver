# Node Interface - Physical

## QoS stats focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view ether

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+-----------+-----------+-----------+-----------+-----------+----------------+---------------+---------------+---------------+---------------+----------------+
| Node                 | Interface | Oper | Packets   | Broadcast | Multicast | Rx        | Tx        | Size up to 64B | Size 65-1270B | Size 128-255B | Size 256-511B | Size 512-1023 | Size 1024-1518 |
+----------------------+-----------+------+-----------+-----------+-----------+-----------+-----------+----------------+---------------+---------------+---------------+---------------+----------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | 622359    | 0         | 622359    | 311194    | 311163    | 0              | 0             | 248938        | 373421        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | 622345    | 0         | 622345    | 311180    | 311165    | 0              | 0             | 248933        | 373412        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/3       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/4       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/5       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/6       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/7       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/8       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/9       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/10      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | 622361    | 0         | 622361    | 311196    | 311165    | 0              | 0             | 248934        | 373427        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | 622345    | 0         | 622345    | 311179    | 311166    | 0              | 0             | 248934        | 373411        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/13      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/14      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/15      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/16      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/17      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/18      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | 5278271   | 4718382   | 559889    | 248725    | 5029546   | 0              | 4718382       | 373184        | 186705        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/20      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/21      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/22      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/23      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/24      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | 418893798 | 16        | 373423    | 354652541 | 64241257  | 5551172        | 214652874     | 71654026      | 10802518      | 6212462       | 91989034       | 
| pod-1/bl2205-eu-spdc | 1/26      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | 622339    | 0         | 622339    | 311175    | 311164    | 0              | 0             | 248934        | 373405        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/28      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/29      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/30      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/31      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/32      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/33      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/34      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/35      | up   | 270944654 | 8         | 10837997  | 57598836  | 213345818 | 7339970        | 75619382      | 99434845      | 10971350      | 5879166       | 48097477       | 
| pod-1/bl2205-eu-spdc | 1/36      | up   | 330881180 | 4         | 43327427  | 112079164 | 218802016 | 5632146        | 116278670     | 109089836     | 10481085      | 4512383       | 42955327       | 
+----------------------+-----------+------+-----------+-----------+-----------+-----------+-----------+----------------+---------------+---------------+---------------+---------------+----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view ether

{
    "duration": 2801,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 1791,
        "total_time": 2192
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

True	401	-	connect apic21o.emea-sp.cisco.com:443
True	299	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	881	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	300	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	311	58	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=rmonEtherStats
```

[[Back]](./InterfacePhy.md)