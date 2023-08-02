# Node Interface - MACsec

## State view

```
# iserver get aci intf macsec --apic apic21 --node bl2205-eu-spdc

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface MacSec - State [#28]
------------------------------

+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| Node                 | Health | Faults  | Interface | Admin    | Oper | Reason     | Session         | Peers | Cepher Suite | Confid Offset | Ker Server Prio | Replay Window |
+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/1    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/2    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/3    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/4    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/5    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/6    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/7    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/8    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/9    | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/10   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/11   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/12   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/13   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/14   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/15   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/16   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/17   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/18   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/19   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/20   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/21   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/22   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/23   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/24   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/25   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/26   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/27   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/28   | disabled | down | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
+----------------------+--------+---------+-----------+----------+------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
```

Developer

```
# iserver get aci intf macsec --apic apic21 --node bl2205-eu-spdc

{
    "duration": 3300,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 552,
        "disconnect_time": 0,
        "mo_time": 2330,
        "total_time": 2882
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

True	552	-	connect apic21o.emea-sp.cisco.com:443
True	376	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	462	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1083	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	409	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
```

[[Back]](./InterfaceMacSec.md)