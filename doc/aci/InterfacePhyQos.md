# Node Interface - Physical

## Filter by QoS stats

Example: ports with data

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --qos data
    --view qos

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+---------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
| Node                | Interface | Admin | Oper | Class         | Rx Admit [B] | Rx Admin | Rx Drop [B] | Rx Drop | Tx Admit [B] | Tx Admin | Tx Drop [B] | Tx Drop |
+---------------------+-----------+-------+------+---------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
| pod-1/bl205-eu-spdc | eth1/1    | up    | up   | control-plane | 39121848     | 315153   | 0           | 0       | 119765577    | 1497448  | 0           | 0       | 
|                     |           |       |      | level3        | 11492        | 169      | 0           | 0       | 3347786      | 37427    | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/2    | up    | up   | control-plane | 3811928      | 13453    | 0           | 0       | 68731495     | 964512   | 0           | 0       | 
|                     |           |       |      | level3        | 0            | 0        | 0           | 0       | 3347786      | 37427    | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/11   | up    | up   | control-plane | 3757877      | 13451    | 0           | 0       | 4051277      | 13451    | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/12   | up    | up   | control-plane | 3758156      | 13452    | 0           | 0       | 4051591      | 13452    | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/15   | up    | up   | control-plane | 424342       | 4958     | 0           | 0       | 2157788      | 4945     | 0           | 0       | 
|                     |           |       |      | level3        | 1104         | 14       | 0           | 0       | 0            | 0        | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/16   | up    | up   | control-plane | 562741       | 7118     | 0           | 0       | 7967489      | 90376    | 0           | 0       | 
|                     |           |       |      | level3        | 14411102     | 219017   | 0           | 0       | 29037243     | 309323   | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/19   | up    | up   | control-plane | 405509       | 4657     | 0           | 0       | 7837457      | 87919    | 0           | 0       | 
|                     |           |       |      | level3        | 5252         | 64       | 0           | 0       | 11466860     | 104197   | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/24   | up    | up   | control-plane | 35267395     | 393244   | 0           | 0       | 7793680525   | 11158742 | 0           | 0       | 
|                     |           |       |      | level3        | 2745925319   | 12302601 | 0           | 0       | 3327776863   | 10178280 | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/27   | up    | up   | control-plane | 2900358      | 13453    | 0           | 0       | 4011108      | 13451    | 0           | 0       | 
|                     |           |       |      | policy-plane  | 0            | 0        | 5806440     | 80645   | 0            | 0        | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/28   | up    | up   | control-plane | 1902288      | 19014    | 0           | 0       | 10638900     | 111146   | 0           | 0       | 
|                     |           |       |      | level3        | 0            | 0        | 0           | 0       | 900          | 6        | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/35   | up    | up   | control-plane | 4369444893   | 6631865  | 0           | 0       | 367708763    | 706658   | 0           | 0       | 
|                     |           |       |      | level3        | 3494976191   | 9228790  | 0           | 0       | 1715489286   | 6102316  | 1632        | 24      | 
|                     |           |       |      | policy-plane  | 19677380     | 161290   | 0           | 0       | 585497409    | 872621   | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/36   | up    | up   | control-plane | 6525346641   | 12695222 | 0           | 0       | 406425430    | 1147987  | 0           | 0       | 
|                     |           |       |      | level3        | 505743794    | 1540457  | 0           | 0       | 1794399583   | 6580060  | 2788        | 41      | 
|                     |           |       |      | policy-plane  | 60626112     | 500110   | 0           | 0       | 232448900    | 1440664  | 0           | 0       | 
+---------------------+-----------+-------+------+---------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
Interface context: phy
```

Example: ports with drops

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --qos drops
    --view qos

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+--------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
| Node                | Interface | Admin | Oper | Class        | Rx Admit [B] | Rx Admin | Rx Drop [B] | Rx Drop | Tx Admit [B] | Tx Admin | Tx Drop [B] | Tx Drop |
+---------------------+-----------+-------+------+--------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
| pod-1/bl205-eu-spdc | eth1/27   | up    | up   | policy-plane | 0            | 0        | 5806800     | 80650   | 0            | 0        | 0           | 0       | 
| pod-1/bl205-eu-spdc | eth1/35   | up    | up   | level3       | 3495098040   | 9229382  | 0           | 0       | 1715562016   | 6102760  | 1632        | 24      | 
| pod-1/bl205-eu-spdc | eth1/36   | up    | up   | level3       | 505785835    | 1540609  | 0           | 0       | 1794477163   | 6580543  | 2788        | 41      | 
+---------------------+-----------+-------+------+--------------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
Interface context: phy
```

Example: ports with transmit drops

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --qos drops-tx
    --view qos

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
| Node                | Interface | Admin | Oper | Class  | Rx Admit [B] | Rx Admin | Rx Drop [B] | Rx Drop | Tx Admit [B] | Tx Admin | Tx Drop [B] | Tx Drop |
+---------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
| pod-1/bl205-eu-spdc | eth1/35   | up    | up   | level3 | 3495318159   | 9229943  | 0           | 0       | 1715638320   | 6103230  | 1632        | 24      | 
| pod-1/bl205-eu-spdc | eth1/36   | up    | up   | level3 | 505797499    | 1540685  | 0           | 0       | 1794552998   | 6581012  | 2788        | 41      | 
+---------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+----------+-------------+---------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --qos data
    --view qos

{
    "duration": 2232,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 617,
        "disconnect_time": 0,
        "mo_time": 1277,
        "total_time": 1894
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

True	617	-	connect apic11o.emea-sp.cisco.com
True	318	13	apic11o.emea-sp.cisco.com class fabricNode
True	298	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	310	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	351	324	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/qosmIfClass
```

[[Back]](./InterfacePhy.md)