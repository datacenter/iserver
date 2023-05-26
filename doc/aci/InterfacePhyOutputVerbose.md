# Node Interface - Physical

## Verbose output

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --id 1/1 -o verbose

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

Fabric Port Details
-------------------
- Node                          : pod-1/bl205-eu-spdc
- Port                          : eth1/1
- Admin State                   : up
- Usage                         : epg
- Oper Speed                    : 40G
- Oper State                    : up
- Oper State Reason             : connected
- Backplane Mac                 : 4C:71:0D:7E:83:F1
- Last Link State Change        : 2023-03-03T02:30:07.845+02:00
- Oper Router Mac               : 00:00:00:00:00:00
- Oper Mdix                     : auto
- Oper Mode                     : trunk
- Access VLAN                   : unknown
- Native VLAN                   : unknown
- Reset Counter                 : 2
- Operational VLANs             : 5-8,11-12,14-15,17-19,22-31,35,37-38,43-44,46-51,53-59,61,63,69-70,72-81
- Allowed VLANs                 : 5-8,11-12,14-15,17-19,22-31,35,37-38,43-44,46-51,53-59,61,63,69-70,72-81
- Port Channel                  : po5
- Bandwidth (kb)                : 0
- Delay (usec)                  : 1
- Mdix                          : auto
- Medium                        : broadcast
- MTU                           : 9000
- Router Mac                    : not-applicable
- Speed                         : inherit
- Forward Error Correction      : inherit
- Auto Negotiation              : on
- Link Debounce Interval (msec) : 100
- Dot1Q Ether Type              : 0x8100
- Layer                         : switched
- Mode                          : trunk
- Switching State               : enabled
- Destination SPAN Mode         : not-a-span-dest
- Eee Lat                       : variable
- Eee Lpi                       : aggressive
- Eee State                     : not-applicable
- Transceiver Present           : yes
- Transceiver Type              : QSFP-40G-SR-BD
- Transceiver Actual Type       : qsfp
- Transceiver Name              : CISCO-AVAGO
- Transceiver Part Number       : AFBR-79EBPZ-CS1
- Transceiver Revision          : 01Bh
- Transceiver Serial Number     : AVM1814S1HN


CDP
---
- System Name    : FI-ucsb1-eu-spdc-A
- System Version : Cisco Nexus Operating System (NX-OS) Software, Version 9.3(5)I42(2c)
- Platform       : UCS-FI-6454
- Port ID        : Ethernet1/51
- Capability     : igmp-filter,router,stp-dispute,switch
- State          : nativevlan-mismatch


LLDP
----
- System Name        : FI-ucsb1-eu-spdc-A.cisco.com
- System Description :
	Cisco Nexus Operating System (NX-OS) Software 9.3(5)I42(2c)
	TAC support: http://www.cisco.com/tac
	Copyright (c) 2002-2022, Cisco Systems, Inc. All rights reserved.
- Port Description   : U: Uplink
- Port Id Type       : if-name
- Port Id Value      : Ethernet1/51
- Capability         : bridge,router


+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| Up | EPG Name           | App Profile           | Tenant            | Preferred Member | Flood    | Class ID | QoS Class   | Isolation  | Label Match |
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | CNC_bus            | CNC_ANP               | CNC_demo          | exclude          | disabled | 32779    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | Data               | DT-EPNM               | DT-EPNM           | exclude          | disabled | 16414    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | Device             | DT-EPNM               | DT-EPNM           | exclude          | disabled | 16415    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | EPG1               | TEST                  | NXOS-HandOff_Test | exclude          | disabled | 16388    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | EU-SPDC-ERSPAN     | EU-SPDC_ANP           | mgmt              | exclude          | disabled | 16386    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | F5_IN              | F5_ANP                | MPC-F5T           | exclude          | disabled | 32770    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | F5_OUT             | F5_ANP                | MPC-F5T           | exclude          | disabled | 16387    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | MGMT               | DT-EPNM               | DT-EPNM           | exclude          | disabled | 16413    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | MPC-CDC-2          | AP-ECMP-demo_ANP      | ECMP-demo         | exclude          | disabled | 32771    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | P5G-F1C-NGC-N2     | P5G_App               | P5G               | exclude          | disabled | 17       | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | P5G-mgmt           | P5G_App               | P5G               | exclude          | disabled | 32785    | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | PrivateIP-MGMT     | Infra_ANP             | common            | exclude          | disabled | 18       | unspecified | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SITE1              | UntitledAP1           | TESTING_BRUNO     | exclude          | disabled | 16386    | unspecified | unenforced | None        | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN-Backend01     | SPIN_InnoLab          | SPIN_InnoLab      | exclude          | disabled | 32771    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN-CSR-A         | SPIN_InnoLab          | SPIN_InnoLab      | exclude          | disabled | 32773    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN-CSR-P         | SPIN_InnoLab          | SPIN_InnoLab      | exclude          | disabled | 49154    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN-CSR-P-2       | SPIN_InnoLab          | SPIN_InnoLab      | exclude          | disabled | 32775    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN-MGMT          | SPIN_InnoLab          | SPIN_InnoLab      | exclude          | disabled | 49154    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | TEST1              | SPN_Connect_ANP       | SPN_IntraLab      | exclude          | disabled | 32772    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | Vitria-Mon-BackEnd | Vitria-Monitoring_ANP | iks-monitoring    | exclude          | disabled | 32770    | level3      | unenforced | AtleastOne  | 
+----+--------------------+-----------------------+-------------------+------------------+----------+----------+-------------+------------+-------------+

