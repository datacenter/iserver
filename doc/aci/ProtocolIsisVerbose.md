# Node Protocol - IS-IS

## Show all details for selected node

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view verbose

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

IS-IS Instance
--------------
- Node        : pod-1/cl201-eu-spdc
- Admin State : enabled
- Oper State  : enabled
- Domains     : 1


Domain
------
- Name         : overlay-1
- Oper State   : ok
- System ID    : 43:C0:03:0A:00:00
- Area         : 1
- Protocol     : ip
- Mode         : fabric
- Max ECMP     : 18
- Metric Style : narrow
- MTU          : 1492


Interfaces
----------

+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+
| Node                | Domain  | Id           | Admin State | Circuit Type | Control            | Protocol State |
+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+
| pod-1/cl201-eu-spdc | overlay | eth1/107.7   | enabled     | l1           |                    | Ready          | 
| pod-1/cl201-eu-spdc | overlay | eth1/108.504 | enabled     | l1           |                    | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo0          | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo1          | enabled     | l1           | advert-tep,passive | Ready          | 
| pod-1/cl201-eu-spdc | overlay | lo2          | enabled     | l1           | passive            | Ready          | 
+---------------------+---------+--------------+-------------+--------------+--------------------+----------------+

LSP Records
-----------

+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| Node                | Domain  | Sys Id            | Lan Id | Frag | Type | Lifetime                      | Seqnum |
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+
| pod-1/cl201-eu-spdc | overlay | 40:20:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:20:33.000+02:00 | 54739  | 
| pod-1/cl201-eu-spdc | overlay | 40:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:16:39.000+02:00 | 54714  | 
| pod-1/cl201-eu-spdc | overlay | 41:20:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:18:08.000+02:00 | 54793  | 
| pod-1/cl201-eu-spdc | overlay | 41:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:15:51.000+02:00 | 54785  | 
| pod-1/cl201-eu-spdc | overlay | 43:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:08:40.000+02:00 | 54733  | 
| pod-1/cl201-eu-spdc | overlay | 44:C0:03:0A:00:00 | 0      | 0    | l1   | 2023-05-30T20:20:33.000+02:00 | 54757  | 
+---------------------+---------+-------------------+--------+------+------+-------------------------------+--------+

Neighbors
---------

+---------------------+---------+--------------+-------------------+-------+--------------+-------------+-------+
| Node                | Domain  | Interface    | System Id         | Level | Circuit Type | Peer IP     | State |
+---------------------+---------+--------------+-------------------+-------+--------------+-------------+-------+
| pod-1/cl201-eu-spdc | overlay | eth1/108.504 | 41:20:03:0A:00:00 | l1    | bcast        | 10.3.32.65  | up    | 
| pod-1/cl201-eu-spdc | overlay | eth1/107.7   | 41:C0:03:0A:00:00 | l1    | bcast        | 10.3.192.65 | up    | 
+---------------------+---------+--------------+-------------------+-------+--------------+-------------+-------+

IS-IS Routes
------------

+---------------------+---------+--------------------+--------+------------+--------------+-------------+
| Node                | Domain  | Prefix             | Metric | Preference | NH Interface | NH Address  |
+---------------------+---------+--------------------+--------+------------+--------------+-------------+
| pod-1/cl201-eu-spdc | overlay | 10.3.0.33/32       | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.0.34/32       | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.0.35/32       | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.152.65/32     | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.152.66/32     | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.152.67/32     | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.101/32    | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.102/32    | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.103/32    | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.64/32     | 3      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.65/32     | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.68/32     | 3      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.64/32      | 3      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.65/32      | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.64/32      | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.65/32      | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.66/32      | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.67/32      | 3      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.48.64/32      | 3      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 101.101.101.101/32 | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 102.102.102.102/32 | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 111.111.111.111/32 | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 112.112.112.112/32 | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 15.16.2.1/32       | 12     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 15.16.2.5/32       | 12     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.1.1/32      | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.10.1/32     | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.1/32     | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.225/32   | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.226/32   | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.227/32   | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.228/32   | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.231/32   | 3      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.233/32   | 3      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.236/32   | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.11.237/32   | 3      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.12.1/32     | 2      | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.21.0/24     | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.21.1/32     | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.22.1/32     | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.120/32   | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.121/32   | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.160/32   | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.161/32   | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 172.16.30.88/32    | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 192.168.1.0/30     | 11     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 192.168.1.4/30     | 11     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 192.168.31.0/30    | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
| pod-1/cl201-eu-spdc | overlay | 192.168.32.0/30    | 64     | 115        | eth1/107.7   | 10.3.192.65 | 
|                     |         |                    |        |            | eth1/108.504 | 10.3.32.65  | 
+---------------------+---------+--------------------+--------+------------+--------------+-------------+

