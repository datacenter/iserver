# Node Protocol - LLDP

## All view

```
# iserver get aci proto lldp
    --apic apic11
    --node bl205-eu-spdc
    --view all
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol LLDP - Instance [#1]
-----------------------------

+---------------------+-------------+--------+---------+-----------+-----------------+------------------------+-----------+--------+
| Node                | Admin State | Health | Faults  | Hold Time | Init Delay Time | Transmission Frequency | Neighbors | Errors |
+---------------------+-------------+--------+---------+-----------+-----------------+------------------------+-----------+--------+
| pod-1/bl205-eu-spdc | enabled     | 100    | 0 0 0 0 | 120       | 2               | 30                     | 13        | X      | 
+---------------------+-------------+--------+---------+-----------+-----------------+------------------------+-----------+--------+

Protocol LLDP - Stats [#1]
--------------------------

+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
| Node                | Packets Sent | Packets Received | Packets Discarded | Error Received Packets | Unrecognized TLV | Adjacencies Added | Adjacencies Removed | Entries Aged |
+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+
| pod-1/bl205-eu-spdc | 1914456      | 1916553          | 0                 | 0                      | 0                | 17                | 0                   | 0            | 
+---------------------+--------------+------------------+-------------------+------------------------+------------------+-------------------+---------------------+--------------+

LLDP Adjacency [#13]
--------------------

+---------------------+--------+---------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+
| Node                | Health | Faults  | Interface ID | Hold Time | Neighbor Device               | MAC               | Port            | VLAN | Port Description                         | Capabilities  |
+---------------------+--------+---------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/35      | 120       | s101-eu-spdc                  | 4c:71:0d:55:d1:d1 | Eth1/5          |      | topology/pod-1/paths-101/pathep-[eth1/5] | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/36      | 120       | s102-eu-spdc                  | 8c:94:1f:fa:54:25 | Eth1/5          |      | topology/pod-1/paths-102/pathep-[eth1/5] | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | mgmt0        | 120       | r22-eu-spdc.emea-sp.cisco.com | 70:61:7b:d8:60:da | Ethernet1/27    | 12   | ***** BL-205-206 ACI1 Management *****   | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/1       | 120       | FI-ucsb1-eu-spdc-A.cisco.com  | 00:3a:9c:bd:92:40 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/2       | 120       | FI-ucsb1-eu-spdc-B.cisco.com  | 00:3a:9c:bd:8f:40 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/11      | 120       | HX1-eu-spdc-A.cisco.com       | 00:3a:9c:c0:04:80 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/12      | 120       | HX1-eu-spdc-B.cisco.com       | 00:3a:9c:c0:04:20 | Eth1/51         | 1    | U: Uplink                                | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/15      | 121       |                               | 3c:fd:fe:e2:f8:18 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/16      | 121       |                               | 3c:fd:fe:e2:ee:d8 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/19      | 121       |                               | 3c:fd:fe:e2:f4:f8 |                 |      |                                          |               | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/24      | 120       | ipn-eu-spdc.emea-sp.cisco.com | ec:ce:13:c0:46:34 | Ethernet3/25    |      | ***** BGP Peering to ACI1 BL205  ******* | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/27      | 120       | Yavin-129                     | e0:0e:da:a3:38:28 | Ethernet1/21    | 1    | Ethernet1/21                             | bridge,router | 
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | eth1/28      | 120       | Lisboa-54                     | 00:8a:96:1c:7c:de | TenGigE0/0/0/45 |      | *** Link to BL-205 for SR Handoff ***    | router        | 
+---------------------+--------+---------+--------------+-----------+-------------------------------+-------------------+-----------------+------+------------------------------------------+---------------+

Protocol LLDP - Faults [#0]
---------------------------
None

Protocol LLDP - Fault Records last 90d [#0]
-------------------------------------------
None

Protocol LLDP - Event Logs last 90d [#115]
------------------------------------------

+---------------------+--------------+----------+----------+-------------------+-------------------------------+-----------------------------------------+----------------------------------------+
| Node                | Interface Id | Severity | Code     | Cause             | Created Time                  | Description                             | Affected                               |
+---------------------+--------------+----------+----------+-------------------+-------------------------------+-----------------------------------------+----------------------------------------+
| pod-1/bl205-eu-spdc | eth1/35      | Info     | E4205082 | oper-state-change | 2023-06-12T09:17:53.391+02:00 | New adjacency discovered on eth1/35     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:4c:71:0d:55:d1:d1   | if-[eth1/35]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/5            |                                        | 
| pod-1/bl205-eu-spdc | eth1/35      | Info     | E4205082 | oper-state-change | 2023-05-31T23:06:12.266+02:00 | New adjacency discovered on eth1/35     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:4c:71:0d:55:d1:d1   | if-[eth1/35]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/5            |                                        | 
| pod-1/bl205-eu-spdc | eth1/36      | Info     | E4205082 | oper-state-change | 2023-06-12T09:17:53.999+02:00 | New adjacency discovered on eth1/36     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:8c:94:1f:fa:54:25   | if-[eth1/36]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/5            |                                        | 
| pod-1/bl205-eu-spdc | eth1/36      | Info     | E4205082 | oper-state-change | 2023-05-31T23:06:13.107+02:00 | New adjacency discovered on eth1/36     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:8c:94:1f:fa:54:25   | if-[eth1/36]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/5            |                                        | 
| pod-1/bl205-eu-spdc | eth1/36      | Info     | E4205082 | oper-state-change | 2023-05-31T22:30:23.782+02:00 | New adjacency discovered on eth1/36     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:8c:94:1f:fa:54:25   | if-[eth1/36]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/5            |                                        | 
| pod-1/bl205-eu-spdc | eth1/36      | Info     | E4205083 | oper-state-change | 2023-05-31T22:20:00.307+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/36]/adj-1                     | 
| pod-1/bl205-eu-spdc | mgmt0        | Info     | E4205082 | oper-state-change | 2023-06-12T10:35:08.039+02:00 | New adjacency discovered on mgmt0       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:70:61:7b:d8:60:da   | if-[mgmt0]/adj-1                       | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/27        |                                        | 
| pod-1/bl205-eu-spdc | mgmt0        | Info     | E4205082 | oper-state-change | 2023-06-12T10:35:07.270+02:00 | New adjacency discovered on mgmt0       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:70:61:7b:d8:60:da   | if-[mgmt0]/adj-1                       | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/27        |                                        | 
| pod-1/bl205-eu-spdc | mgmt0        | Info     | E4205082 | oper-state-change | 2023-05-31T23:08:42.949+02:00 | New adjacency discovered on mgmt0       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:70:61:7b:d8:60:da   | if-[mgmt0]/adj-1                       | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/27        |                                        | 
| pod-1/bl205-eu-spdc | mgmt0        | Info     | E4205082 | oper-state-change | 2023-05-31T23:08:42.345+02:00 | New adjacency discovered on mgmt0       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:70:61:7b:d8:60:da   | if-[mgmt0]/adj-1                       | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/27        |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-07-12T17:50:38.229+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205082 | oper-state-change | 2023-07-12T17:50:38.225+02:00 | New adjacency discovered on eth1/1      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:92:40   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-07-12T17:50:38.206+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-07-12T17:50:38.198+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205082 | oper-state-change | 2023-07-12T17:50:38.194+02:00 | New adjacency discovered on eth1/1      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:92:40   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205083 | oper-state-change | 2023-07-12T17:50:04.873+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/1]/adj-1                      | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:24.199+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:24.196+02:00 | New adjacency discovered on eth1/1      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:92:40   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:24.175+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:24.166+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:24.159+02:00 | New adjacency discovered on eth1/1      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:92:40   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-06-07T18:23:12.689+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205082 | oper-state-change | 2023-06-07T18:23:12.686+02:00 | New adjacency discovered on eth1/1      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:92:40   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-06-07T18:23:12.675+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-06-07T18:23:12.664+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205082 | oper-state-change | 2023-06-07T18:23:12.658+02:00 | New adjacency discovered on eth1/1      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:92:40   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205083 | oper-state-change | 2023-06-07T18:12:47.497+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/1]/adj-1                      | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.999+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205082 | oper-state-change | 2023-05-31T23:11:00.996+02:00 | New adjacency discovered on eth1/1      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:92:40   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/51        |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.985+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.977+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/1       | Info     | E4205082 | oper-state-change | 2023-05-31T23:11:00.972+02:00 | New adjacency discovered on eth1/1      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:92:40   | if-[eth1/1]/adj-1                      | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/51        |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:23.768+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:23.765+02:00 | New adjacency discovered on eth1/2      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:8f:40   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:23.753+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:23.732+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:23.727+02:00 | New adjacency discovered on eth1/2      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:8f:40   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-06-07T19:00:32.126+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Info     | E4205082 | oper-state-change | 2023-06-07T19:00:32.123+02:00 | New adjacency discovered on eth1/2      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:8f:40   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-06-07T19:00:32.104+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-06-07T19:00:32.096+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Info     | E4205082 | oper-state-change | 2023-06-07T19:00:32.093+02:00 | New adjacency discovered on eth1/2      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:8f:40   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Info     | E4205083 | oper-state-change | 2023-06-07T18:50:05.659+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/2]/adj-1                      | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.092+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Info     | E4205082 | oper-state-change | 2023-05-31T23:11:00.088+02:00 | New adjacency discovered on eth1/2      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:8f:40   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/51        |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.073+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.063+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/2       | Info     | E4205082 | oper-state-change | 2023-05-31T23:11:00.058+02:00 | New adjacency discovered on eth1/2      | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:bd:8f:40   | if-[eth1/2]/adj-1                      | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/51        |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:22.668+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:22.665+02:00 | New adjacency discovered on eth1/11     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:c0:04:80   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:22.660+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:22.653+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:22.649+02:00 | New adjacency discovered on eth1/11     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:c0:04:80   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Info     | E4205083 | oper-state-change | 2023-06-07T11:56:52.574+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/11]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/11      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:01.949+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Info     | E4205082 | oper-state-change | 2023-05-31T23:11:01.946+02:00 | New adjacency discovered on eth1/11     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:c0:04:80   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:01.936+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:01.927+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/11      | Info     | E4205082 | oper-state-change | 2023-05-31T23:11:01.924+02:00 | New adjacency discovered on eth1/11     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:c0:04:80   | if-[eth1/11]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:22.178+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:22.175+02:00 | New adjacency discovered on eth1/12     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:c0:04:20   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:22.170+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:22.163+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:22.159+02:00 | New adjacency discovered on eth1/12     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:c0:04:20   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Info     | E4205083 | oper-state-change | 2023-06-07T11:57:06.897+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/12]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/12      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.536+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Info     | E4205082 | oper-state-change | 2023-05-31T23:11:00.533+02:00 | New adjacency discovered on eth1/12     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:c0:04:20   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.522+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:11:00.514+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/12      | Info     | E4205082 | oper-state-change | 2023-05-31T23:11:00.511+02:00 | New adjacency discovered on eth1/12     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:3a:9c:c0:04:20   | if-[eth1/12]/adj-1                     | 
|                     |              |          |          |                   |                               | port Locally assigned:Eth1/51           |                                        | 
| pod-1/bl205-eu-spdc | eth1/15      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:46.287+02:00 | New adjacency discovered on eth1/15     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f8:18   | if-[eth1/15]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f8:18      |                                        | 
| pod-1/bl205-eu-spdc | eth1/15      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:46.267+02:00 | New adjacency discovered on eth1/15     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f8:18   | if-[eth1/15]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f8:18      |                                        | 
| pod-1/bl205-eu-spdc | eth1/15      | Info     | E4205083 | oper-state-change | 2023-06-12T16:52:35.412+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/15]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/15      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:33.537+02:00 | New adjacency discovered on eth1/15     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f8:18   | if-[eth1/15]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f8:18      |                                        | 
| pod-1/bl205-eu-spdc | eth1/15      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:33.517+02:00 | New adjacency discovered on eth1/15     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f8:18   | if-[eth1/15]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f8:18      |                                        | 
| pod-1/bl205-eu-spdc | eth1/15      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:16.777+02:00 | New adjacency discovered on eth1/15     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f8:18   | if-[eth1/15]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f8:18      |                                        | 
| pod-1/bl205-eu-spdc | eth1/15      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:16.757+02:00 | New adjacency discovered on eth1/15     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f8:18   | if-[eth1/15]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f8:18      |                                        | 
| pod-1/bl205-eu-spdc | eth1/16      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:47.702+02:00 | New adjacency discovered on eth1/16     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:ee:d8   | if-[eth1/16]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:ee:d8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/16      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:47.681+02:00 | New adjacency discovered on eth1/16     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:ee:d8   | if-[eth1/16]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:ee:d8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/16      | Info     | E4205083 | oper-state-change | 2023-06-12T16:52:35.468+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/16]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/16      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:33.083+02:00 | New adjacency discovered on eth1/16     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:ee:d8   | if-[eth1/16]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:ee:d8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/16      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:33.063+02:00 | New adjacency discovered on eth1/16     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:ee:d8   | if-[eth1/16]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:ee:d8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/16      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:15.340+02:00 | New adjacency discovered on eth1/16     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:ee:d8   | if-[eth1/16]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:ee:d8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/16      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:15.307+02:00 | New adjacency discovered on eth1/16     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:ee:d8   | if-[eth1/16]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:ee:d8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/19      | Warn     | E4209105 | config-mismatch   | 2023-06-12T16:52:44.888+02:00 | LLDP neighbor port vlan information is  | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | missing                                 | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:44.885+02:00 | New adjacency discovered on eth1/19     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f4:f8   | if-[eth1/19]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f4:f8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/19      | Warn     | E4209105 | config-mismatch   | 2023-06-12T16:52:44.859+02:00 | LLDP neighbor port vlan information is  | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | missing                                 | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Info     | E4205083 | oper-state-change | 2023-06-12T16:52:34.895+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Warn     | E4209105 | config-mismatch   | 2023-06-12T16:52:32.040+02:00 | LLDP neighbor port vlan information is  | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | missing                                 | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:32.038+02:00 | New adjacency discovered on eth1/19     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f4:f8   | if-[eth1/19]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f4:f8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/19      | Warn     | E4209105 | config-mismatch   | 2023-06-12T16:52:32.027+02:00 | LLDP neighbor port vlan information is  | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | missing                                 | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Warn     | E4209105 | config-mismatch   | 2023-06-12T16:52:32.020+02:00 | LLDP neighbor port vlan information is  | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | missing                                 | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Info     | E4205082 | oper-state-change | 2023-06-12T16:52:32.017+02:00 | New adjacency discovered on eth1/19     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f4:f8   | if-[eth1/19]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f4:f8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/19      | Info     | E4205083 | oper-state-change | 2023-06-07T19:01:40.679+02:00 | Adjacency removed                       | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               |                                         | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Warn     | E4209105 | config-mismatch   | 2023-05-31T23:10:14.081+02:00 | LLDP neighbor port vlan information is  | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | missing                                 | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:14.079+02:00 | New adjacency discovered on eth1/19     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f4:f8   | if-[eth1/19]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f4:f8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/19      | Warn     | E4209105 | config-mismatch   | 2023-05-31T23:10:14.067+02:00 | LLDP neighbor port vlan information is  | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | missing                                 | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Warn     | E4209105 | config-mismatch   | 2023-05-31T23:10:14.060+02:00 | LLDP neighbor port vlan information is  | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | missing                                 | if-[eth1/19]/adj-1                     | 
| pod-1/bl205-eu-spdc | eth1/19      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:14.057+02:00 | New adjacency discovered on eth1/19     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:3c:fd:fe:e2:f4:f8   | if-[eth1/19]/adj-1                     | 
|                     |              |          |          |                   |                               | port Mac address:3c:fd:fe:e2:f4:f8      |                                        | 
| pod-1/bl205-eu-spdc | eth1/24      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:03.572+02:00 | New adjacency discovered on eth1/24     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:ec:ce:13:c0:46:34   | if-[eth1/24]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet3/25        |                                        | 
| pod-1/bl205-eu-spdc | eth1/24      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:03.535+02:00 | New adjacency discovered on eth1/24     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:ec:ce:13:c0:46:34   | if-[eth1/24]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet3/25        |                                        | 
| pod-1/bl205-eu-spdc | eth1/24      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:17.880+02:00 | New adjacency discovered on eth1/24     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:ec:ce:13:c0:46:34   | if-[eth1/24]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet3/25        |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:17.975+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:17.972+02:00 | New adjacency discovered on eth1/27     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:e0:0e:da:a3:38:28   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/21        |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:17.952+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Maj      | E4209330 | config-mismatch   | 2023-06-12T10:37:17.945+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:17.940+02:00 | New adjacency discovered on eth1/27     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:e0:0e:da:a3:38:28   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/21        |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:10:52.177+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:52.173+02:00 | New adjacency discovered on eth1/27     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:e0:0e:da:a3:38:28   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/21        |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:10:52.146+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Maj      | E4209330 | config-mismatch   | 2023-05-31T23:10:52.138+02:00 | LLDP neighbor is bridge and its port    | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | vlan 1 mismatches with the local port   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | vlan Unspecified. If neighbor is        |                                        | 
|                     |              |          |          |                   |                               | running MST(802.1s) protocol, this      |                                        | 
|                     |              |          |          |                   |                               | could result in a layer2 topology with  |                                        | 
|                     |              |          |          |                   |                               | a loop                                  |                                        | 
| pod-1/bl205-eu-spdc | eth1/27      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:52.134+02:00 | New adjacency discovered on eth1/27     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:e0:0e:da:a3:38:28   | if-[eth1/27]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:Ethernet1/21        |                                        | 
| pod-1/bl205-eu-spdc | eth1/28      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:24.369+02:00 | New adjacency discovered on eth1/28     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:8a:96:1c:7c:de   | if-[eth1/28]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:TenGigE0/0/0/45     |                                        | 
| pod-1/bl205-eu-spdc | eth1/28      | Info     | E4205082 | oper-state-change | 2023-06-12T10:37:24.347+02:00 | New adjacency discovered on eth1/28     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:8a:96:1c:7c:de   | if-[eth1/28]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:TenGigE0/0/0/45     |                                        | 
| pod-1/bl205-eu-spdc | eth1/28      | Info     | E4205082 | oper-state-change | 2023-05-31T23:10:35.563+02:00 | New adjacency discovered on eth1/28     | topology/pod-1/node-205/sys/lldp/inst/ | 
|                     |              |          |          |                   |                               | chassis Mac address:00:8a:96:1c:7c:de   | if-[eth1/28]/adj-1                     | 
|                     |              |          |          |                   |                               | port Interface name:TenGigE0/0/0/45     |                                        | 
+---------------------+--------------+----------+----------+-------------------+-------------------------------+-----------------------------------------+----------------------------------------+
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp
    --apic apic11
    --node bl205-eu-spdc
    --view all
    --when 90d

{
    "duration": 4646,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 2529,
        "total_time": 2943
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

True	414	-	connect apic11o.emea-sp.cisco.com:443
True	298	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	283	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query rsp-subtree-include=health,fault-count
True	281	1	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/lldpInstStats
True	288	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	301	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query rsp-subtree-include=faults,no-scoped,subtree
True	353	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	725	1000	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolLldp.md)