+---------------------------------------------------------+---------------+------------+--------------+-----------------+
| EPG                                                     | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------------------------------------------+---------------+------------+--------------+-----------------+
| CNC_demo/CNC_ANP/CNC_bus                                | 27            | vlan-2001  | vxlan-11892  | up              | 
| DT-EPNM/DT-EPNM/Data                                    | 78            | vlan-2170  | vxlan-12061  | up              | 
| DT-EPNM/DT-EPNM/Device                                  | 79            | vlan-2003  | vxlan-11894  | up              | 
| NXOS-HandOff_Test/TEST/EPG1                             | 8             | vlan-2343  | vxlan-12234  | up              | 
| mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         | 15            | vlan-2338  | vxlan-12229  | up              | 
| MPC-F5T/F5_ANP/F5_IN                                    | 38            | vlan-2008  | vxlan-11899  | up              | 
| MPC-F5T/F5_ANP/F5_OUT                                   | 18            | vlan-2009  | vxlan-11900  | up              | 
| DT-EPNM/DT-EPNM/MGMT                                    | 80            | vlan-2169  | vxlan-12060  | up              | 
| ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    | 54            | vlan-2172  | vxlan-12063  | up              | 
| P5G/P5G_App/P5G-F1C-NGC-N2                              | 77            | vlan-2337  | vxlan-12228  | up              | 
| P5G/P5G_App/P5G-mgmt                                    | 44            | vlan-2173  | vxlan-12064  | up              | 
| common/Infra_ANP/PrivateIP-MGMT                         | 56            | vlan-2007  | vxlan-11898  | up              | 
| TESTING_BRUNO/UntitledAP1/SITE1                         | 12            | vlan-2168  | vxlan-12059  | up              | 
| SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                | 47            | vlan-2006  | vxlan-11897  | up              | 
| SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    | 49            | vlan-2342  | vxlan-12233  | up              | 
| SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    | 6             | vlan-2002  | vxlan-11893  | up              | 
| SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  | 31            | vlan-2335  | vxlan-12226  | up              | 
| SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     | 23            | vlan-2341  | vxlan-12232  | up              | 
| SPN_IntraLab/SPN_Connect_ANP/TEST1                      | 51            | vlan-2339  | vxlan-12230  | up              | 
| iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd | 58            | vlan-2340  | vxlan-12231  | up              | 
+---------------------------------------------------------+---------------+------------+--------------+-----------------+

Ethernet Packets Statistics
---------------------------
- Packets with no errors : 40961284306
- Broadcast              : 23668752
- Multicast              : 3132120
- Size up to 64B         : 52
- Size 65-1270B          : 36373743997
- Size 128-255B          : 6117328
- Size 256-511B          : 10485361
- Size 512-1023          : 4832351
- Size 1024-1518         : 4562971665
- Oversize               : 3133553
- Undersize              : 0
- Rx with no errors      : 20471089941
- Rx giant               : 0
- Rx oversize            : 108668
- Tx with no errors      : 20482150888
- Tx giant               : 0
- Tx oversize            : 3024885
- Collisions             : 0
- CRC errors             : 0
- Drops                  : 0


+---------------+----------------+------------------+---------------+-----------------+----------------+------------------+---------------+-----------------+
| Class         | Rx Admit Bytes | Rx Admin Packets | Rx Drop Bytes | Rx Drop Packets | Tx Admit Bytes | Tx Admin Packets | Tx Drop Bytes | Tx Drop Packets |
+---------------+----------------+------------------+---------------+-----------------+----------------+------------------+---------------+-----------------+
| control-plane | 6278525906     | 55099090         | 0             | 0               | 6887814261     | 68040486         | 4948          | 67              | 
| level1        | 108233536927   | 382041173        | 0             | 0               | 23057574830    | 303076787        | 0             | 0               | 
| level2        | 0              | 0                | 0             | 0               | 0              | 0                | 0             | 0               | 
| level3        | 3804944462578  | 20033271157      | 275788        | 1738            | 3934673809917  | 20119077208      | 50845         | 539             | 
| level4        | 0              | 0                | 0             | 0               | 0              | 0                | 0             | 0               | 
| level5        | 0              | 0                | 0             | 0               | 0              | 0                | 0             | 0               | 
| level6        | 0              | 0                | 0             | 0               | 0              | 0                | 0             | 0               | 
| policy-plane  | 0              | 0                | 0             | 0               | 0              | 0                | 0             | 0               | 
| span          | 0              | 0                | 0             | 0               | 0              | 0                | 0             | 0               | 
+---------------+----------------+------------------+---------------+-----------------+----------------+------------------+---------------+-----------------+
```

[[Back]](./InterfacePhy.md)