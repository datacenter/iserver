# Node Interface - MACsec

## Single node

```
# iserver get aci intf macsec --apic apic11 --node bl205-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| Node                | Interface | Admin State | Oper State | Reason     | Session State   | Peers | Cepher Suite | Confid Offset | Ker Server Prio | Replay Window |
+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| pod-1/bl205-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
```

Developer

```
# iserver get aci intf macsec --apic apic11 --node bl205-eu-spdc

{
    "duration": 1743,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 393,
        "disconnect_time": 0,
        "mo_time": 1211,
        "total_time": 1604
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
True	294	13	apic11o.emea-sp.cisco.com class fabricNode
True	298	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/macsecIf
True	293	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	326	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
```

[[Back]](./InterfaceMacSec.md)