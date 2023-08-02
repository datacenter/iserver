# Physical Domain

## VLAN view

```
# iserver get aci domain phy --apic apic21 --view vlan

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call
[INFO] Requires per-interface api call

Physical Domain - Interfaces VLAN [#12]
---------------------------------------

+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| Faults  | Domain                | AAEP               | VLAN Pool              | Encapsulation Block   | Node           | Interface | State | Mode  | VLANs                                   |
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | ESX-CDC-22_PhysDom    | ESX-CDC-22_AAEP    | ESX-CDC-22_VlanPool    | [2501-2502] (static)  | cl2201-eu-spdc | eth1/31   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                    |                        | [2503-2509] (static)  | cl2201-eu-spdc | eth1/32   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                    |                        | [2700-2999] (dynamic) | cl2201-eu-spdc | eth1/33   | down  | trunk | 2701-2704,2708,2902                     | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/34   | up    | trunk | 2701-2704,2708,2800-2801,2804,2900-2902 | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/35   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/36   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/37   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/38   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/39   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/40   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/41   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/42   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/43   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/44   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/45   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/46   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/47   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/31   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/32   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/33   | down  | trunk | 2701-2704,2708,2902                     | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/34   | up    | trunk | 2701-2704,2708,2800-2801,2804,2900-2902 | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/35   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/36   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/37   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/38   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/39   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/40   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/41   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/42   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/43   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/44   | up    | trunk | 2701-2704,2708,2902                     | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/45   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/46   | up    | trunk | 2701-2704,2708,2804,2902                | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/47   | up    | trunk | 2701-2704,2708,2804,2902                | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | ESX-R7DC_PhysDom      | ESX-R7DC_AAEP      | ESX-R7DC_VlanPool      | [3701-3800] (dynamic) | rl2701-eu-spdc | eth1/1    | down  | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/10   | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/11   | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/12   | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/13   | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/2    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/3    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/4    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/5    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/6    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/7    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/8    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/9    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/1    | down  | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/10   | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/11   | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/12   | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/13   | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/2    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/3    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/4    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/5    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/6    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/7    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/8    | up    | trunk | 3735-3736                               | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/9    | up    | trunk | 3735-3736                               | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | HX1_PhysDom           | HX1_AAEP           | HX1_VlanPool           | [70-79] (static)      | bl2205-eu-spdc | eth1/11   | up    | trunk |                                         | 
|         |                       |                    |                        | [1000-4048] (static)  | bl2205-eu-spdc | eth1/12   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | bl2206-eu-spdc | eth1/11   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | bl2206-eu-spdc | eth1/12   | up    | trunk |                                         | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | Infra_PhysDom         | vEPC-ESX21-22_AAEP | Infra_VlanPool         | [1-1000] (static)     | bl2205-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                       | Infra_AAEP         |                        |                       | bl2205-eu-spdc | eth1/25   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | bl2206-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                       |                    |                        |                       | bl2206-eu-spdc | eth1/25   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/25   | down  | trunk |                                         | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/96   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/25   | down  | trunk |                                         | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/96   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/19   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/19   | up    | trunk |                                         | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | k8s_esx_PhysDom       | k8s_esx_AAEP       | k8s_esx_VlanPool       | [800-809] (static)    | cl2207-eu-spdc | eth1/1/1  | up    | trunk | 1300-1306,1367-1369,1435,1437           | 
|         |                       |                    |                        | [1300-1499] (dynamic) | cl2207-eu-spdc | eth1/1/2  | up    | trunk | 1300-1306,1367-1369,1435,1437           | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/1/1  | up    | trunk | 1300-1306,1367-1369,1435,1437           | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/1/2  | up    | trunk | 1300-1306,1367-1369,1435,1437           | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | k8s_phys_PhysDom      | k8s_phys_AAEP      | k8s_phys_VlanPool      | [800-809] (static)    | cl2207-eu-spdc | eth1/1/3  | up    | trunk | 801,809                                 | 
|         |                       |                    |                        | [810-813] (static)    | cl2207-eu-spdc | eth1/1/4  | up    | trunk | 802,809                                 | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/2/1  | down  | trunk | 809                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/2/2  | up    | trunk | 809                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/2/3  | up    | trunk | 809                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/3/1  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/3/2  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/3/3  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/3/4  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/4/1  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/4/2  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/4/3  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/5/1  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/5/2  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/5/3  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/5/4  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/6/1  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/6/2  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/6/3  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/1/3  | up    | trunk | 801,809                                 | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/1/4  | up    | trunk | 802,809                                 | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/2/1  | down  | trunk | 809                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/2/2  | up    | trunk | 809                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/2/3  | up    | trunk | 809                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/3/1  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/3/2  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/3/3  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/3/4  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/4/1  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/4/2  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/4/3  | up    | trunk | 808                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/5/1  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/5/2  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/5/3  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/5/4  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/6/1  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/6/2  | up    | trunk | 807                                     | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/6/3  | down  | trunk | 807                                     | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | nidemo                | nidemo             | nidemo-3000-3001       | [3000-3001] (static)  | rl2701-eu-spdc | eth1/19   | down  | trunk |                                         | 
|         |                       |                    |                        |                       | rl2701-eu-spdc | eth1/20   | down  | trunk |                                         | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/19   | down  | trunk | 3000                                    | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/20   | down  | trunk |                                         | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | SPN_PhysDom           | SPN_AAEP           | SPN_VlanPool           | [2600-2699] (static)  | bl2205-eu-spdc | eth1/27   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | bl2206-eu-spdc | eth1/27   | up    | trunk |                                         | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | UCSB1-R7DC_PhysDom    | UCSB1-R7DC_AAEP    | UCSB1-R7DC_VlanPool    | [2-100] (static)      | rl2701-eu-spdc | eth1/49   | up    | trunk |                                         | 
|         |                       |                    |                        | [1701-1899] (dynamic) | rl2701-eu-spdc | eth1/50   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/49   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | rl2702-eu-spdc | eth1/50   | up    | trunk |                                         | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | UCSB1_PhysDom         | UCSB1_AAEP         | UCSB1_VlanPool         | [2-100] (static)      | bl2205-eu-spdc | eth1/1    | up    | trunk |                                         | 
|         |                       |                    |                        | [3701-4000] (dynamic) | bl2205-eu-spdc | eth1/2    | up    | trunk |                                         | 
|         |                       |                    |                        |                       | bl2206-eu-spdc | eth1/1    | up    | trunk |                                         | 
|         |                       |                    |                        |                       | bl2206-eu-spdc | eth1/2    | up    | trunk |                                         | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | vEPC-ESX20_PhysDom    | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  | bl2205-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                       |                    |                        | [2700-2999] (dynamic) | bl2206-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/19   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/19   | up    | trunk |                                         | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
| 0 0 0 0 | vEPC-ESX21-22_PhysDom | vEPC-ESX21-22_AAEP | vEPC-ESX21-22_VlanPool | [2501-2509] (static)  | bl2205-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                       |                    |                        | [2700-2999] (dynamic) | bl2206-eu-spdc | eth1/19   | up    | trunk | 2700-2701,2800,2900                     | 
|         |                       |                    |                        |                       | cl2201-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2202-eu-spdc | eth1/90   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2207-eu-spdc | eth1/19   | up    | trunk |                                         | 
|         |                       |                    |                        |                       | cl2208-eu-spdc | eth1/19   | up    | trunk |                                         | 
+---------+-----------------------+--------------------+------------------------+-----------------------+----------------+-----------+-------+-------+-----------------------------------------+
```

