# Node Interface - Physical

## Ethernet stats focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view ether

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+----------+-----------+-----------+----------+----------+----------------+---------------+---------------+---------------+---------------+----------------+
| Node                | Interface | Oper | Packets  | Broadcast | Multicast | Rx       | Tx       | Size up to 64B | Size 65-1270B | Size 128-255B | Size 256-511B | Size 512-1023 | Size 1024-1518 |
+---------------------+-----------+------+----------+-----------+-----------+----------+----------+----------------+---------------+---------------+---------------+---------------+----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | 1426408  | 907110    | 50305     | 257299   | 1169109  | 0              | 1403689       | 9114          | 13605         | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | 739113   | 688810    | 50303     | 11335    | 727778   | 0              | 716396        | 9113          | 13604         | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/3       | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/4       | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/5       | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/6       | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/7       | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/8       | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/9       | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/10      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/11      | up   | 22670    | 0         | 22670     | 11336    | 11334    | 0              | 0             | 9069          | 13601         | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/12      | up   | 22678    | 9         | 22669     | 11344    | 11334    | 9              | 1             | 9068          | 13600         | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/13      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/14      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/15      | up   | 8110     | 260       | 7600      | 4072     | 4038     | 256            | 4070          | 0             | 3784          | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | 511292   | 153487    | 7817      | 184757   | 326535   | 232846         | 255042        | 15            | 23389         | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/17      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/18      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | 327889   | 320028    | 7853      | 170942   | 156947   | 235106         | 72073         | 15            | 20695         | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/20      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/21      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/22      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/23      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/24      | up   | 27452504 | 67        | 13606     | 10072280 | 17380224 | 92675          | 13375479      | 7686836       | 217344        | 311173        | 5753913        | 
| pod-1/bl205-eu-spdc | 1/25      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/26      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/27      | up   | 90602    | 0         | 90602     | 79269    | 11333    | 0              | 67934         | 9068          | 13600         | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/28      | up   | 109663   | 3         | 13620     | 16023    | 93640    | 9325           | 86687         | 6837          | 6806          | 6             | 2              | 
| pod-1/bl205-eu-spdc | 1/29      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/30      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/31      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/32      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/33      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/34      | down | 0        | 0         | 0         | 0        | 0        | 0              | 0             | 0             | 0             | 0             | 0              | 
| pod-1/bl205-eu-spdc | 1/35      | up   | 19379877 | 607       | 835067    | 13166218 | 6213659  | 350558         | 7146830       | 5102684       | 2682520       | 259922        | 599169         | 
| pod-1/bl205-eu-spdc | 1/36      | up   | 19316829 | 605       | 6200372   | 11946426 | 7370403  | 202159         | 9583249       | 5413407       | 469695        | 175404        | 1460675        | 
+---------------------+-----------+------+----------+-----------+-----------+----------+----------+----------------+---------------+---------------+---------------+---------------+----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view ether

{
    "duration": 1761,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 393,
        "disconnect_time": 0,
        "mo_time": 1209,
        "total_time": 1602
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

True	393	-	connect apic11o.emea-sp.cisco.com
True	300	13	apic11o.emea-sp.cisco.com class fabricNode
True	289	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	309	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	311	91	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys query query-target=subtree&target-subtree-class=rmonEtherStats
```

[[Back]](./InterfacePhy.md)