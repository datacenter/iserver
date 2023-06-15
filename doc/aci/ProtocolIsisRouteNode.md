# Node Protocol - IS-IS

## Show IS-IS routes for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view route

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

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
| pod-1/cl201-eu-spdc | overlay | 111.111.111.111/32 | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 112.112.112.112/32 | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 15.16.2.1/32       | 12     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 15.16.2.5/32       | 12     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.1.1/32      | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.10.1/32     | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.1/32     | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
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
| pod-1/cl201-eu-spdc | overlay | 172.16.12.1/32     | 2      | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.21.0/24     | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.21.1/32     | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
|                     |         |                    |        |            | eth1/107.7   | 10.3.192.65 | 
| pod-1/cl201-eu-spdc | overlay | 172.16.22.1/32     | 64     | 115        | eth1/108.8   | 10.3.32.65  | 
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
    "duration": 2305,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 464,
        "disconnect_time": 0,
        "mo_time": 1353,
        "total_time": 1817
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

True	464	-	connect apic11o.emea-sp.cisco.com
True	367	13	apic11o.emea-sp.cisco.com class fabricNode
True	291	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	358	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	337	142	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisRoute&target-subtree-class=isisRsNhAtt
```

[[Back]](./ProtocolIsis.md)