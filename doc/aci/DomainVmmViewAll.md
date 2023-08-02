# VMM Domain

## All view

```
# iserver get aci domain vmm --apic apic21 --name *cdc* --when any --view all

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call
[INFO] Requires per-interface api call

VMM Domain [#1]
---------------

+---------+----------------+-----------------+---------------------+---------+-----------------------+-----+--------------+
| Faults  | Domain         | AAEP            | VLAN Pool           | Mode    | Encapsulation Block   | EPG | Sec Domain   |
+---------+----------------+-----------------+---------------------+---------+-----------------------+-----+--------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | dynamic | [2501-2502] (static)  | 11  | UCSB1_SecDom | 
|         |                |                 |                     |         | [2503-2509] (static)  |     |              | 
|         |                |                 |                     |         | [2700-2999] (dynamic) |     |              | 
+---------+----------------+-----------------+---------------------+---------+-----------------------+-----+--------------+

VMM Domain - Properties [#1]
----------------------------

+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+
| Domain Name    | Encap | Access Mode | Cfg Infra PGs | Tag Collection | VM Folder Data | Ep Inventory | Ep Retention Time | Uplinks |
+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+
| EU-SPDC-CDC-22 | vlan  | RW          | no            | no             | no             | on-link      | 0                 | None    | 
+----------------+-------+-------------+---------------+----------------+----------------+--------------+-------------------+---------+

VMM Domain - vCenter [#1]
-------------------------

+---------+----------------+-------------------+-----------------+-------------+-------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+
| Faults  | Domain Name    | Controller Faults | Controller Name | IP          | Username          | Online | Model                                      | Serial   | Rev   | Datacenter | HV | VM  |
+---------+----------------+-------------------+-----------------+-------------+-------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+
| 0 6 0 0 | EU-SPDC-CDC-22 | 0 7 0 0           | EU-SPDC-CDC-22  | 10.58.28.18 | admin@admin.local | V      | VMware vCenter Server 7.0.3 build-21958406 | 53aba35e | 7.0.3 | eu-spdc-dc | 34 | 332 | 
+---------+----------------+-------------------+-----------------+-------------+-------------------+--------+--------------------------------------------+----------+-------+------------+----+-----+

VMM Domain - Associated EPG [#11]
---------------------------------

+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| Domain Name    | EPG                                | VLAN Pool           | Alloc Mode | VLAN | Deployment | Resolution    | Switching |
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | SPN_IntraLab/SPN_Connect_ANP/TEST2 | ESX-CDC-22_VlanPool | dynamic    | 2703 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | common/privIP_TEST/privIP_TEST     | ESX-CDC-22_VlanPool | dynamic    | 2804 | immediate  | immediate     | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | hefernan_ni-demo/APP/EPG1          | ESX-CDC-22_VlanPool | dynamic    | 2701 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | hefernan_ni-demo/APP/EPG2          | ESX-CDC-22_VlanPool | dynamic    | 2702 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    | ESX-CDC-22_VlanPool | dynamic    | 2704 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | nidemo/streamz/appserver           | ESX-CDC-22_VlanPool | dynamic    | 2901 | lazy       | lazy          | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | nidemo/streamz/database            | ESX-CDC-22_VlanPool | dynamic    | 2801 | lazy       | lazy          | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | nidemo/streamz/frontend            | ESX-CDC-22_VlanPool | dynamic    | 2900 | lazy       | lazy          | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | nidemo/streamz/management          | ESX-CDC-22_VlanPool | dynamic    | 2800 | lazy       | lazy          | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | vEPC/vSFO_ANP/WWW                  | ESX-CDC-22_VlanPool | dynamic    | 2902 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+
| EU-SPDC-CDC-22 | vEPC_demo/vEPG_ANP/vEPG_MGMT       | ESX-CDC-22_VlanPool | dynamic    | 2708 | immediate  | pre-provision | native    | 
+----------------+------------------------------------+---------------------+------------+------+------------+---------------+-----------+

VMM Domain - Nodes [#1]
-----------------------

+---------+----------------+-----------------+---------------------+----------------+------------+
| Faults  | Domain         | AAEP            | VLAN Pool           | Node           | Interfaces |
+---------+----------------+-----------------+---------------------+----------------+------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | cl2201-eu-spdc | 17         | 
|         |                |                 |                     | cl2202-eu-spdc | 17         | 
+---------+----------------+-----------------+---------------------+----------------+------------+

VMM Domain - Interfaces [#1]
----------------------------

+---------+----------------+-----------------+---------------------+----------------+-----------+
| Faults  | Domain         | AAEP            | VLAN Pool           | Node           | Interface |
+---------+----------------+-----------------+---------------------+----------------+-----------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | cl2201-eu-spdc | eth1/31   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/32   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/33   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/34   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/35   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/36   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/37   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/38   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/39   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/40   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/41   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/42   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/43   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/44   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/45   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/46   | 
|         |                |                 |                     | cl2201-eu-spdc | eth1/47   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/31   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/32   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/33   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/34   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/35   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/36   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/37   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/38   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/39   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/40   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/41   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/42   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/43   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/44   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/45   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/46   | 
|         |                |                 |                     | cl2202-eu-spdc | eth1/47   | 
+---------+----------------+-----------------+---------------------+----------------+-----------+

VMM Domain - Interfaces VLAN [#1]
---------------------------------

+---------+----------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| Faults  | Domain         | AAEP            | VLAN Pool           | Encapsulation Block   | Node           | Interface | State | Mode  | VLANs                                   |
+---------+----------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | ESX-CDC-22_AAEP | ESX-CDC-22_VlanPool | [2501-2502] (static)  | cl2201-eu-spdc | eth1/31   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                 |                     | [2503-2509] (static)  | cl2201-eu-spdc | eth1/32   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                 |                     | [2700-2999] (dynamic) | cl2201-eu-spdc | eth1/33   | down  | trunk | 2701-2704,2708,2902                     | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/34   | up    | trunk | 2701-2704,2708,2800-2801,2804,2900-2902 | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/35   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/36   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/37   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/38   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/39   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/40   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/41   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/42   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/43   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/44   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/45   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/46   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2201-eu-spdc | eth1/47   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/31   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/32   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/33   | down  | trunk | 2701-2704,2708,2902                     | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/34   | up    | trunk | 2701-2704,2708,2800-2801,2804,2900-2902 | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/35   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/36   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/37   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/38   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/39   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/40   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/41   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/42   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/43   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/44   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/45   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/46   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                |                 |                     |                       | cl2202-eu-spdc | eth1/47   | up    | trunk | 2701-2704,2708,2804,2902                | 
+---------+----------------+-----------------+---------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+

VMM Domain - Policy Relationships [#1]
--------------------------------------

+---------+----------------+-----------------+------------------------------------+
| Faults  | Domain         | Policy Type     | Policy Name                        |
+---------+----------------+-----------------+------------------------------------+
| 0 6 0 0 | EU-SPDC-CDC-22 | Application EPG | SPN_IntraLab/SPN_Connect_ANP/TEST2 | 
|         |                | Application EPG | common/privIP_TEST/privIP_TEST     | 
|         |                | Application EPG | hefernan_ni-demo/APP/EPG1          | 
|         |                | Application EPG | hefernan_ni-demo/APP/EPG2          | 
|         |                | Application EPG | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN    | 
|         |                | Application EPG | nidemo/streamz/appserver           | 
|         |                | Application EPG | nidemo/streamz/database            | 
|         |                | Application EPG | nidemo/streamz/frontend            | 
|         |                | Application EPG | nidemo/streamz/management          | 
|         |                | Application EPG | vEPC/vSFO_ANP/WWW                  | 
|         |                | Application EPG | vEPC_demo/vEPG_ANP/vEPG_MGMT       | 
|         |                | AAEP            | ESX-CDC-22_AAEP                    | 
+---------+----------------+-----------------+------------------------------------+

VMM Domain - Faults [#6]
------------------------

+----------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Domain         | Sev | Code  | Cause              | Created Time                  | Lifecycle | Description                                                                      |
+----------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Maj | F2840 | remote-oper-issues | 2023-06-19T14:01:51.640+02:00 | raised    | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |     |       |                    |                               |           | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |     |       |                    |                               |           | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj | F2840 | remote-oper-issues | 2023-06-19T14:21:51.755+02:00 | raised    | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |     |       |                    |                               |           | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |     |       |                    |                               |           | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj | F1313 | operational-issues | 2023-06-20T17:26:09.864+02:00 | raised    | Fault delegate: Operational issues detected on Host: esx00-eu-spdc.cisco.com     | 
|                |     |       |                    |                               |           | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2D:30, error: [Could not find        | 
|                |     |       |                    |                               |           | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj | F1313 | operational-issues | 2023-06-20T17:26:09.869+02:00 | raised    | Fault delegate: Operational issues detected on Host: esx00-eu-spdc.cisco.com     | 
|                |     |       |                    |                               |           | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2D:31, error: [Could not find        | 
|                |     |       |                    |                               |           | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj | F2840 | remote-oper-issues | 2023-07-26T17:14:15.281+02:00 | raised    | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |     |       |                    |                               |           | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |     |       |                    |                               |           | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj | F2840 | remote-oper-issues | 2023-07-26T17:32:49.442+02:00 | raised    | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |     |       |                    |                               |           | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |     |       |                    |                               |           | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |     |       |                    |                               |           | responding.                                                                      | 
+----------------+-----+-------+--------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+

VMM Domain - Fault Records last 10y [#1000]
-------------------------------------------

+----------------+------+---------+--------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
| Domain         | Sev  | Code    | Cause              | Created Time                  | Lifecycle        | Description                                                                      |
+----------------+------+---------+--------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T17:35:18.975+02:00 | raised           | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F0132   | operational-issues | 2023-07-26T17:33:48.853+02:00 |                  | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T17:32:49.506+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-07-26T17:25:18.744+02:00 |                  | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T17:16:18.515+02:00 | raised           | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T17:14:15.343+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-07-26T17:00:18.110+02:00 |                  | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T16:56:18.038+02:00 | raised           | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F0130   | connect-failed     | 2023-07-26T16:55:47.923+02:00 |                  | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T16:54:15.180+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F606262 | fsm-failed         | 2023-07-26T16:53:17.971+02:00 |                  | Fault delegate: [FSM:FAILED]: Add-FSM for VM Controller: EU-SPDC-CDC-22 VM       | 
|                |      |         |                    |                               |                  | Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to retrieve             | 
|                |      |         |                    |                               |                  | ServiceContent from the vCenter server 10.58.28.18(FSM:ifc:vmmmgr:CompCtrlrAdd)  | 
| EU-SPDC-CDC-22 | --   | F16438  | connect-failed     | 2023-07-26T16:53:17.970+02:00 |                  | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T16:36:17.537+02:00 | raised           | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T16:34:16.073+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F0132   | operational-issues | 2023-07-26T16:33:47.377+02:00 | retaining        | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T16:31:28.819+02:00 | raised-clearing  | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T16:29:47.280+02:00 | raised           | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T16:27:28.718+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-07-26T16:25:17.252+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F0132   | operational-issues | 2023-07-26T16:23:47.140+02:00 | retaining        | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T16:23:15.144+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T16:21:28.562+02:00 | raised-clearing  | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T16:19:47.036+02:00 | raised           | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T16:19:31.508+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T16:17:28.469+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.,Event channel from      | 
|                |      |         |                    |                               |                  | external VMM controller is down.                                                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T16:17:28.467+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T16:16:17.059+02:00 | raised           | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T16:13:58.992+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-07-26T16:00:16.677+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-07-26T16:00:16.676+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-07-26T16:00:16.674+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-07-26T15:59:16.622+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T15:57:54.641+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T15:57:53.583+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T15:57:52.592+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-07-26T15:57:06.556+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F0130   | connect-failed     | 2023-07-26T15:55:46.463+02:00 | retaining        | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | --   | F0132   | operational-issues | 2023-07-26T15:55:46.461+02:00 | retaining        | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.                         | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T15:53:27.815+02:00 | raised-clearing  | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.                         | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T15:53:27.813+02:00 | raised           | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.                         | 
| EU-SPDC-CDC-22 | --   | F606262 | fsm-failed         | 2023-07-26T15:53:16.579+02:00 | retaining        | Fault delegate: [FSM:FAILED]: Add-FSM for VM Controller: EU-SPDC-CDC-22 VM       | 
|                |      |         |                    |                               |                  | Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to retrieve             | 
|                |      |         |                    |                               |                  | ServiceContent from the vCenter server 10.58.28.18(FSM:ifc:vmmmgr:CompCtrlrAdd)  | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-07-26T15:53:16.576+02:00 | raised-clearing  | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-07-26T15:53:10.007+02:00 | raised           | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | --   | F16438  | connect-failed     | 2023-07-26T15:53:09.935+02:00 | retaining        | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-07-26T15:51:48.929+02:00 | raised           | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-07-26T15:51:46.361+02:00 | raised           | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: [Failed to retrieve ServiceContent from the vCenter       | 
|                |      |         |                    |                               |                  | server 10.58.28.18]. Please verify network connectivity of VMM controller        | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-07-26T15:51:33.850+02:00 | raised           | Fault delegate: [FSM:STAGE:RETRY:]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | --   | F16438  | connect-failed     | 2023-07-26T15:51:18.887+02:00 | retaining        | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F606262 | fsm-failed         | 2023-07-26T15:49:57.900+02:00 | raised           | Fault delegate: [FSM:FAILED]: Add-FSM for VM Controller: EU-SPDC-CDC-22 VM       | 
|                |      |         |                    |                               |                  | Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to retrieve             | 
|                |      |         |                    |                               |                  | ServiceContent from the vCenter server 10.58.28.18(FSM:ifc:vmmmgr:CompCtrlrAdd)  | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-07-26T15:49:57.897+02:00 | raised           | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T15:49:46.350+02:00 | raised           | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.,Event channel from      | 
|                |      |         |                    |                               |                  | external VMM controller is down.                                                 | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-07-26T15:49:42.723+02:00 | raised           | Fault delegate: [FSM:STAGE:RETRY:]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-07-26T15:49:24.934+02:00 | soaking          | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: [Failed to retrieve ServiceContent from the vCenter       | 
|                |      |         |                    |                               |                  | server 10.58.28.18]. Please verify network connectivity of VMM controller        | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T15:47:27.703+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.,Event channel from      | 
|                |      |         |                    |                               |                  | external VMM controller is down.                                                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-07-26T15:47:27.702+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-21T12:50:11.534+02:00 |                  | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CC, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-21T12:50:11.532+02:00 |                  | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CD, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-21T11:50:10.109+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CC, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-21T11:50:10.107+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CD, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-21T11:47:52.347+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CD, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-21T11:47:52.346+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CC, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:36:46.838+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CD, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:36:46.837+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CC, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:36:36.804+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CC, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.,NIC operational state is down.]                               | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:36:36.804+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CD, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.,NIC operational state is down.]                               | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:29:14.145+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CC, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:29:14.144+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CD, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:28:14.084+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx00-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2D:31, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:28:14.082+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx00-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2D:30, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:26:50.975+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CD, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:26:50.974+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CC, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:26:50.833+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx01-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2C:CD, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:26:09.957+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx00-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2D:31, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-20T17:26:09.955+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx00-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EE:2D:30, error: [Could not find        | 
|                |      |         |                    |                               |                  | adjacency for NIC.]                                                              | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-19T22:54:18.004+02:00 | raised           | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-19T22:51:54.829+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-19T14:24:05.992+02:00 | raised           | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-19T14:21:51.817+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-19T14:04:05.523+02:00 | raised           | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-19T14:01:51.701+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-19T13:42:34.944+02:00 | raised           | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-19T13:40:05.707+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.683+02:00 |                  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.682+02:00 |                  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.682+02:00 |                  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.681+02:00 |                  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.681+02:00 |                  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.681+02:00 |                  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.680+02:00 |                  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.680+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.680+02:00 |                  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.679+02:00 |                  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.678+02:00 |                  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.677+02:00 |                  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:46:56.675+02:00 |                  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.049+02:00 |                  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.049+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.048+02:00 |                  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.047+02:00 |                  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.046+02:00 |                  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.045+02:00 |                  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.045+02:00 |                  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.043+02:00 |                  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.043+02:00 |                  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.042+02:00 |                  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.041+02:00 |                  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.040+02:00 |                  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T10:20:56.039+02:00 |                  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.238+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.237+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.236+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.234+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.234+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.233+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.232+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.231+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.230+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.229+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.229+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.227+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:46:55.225+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:45.938+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.114+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.114+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.113+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.112+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.111+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.110+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.110+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.109+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.108+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.107+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:44.106+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:44:42.945+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.975+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.975+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.974+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.974+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.973+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.972+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.972+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.971+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.970+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.969+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.968+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.967+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:33:24.966+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.838+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.837+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.836+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.835+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.834+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.833+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.832+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.831+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.830+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.829+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.828+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.827+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:31:04.825+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.861+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.860+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.859+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.858+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.857+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.856+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.855+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.854+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.853+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.852+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.851+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:30:54.849+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:55.665+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:54.796+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:54.684+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:52.784+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:52.687+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:52.686+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:52.684+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:49.819+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:49.819+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:49.817+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:49.679+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:49.677+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:47.834+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:47.832+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:46.696+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:46.695+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:46.694+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:46.692+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:45.840+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:45.839+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:45.838+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:45.836+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:45.701+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:45.700+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:44.698+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:28:44.696+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.619+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.617+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.616+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.614+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.613+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.611+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.609+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.608+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.607+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.606+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.604+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.603+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-18T09:20:54.601+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:35.678+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:29.645+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.394+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.393+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.392+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.392+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.391+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.391+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.390+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.390+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.389+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:28.388+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:18:27.702+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.385+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.385+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.384+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.383+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.382+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.381+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.381+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.380+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.380+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.379+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.378+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.377+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:06:24.375+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.131+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.131+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.130+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.130+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.129+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.128+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.128+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.127+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.127+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.126+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.125+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.124+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:04:13.122+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:36.372+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:35.524+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:27.939+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:25.531+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:15.935+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:15.527+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:06.936+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:05.496+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:05.434+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:05.433+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:05.431+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:04.514+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:04.513+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:04.511+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:03.934+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:02.531+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:00.940+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:02:00.939+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:01:59.509+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:01:59.507+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:01:59.423+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:01:58.513+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:01:57.593+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:01:57.517+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:01:56.612+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-18T09:01:56.548+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.356+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.356+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.355+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx8-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.354+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.353+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.353+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.352+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx13-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.351+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx20-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.350+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx37-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.349+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx4-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.349+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx7-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.345+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx6-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.345+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.344+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.343+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx5-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.342+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.341+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx10-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.341+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx11-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.332+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.325+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx12-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.324+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.323+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.314+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx1-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.313+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx14-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.116+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx5-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.115+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.114+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx6-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.112+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.111+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx37-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.110+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx10-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.108+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx20-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.107+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx12-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.105+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.103+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.099+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx14-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.098+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.098+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx8-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.097+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx11-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.096+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.095+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.095+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx1-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.094+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx13-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.093+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.092+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.091+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.090+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx4-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.089+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T15:29:36.088+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx7-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-08T11:48:35.407+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-08T11:46:05.353+02:00 |                  | Fault delegate: Operational issues detected for Host esx44-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-08T10:48:33.399+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T10:46:27.885+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-08T10:46:03.362+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx44-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-08T10:43:41.936+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx44-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:35:05.985+02:00 | raised           | Fault delegate: Operational issues detected for Host esx6-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:35:05.985+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.167+02:00 | raised           | Fault delegate: Operational issues detected for Host esx12-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.166+02:00 | raised           | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.166+02:00 | raised           | Fault delegate: Operational issues detected for Host esx20-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.165+02:00 | raised           | Fault delegate: Operational issues detected for Host esx11-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.164+02:00 | raised           | Fault delegate: Operational issues detected for Host esx37-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.163+02:00 | raised           | Fault delegate: Operational issues detected for Host esx10-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.162+02:00 | raised           | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.161+02:00 | raised           | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.160+02:00 | raised           | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.159+02:00 | raised           | Fault delegate: Operational issues detected for Host esx44-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.158+02:00 | raised           | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.157+02:00 | raised           | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.150+02:00 | raised           | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.149+02:00 | raised           | Fault delegate: Operational issues detected for Host esx7-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.148+02:00 | raised           | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.147+02:00 | raised           | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.147+02:00 | raised           | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.146+02:00 | raised           | Fault delegate: Operational issues detected for Host esx5-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.146+02:00 | raised           | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.145+02:00 | raised           | Fault delegate: Operational issues detected for Host esx14-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.144+02:00 | raised           | Fault delegate: Operational issues detected for Host esx4-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.143+02:00 | raised           | Fault delegate: Operational issues detected for Host esx1-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.142+02:00 | raised           | Fault delegate: Operational issues detected for Host esx8-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:34:36.141+02:00 | raised           | Fault delegate: Operational issues detected for Host esx13-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.112+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx8-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.111+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.110+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx10-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.109+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.108+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.098+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx14-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.097+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.096+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.095+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx12-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.094+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.093+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.092+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.091+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx6-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.090+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.089+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.089+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx44-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.088+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx4-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.087+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.086+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx11-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.076+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx5-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.075+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx1-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.074+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx37-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.073+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.072+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx20-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.071+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx13-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T20:32:36.069+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx7-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T19:01:33.007+02:00 |                  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T19:01:02.972+02:00 |                  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T18:30:01.988+02:00 |                  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T18:30:01.987+02:00 |                  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T18:29:32.024+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T18:29:32.022+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T18:01:31.101+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T18:01:01.028+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:59:27.521+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:59:26.263+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:59:00.237+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:59:00.102+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T17:30:00.081+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T17:30:00.080+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T17:29:30.054+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-07T17:29:30.052+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:27:34.712+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:27:34.711+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:27:34.568+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:27:34.566+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:27:29.762+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:27:29.761+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:27:29.655+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-06-07T17:27:29.653+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T16:37:58.401+02:00 |                  | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T16:14:27.645+02:00 |                  | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T16:13:27.654+02:00 |                  | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T16:12:57.613+02:00 |                  | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T15:37:56.474+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T15:35:50.860+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T15:32:26.347+02:00 | raised           | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T15:30:14.658+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T15:14:25.768+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T15:13:25.754+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T15:13:25.752+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-07T15:12:55.667+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T15:11:56.349+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T15:11:00.411+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T15:10:59.581+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-07T15:10:48.380+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-04T19:41:17.260+02:00 |                  | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-04T19:40:47.167+02:00 |                  | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-04T18:41:15.363+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-06-04T18:40:45.225+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-04T18:39:12.238+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-06-04T18:38:31.107+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-06-01T00:08:22.454+02:00 |                  | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:35:21.306+02:00 |                  | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.973+02:00 |                  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.972+02:00 |                  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.970+02:00 |                  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.970+02:00 |                  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.969+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.968+02:00 |                  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.968+02:00 |                  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.967+02:00 |                  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.966+02:00 |                  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.959+02:00 |                  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.958+02:00 |                  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.957+02:00 |                  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:24:50.956+02:00 |                  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T23:08:20.497+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T23:06:19.982+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:55:20.106+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:53:02.969+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:50:56.749+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:50:54.867+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:35:19.406+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:33:14.732+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.125+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.123+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.122+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.121+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.119+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.118+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.116+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.115+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.111+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.109+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.108+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.106+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:24:49.105+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.584+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.583+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.582+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.582+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.581+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.579+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.578+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.572+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.571+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.570+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.545+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:24.544+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:22:23.570+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:21:48.970+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:19:40.988+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:17:34.359+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:17:33.416+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.668+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.666+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.665+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.664+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.663+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.662+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.661+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.660+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.659+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.657+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.656+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.655+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:10:48.645+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.647+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.645+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.643+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.642+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.640+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.639+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.637+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.636+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.634+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.633+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.625+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.617+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:08:34.615+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.678+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.676+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.675+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.674+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.673+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.672+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.670+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.668+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.667+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.665+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.663+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.662+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-31T22:07:48.660+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:46.451+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:44.271+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:43.194+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:42.329+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:42.216+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:41.351+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:41.214+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:41.214+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:41.213+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:40.335+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:40.334+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:40.324+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:39.567+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:39.566+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:39.558+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:39.372+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:39.363+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:39.358+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:38.475+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:38.474+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:38.306+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:38.287+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:37.416+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:37.406+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:36.418+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-31T22:05:36.294+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.753+02:00 |                  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.751+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.750+02:00 |                  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.748+02:00 |                  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.747+02:00 |                  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.746+02:00 |                  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.745+02:00 |                  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.738+02:00 |                  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.737+02:00 |                  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.737+02:00 |                  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.736+02:00 |                  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.732+02:00 |                  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T22:09:02.731+02:00 |                  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.988+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.987+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.987+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.986+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.985+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.984+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.983+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.983+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.982+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.980+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.979+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.978+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T21:09:00.976+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.967+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.966+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.965+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.963+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.962+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.961+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.961+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.952+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.945+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.944+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:40.942+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:39.979+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T21:06:39.978+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.444+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.442+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.441+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.439+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.438+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.436+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.434+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.433+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.431+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.429+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.427+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.419+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:55:00.415+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.678+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.676+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.674+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.671+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.665+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.663+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.652+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.650+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.648+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.646+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.643+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.631+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:52:50.628+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:30.295+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:30.279+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.384+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.381+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.379+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.377+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.375+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.373+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.371+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.369+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.367+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.364+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-05-30T20:52:00.347+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:50:17.490+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:50:14.740+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:50:05.484+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:50:04.786+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:56.452+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:53.652+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:53.485+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:52.698+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:52.553+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:51.808+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:51.684+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:51.658+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:51.642+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:50.723+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:50.706+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:50.696+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:49.920+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:49.917+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:49.728+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:49.726+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:46.831+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:46.729+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:45.902+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:45.796+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:45.780+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-05-30T20:49:45.761+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:31:59.861+02:00 | raised           | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:31:59.859+02:00 | raised           | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:31:59.858+02:00 | raised           | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:31:59.856+02:00 | raised           | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:31:59.854+02:00 | raised           | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:31:59.852+02:00 | raised           | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:29:35.238+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:29:35.236+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:29:35.233+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:29:35.229+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:29:35.220+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T20:29:35.213+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T19:58:28.480+02:00 | raised           | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T19:58:28.478+02:00 | raised           | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T19:58:28.475+02:00 | raised           | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T19:58:28.472+02:00 | raised           | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T19:58:28.469+02:00 | raised           | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-05-30T19:58:28.450+02:00 | raised           | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Min  | F1606   | oper-issues        | 2023-05-25T11:42:41.368+02:00 |                  | Fault delegate: Operational issues detected on portgroup:                        | 
|                |      |         |                    |                               |                  | TESTING_BRUNO|sdfgd|site2 in VM Controller:EU-SPDC-CDC-22, VM                    | 
|                |      |         |                    |                               |                  | Domain:EU-SPDC-CDC-22, VM Provider:VMware, error: Cannot find an EPG policy in   | 
|                |      |         |                    |                               |                  | the domain for the portgroup.                                                    | 
| EU-SPDC-CDC-22 | Min  | F1606   | oper-issues        | 2023-05-25T11:42:40.959+02:00 | soaking          | Fault delegate: Operational issues detected on portgroup:                        | 
|                |      |         |                    |                               |                  | TESTING_BRUNO|sdfgd|site2 in VM Controller:EU-SPDC-CDC-22, VM                    | 
|                |      |         |                    |                               |                  | Domain:EU-SPDC-CDC-22, VM Provider:VMware, error: Cannot find an EPG policy in   | 
|                |      |         |                    |                               |                  | the domain for the portgroup.                                                    | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-25T12:43:33.645+02:00 | raised           | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-25T12:41:29.240+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-04-25T12:23:33.089+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-25T12:21:15.218+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-18T10:33:33.970+02:00 | raised           | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-18T10:31:32.987+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-04-18T10:13:33.337+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-18T10:11:16.850+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-13T03:17:27.669+02:00 | raised           | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-13T03:17:27.666+02:00 | raised           | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-13T03:15:05.014+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx22-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-13T03:15:05.010+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx21-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-04-12T14:51:03.666+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-04-12T14:51:03.664+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-04-12T13:51:01.681+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-04-12T13:51:01.677+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-04-12T13:48:48.170+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-04-12T13:48:48.168+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-04-12T13:48:48.072+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-04-12T13:48:48.069+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-04T12:32:45.736+02:00 | raised           | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-04T12:30:44.910+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-04T11:33:13.770+02:00 | raised           | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-04T11:30:44.412+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-04T11:13:13.124+02:00 | raised           | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-04-04T11:10:44.250+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx36-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-31T13:39:41.057+02:00 | raised           | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-31T13:37:14.427+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F0132   | operational-issues | 2023-03-31T02:40:49.462+02:00 |                  | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.                         | 
| EU-SPDC-CDC-22 | --   | F0130   | connect-failed     | 2023-03-31T02:39:49.429+02:00 |                  | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | --   | F16438  | connect-failed     | 2023-03-31T02:37:19.409+02:00 |                  | Fault delegate: [FSM:STAGE:RETRY:]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T02:18:48.849+02:00 |                  | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T02:18:48.846+02:00 |                  | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T02:17:48.832+02:00 |                  | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T02:17:48.830+02:00 |                  | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T02:17:48.827+02:00 |                  | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F606262 | fsm-failed         | 2023-03-31T02:12:48.568+02:00 |                  | Fault delegate: [FSM:FAILED]: Add-FSM for VM Controller: EU-SPDC-CDC-22 VM       | 
|                |      |         |                    |                               |                  | Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to retrieve             | 
|                |      |         |                    |                               |                  | ServiceContent from the vCenter server 10.58.28.18(FSM:ifc:vmmmgr:CompCtrlrAdd)  | 
| EU-SPDC-CDC-22 | --   | F0132   | operational-issues | 2023-03-31T01:40:47.538+02:00 | retaining        | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.                         | 
| EU-SPDC-CDC-22 | --   | F0130   | connect-failed     | 2023-03-31T01:39:47.507+02:00 | retaining        | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:38:45.295+02:00 | raised-clearing  | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.                         | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:38:15.244+02:00 | raised           | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.                         | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-03-31T01:37:36.217+02:00 | soaking-clearing | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-03-31T01:37:16.179+02:00 | soaking          | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | --   | F16438  | connect-failed     | 2023-03-31T01:37:16.042+02:00 | retaining        | Fault delegate: [FSM:STAGE:RETRY:]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-03-31T01:37:00.236+02:00 | raised           | Fault delegate: [FSM:STAGE:RETRY:]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-03-31T01:36:42.459+02:00 | soaking          | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: [Failed to retrieve ServiceContent from the vCenter       | 
|                |      |         |                    |                               |                  | server 10.58.28.18]. Please verify network connectivity of VMM controller        | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:36:17.453+02:00 | raised           | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.,Event channel from      | 
|                |      |         |                    |                               |                  | external VMM controller is down.                                                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:34:45.210+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.,Event channel from      | 
|                |      |         |                    |                               |                  | external VMM controller is down.                                                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:34:15.164+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T01:18:46.837+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T01:18:46.834+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T01:17:46.814+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T01:17:46.812+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-31T01:17:46.809+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-31T01:16:19.711+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx35-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-31T01:16:18.744+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx34-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F0132   | operational-issues | 2023-03-31T01:16:16.797+02:00 | retaining        | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-31T01:15:34.731+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx33-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-31T01:15:33.593+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx32-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-31T01:15:30.659+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx31-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F0130   | connect-failed     | 2023-03-31T01:14:46.688+02:00 | retaining        | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:14:14.492+02:00 | raised-clearing  | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:12:44.443+02:00 | raised           | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | --   | F606262 | fsm-failed         | 2023-03-31T01:12:21.799+02:00 | retaining        | Fault delegate: [FSM:FAILED]: Add-FSM for VM Controller: EU-SPDC-CDC-22 VM       | 
|                |      |         |                    |                               |                  | Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to retrieve             | 
|                |      |         |                    |                               |                  | ServiceContent from the vCenter server 10.58.28.18(FSM:ifc:vmmmgr:CompCtrlrAdd)  | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-03-31T01:12:21.797+02:00 | raised-clearing  | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-03-31T01:12:17.637+02:00 | raised           | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: []. Please verify network connectivity of VMM controller  | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | --   | F16438  | connect-failed     | 2023-03-31T01:12:17.539+02:00 | retaining        | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-03-31T01:10:56.584+02:00 | raised           | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-03-31T01:10:41.393+02:00 | raised           | Fault delegate: [FSM:STAGE:RETRY:]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | --   | F16438  | connect-failed     | 2023-03-31T01:10:26.434+02:00 | retaining        | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-03-31T01:09:05.469+02:00 | raised           | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-03-31T01:08:50.334+02:00 | raised           | Fault delegate: [FSM:STAGE:RETRY:]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-03-31T01:08:46.493+02:00 | raised           | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: [Failed to retrieve ServiceContent from the vCenter       | 
|                |      |         |                    |                               |                  | server 10.58.28.18]. Please verify network connectivity of VMM controller        | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | --   | F16438  | connect-failed     | 2023-03-31T01:08:35.361+02:00 | retaining        | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F606262 | fsm-failed         | 2023-03-31T01:07:14.456+02:00 | raised           | Fault delegate: [FSM:FAILED]: Add-FSM for VM Controller: EU-SPDC-CDC-22 VM       | 
|                |      |         |                    |                               |                  | Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to retrieve             | 
|                |      |         |                    |                               |                  | ServiceContent from the vCenter server 10.58.28.18(FSM:ifc:vmmmgr:CompCtrlrAdd)  | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-03-31T01:07:14.453+02:00 | raised           | Fault delegate: [FSM:STAGE:FAILED]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Warn | F16438  | connect-failed     | 2023-03-31T01:06:59.239+02:00 | raised           | Fault delegate: [FSM:STAGE:RETRY:]: Connect stage for VM Controller:             | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 VM Domain: EU-SPDC-CDC-22 VM Provider: VMware Error: Failed to    | 
|                |      |         |                    |                               |                  | retrieve ServiceContent from the vCenter server                                  | 
|                |      |         |                    |                               |                  | 10.58.28.18(FSM-STAGE:ifc:vmmmgr:CompCtrlrAdd:Connect)                           | 
| EU-SPDC-CDC-22 | Maj  | F0130   | connect-failed     | 2023-03-31T01:06:41.428+02:00 | soaking          | Fault delegate: Connection to VMM controller: 10.58.28.18 with name              | 
|                |      |         |                    |                               |                  | EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 is failing     | 
|                |      |         |                    |                               |                  | repeatedly with error: [Failed to retrieve ServiceContent from the vCenter       | 
|                |      |         |                    |                               |                  | server 10.58.28.18]. Please verify network connectivity of VMM controller        | 
|                |      |         |                    |                               |                  | 10.58.28.18 and check VMM controller user credentials are valid.                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:06:16.523+02:00 | raised           | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.,Event channel from      | 
|                |      |         |                    |                               |                  | external VMM controller is down.                                                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:04:44.184+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Connection to external VMM controller is down.,Event channel from      | 
|                |      |         |                    |                               |                  | external VMM controller is down.                                                 | 
| EU-SPDC-CDC-22 | Maj  | F0132   | operational-issues | 2023-03-31T01:04:14.228+02:00 | soaking          | Fault delegate: Operational issues detected for VMM controller: 10.58.28.18      | 
|                |      |         |                    |                               |                  | with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in domain: EU-SPDC-CDC-22 due  | 
|                |      |         |                    |                               |                  | to error: Event channel from external VMM controller is down.                    | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-24T19:33:25.459+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-24T18:33:23.445+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-24T18:31:20.569+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-24T11:23:39.452+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-24T11:21:17.301+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-21T03:31:03.964+02:00 |                  | Fault delegate: Operational issues detected for Host esx51-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-21T03:30:34.080+02:00 |                  | Fault delegate: Operational issues detected for Host esx43-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-21T03:30:34.079+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-21T03:30:34.078+02:00 |                  | Fault delegate: Operational issues detected for Host esx42-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-21T02:31:02.022+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx51-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-21T02:30:32.087+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx43-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-21T02:30:32.085+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-21T02:30:32.083+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx42-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-21T02:28:37.052+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx51-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-21T02:28:36.186+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx51-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-21T02:28:30.098+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-21T02:28:29.065+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-21T02:28:21.002+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx42-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-21T02:28:20.018+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx42-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-21T02:28:07.931+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx43-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-21T02:28:06.919+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx43-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T19:30:18.478+02:00 |                  | Fault delegate: Operational issues detected for Host esx42-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T19:30:18.477+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T19:30:18.476+02:00 |                  | Fault delegate: Operational issues detected for Host esx51-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T19:29:48.451+02:00 |                  | Fault delegate: Operational issues detected for Host esx43-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T18:30:16.563+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx51-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T18:30:16.562+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T18:30:16.560+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx42-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T18:29:46.454+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx43-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T18:28:12.227+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx51-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T18:28:11.232+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx51-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T18:28:08.222+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T18:28:07.139+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T18:28:01.176+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx42-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T18:27:59.234+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx42-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T18:27:43.186+02:00 | soaking-clearing | Fault delegate: Operational issues detected for Host esx43-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T18:27:41.194+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx43-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T18:20:46.159+02:00 |                  | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-20T18:18:16.116+02:00 |                  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T18:17:16.143+02:00 |                  | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T17:20:44.227+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T17:18:26.428+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-20T17:18:14.185+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-20T17:17:14.211+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-20T17:15:58.502+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-20T17:15:58.500+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T17:15:08.296+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T17:02:13.660+02:00 | raised           | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T16:59:49.133+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx3-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T16:57:13.521+02:00 | raised           | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-20T16:54:49.031+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx2-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-07T19:20:41.857+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-07T18:20:39.865+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-07T18:18:15.044+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-07T11:30:26.583+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-07T11:28:09.404+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-06T19:19:55.246+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-06T18:19:53.248+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-06T18:17:39.362+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-06T18:11:52.983+02:00 |                  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-06T18:11:23.066+02:00 |                  | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-06T17:11:51.068+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-06T17:11:21.093+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-06T17:09:49.947+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-06T17:09:49.938+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-06T17:09:09.789+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-06T11:56:10.980+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-06T11:54:02.135+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-06T11:19:39.797+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-06T11:04:09.283+02:00 | raised           | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-06T11:02:01.689+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx9-eu-spdc.cisco.com in   | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-06T10:19:37.769+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-06T10:17:19.314+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T19:29:52.446+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T19:27:49.481+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-04T19:18:22.073+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-04T18:18:20.094+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T18:15:59.933+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T11:49:07.703+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T11:46:46.655+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-04T11:35:07.212+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-04T10:35:05.286+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T10:32:44.085+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T10:26:04.938+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T10:23:45.879+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-04T03:34:51.699+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-04T02:34:49.706+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-04T02:32:35.358+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T18:55:41.203+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T18:53:37.131+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T18:48:04.658+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T18:45:41.065+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-03T18:45:04.609+02:00 |                  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F2840   | remote-oper-issues | 2023-03-03T17:45:02.611+02:00 | retaining        | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T17:42:50.311+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T17:35:41.287+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T17:34:04.167+02:00 | raised-clearing  | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T17:28:02.075+02:00 | raised           | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | Maj  | F2840   | remote-oper-issues | 2023-03-03T17:25:41.243+02:00 | soaking          | Fault delegate: Operational issues detected for Host esx41-eu-spdc.cisco.com in  | 
|                |      |         |                    |                               |                  | VMM controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain: EU-SPDC-CDC-22 due to error: ESX Host is disconnected or not          | 
|                |      |         |                    |                               |                  | responding.                                                                      | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-03T11:41:51.002+02:00 |                  | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-03T10:41:49.045+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T10:39:23.035+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T10:30:48.642+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T10:28:28.636+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-03T10:27:48.545+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T10:25:29.254+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T10:25:28.389+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:12, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-03T02:18:02.788+02:00 |                  | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-03T01:18:00.819+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T01:15:34.409+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T01:06:00.443+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T01:03:36.971+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-03T01:03:30.405+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T01:01:27.899+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-03T01:01:27.810+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx4-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:1B:13, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.486+02:00 |                  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.484+02:00 |                  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.483+02:00 |                  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.481+02:00 |                  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.479+02:00 |                  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.478+02:00 |                  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.477+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.475+02:00 |                  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.474+02:00 |                  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.473+02:00 |                  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.471+02:00 |                  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.469+02:00 |                  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T22:28:55.467+02:00 |                  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.243+02:00 |                  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.241+02:00 |                  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.240+02:00 |                  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.239+02:00 |                  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.237+02:00 |                  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.236+02:00 |                  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.234+02:00 |                  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.232+02:00 |                  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.230+02:00 |                  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.228+02:00 |                  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.227+02:00 |                  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.225+02:00 |                  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:49:54.223+02:00 |                  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.551+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.550+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.548+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.547+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.545+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.543+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.541+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.539+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.537+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.534+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.532+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.529+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T21:28:53.527+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.032+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.031+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.029+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.022+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.021+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.020+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.014+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.013+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.012+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.009+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:36.007+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:35.142+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:26:35.140+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.042+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.041+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.039+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.038+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.036+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.035+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.033+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.026+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.025+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.017+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:53.016+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:52.999+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:13:52.995+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.481+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.480+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.478+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.469+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.468+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.466+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.465+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.463+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.462+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.457+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.455+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.454+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:11:47.445+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:50.307+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:48.922+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:41.309+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:41.294+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:38.929+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C8, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:38.927+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:11, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:36.877+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:36.875+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:50, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:36.727+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:36.726+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:36.724+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:36.711+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:35.993+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:08, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:35.983+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:68, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:35.981+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:01, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:35.978+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:78, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:35.356+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:35.349+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:35.347+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:34.918+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:40, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:34.916+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:40, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:34.899+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:61, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:32.287+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:31.870+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F0, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:31.706+02:00 | soaking-clearing | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T21:09:29.858+02:00 | soaking          | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:98, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.310+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.309+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.308+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.306+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.305+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.303+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.302+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.300+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.298+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.297+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.295+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.289+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | --   | F1313   | operational-issues | 2023-03-02T20:49:52.286+02:00 | retaining        | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.585+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx6-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:3E:60, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.584+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx1-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:B0:00, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.581+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx8-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:10, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.579+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.578+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx13-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:F0:13:09, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.576+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx12-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 40:A6:B7:15:53:C9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.568+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.560+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx14-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:A5:69, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.545+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.543+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:44.532+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx7-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:EF:63:79, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:43.577+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx2-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:11:41, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:47:43.575+02:00 | raised-clearing  | Fault delegate: Operational issues detected on Host: esx10-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:41, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:35:21.841+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx11-eu-spdc.cisco.com     | 
|                |      |         |                    |                               |                  | for controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc    | 
|                |      |         |                    |                               |                  | in domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:EC:E9, error: [NIC operational       | 
|                |      |         |                    |                               |                  | state is down.]                                                                  | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:35:21.839+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx3-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CE:19:F1, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:35:21.838+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx9-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:F5:51, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
| EU-SPDC-CDC-22 | Maj  | F1313   | operational-issues | 2023-03-02T20:35:21.837+02:00 | raised           | Fault delegate: Operational issues detected on Host: esx5-eu-spdc.cisco.com for  | 
|                |      |         |                    |                               |                  | controller: 10.58.28.18 with name EU-SPDC-CDC-22 in datacenter eu-spdc-dc in     | 
|                |      |         |                    |                               |                  | domain EU-SPDC-CDC-22 HpNic: 3C:FD:FE:CB:FA:99, error: [NIC operational state    | 
|                |      |         |                    |                               |                  | is down.]                                                                        | 
+----------------+------+---------+--------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+

VMM Domain - Event Logs last 10y [#1]
-------------------------------------

+----------------+------+----------+-------------------------+-------------------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Domain         | Sev  | Code     | Cause                   | Created Time                  | Description                                                                  | Change Set                                                                    |
+----------------+------+----------+-------------------------+-------------------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4205018 | user-association-formed | 2021-01-05T20:41:53.340+02:00 | Association from VMM Controller:                                             | forceResolve:yes, rType:mo, state:formed, stateQual:none, tCl:vmmUsrAccP,     | 
|                |      |          |                         |                               | uni/vmmp-VMware/dom-EU-SPDC-CDC-22/ctrlr-EU-SPDC-CDC-22 to User Account:     | tDn:uni/vmmp-VMware/dom-EU-SPDC-CDC-22/usracc-EU-SPDC-CDC-22_Cred, tType:mo,  | 
|                |      |          |                         |                               | uni/vmmp-VMware/dom-EU-SPDC-CDC-22/usracc-EU-SPDC-CDC-22_Cred is Established | userdom::all:common:                                                          | 
+----------------+------+----------+-------------------------+-------------------------------+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

VMM Domain - Audit Logs last 10y [#53]
--------------------------------------

+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| Domain         | Sev  | Code     | Cause      | Created Time                  | Description                          | Change Set                                                                      |
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4211024 | transition | 2022-07-26T20:57:46.748+02:00 | DomainRef UCSB1_SecDom created       | name:UCSB1_SecDom, userdom::all:common:                                         | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213401 | transition | 2022-07-26T19:32:26.081+02:00 | RsVswitchOverrideLacpPol modified    | tDn (Old: uni/infra/lacplagp-vEPC-dataplane_vPCPol, New:                        | 
|                |      |          |            |                               |                                      | uni/infra/lacplagp-default)                                                     | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213403 | transition | 2021-06-15T14:04:23.623+02:00 | RsVswitchOverrideLldpIfPol created   | tDn:uni/infra/lldpIfP-LLDP-enable, userdom::all:common:                         | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4217633 | transition | 2021-06-15T14:04:23.623+02:00 | RsVswitchOverrideMtuPol created      | tDn:uni/fabric/l2pol-default, userdom::all:common:                              | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213400 | transition | 2021-06-15T14:04:23.622+02:00 | RsVswitchOverrideLacpPol created     | tDn:uni/infra/lacplagp-vEPC-dataplane_vPCPol, userdom::all:common:              | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213394 | transition | 2021-06-15T14:04:23.622+02:00 | RsVswitchOverrideCdpIfPol created    | tDn:uni/infra/cdpIfP-CDP-enable, userdom::all:common:                           | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213423 | transition | 2021-06-15T00:40:46.407+02:00 | UsrAggr vEPG-SX_L3out_PG deleted     |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214209 | transition | 2021-06-15T00:40:46.407+02:00 | EncapBlk vlan-2503 vlan-2503 deleted |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214209 | transition | 2021-06-15T00:40:38.985+02:00 | EncapBlk vlan-2502 vlan-2502 deleted |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213423 | transition | 2021-06-15T00:40:38.985+02:00 | UsrAggr vEPG-INT_L3out_PG deleted    |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213423 | transition | 2021-06-15T00:40:28.269+02:00 | UsrAggr vEPG-ACC_L3out_PG deleted    |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214209 | transition | 2021-06-15T00:40:28.269+02:00 | EncapBlk vlan-2501 vlan-2501 deleted |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213320 | transition | 2021-06-15T00:12:36.218+02:00 | CtrlrP EU-SPDC-CDC-22 modified       | seqNum (Old: 0, New: 1)                                                         | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213422 | transition | 2021-06-10T11:40:29.097+02:00 | UsrAggr vEPG-INT_L3out_PG modified   | promMode (Old: Disabled, New: Enabled)                                          | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213422 | transition | 2021-06-07T22:43:12.140+02:00 | UsrAggr vEPG-SX_L3out_PG modified    | forgedTransmit (Old: Disabled, New: Enabled), macChange (Old: Disabled, New:    | 
|                |      |          |            |                               |                                      | Enabled)                                                                        | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213421 | transition | 2021-06-07T22:42:29.796+02:00 | UsrAggr vEPG-SX_L3out_PG created     | aggrImedcy:immediate, allocMode:dynamic, classPref:encap,                       | 
|                |      |          |            |                               |                                      | forgedTransmit:Disabled, macChange:Disabled, name:vEPG-SX_L3out_PG,             | 
|                |      |          |            |                               |                                      | promMode:Enabled, untagged:no, userdom::all:common:                             | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214207 | transition | 2021-06-07T22:42:29.796+02:00 | EncapBlk vlan-2503 vlan-2503 created | allocMode:inherit, from:vlan-2503, role:external, to:vlan-2503,                 | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213423 | transition | 2021-06-07T22:39:24.617+02:00 | UsrAggr vEPG-SX_L3out_PG deleted     |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214209 | transition | 2021-06-07T22:39:24.617+02:00 | EncapBlk vlan-2503 vlan-2503 deleted |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213422 | transition | 2021-06-07T22:13:25.396+02:00 | UsrAggr vEPG-SX_L3out_PG modified    | forgedTransmit (Old: Disabled, New: Enabled), macChange (Old: Disabled, New:    | 
|                |      |          |            |                               |                                      | Enabled), promMode (Old: Disabled, New: Enabled)                                | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213422 | transition | 2021-06-07T19:12:27.458+02:00 | UsrAggr vEPG-SX_L3out_PG modified    | forgedTransmit (Old: Enabled, New: Disabled), macChange (Old: Enabled, New:     | 
|                |      |          |            |                               |                                      | Disabled), promMode (Old: Enabled, New: Disabled)                               | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213422 | transition | 2021-06-07T17:05:12.667+02:00 | UsrAggr vEPG-SX_L3out_PG modified    | forgedTransmit (Old: Disabled, New: Enabled), macChange (Old: Disabled, New:    | 
|                |      |          |            |                               |                                      | Enabled)                                                                        | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214207 | transition | 2021-06-07T16:57:02.784+02:00 | EncapBlk vlan-2503 vlan-2503 created | allocMode:inherit, from:vlan-2503, role:external, to:vlan-2503,                 | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213421 | transition | 2021-06-07T16:57:02.783+02:00 | UsrAggr vEPG-SX_L3out_PG created     | aggrImedcy:immediate, allocMode:dynamic, classPref:encap,                       | 
|                |      |          |            |                               |                                      | forgedTransmit:Disabled, macChange:Disabled, name:vEPG-SX_L3out_PG,             | 
|                |      |          |            |                               |                                      | promMode:Enabled, untagged:no, userdom::all:common:                             | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214207 | transition | 2021-05-26T10:50:58.242+02:00 | EncapBlk vlan-2501 vlan-2501 created | allocMode:inherit, from:vlan-2501, role:external, to:vlan-2501,                 | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214209 | transition | 2021-05-26T10:50:39.580+02:00 | EncapBlk vlan-2503 vlan-2503 deleted |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214207 | transition | 2021-05-26T10:16:28.749+02:00 | EncapBlk vlan-2503 vlan-2503 created | allocMode:inherit, from:vlan-2503, role:external, to:vlan-2503,                 | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214209 | transition | 2021-05-26T10:16:10.913+02:00 | EncapBlk vlan-2501 vlan-2501 deleted |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213422 | transition | 2021-05-25T19:11:18.828+02:00 | UsrAggr vEPG-ACC_L3out_PG modified   | promMode (Old: Disabled, New: Enabled)                                          | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214207 | transition | 2021-05-25T02:29:51.896+02:00 | EncapBlk vlan-2502 vlan-2502 created | allocMode:inherit, from:vlan-2502, role:external, to:vlan-2502,                 | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213421 | transition | 2021-05-25T02:29:51.895+02:00 | UsrAggr vEPG-INT_L3out_PG created    | aggrImedcy:immediate, allocMode:dynamic, classPref:encap,                       | 
|                |      |          |            |                               |                                      | forgedTransmit:Enabled, macChange:Enabled, name:vEPG-INT_L3out_PG,              | 
|                |      |          |            |                               |                                      | promMode:Disabled, untagged:no, userdom::all:common:                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213421 | transition | 2021-05-25T02:29:15.410+02:00 | UsrAggr vEPG-ACC_L3out_PG created    | aggrImedcy:immediate, allocMode:dynamic, classPref:encap,                       | 
|                |      |          |            |                               |                                      | forgedTransmit:Enabled, macChange:Enabled, name:vEPG-ACC_L3out_PG,              | 
|                |      |          |            |                               |                                      | promMode:Disabled, untagged:no, userdom::all:common:                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214207 | transition | 2021-05-25T02:29:15.410+02:00 | EncapBlk vlan-2501 vlan-2501 created | allocMode:inherit, from:vlan-2501, role:external, to:vlan-2501,                 | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213423 | transition | 2021-05-25T02:28:32.357+02:00 | UsrAggr INT_L3out_PG deleted         |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214209 | transition | 2021-05-25T02:28:32.357+02:00 | EncapBlk vlan-2502 vlan-2502 deleted |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213423 | transition | 2021-05-25T02:28:27.309+02:00 | UsrAggr ACC_L3out_PG deleted         |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214209 | transition | 2021-05-25T02:28:27.309+02:00 | EncapBlk vlan-2501 vlan-2501 deleted |                                                                                 | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214207 | transition | 2021-05-25T02:27:29.079+02:00 | EncapBlk vlan-2502 vlan-2502 created | allocMode:inherit, from:vlan-2502, role:external, to:vlan-2502,                 | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213421 | transition | 2021-05-25T02:27:29.078+02:00 | UsrAggr INT_L3out_PG created         | aggrImedcy:immediate, allocMode:dynamic, classPref:encap,                       | 
|                |      |          |            |                               |                                      | forgedTransmit:Enabled, macChange:Enabled, name:INT_L3out_PG,                   | 
|                |      |          |            |                               |                                      | promMode:Disabled, untagged:no, userdom::all:common:                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214207 | transition | 2021-05-25T02:26:50.947+02:00 | EncapBlk vlan-2501 vlan-2501 created | allocMode:inherit, from:vlan-2501, role:external, to:vlan-2501,                 | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213421 | transition | 2021-05-25T02:26:50.946+02:00 | UsrAggr ACC_L3out_PG created         | aggrImedcy:immediate, allocMode:dynamic, classPref:encap,                       | 
|                |      |          |            |                               |                                      | forgedTransmit:Enabled, macChange:Enabled, name:ACC_L3out_PG,                   | 
|                |      |          |            |                               |                                      | promMode:Disabled, untagged:no, userdom::all:common:                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213355 | transition | 2021-01-05T20:41:53.041+02:00 | RsAcc created                        | tDn:uni/vmmp-VMware/dom-EU-SPDC-CDC-22/usracc-EU-SPDC-CDC-22_Cred,              | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213319 | transition | 2021-01-05T20:41:53.041+02:00 | CtrlrP EU-SPDC-CDC-22 created        | dvsVersion:unmanaged, hostOrIp:10.58.28.18, inventoryTrigSt:untriggered,        | 
|                |      |          |            |                               |                                      | mode:default, n1kvStatsMode:enabled, name:EU-SPDC-CDC-22, port:0,               | 
|                |      |          |            |                               |                                      | rootContName:eu-spdc-dc, scope:vm, seqNum:0, statsMode:disabled,                | 
|                |      |          |            |                               |                                      | userdom::all:common:, vxlanDeplPref:vxlan                                       | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213424 | transition | 2021-01-05T20:41:53.041+02:00 | VSwitchPolicyCont created            | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4214354 | transition | 2021-01-05T20:41:53.041+02:00 | RsVlanNs created                     | tDn:uni/infra/vlanns-[ESX-CDC-22_VlanPool]-dynamic, userdom::all:common:        | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213418 | transition | 2021-01-05T20:41:53.041+02:00 | UsrAccP EU-SPDC-CDC-22_Cred created  | name:EU-SPDC-CDC-22_Cred, pwd:****, userdom::all:common:, usr:admin@admin.local | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213367 | transition | 2021-01-05T20:41:53.040+02:00 | RsDefaultL2InstPol created           | userdom:all                                                                     | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213370 | transition | 2021-01-05T20:41:53.040+02:00 | RsDefaultLacpLagPol created          | userdom:all                                                                     | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213373 | transition | 2021-01-05T20:41:53.040+02:00 | RsDefaultLldpIfPol created           | userdom:all                                                                     | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213364 | transition | 2021-01-05T20:41:53.040+02:00 | RsDefaultFwPol created               | userdom:all                                                                     | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213376 | transition | 2021-01-05T20:41:53.040+02:00 | RsDefaultStpIfPol created            | userdom:all                                                                     | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213361 | transition | 2021-01-05T20:41:53.040+02:00 | RsDefaultCdpIfPol created            | userdom:all                                                                     | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
| EU-SPDC-CDC-22 | Info | E4213322 | transition | 2021-01-05T20:41:53.039+02:00 | DomP EU-SPDC-CDC-22 created          | accessMode:read-write, aveTimeOut:30, configInfraPg:no, ctrlKnob:epDpVerify,    | 
|                |      |          |            |                               |                                      | enableAVE:no, enableTag:no, enableVmFolder:no, encapMode:unknown, enfPref:hw,   | 
|                |      |          |            |                               |                                      | epInventoryType:on-link, epRetTime:0, hvAvailMonitor:no, mcastAddr:0.0.0.0,     | 
|                |      |          |            |                               |                                      | mode:default, name:EU-SPDC-CDC-22, prefEncapMode:unspecified,                   | 
|                |      |          |            |                               |                                      | userdom::all:common:                                                            | 
+----------------+------+----------+------------+-------------------------------+--------------------------------------+---------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci domain vmm --apic apic21 --name *cdc* --when any --view all

{
    "duration": 40782,
    "apic": {
        "read": true,
        "success": 51,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 50,
        "connect_time": 498,
        "disconnect_time": 0,
        "mo_time": 26424,
        "total_time": 26922
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

True	498	-	connect apic21o.emea-sp.cisco.com:443
True	392	4	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRtDomP,vmmUplinkPCont,infraRsVlanNs,vmmUsrAccP,vmmCtrlrP,vmmVSwitchPolicyCont,aaaDomainRef,vmmEpPD
True	812	4	apic21o.emea-sp.cisco.com:443 class compCtrlr query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=compHv,compVm
True	378	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	678	1	apic21o.emea-sp.cisco.com:443 mo uni/vmmp-VMware/dom-EU-SPDC-CDC-22 query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	397	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	2201	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	465	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	392	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	542	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	365	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	402	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	398	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	383	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	435	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	361	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	364	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	343	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	393	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	368	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	413	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2177	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	468	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	378	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	340	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	387	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	413	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	437	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	423	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	385	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	416	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	330	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	409	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	426	16	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree-include=faults,no-scoped,subtree
True	2648	3000	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	542	8	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	565	235	apic21o.emea-sp.cisco.com:443 class vmmDomP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./DomainVmm.md)