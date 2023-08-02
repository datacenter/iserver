# Node Protocol - LACP

## All view

```
# iserver get aci proto lacp
    --apic apic11
    --node bl205-eu-spdc
    --view all
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol LACP - Instance [#1]
-----------------------------

+---------------------+---------+-------------------+------------+-----------+---------+-----------+------------+
| Node                | Admin   | System MAC        | Admin Prio | Oper Prio | Intf Up | Intf Down | Intf Count |
+---------------------+---------+-------------------+------------+-----------+---------+-----------+------------+
| pod-1/bl205-eu-spdc | enabled | 4C:71:0D:7E:84:C0 | 32768      | 32768     | 5       | 0         | 5          | 
+---------------------+---------+-------------------+------------+-----------+---------+-----------+------------+

Protocol LACP - Port Channels [#5]
----------------------------------

+---------------------+---------+-------------------+-------+------+---------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| Node                | Intf Id | Name              | Admin | Oper | Member  | Oper Key | Nbr System MAC    | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State                           |
+---------------------+---------+-------------------+-------+------+---------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+
| pod-1/bl205-eu-spdc | po1     | HX1-FI-A_PolGrp   | up    | up   | eth1/11 | 32769    | 00:3A:9C:C0:04:47 | 32768           | 200          | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| pod-1/bl205-eu-spdc | po2     | HX1-FI-B_PolGrp   | up    | up   | eth1/12 | 32770    | 00:3A:9C:C0:03:E7 | 32768           | 241          | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| pod-1/bl205-eu-spdc | po3     | SPN_PolGrp        | up    | up   | eth1/27 | 33112    | E0:0E:DA:A3:38:13 | 32768           | 1            | 337      | 32768         | active,aggregate,collect,distribute,sync | 
| pod-1/bl205-eu-spdc | po4     | UCSB1-FI-B_PolGrp | up    | up   | eth1/2  | 33111    | 00:3A:9C:BD:8F:07 | 32768           | 15           | 457      | 32768         | active,aggregate,collect,distribute,sync | 
| pod-1/bl205-eu-spdc | po5     | UCSB1-FI-A_PolGrp | up    | up   | eth1/1  | 32771    | 00:3A:9C:BD:92:07 | 32768           | 14           | 457      | 32768         | active,aggregate,collect,distribute,sync | 
+---------------------+---------+-------------------+-------+------+---------+----------+-------------------+-----------------+--------------+----------+---------------+------------------------------------------+

Protocol LACP - Interface Stats [#5]
------------------------------------

+---------------------+---------+-------------------+-------+------+---------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| Node                | Intf Id | Name              | Admin | Oper | Member  | PDU Sent | PDU Recv | PDU Recv Err | Marker Sent | Marker Recv | Marker Response Sent | Marker Response Recv |
+---------------------+---------+-------------------+-------+------+---------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| pod-1/bl205-eu-spdc | po1     | HX1-FI-A_PolGrp   | up    | up   | eth1/11 | 147398   | 147399   | 0            | 0           | 0           | 0                    | 0                    | 
| pod-1/bl205-eu-spdc | po2     | HX1-FI-B_PolGrp   | up    | up   | eth1/12 | 147398   | 147397   | 0            | 0           | 0           | 0                    | 0                    | 
| pod-1/bl205-eu-spdc | po3     | SPN_PolGrp        | up    | up   | eth1/27 | 147397   | 147399   | 0            | 0           | 0           | 0                    | 0                    | 
| pod-1/bl205-eu-spdc | po4     | UCSB1-FI-B_PolGrp | up    | up   | eth1/2  | 147398   | 147400   | 0            | 0           | 0           | 0                    | 0                    | 
| pod-1/bl205-eu-spdc | po5     | UCSB1-FI-A_PolGrp | up    | up   | eth1/1  | 147403   | 147407   | 0            | 0           | 0           | 0                    | 0                    | 
+---------------------+---------+-------------------+-------+------+---------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+

Protocol LACP - Event Logs [#15]
--------------------------------

+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| Node                | Interface | Sev  | Code     | Cause              | Created Time                  | Description                            | Affected                               |
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/1    | Info | E4204996 | oper-state-change  | 2023-07-12T17:50:40.239+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/1]                            | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/1    | Info | E4204996 | oper-state-change  | 2023-06-12T10:37:26.807+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/1]                            | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/2    | Info | E4204996 | oper-state-change  | 2023-06-12T10:37:25.831+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/2]                            | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/11   | Info | E4204996 | oper-state-change  | 2023-06-12T10:37:25.446+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/11]                           | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/12   | Info | E4204996 | oper-state-change  | 2023-06-12T10:37:24.210+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/12]                           | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/27   | Info | E4204996 | oper-state-change  | 2023-06-12T10:37:20.189+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/27]                           | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | --        | Info | E4208088 | admin-state-change | 2023-06-12T09:12:22.732+02:00 | LACP instance is administratively      | topology/pod-1/node-205/sys/lacp/inst  | 
|                     |           |      |          |                    |                               | Enabled                                |                                        | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/2    | Info | E4204996 | oper-state-change  | 2023-06-07T19:00:34.148+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/2]                            | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/1    | Info | E4204996 | oper-state-change  | 2023-06-07T18:23:14.803+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/1]                            | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/11   | Info | E4204996 | oper-state-change  | 2023-05-31T23:11:04.778+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/11]                           | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/1    | Info | E4204996 | oper-state-change  | 2023-05-31T23:11:03.633+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/1]                            | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/12   | Info | E4204996 | oper-state-change  | 2023-05-31T23:11:03.328+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/12]                           | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/2    | Info | E4204996 | oper-state-change  | 2023-05-31T23:11:02.139+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/2]                            | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/27   | Info | E4204996 | oper-state-change  | 2023-05-31T23:10:54.631+02:00 | LACP port priority is changed to 32768 | topology/pod-1/node-205/sys/lacp/inst/ | 
|                     |           |      |          |                    |                               |                                        | if-[eth1/27]                           | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | --        | Info | E4208088 | admin-state-change | 2023-05-31T23:00:34.243+02:00 | LACP instance is administratively      | topology/pod-1/node-205/sys/lacp/inst  | 
|                     |           |      |          |                    |                               | Enabled                                |                                        | 
+---------------------+-----------+------+----------+--------------------+-------------------------------+----------------------------------------+----------------------------------------+
```

Developer

```
# iserver get aci proto lacp
    --apic apic11
    --node bl205-eu-spdc
    --view all
    --when 90d

{
    "duration": 2751,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 401,
        "disconnect_time": 0,
        "mo_time": 1978,
        "total_time": 2379
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

True	401	-	connect apic11o.emea-sp.cisco.com:443
True	299	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	280	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst
True	456	5	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	291	5	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	282	5	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp&rsp-subtree-include=fault-count
True	370	63	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lacp/inst query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolLacp.md)