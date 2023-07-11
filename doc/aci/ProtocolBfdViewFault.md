# Node Protocol - ARP

## Fault view

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --view fault
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

BFD Faults [#2]
---------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.050+02:00 | raised    | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |           | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519046 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-07T14:57:16.415+02:00 | raised    | BFD session 1090519046 to neighbor 15.100.103.41 on node 201 interface vlan471   | 
|                     |            |          |       |                             |                               |           | is down. Reason: No Diagnostic.                                                  | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+

BFD Fault Records last 90d [#20]
--------------------------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle        | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-05-31T23:11:25.700+02:00 | soaking          | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-05-31T23:13:32.882+02:00 | raised           | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:45.779+02:00 | soaking          | BFD session 1090519045 to neighbor 15.254.103.191 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519042 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:45.827+02:00 | soaking          | BFD session 1090519042 to neighbor 15.254.106.191 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:46.762+02:00 | soaking-clearing | BFD session 1090519045 to neighbor 15.254.103.191 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519042 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:46.772+02:00 | soaking-clearing | BFD session 1090519042 to neighbor 15.254.106.191 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:48.248+02:00 |                  | BFD session 1090519045 to neighbor 15.254.103.191 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519042 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:48.259+02:00 |                  | BFD session 1090519042 to neighbor 15.254.106.191 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519044 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:19.725+02:00 | soaking          | BFD session 1090519044 to neighbor 15.254.106.192 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519043 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:19.640+02:00 | soaking          | BFD session 1090519043 to neighbor 15.254.103.192 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519044 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:20.542+02:00 | soaking-clearing | BFD session 1090519044 to neighbor 15.254.106.192 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519043 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:20.532+02:00 | soaking-clearing | BFD session 1090519043 to neighbor 15.254.103.192 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519044 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:22.259+02:00 |                  | BFD session 1090519044 to neighbor 15.254.106.192 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519043 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:22.248+02:00 |                  | BFD session 1090519043 to neighbor 15.254.103.192 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:40:48.057+02:00 | raised-clearing  | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:40:48.258+02:00 |                  | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.051+02:00 | soaking          | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:23:34.715+02:00 | raised           | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519046 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-07T14:57:16.417+02:00 | soaking          | BFD session 1090519046 to neighbor 15.100.103.41 on node 201 interface vlan471   | 
|                     |            |          |       |                             |                               |                  | is down. Reason: No Diagnostic.                                                  | 
| pod-1/cl201-eu-spdc | 1090519046 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-07T14:59:36.715+02:00 | raised           | BFD session 1090519046 to neighbor 15.100.103.41 on node 201 interface vlan471   | 
|                     |            |          |       |                             |                               |                  | is down. Reason: No Diagnostic.                                                  | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --view fault
    --when 90d

{
    "duration": 5985,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 456,
        "disconnect_time": 0,
        "mo_time": 3184,
        "total_time": 3640
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

True	456	-	connect apic11o.emea-sp.cisco.com:443
True	333	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	318	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	354	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	2179	2215	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=faults,fault-records,no-scoped,subtree
```

[[Back]](./ProtocolBfd.md)