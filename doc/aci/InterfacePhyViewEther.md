# Node Interface - Physical

## Ethernet stats focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view ether

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+-----------+-----------+-----------+-----------+-----------+----------------+---------------+---------------+---------------+---------------+----------------+
| Node                 | Interface | Oper | Packets   | Broadcast | Multicast | Rx        | Tx        | Size up to 64B | Size 65-1270B | Size 128-255B | Size 256-511B | Size 512-1023 | Size 1024-1518 |
+----------------------+-----------+------+-----------+-----------+-----------+-----------+-----------+----------------+---------------+---------------+---------------+---------------+----------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | 622361    | 0         | 622361    | 311194    | 311165    | 0              | 0             | 248939        | 373422        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | 622349    | 0         | 622349    | 311182    | 311167    | 0              | 0             | 248935        | 373414        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/3       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/4       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/5       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/6       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/7       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/8       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/9       | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/10      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | 622363    | 0         | 622363    | 311196    | 311167    | 0              | 0             | 248935        | 373428        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | 622349    | 0         | 622349    | 311181    | 311168    | 0              | 0             | 248936        | 373413        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/13      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/14      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/15      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/16      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/17      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/18      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | 5278304   | 4718412   | 559892    | 248726    | 5029578   | 0              | 4718412       | 373186        | 186706        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/20      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/21      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/22      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/23      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/24      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | 418895631 | 16        | 373425    | 354654298 | 64241333  | 5551190        | 214654149     | 71654535      | 10802524      | 6212471       | 91989050       | 
| pod-1/bl2205-eu-spdc | 1/26      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | 622342    | 0         | 622342    | 311176    | 311166    | 0              | 0             | 248935        | 373407        | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/28      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/29      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/30      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/31      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/32      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/33      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/34      | down | 0         | 0         | 0         | 0         | 0         | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl2205-eu-spdc | 1/35      | up   | 270945783 | 8         | 10838057  | 57599027  | 213346756 | 7340006        | 75619653      | 99434982      | 10971398      | 5879173       | 48097493       | 
| pod-1/bl2205-eu-spdc | 1/36      | up   | 330884003 | 4         | 43327654  | 112080037 | 218803966 | 5632463        | 116279761     | 109090855     | 10481143      | 4512402       | 42955337       | 
+----------------------+-----------+------+-----------+-----------+-----------+-----------+-----------+----------------+---------------+---------------+---------------+---------------+----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view ether

{
    "duration": 3233,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 483,
        "disconnect_time": 0,
        "mo_time": 2186,
        "total_time": 2669
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

True	483	-	connect apic21o.emea-sp.cisco.com:443
True	363	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1121	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	354	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	348	58	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=rmonEtherStats
```

[[Back]](./InterfacePhy.md)