Developer

```
# iserver get aci domain phy --apic apic21 --view vlan

{
    "duration": 89391,
    "apic": {
        "read": true,
        "success": 173,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 172,
        "connect_time": 476,
        "disconnect_time": 0,
        "mo_time": 82084,
        "total_time": 82560
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

True	476	-	connect apic21o.emea-sp.cisco.com:443
True	407	12	apic21o.emea-sp.cisco.com:443 class physDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,infraRtDomAtt,aaaDomainRef
True	464	13	apic21o.emea-sp.cisco.com:443 class fvnsVlanInstP query rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs
True	771	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-k8s_esx_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	423	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1368	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	460	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ethpmPhysIf
True	406	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	476	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	345	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	378	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1336	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	382	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ethpmPhysIf
True	419	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	405	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	766	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-k8s_phys_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	347	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	323	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/2/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	372	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	357	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	434	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/3/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	437	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	745	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/4/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	383	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	445	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/5/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	402	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	331	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/6/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	463	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	378	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/2/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	428	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	322	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	378	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/3/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	399	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	378	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/4/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	364	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	401	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	364	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	420	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/5/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	417	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/6/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	647	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-UCSB1-R7DC_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	1785	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	380	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ethpmPhysIf
True	358	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/49] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	466	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/50] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1844	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	430	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ethpmPhysIf
True	374	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/49] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/50] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	738	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-vEPC-ESX20_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	1050	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	393	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	345	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	1019	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	359	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	411	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	394	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	2062	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	581	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	440	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/90] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	2100	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	388	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	410	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/90] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	403	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2207/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2208/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	795	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-vEPC-ESX21-22_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	928	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-Infra_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	373	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	381	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	405	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/96] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	702	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-nidemo query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	414	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	358	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	331	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vlanCktEp
True	487	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	668	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-SPN_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	431	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	346	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	672	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-UCSB1_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	401	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	389	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	343	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	390	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	677	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-HX1_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	354	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	419	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	414	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2206/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	670	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-ESX-CDC-22_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	358	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	404	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	374	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	436	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	421	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	345	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	364	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	411	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	380	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	473	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2201/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	411	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	358	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	366	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	390	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	416	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	384	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	414	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/37] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	479	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/38] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	383	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/39] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	489	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/40] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	472	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/41] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	403	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/42] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	473	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/43] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	406	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/44] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	412	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/45] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	425	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/46] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2202/sys/phys-[eth1/47] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	794	1	apic21o.emea-sp.cisco.com:443 mo uni/phys-ESX-R7DC_PhysDom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	381	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	362	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vlanCktEp
True	435	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	377	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	366	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	431	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	330	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	322	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	355	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	461	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	478	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	1416	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2701/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	377	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	404	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	401	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	360	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	415	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	342	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	402	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	447	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	400	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	413	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	406	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	388	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2702/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./DomainPhy.md)