IS-IS Fabric Multicast Trees
----------------------------

+---------------------+---------+----+--------------+--------------+----------+--------+----------------+------------+
| Node                | Domain  | Id | Root Address | Root Port    | Diameter | Origin | Diameter Alert | Oper State |
+---------------------+---------+----+--------------+--------------+----------+--------+----------------+------------+
| pod-1/cl201-eu-spdc | overlay | 0  | 10.3.192.65  | eth1/107.7   | 6        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 1  | 10.3.32.65   | eth1/108.504 | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 2  | 10.3.32.65   | eth1/108.504 | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 3  | 10.3.32.65   | eth1/108.504 | 6        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 4  | 10.3.32.65   | eth1/108.504 | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 5  | 10.3.192.65  | eth1/107.7   | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 6  | 10.3.192.65  | eth1/107.7   | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 7  | 10.3.192.65  | eth1/107.7   | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 8  | 10.3.192.65  | eth1/107.7   | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 9  | 10.3.192.65  | eth1/107.7   | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 10 | 10.3.192.65  | eth1/107.7   | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 11 | 10.3.32.65   | eth1/108.504 | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 12 | 10.3.32.65   | eth1/108.504 | 7        | isis   | inactive       | active     | 
| pod-1/cl201-eu-spdc | overlay | 13 | 0.0.0.0      | unspecified  | 0        | static | inactive       | inactive   | 
| pod-1/cl201-eu-spdc | overlay | 14 | 0.0.0.0      | unspecified  | 0        | static | inactive       | inactive   | 
| pod-1/cl201-eu-spdc | overlay | 15 | 0.0.0.0      | unspecified  | 0        | static | inactive       | inactive   | 
+---------------------+---------+----+--------------+--------------+----------+--------+----------------+------------+

Discovered Tunnel Endpoints
---------------------------

+---------------------+---------+-------------+-------+--------------------------+
| Node                | Domain  | Id          | Role  | Type                     |
+---------------------+---------+-------------+-------+--------------------------+
| pod-1/cl201-eu-spdc | overlay | 10.3.192.64 | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.65 | spine | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.192.68 | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.64  | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.32.65  | spine | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.64  | spine | physical,proxy-acast-v4  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.65  | spine | physical,proxy-acast-mac | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.66  | spine | physical,proxy-acast-v6  | 
| pod-1/cl201-eu-spdc | overlay | 10.3.40.67  | leaf  | physical                 | 
| pod-1/cl201-eu-spdc | overlay | 10.3.48.64  | leaf  | physical                 | 
+---------------------+---------+-------------+-------+--------------------------+
```

Developer

```
# iserver get aci proto isis --apic apic11 --node cl201-eu-spdc --view verbose

{
    "duration": 3748,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 2989,
        "total_time": 3416
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
    }
}

Log: apic
----------

True	427	-	connect apic11o.emea-sp.cisco.com
True	336	11	apic11o.emea-sp.cisco.com class fabricNode
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis query query-target=subtree&target-subtree-class=isisDom
True	304	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisDTEp
True	306	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisLspRec
True	359	5	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisIf
True	326	2	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisAdjEp&rsp-subtree=children&rsp-subtree-class=isisPeerIpAddr
True	341	16	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisFmcastTree
True	373	132	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1 query query-target=subtree&target-subtree-class=isisRoute&target-subtree-class=isisRsNhAtt
```


[[Back]](./ProtocolIsis.md)