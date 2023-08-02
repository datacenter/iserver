# Node Interface - Port Channel (PC)

## All view

```
# iserver get aci intf pc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id po1
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Port Channel - State [#1]
-----------------------------------

+----------------------+--------+---------+-----+------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
| Node                 | Health | Faults  | Id  | Name       | Protocol    | Admin | State | Reason | VPC | Members | Layer    | Mode  | Speed |
+----------------------+--------+---------+-----+------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po1 | SPN_PolGrp | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 10G   | 
+----------------------+--------+---------+-----+------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+

Interface Port Channel Member - Phy State [#1]
----------------------------------------------

+----------------------+-----+--------+--------------+--------+---------+-------+------+-------+--------+-------+------+
| Node                 | Id  | Active | Interface Id | Health | Faults  | Admin | Oper | Mode  | Duplex | Speed | VLAN |
+----------------------+-----+--------+--------------+--------+---------+-------+------+-------+--------+-------+------+
| pod-1/bl2205-eu-spdc | po1 | V      | eth1/27      | 100    | 0 0 0 0 | up    | up   | trunk | full   | 10G   |      | 
+----------------------+-----+--------+--------------+--------+---------+-------+------+-------+--------+-------+------+

Interface Port Channel - VLAN [#1]
----------------------------------

+----------------------+-----+---------------+------------+--------------+---------+-------+-------+-----+--------------+
| Node                 | Id  | Allowed VLANs | Oper VLANs | Primary VLAN | VLAN ID | HW ID | Encap | EPG | Fabric Encap |
+----------------------+-----+---------------+------------+--------------+---------+-------+-------+-----+--------------+
| pod-1/bl2205-eu-spdc | po1 |               |            | vlan-1       |         |       |       |     |              | 
+----------------------+-----+---------------+------------+--------------+---------+-------+-------+-----+--------------+

Interface Port Channel - Traffic Counters [#1]
----------------------------------------------

+----------------------+-----+----------+--------+--------+-------+------+-----+-----------+--------+--------+-------+------+-----+
| Node                 | Id  | Bytes In | Ucast  | Mcast  | Bcast | Disc | Err | Bytes Out | Ucast  | Mcast  | Bcast | Disc | Err |
+----------------------+-----+----------+--------+--------+-------+------+-----+-----------+--------+--------+-------+------+-----+
| pod-1/bl2205-eu-spdc | po1 | 67109044 | 311269 | 311269 | 0     | 0    | 0   | 95558128  | 311258 | 311258 | 0     | 0    | 0   | 
+----------------------+-----+----------+--------+--------+-------+------+-----+-----------+--------+--------+-------+------+-----+

Interface Port Channel - Ether Counters [#1]
--------------------------------------------

+----------------------+-----+---------+-----------+--------+-------+------+----------+-----------+-----------+------------+-------------+
| Node                 | Id  | Packets | Bytes     | Mcast  | Bcast | <64B | 65B-127B | 128B-255B | 256B-511B | 512B-1023B | 1024B-1518B |
+----------------------+-----+---------+-----------+--------+-------+------+----------+-----------+-----------+------------+-------------+
| pod-1/bl2205-eu-spdc | po1 | 622527  | 162667172 | 622527 | 0     | 0    | 0        | 249009    | 373518    | 0          | 0           | 
+----------------------+-----+---------+-----------+--------+-------+------+----------+-----------+-----------+------------+-------------+

Interface Port Channel Member - LACP State [#1]
-----------------------------------------------

+----------------------+-----+--------+-----------+---------+----------+---------------+------------------------------------------+-------+
| Node                 | Id  | Active | Interface | Admin   | Port Num | Port Priority | Activity Flags                           | Key   |
+----------------------+-----+--------+-----------+---------+----------+---------------+------------------------------------------+-------+
| pod-1/bl2205-eu-spdc | po1 | V      | eth1/27   | enabled | 283      | 32768         | active,aggregate,collect,distribute,sync | 33111 | 
+----------------------+-----+--------+-----------+---------+----------+---------------+------------------------------------------+-------+

Interface Port Channel Member - LACP Neighbor [#1]
--------------------------------------------------

+----------------------+-----+--------+-----------+--------------+-------------------+-------------------+------------------------------------------+---------+
| Node                 | Id  | Active | Interface | Nbr Port Num | Nbr Port Priority | Nbr System Id     | Nbr Activity Flags                       | Nbr Key |
+----------------------+-----+--------+-----------+--------------+-------------------+-------------------+------------------------------------------+---------+
| pod-1/bl2205-eu-spdc | po1 | V      | eth1/27   | 345          | 32768             | E0:0E:DA:A3:38:13 | active,aggregate,collect,distribute,sync | 2       | 
+----------------------+-----+--------+-----------+--------------+-------------------+-------------------+------------------------------------------+---------+

Interface Port Channel Member - LACP PDU [#1]
---------------------------------------------

+----------------------+-----+--------+-----------+----------+----------+-------------+-------------+-------------+-----------------+-----------------+
| Node                 | Id  | Active | Interface | PDU Sent | PDU Rcvd | PDU Timeout | Marker Sent | Marker Rcvd | Marker Rsp Sent | Marker Rsp Rcvd |
+----------------------+-----+--------+-----------+----------+----------+-------------+-------------+-------------+-----------------+-----------------+
| pod-1/bl2205-eu-spdc | po1 | V      | eth1/27   | 124498   | 124512   | 0           | 0           | 0           | 0               | 0               | 
+----------------------+-----+--------+-----------+----------+----------+-------------+-------------+-------------+-----------------+-----------------+

Interface Port Channel - Faults [#0]
------------------------------------
None

Interface Port Channel - Fault Records last 10y [#64]
-----------------------------------------------------

+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code  | Cause                   | Created Time                  | Lifecycle        | Description                                                                     |
+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-09-22T17:38:32.853+02:00 | soaking          | Port is down, reason being init(connected), used by EPG on node 2205 of fabric  | 
|                      |           |      |       |                         |                               |                  | ACI2-EU-SPDC with hostname bl2205-eu-spdc                                       | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-09-22T17:40:53.117+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-09-22T17:47:46.500+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0532 | interface-physical-down | 2021-09-22T17:49:53.196+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0532 | interface-physical-down | 2021-09-22T18:49:53.810+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-10-14T19:08:40.557+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-10-14T19:10:40.741+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F1192 | config-failure          | 2021-11-09T10:55:51.428+02:00 | soaking          | Port-channel(po1) membership configuration failure for eth1/25                  | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F1192 | config-failure          | 2021-11-09T10:56:00.127+02:00 | soaking-clearing | Port-channel(po1) membership configuration failure for eth1/25                  | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F1192 | config-failure          | 2021-11-09T10:56:21.101+02:00 |                  | Port-channel(po1) membership configuration failure for eth1/25                  | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-12-17T13:15:50.357+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-01-14T00:01:03.417+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-01-14T00:02:02.560+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-01-14T00:04:18.690+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-01-14T01:04:19.291+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-01-27T16:48:01.835+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-01-27T16:49:00.464+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-01-27T16:51:16.846+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-01-27T17:51:17.489+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-04-22T15:56:36.277+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-04-22T15:57:35.987+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-04-22T15:59:51.172+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-04-22T16:59:51.990+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-05-09T23:40:41.869+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-05-09T23:43:11.178+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-05-09T23:48:08.997+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-05-09T23:50:11.286+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-05-10T00:50:11.895+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-13T12:13:44.025+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-13T12:14:51.436+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-06-13T12:16:58.786+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-06-13T13:16:59.392+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-18T12:13:05.029+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-18T12:15:19.688+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-18T12:16:53.846+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-06-18T12:19:19.718+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-06-18T13:19:20.518+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:03.651+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:59.870+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-09-14T23:59:19.033+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-09-15T00:59:19.748+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-02T20:49:49.417+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-02T20:50:39.897+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-03-02T20:52:49.629+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-03-02T21:52:50.188+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-03T02:19:27.603+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-03T02:21:53.202+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-03T02:30:07.889+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-03-03T02:32:23.297+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-03-03T03:32:24.448+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-05-30T21:08:36.206+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-05-30T21:09:33.766+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-05-30T21:11:51.397+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-05-30T22:11:51.954+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-07T11:57:06.889+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-07T11:59:16.898+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-12T11:30:18.855+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-12T11:31:16.856+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-06-12T11:33:33.562+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-06-12T12:33:35.173+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-18T09:46:23.479+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-18T09:47:29.645+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-06-18T09:49:38.647+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-06-18T10:49:39.134+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+

Interface Port Channel Event Logs last 10y [#4]
-----------------------------------------------

+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code     | Cause     | Created Time                  | Description                         | Change Set                                                                      |
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Info | E4215671 | port-down | 2023-06-07T11:57:06.899+02:00 | Port is down. Reason: noOperMembers | lastLinkStChg (New: 2023-06-07T11:57:06.850+02:00), operSt (New: down),         | 
|                      |           |      |          |           |                               |                                     | operStQual (New: port-channel-members-down)                                     | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Info | E4215670 | port-up   | 2023-06-12T11:31:16.883+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-12T11:31:16.829+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Info | E4215671 | port-down | 2023-06-18T09:45:00.384+02:00 | Port is down. Reason: disabled      | accessVlan:vlan-0, backplaneMac:00:00:00:00:00:00, bundleBupId:1,               | 
|                      |           |      |          |           |                               |                                     | bundleIndex:unspecified, cfgAccessVlan:vlan-0, cfgNativeVlan:vlan-0,            | 
|                      |           |      |          |           |                               |                                     | currErrIndex:4294967295, diags:none, encap:3, errDisTimerRunning:no,            | 
|                      |           |      |          |           |                               |                                     | errVlanStatusHt:0, hwBdId:0, hwResourceId:0, intfT:phy, iod:45, lastErrors:0,   | 
|                      |           |      |          |           |                               |                                     | lastLinkStChg:1970-01-01T02:00:00.000+02:00, media:2, nativeVlan:vlan-0,        | 
|                      |           |      |          |           |                               |                                     | numActivePorts:0, numMbrUp:0, numOfSI:0, operDceMode:edge, operDuplex:auto,     | 
|                      |           |      |          |           |                               |                                     | operEEERxWkTime:0, operEEEState:not-applicable, operEEETxWkTime:0,              | 
|                      |           |      |          |           |                               |                                     | operErrDisQual:none, operFlowCtrl:0, operMdix:255, operMode:access,             | 
|                      |           |      |          |           |                               |                                     | operModeDetail:unknown, operPhyEnSt:unknown, operRouterMac:3C:13:CC:B9:EE:80,   | 
|                      |           |      |          |           |                               |                                     | operSpeed:auto, operSt:down, operStQual:admin-down, operStQualCode:0,           | 
|                      |           |      |          |           |                               |                                     | osSum:failed, portCfgWaitFlags:0, primaryVlan:vlan-1, resetCtr:0, txT:unknown,  | 
|                      |           |      |          |           |                               |                                     | usage:blacklist, userCfgdFlags:4, vdcId:1                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po1       | Info | E4215670 | port-up   | 2023-06-18T09:47:29.670+02:00 | Port is up                          | lastLinkStChg (New: 2023-06-18T09:47:29.600+02:00), operSt (New: up),           | 
|                      |           |      |          |           |                               |                                     | operStQual (New: none), resetCtr (New: 1)                                       | 
+----------------------+-----------+------+----------+-----------+-------------------------------+-------------------------------------+---------------------------------------------------------------------------------+

Interface Port Channel - Audit Logs last 10y [#0]
-------------------------------------------------
None
```

Developer

```
# iserver get aci intf pc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --id po1
    --view all

{
    "duration": 7687,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 416,
        "disconnect_time": 0,
        "mo_time": 5704,
        "total_time": 6120
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

True	416	-	connect apic21o.emea-sp.cisco.com:443
True	320	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	465	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	932	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	362	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	331	6	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpAdjEp&rsp-subtree-include=fault-count
True	300	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/lacpIf query rsp-subtree=children&rsp-subtree-class=lacpIfStats
True	542	6	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/lacp/inst query query-target=subtree&target-subtree-class=lacpIfStats
True	314	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	310	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	350	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree-include=faults,no-scoped,subtree
True	718	451	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	401	112	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	359	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./InterfacePc.md)