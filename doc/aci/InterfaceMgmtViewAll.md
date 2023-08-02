# Node Interface - Management

## All view

```
# iserver get aci intf mgmt
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Management - State [#1]
---------------------------------

+----------------------+--------+---------+-----------+-------+-----------+------+------------------+--------+------+-------+-------------------------------+
| Node                 | Health | Faults  | Interface | Admin | Switching | Oper | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+----------------------+--------+---------+-----------+-------+-----------+------+------------------+--------+------+-------+-------------------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | mgmt0     | up    | disabled  | up   | on               | full   | 1500 | 1G    | 2023-06-18T09:38:34.501+02:00 | 
+----------------------+--------+---------+-----------+-------+-----------+------+------------------+--------+------+-------+-------------------------------+

Interface Management - Address [#1]
-----------------------------------

+----------------------+-----------+-------+------+-------------------+-----------------+-------------------+
| Node                 | Interface | Admin | Oper | MAC Address       | IP Address      | Router MAC        |
+----------------------+-----------+-------+------+-------------------+-----------------+-------------------+
| pod-1/bl2205-eu-spdc | mgmt0     | up    | up   | 3C:13:CC:B9:ED:B0 | 10.58.50.145/27 | 3C:13:CC:B9:ED:B0 | 
+----------------------+-----------+-------+------+-------------------+-----------------+-------------------+

Interface Management - CDP/LLDP Neighbor [#1]
---------------------------------------------

+----------------------+-----------+-------+------+----------------+-------------------+--------------+-------------------------------+--------------+
| Node                 | Interface | Admin | Oper | CDP - Platform | CDP - System Name | CDP - Port   | LLDP - System Name            | LLDP - Port  |
+----------------------+-----------+-------+------+----------------+-------------------+--------------+-------------------------------+--------------+
| pod-1/bl2205-eu-spdc | mgmt0     | up    | up   | N9K-C92348GC-X | r25-eu-spdc       | Ethernet1/41 | r25-eu-spdc.emea-sp.cisco.com | Ethernet1/41 | 
+----------------------+-----------+-------+------+----------------+-------------------+--------------+-------------------------------+--------------+

Interface Management - Faults [#0]
----------------------------------
None

Interface Management - Fault Records last 10y [#57]
---------------------------------------------------

+----------------------+-----------+------+-------+---------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code  | Cause                     | Created Time                  | Lifecycle        | Description                                                                     |
+----------------------+-----------+------+-------+---------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2021-10-14T18:42:38.181+02:00 | soaking          | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2021-10-14T18:44:40.507+02:00 | raised           | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2021-10-27T15:22:27.041+02:00 | raised-clearing  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2021-10-27T15:24:30.675+02:00 | retaining        | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2021-10-27T16:24:31.225+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2021-10-27T19:41:26.373+02:00 | soaking          | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2021-10-27T19:41:29.376+02:00 | soaking-clearing | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2021-10-27T19:43:32.092+02:00 | retaining        | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2021-10-27T20:43:32.773+02:00 |                  | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-01-13T23:53:31.478+02:00 | soaking          | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-01-13T23:53:38.035+02:00 | soaking-clearing | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-01-13T23:55:48.273+02:00 | retaining        | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-01-14T00:55:49.222+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-01-27T16:40:32.736+02:00 | soaking          | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-01-27T16:40:39.259+02:00 | soaking-clearing | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-01-27T16:42:45.392+02:00 | retaining        | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-01-27T17:42:47.413+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-04-22T15:49:02.688+02:00 | soaking          | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-04-22T15:49:09.245+02:00 | soaking-clearing | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-04-22T15:51:20.553+02:00 | retaining        | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-04-22T16:51:21.902+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-04-28T16:07:41.237+02:00 | soaking          | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-04-28T16:09:45.990+02:00 | raised           | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-04-28T16:52:54.452+02:00 | raised-clearing  | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-04-28T16:55:16.515+02:00 | retaining        | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-04-28T17:55:17.347+02:00 |                  | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-05-08T18:37:11.060+02:00 | soaking          | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-05-08T18:39:32.232+02:00 | raised           | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-05-08T18:41:41.780+02:00 | raised-clearing  | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-05-08T18:44:02.267+02:00 | retaining        | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-05-08T19:44:03.244+02:00 |                  | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-05-09T23:40:40.783+02:00 | soaking          | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-05-09T23:40:47.339+02:00 | soaking-clearing | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-05-09T23:43:11.176+02:00 | retaining        | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-05-10T00:43:11.836+02:00 |                  | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-05-20T17:01:22.212+02:00 | soaking          | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-05-20T17:03:24.160+02:00 | raised           | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-05-20T17:05:31.873+02:00 | raised-clearing  | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-05-20T17:07:54.198+02:00 | retaining        | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-05-20T18:07:54.706+02:00 |                  | Management port is down, reason being fail on node 2205 of fabric ACI2-EU-SPDC  | 
|                      |           |      |       |                           |                               |                  | with hostname bl2205-eu-spdc                                                    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-09-14T23:48:28.324+02:00 | soaking          | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2022-09-14T23:48:34.865+02:00 | soaking-clearing | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-09-14T23:50:48.896+02:00 | retaining        | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2022-09-15T00:50:49.672+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2023-03-02T21:44:20.099+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2023-05-30T21:01:04.831+02:00 | soaking          | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2023-05-30T21:01:11.368+02:00 | soaking-clearing | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2023-05-30T21:03:20.871+02:00 | retaining        | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2023-05-30T22:03:21.875+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2023-06-12T09:52:39.387+02:00 | soaking          | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2023-06-12T09:52:45.932+02:00 | soaking-clearing | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2023-06-12T09:55:01.122+02:00 | retaining        | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2023-06-12T10:55:01.627+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2023-06-18T09:38:27.887+02:00 | soaking          | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | Crit | F1907 | interface-management-down | 2023-06-18T09:38:34.504+02:00 | soaking-clearing | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2023-06-18T09:40:37.511+02:00 | retaining        | Management port is down, reason being fail on node 0 of fabric with hostname    | 
| pod-1/bl2205-eu-spdc | mgmt0     | --   | F1907 | interface-management-down | 2023-06-18T10:40:39.054+02:00 |                  | Management port is down, reason being fail on node 0 of fabric with hostname    | 
+----------------------+-----------+------+-------+---------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+

Interface Management - Event Logs last 10y [#0]
-----------------------------------------------
None

Interface Management - Audit Logs last 10y [#0]
-----------------------------------------------
None
```

Developer

```
# iserver get aci intf mgmt
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view all

{
    "duration": 3778,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 370,
        "disconnect_time": 0,
        "mo_time": 3075,
        "total_time": 3445
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

True	370	-	connect apic21o.emea-sp.cisco.com:443
True	272	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	286	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	266	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys query query-target=subtree&target-subtree-class=imMgmtIf
True	270	7	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count
True	271	10	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	281	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/mgmt-[mgmt0]/fltCnts
True	256	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/ipv4/inst/dom-management query query-target=subtree&target-subtree-class=ipv4Addr
True	274	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree-include=faults,no-scoped,subtree
True	343	57	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	280	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	276	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/mgmtMgmtIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfaceMgmt.md)