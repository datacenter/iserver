# Node Protocol - IS-IS

## Route view

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view route

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol ISIS - Route [#47]
---------------------------

+---------------------+---------+--------------------+--------+------------+--------------+-------------+
| Node                | Domain  | Prefix             | Metric | Preference | NH Interface | NH Address  |
+---------------------+---------+--------------------+--------+------------+--------------+-------------+
| pod-1/cl201-eu-spdc | overlay | 10.3.0.1/32        | 12     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.0.33/32       | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.0.34/32       | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.0.35/32       | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.136.64/32     | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.136.65/32     | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.152.65/32     | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.152.66/32     | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.152.67/32     | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.101/32    | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.102/32    | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.103/32    | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.64/32     | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.65/32     | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.68/32     | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.64/32      | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.65/32      | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.64/32      | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.65/32      | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.66/32      | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.67/32      | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.48.64/32      | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 101.101.101.101/32 | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 102.102.102.102/32 | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 15.16.2.1/32       | 12     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 15.16.2.5/32       | 12     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.1.1/32      | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.10.1/32     | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.1/32     | 11     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.225/32   | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.226/32   | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.227/32   | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.228/32   | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.230/32   | 12     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.231/32   | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.233/32   | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.236/32   | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.237/32   | 3      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.120/32   | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.121/32   | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.160/32   | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.161/32   | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.88/32    | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 192.168.1.0/30     | 11     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 192.168.1.4/30     | 11     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 192.168.31.0/30    | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 192.168.32.0/30    | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
+---------------------+---------+--------------------+--------+------------+--------------+-------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view route

{
    "duration": 1743,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 391,
        "disconnect_time": 0,
        "mo_time": 1159,
        "total_time": 1550
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

True	391	-	connect apic11o.emea-sp.cisco.com:443
True	289	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	270	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=children&rsp-subtree-include=health,fault-count
True	288	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	312	123	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisRoute&target-subtree-class=isisRsNhAtt
```

[[Back]](./ProtocolIsis.md)