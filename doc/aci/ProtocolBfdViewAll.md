# Node Protocol - BFD

## All view

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --view all
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
| Node                | Role | HW               | Admin   | Health | Faults  | Echo Intf   | Sessions | Intf    | State   | Sessions |
+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+
| pod-1/cl201-eu-spdc | leaf | N9K-C93360YC-FX2 | enabled | 93     | 0 2 0 0 | unspecified | 7/9      | vlan472 | enabled | 0/1      | 
|                     |      |                  |         |        |         |             |          | vlan473 | enabled | 3/3      | 
|                     |      |                  |         |        |         |             |          | vlan496 | enabled | 2/2      | 
+---------------------+------+------------------+---------+--------+---------+-------------+----------+---------+---------+----------+

Protocol BFD - Session [#9]
---------------------------

+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| Node                | Health | Faults  | VRF                           | Interface | Type      | Local Address  | Local MAC         | State | Session Id | Remote Address | Remote MAC        | State | Session Id |
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| pod-1/cl201-eu-spdc | 90     | 0 1 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan471   | singlehop | 15.254.101.0   | 00:22:BD:F8:19:FF | down  | 1090519046 | 15.100.103.41  | FA:16:3E:D6:A8:CB | down  | 0          | 
| pod-1/cl201-eu-spdc | 90     | 0 1 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan472   | singlehop | 15.254.101.4   | 00:22:BD:F8:19:FF | down  | 1090519045 | 15.100.7.41    | FA:16:3E:BC:A6:70 | down  | 0          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan496   | singlehop | 15.254.103.252 | 00:22:BD:F8:19:FF | up    | 1090519044 | 15.254.103.191 | FA:16:3E:B6:A6:15 | up    | 3          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan496   | singlehop | 15.254.103.252 | 00:22:BD:F8:19:FF | up    | 1090519042 | 15.254.103.192 | FA:16:3E:C4:FE:86 | up    | 3          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N6_VRF    | vlan492   | singlehop | 15.254.106.252 | 00:22:BD:F8:19:FF | up    | 1090519043 | 15.254.106.191 | FA:16:3E:B6:A6:15 | up    | 1          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N6_VRF    | vlan492   | singlehop | 15.254.106.252 | 00:22:BD:F8:19:FF | up    | 1090519041 | 15.254.106.192 | FA:16:3E:C4:FE:86 | up    | 1          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan473   | singlehop | 15.254.133.252 | 00:22:BD:F8:19:FF | up    | 1090519048 | 15.254.133.191 | FA:16:3E:45:71:99 | up    | 1          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan473   | singlehop | 15.254.133.252 | 00:22:BD:F8:19:FF | up    | 1090519049 | 15.254.133.193 | FA:16:3E:AE:9D:45 | up    | 1          | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim4-N3-N4_VRF | vlan473   | singlehop | 15.254.133.252 | 00:22:BD:F8:19:FF | up    | 1090519047 | 15.254.133.55  | FA:16:3E:8C:96:73 | up    | 1          | 
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+

Protocol BFD - Session Stats [#9]
---------------------------------

+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
| Node                | VRF                           | Local Address  | Remote Address | Up | Down | Rx Cnt  | Rx Interval [msec] | Min | Avg | Max  | Tx Cnt  | Tx Interval [msec] | Min  | Avg  | Max  |
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.101.0   | 15.100.103.41  | 0  | 0    | 0       | 2000               | 0   | 0   | 0    | 1161196 | 2000               | 1933 | 1933 | 1933 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.101.4   | 15.100.7.41    | 0  | 0    | 0       | 2000               | 0   | 0   | 0    | 1242370 | 2000               | 1933 | 1933 | 1933 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252 | 15.254.103.191 | 1  | 0    | 5156321 | 500                | 1   | 465 | 1526 | 4999156 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 15.254.103.252 | 15.254.103.192 | 1  | 0    | 5152809 | 500                | 0   | 466 | 1139 | 4999164 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252 | 15.254.106.191 | 1  | 0    | 5156386 | 500                | 0   | 465 | 2167 | 4999160 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 15.254.106.252 | 15.254.106.192 | 1  | 0    | 5152758 | 500                | 0   | 466 | 764  | 4999164 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.191 | 1  | 0    | 4809722 | 500                | 1   | 466 | 1971 | 4672212 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.193 | 1  | 0    | 4817467 | 500                | 1   | 466 | 1991 | 4672176 | 500                | 480  | 480  | 480  | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 15.254.133.252 | 15.254.133.55  | 1  | 0    | 4805689 | 500                | 4   | 467 | 1881 | 4672366 | 500                | 480  | 480  | 480  | 
+---------------------+-------------------------------+----------------+----------------+----+------+---------+--------------------+-----+-----+------+---------+--------------------+------+------+------+

Protocol BFD - Faults [#2]
--------------------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.050+02:00 | raised    | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |           | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519046 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-07T14:57:16.415+02:00 | raised    | BFD session 1090519046 to neighbor 15.100.103.41 on node 201 interface vlan471   | 
|                     |            |          |       |                             |                               |           | is down. Reason: No Diagnostic.                                                  | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+

Protocol BFD - Fault Records last 90d [#20]
-------------------------------------------

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
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:40:48.258+02:00 |                  | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:40:48.057+02:00 | raised-clearing  | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
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

Protocol BFD - Event Logs last 90d [#116]
-----------------------------------------

+---------------------+------------+----------+----------+-------------------+-------------------------------+------------------------------------------+---------------------------------------+
| Node                | Session Id | Severity | Code     | Cause             | Created Time                  | Description                              | Affected                              |
+---------------------+------------+----------+----------+-------------------+-------------------------------+------------------------------------------+---------------------------------------+
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4215661 | oper-state-change | 2023-05-31T23:11:25.717+02:00 | BFD session 1090519041 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.100.7.41 on interface vlan494 is      | session-1090519041                    | 
|                     |            |          |          |                   |                               | down. Reason: No Diagnostic.             |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-05-31T23:11:25.716+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed TX(2000):         | session-1090519041                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(0), Mult(3), Ver(1), Auth   |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-05-31T23:11:25.715+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed Disc 1090519041   | session-1090519041                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208499 | oper-state-change | 2023-05-31T23:11:25.712+02:00 | BFD session to neighbor 15.100.7.41 on   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | interface vlan494 has been created       | session-1090519041                    | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4215661 | oper-state-change | 2023-05-31T23:11:25.707+02:00 | BFD session 1090519041 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.100.7.41 on interface vlan494 is      | session-1090519041                    | 
|                     |            |          |          |                   |                               | down. Reason: No Diagnostic.             |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-05-31T23:11:25.706+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed TX(2000):         | session-1090519041                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(0), Mult(3), Ver(1), Auth   |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-05-31T23:11:25.705+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed Disc 1090519041   | session-1090519041                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208499 | oper-state-change | 2023-05-31T23:11:25.702+02:00 | BFD session to neighbor 15.100.7.41 on   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | interface vlan494 has been created       | session-1090519041                    | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4215661 | oper-state-change | 2023-05-31T23:11:26.051+02:00 | BFD session 1090519041 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.100.7.41 on interface vlan494 is      | session-1090519041                    | 
|                     |            |          |          |                   |                               | down. Reason: No Diagnostic.             |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-05-31T23:11:26.041+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed TX(2000):         | session-1090519041                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(0), Mult(3), Ver(1), Auth   |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:16.610+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed Disc 1090519042   | session-1090519042                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:16.605+02:00 | BFD session to neighbor 15.254.106.191   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan496 has been created    | session-1090519042                    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:16.596+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed Disc 1090519042   | session-1090519042                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:16.592+02:00 | BFD session to neighbor 15.254.106.191   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan496 has been created    | session-1090519042                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:19.670+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed Disc 1090519044   | session-1090519044                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:19.667+02:00 | BFD session to neighbor 15.254.106.192   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan496 has been created    | session-1090519044                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:19.655+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed Disc 1090519044   | session-1090519044                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:19.652+02:00 | BFD session to neighbor 15.254.106.192   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan496 has been created    | session-1090519044                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:19.676+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed Disc 1090519043   | session-1090519043                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:19.673+02:00 | BFD session to neighbor 15.254.103.192   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan498 has been created    | session-1090519043                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:19.642+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed Disc 1090519043   | session-1090519043                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:19.640+02:00 | BFD session to neighbor 15.254.103.192   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan498 has been created    | session-1090519043                    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:22.815+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed Disc 1090519045   | session-1090519045                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:22.811+02:00 | BFD session to neighbor 15.254.103.191   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan498 has been created    | session-1090519045                    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:22.795+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed Disc 1090519045   | session-1090519045                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:22.791+02:00 | BFD session to neighbor 15.254.103.191   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan498 has been created    | session-1090519045                    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:28.611+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed TX(2000):         | session-1090519042                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(0), Mult(3), Ver(1), Auth   |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208501 | oper-state-change | 2023-05-31T23:12:29.502+02:00 | BFD session 1090519042 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.106.191 on interface vlan496 is   | session-1090519042                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:30.590+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed TX(50): RX(50):   | session-1090519042                    | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No     |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.632+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed TX(50): RX(50):   | session-1090519044                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208501 | oper-state-change | 2023-05-31T23:12:31.169+02:00 | BFD session 1090519044 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.106.192 on interface vlan496 is   | session-1090519044                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.157+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed TX(0): RX(0):     | session-1090519044                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(0), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:31.156+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed Disc 1090519044   | session-1090519044                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.150+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed TX(50): RX(50):   | session-1090519042                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:31.149+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed Disc 1090519042   | session-1090519042                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.625+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed TX(500):          | session-1090519043                    | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1),      |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208501 | oper-state-change | 2023-05-31T23:12:31.176+02:00 | BFD session 1090519043 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.103.192 on interface vlan498 is   | session-1090519043                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.164+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed TX(0): RX(0):     | session-1090519043                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(0), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:31.163+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed Disc 1090519043   | session-1090519043                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:35.626+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed TX(2000):         | session-1090519045                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(0), Mult(3), Ver(1), Auth   |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208501 | oper-state-change | 2023-05-31T23:12:36.729+02:00 | BFD session 1090519045 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.103.191 on interface vlan498 is   | session-1090519045                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:37.626+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed TX(500):          | session-1090519045                    | 
|                     |            |          |          |                   |                               | RX(500): ST(0), Mult(3), Ver(1), Auth    |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:38.380+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed TX(500):          | session-1090519045                    | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1),      |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:38.379+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed Disc 1090519045   | session-1090519045                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4215661 | oper-state-change | 2023-06-07T11:38:45.785+02:00 | BFD session 1090519045 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.103.191 on interface vlan498 is   | session-1090519045                    | 
|                     |            |          |          |                   |                               | down. Reason: Control Detection Time     |                                       | 
|                     |            |          |          |                   |                               | Expired.                                 |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-06-07T11:38:45.783+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed Disc 1090519045   | session-1090519045                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(2000), Mult(3),   |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4215661 | oper-state-change | 2023-06-07T11:38:45.833+02:00 | BFD session 1090519042 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.106.191 on interface vlan496 is   | session-1090519042                    | 
|                     |            |          |          |                   |                               | down. Reason: Control Detection Time     |                                       | 
|                     |            |          |          |                   |                               | Expired.                                 |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-06-07T11:38:45.831+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed Disc 1090519042   | session-1090519042                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(2000), Mult(3),   |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-06-07T11:38:46.232+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed TX(2000):         | session-1090519045                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(2000), Mult(3), Ver(1),     |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-06-07T11:38:46.240+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed TX(2000):         | session-1090519042                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(2000), Mult(3), Ver(1),     |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208500 | oper-state-change | 2023-06-07T11:38:48.252+02:00 | BFD session to neighbor has been         | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | removed                                  | session-1090519045                    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208500 | oper-state-change | 2023-06-07T11:38:48.262+02:00 | BFD session to neighbor has been         | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | removed                                  | session-1090519042                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4215661 | oper-state-change | 2023-06-07T11:39:19.732+02:00 | BFD session 1090519044 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.106.192 on interface vlan496 is   | session-1090519044                    | 
|                     |            |          |          |                   |                               | down. Reason: Control Detection Time     |                                       | 
|                     |            |          |          |                   |                               | Expired.                                 |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-06-07T11:39:19.730+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed Disc 1090519044   | session-1090519044                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(2000), Mult(3),   |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4215661 | oper-state-change | 2023-06-07T11:39:19.646+02:00 | BFD session 1090519043 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.103.192 on interface vlan498 is   | session-1090519043                    | 
|                     |            |          |          |                   |                               | down. Reason: Control Detection Time     |                                       | 
|                     |            |          |          |                   |                               | Expired.                                 |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-06-07T11:39:19.645+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed Disc 1090519043   | session-1090519043                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(2000), Mult(3),   |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-06-07T11:39:20.245+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed TX(2000):         | session-1090519044                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(2000), Mult(3), Ver(1),     |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-06-07T11:39:20.237+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed TX(2000):         | session-1090519043                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(2000), Mult(3), Ver(1),     |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208500 | oper-state-change | 2023-06-07T11:39:22.262+02:00 | BFD session to neighbor has been         | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | removed                                  | session-1090519044                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208500 | oper-state-change | 2023-06-07T11:39:22.252+02:00 | BFD session to neighbor has been         | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | removed                                  | session-1090519043                    | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208500 | oper-state-change | 2023-06-07T11:40:48.262+02:00 | BFD session to neighbor has been         | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | removed                                  | session-1090519041                    | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:03.056+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed Disc 1090519041   | session-1090519041                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:03.052+02:00 | BFD session to neighbor 15.254.106.192   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan492 has been created    | session-1090519041                    | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:03.043+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed Disc 1090519041   | session-1090519041                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:03.038+02:00 | BFD session to neighbor 15.254.106.192   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan492 has been created    | session-1090519041                    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:05.034+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed Disc 1090519042   | session-1090519042                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:05.031+02:00 | BFD session to neighbor 15.254.103.192   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan496 has been created    | session-1090519042                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:09.041+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed Disc 1090519043   | session-1090519043                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:09.038+02:00 | BFD session to neighbor 15.254.106.191   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan492 has been created    | session-1090519043                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:11.042+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed Disc 1090519044   | session-1090519044                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:11.039+02:00 | BFD session to neighbor 15.254.103.191   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan496 has been created    | session-1090519044                    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208501 | oper-state-change | 2023-07-05T19:20:18.853+02:00 | BFD session 1090519042 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.103.192 on interface vlan496 is   | session-1090519042                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:18.839+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed TX(0): RX(0):     | session-1090519042                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(0), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:18.837+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed Disc 1090519042   | session-1090519042                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208501 | oper-state-change | 2023-07-05T19:20:18.861+02:00 | BFD session 1090519041 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.106.192 on interface vlan492 is   | session-1090519041                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:18.848+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed TX(0): RX(0):     | session-1090519041                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(0), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:18.847+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed Disc 1090519041   | session-1090519041                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:19.080+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519042 has changed TX(500):          | session-1090519042                    | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1),      |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:19.057+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519041 has changed TX(50): RX(50):   | session-1090519041                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208501 | oper-state-change | 2023-07-05T19:20:20.864+02:00 | BFD session 1090519043 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.106.191 on interface vlan492 is   | session-1090519043                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:20.858+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed TX(0): RX(0):     | session-1090519043                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(0), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:20.857+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed Disc 1090519043   | session-1090519043                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:21.054+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519043 has changed TX(50): RX(50):   | session-1090519043                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208501 | oper-state-change | 2023-07-05T19:20:22.979+02:00 | BFD session 1090519044 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.103.191 on interface vlan496 is   | session-1090519044                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:22.972+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed TX(0): RX(0):     | session-1090519044                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(0), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:22.971+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed Disc 1090519044   | session-1090519044                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:23.054+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519044 has changed TX(500):          | session-1090519044                    | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1),      |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-07-05T19:21:04.009+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed Disc 1090519045   | session-1090519045                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208499 | oper-state-change | 2023-07-05T19:21:04.006+02:00 | BFD session to neighbor 15.100.7.41 on   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | interface vlan472 has been created       | session-1090519045                    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-07-05T19:21:17.054+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519045 has changed TX(2000):         | session-1090519045                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(0), Mult(3), Ver(1), Auth   |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4215661 | oper-state-change | 2023-07-05T19:21:23.058+02:00 | BFD session 1090519045 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.100.7.41 on interface vlan472 is      | session-1090519045                    | 
|                     |            |          |          |                   |                               | down. Reason: No Diagnostic.             |                                       | 
| pod-1/cl201-eu-spdc | 1090519046 | Info     | E4209847 | oper-state-change | 2023-07-07T14:56:57.150+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519046 has changed Disc 1090519046   | session-1090519046                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519046 | Info     | E4208499 | oper-state-change | 2023-07-07T14:56:57.147+02:00 | BFD session to neighbor 15.100.103.41    | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan471 has been created    | session-1090519046                    | 
| pod-1/cl201-eu-spdc | 1090519046 | Info     | E4209848 | oper-state-change | 2023-07-07T14:57:10.420+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519046 has changed TX(2000):         | session-1090519046                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(0), Mult(3), Ver(1), Auth   |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519046 | Info     | E4215661 | oper-state-change | 2023-07-07T14:57:16.424+02:00 | BFD session 1090519046 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.100.103.41 on interface vlan471 is    | session-1090519046                    | 
|                     |            |          |          |                   |                               | down. Reason: No Diagnostic.             |                                       | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209847 | oper-state-change | 2023-07-07T14:57:19.197+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519047 has changed Disc 1090519047   | session-1090519047                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4208499 | oper-state-change | 2023-07-07T14:57:19.188+02:00 | BFD session to neighbor 15.254.133.55    | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan473 has been created    | session-1090519047                    | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4208501 | oper-state-change | 2023-07-07T14:57:32.473+02:00 | BFD session 1090519047 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.133.55 on interface vlan473 is    | session-1090519047                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209848 | oper-state-change | 2023-07-07T14:57:32.416+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519047 has changed TX(2000):         | session-1090519047                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(0), Mult(3), Ver(1), Auth   |                                       | 
|                     |            |          |          |                   |                               | Type(No authentication)                  |                                       | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209848 | oper-state-change | 2023-07-07T14:57:34.416+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519047 has changed TX(500):          | session-1090519047                    | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1),      |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209848 | oper-state-change | 2023-07-07T14:57:34.351+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519047 has changed TX(2000):         | session-1090519047                    | 
|                     |            |          |          |                   |                               | RX(2000): ST(2000), Mult(3), Ver(1),     |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209847 | oper-state-change | 2023-07-07T14:57:34.349+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519047 has changed Disc 1090519047   | session-1090519047                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209847 | oper-state-change | 2023-07-07T14:58:35.274+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519048 has changed Disc 1090519048   | session-1090519048                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4208499 | oper-state-change | 2023-07-07T14:58:35.271+02:00 | BFD session to neighbor 15.254.133.191   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan473 has been created    | session-1090519048                    | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209847 | oper-state-change | 2023-07-07T14:58:35.265+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519048 has changed Disc 1090519048   | session-1090519048                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4208499 | oper-state-change | 2023-07-07T14:58:35.262+02:00 | BFD session to neighbor 15.254.133.191   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan473 has been created    | session-1090519048                    | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4208501 | oper-state-change | 2023-07-07T14:58:47.830+02:00 | BFD session 1090519048 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.133.191 on interface vlan473 is   | session-1090519048                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209848 | oper-state-change | 2023-07-07T14:58:47.824+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519048 has changed TX(0): RX(0):     | session-1090519048                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(0), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209847 | oper-state-change | 2023-07-07T14:58:47.822+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519048 has changed Disc 1090519048   | session-1090519048                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209848 | oper-state-change | 2023-07-07T14:58:48.351+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519048 has changed TX(500):          | session-1090519048                    | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1),      |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4209847 | oper-state-change | 2023-07-07T14:58:53.266+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519049 has changed Disc 1090519049   | session-1090519049                    | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3),      |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4208499 | oper-state-change | 2023-07-07T14:58:53.263+02:00 | BFD session to neighbor 15.254.133.193   | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | on interface vlan473 has been created    | session-1090519049                    | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4208501 | oper-state-change | 2023-07-07T14:59:05.228+02:00 | BFD session 1090519049 to neighbor       | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 15.254.133.193 on interface vlan473 is   | session-1090519049                    | 
|                     |            |          |          |                   |                               | up.                                      |                                       | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4209848 | oper-state-change | 2023-07-07T14:59:05.222+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519049 has changed TX(0): RX(0):     | session-1090519049                    | 
|                     |            |          |          |                   |                               | ST(2000), Mult(0), Ver(1), Auth Type(No  |                                       | 
|                     |            |          |          |                   |                               | authentication)                          |                                       | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4209847 | oper-state-change | 2023-07-07T14:59:05.220+02:00 | Active parameter of BFD session          | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519049 has changed Disc 1090519049   | session-1090519049                    | 
|                     |            |          |          |                   |                               | TX(500): RX(500): ST(2000), Mult(3),     |                                       | 
|                     |            |          |          |                   |                               | Ver(1)                                   |                                       | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4209848 | oper-state-change | 2023-07-07T14:59:06.352+02:00 | Local parameter of BFD session           | topology/pod-1/node-201/sys/bfd/inst/ | 
|                     |            |          |          |                   |                               | 1090519049 has changed TX(500):          | session-1090519049                    | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1),      |                                       | 
|                     |            |          |          |                   |                               | Auth Type(No authentication)             |                                       | 
+---------------------+------------+----------+----------+-------------------+-------------------------------+------------------------------------------+---------------------------------------+
```

Developer

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --view all
    --when 90d

{
    "duration": 5054,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 3123,
        "total_time": 3522
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

True	399	-	connect apic11o.emea-sp.cisco.com:443
True	310	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	292	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	336	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	314	2	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=faults,no-scoped,subtree
True	988	1000	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	883	1000	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolBfd.md)