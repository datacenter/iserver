# Node Interface - Physical

## Verbose output

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --id 1/1
    --view verbose

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


+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| Up | EPG                                                     | Preferred Member | Flood    | Class ID | QoS Class   | Isolation  | Label Match |
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | CNC_demo/CNC_ANP/CNC_bus                                | exclude          | disabled | 32779    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | DT-EPNM/DT-EPNM/Data                                    | exclude          | disabled | 16414    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | DT-EPNM/DT-EPNM/Device                                  | exclude          | disabled | 16415    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | NXOS-HandOff_Test/TEST/EPG1                             | exclude          | disabled | 16388    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         | exclude          | disabled | 16386    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | MPC-F5T/F5_ANP/F5_IN                                    | exclude          | disabled | 32770    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | MPC-F5T/F5_ANP/F5_OUT                                   | exclude          | disabled | 16387    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | DT-EPNM/DT-EPNM/MGMT                                    | exclude          | disabled | 16413    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    | exclude          | disabled | 32771    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | P5G/P5G_App/P5G-F1C-NGC-N2                              | exclude          | disabled | 17       | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | P5G/P5G_App/P5G-mgmt                                    | exclude          | disabled | 32785    | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | common/Infra_ANP/PrivateIP-MGMT                         | exclude          | disabled | 18       | unspecified | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | TESTING_BRUNO/UntitledAP1/SITE1                         | exclude          | disabled | 16386    | unspecified | unenforced | None        | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                | exclude          | disabled | 32771    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    | exclude          | disabled | 32773    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    | exclude          | disabled | 49154    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  | exclude          | disabled | 32775    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     | exclude          | disabled | 49154    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | exclude          | disabled | 32772    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+
| V  | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd | exclude          | disabled | 32770    | level3      | unenforced | AtleastOne  | 
+----+---------------------------------------------------------+------------------+----------+----------+-------------+------------+-------------+

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
- Packets with no errors : 48020278857
- Broadcast              : 27432328
- Multicast              : 3583114
- Size up to 64B         : 52
- Size 65-1270B          : 42634615662
- Size 128-255B          : 7175609
- Size 256-511B          : 12260101
- Size 512-1023          : 5740415
- Size 1024-1518         : 5356792428
- Oversize               : 3694590
- Undersize              : 0
- Rx with no errors      : 23994790733
- Rx giant               : 0
- Rx oversize            : 127256
- Tx with no errors      : 24017444647
- Tx giant               : 0
- Tx oversize            : 3567334
- Collisions             : 0
- CRC errors             : 0
- Drops                  : 0


+---------------+---------------+-------------+-------------+---------+---------------+-------------+-------------+---------+
| Class         | Rx Admit [B]  | Rx Admin    | Rx Drop [B] | Rx Drop | Tx Admit [B]  | Tx Admin    | Tx Drop [B] | Tx Drop |
+---------------+---------------+-------------+-------------+---------+---------------+-------------+-------------+---------+
| control-plane | 7364030285    | 64619197    | 0           | 0       | 8057129296    | 79476246    | 4948        | 67      | 
| level1        | 108233536927  | 382041173   | 0           | 0       | 23057574830   | 303076787   | 0           | 0       | 
| level2        | 0             | 0           | 0           | 0       | 0             | 0           | 0           | 0       | 
| level3        | 4477936865964 | 23547478678 | 736669      | 5146    | 4627184668794 | 23642965701 | 52303       | 560     | 
| level4        | 0             | 0           | 0           | 0       | 0             | 0           | 0           | 0       | 
| level5        | 0             | 0           | 0           | 0       | 0             | 0           | 0           | 0       | 
| level6        | 0             | 0           | 0           | 0       | 0             | 0           | 0           | 0       | 
| policy-plane  | 0             | 0           | 0           | 0       | 0             | 0           | 0           | 0       | 
| span          | 0             | 0           | 0           | 0       | 0             | 0           | 0           | 0       | 
+---------------+---------------+-------------+-------------+---------+---------------+-------------+-------------+---------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --id 1/1
    --view verbose

{
    "duration": 7360,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 413,
        "disconnect_time": 0,
        "mo_time": 6312,
        "total_time": 6725
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

True	413	-	connect apic11o.emea-sp.cisco.com
True	335	11	apic11o.emea-sp.cisco.com class fabricNode
True	310	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	322	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	483	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	625	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	288	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	365	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query query-target=children&target-subtree-class=rmonEtherStats
True	308	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmFcot
True	277	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query query-target=children&target-subtree-class=l1LoadP
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query query-target=children&target-subtree-class=l1EeeP
True	350	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	306	13	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	342	12	apic11o.emea-sp.cisco.com mo uni/infra/nodecfgcont/node-205 query query-target=subtree&target-subtree-class=infraRsInterfacePolProfile
True	305	3	apic11o.emea-sp.cisco.com mo uni/infra/accportprof-UCSB1-FI-A_IntProf query query-target=subtree&target-subtree-class=infraHPortS,infraRsAccBaseGrp,infraPortBlk,infraSubPortBlk
True	584	37	apic11o.emea-sp.cisco.com mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccBndlGrp&rsp-subtree=children&rsp-subtree-class=infraRsCdpIfPol,infraRsMcpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsLacpPol,infraRsMonIfInfraPol,infraAccBndlSubgrp,infraRsStpIfPol,infraRsAttEntP,infraRsSpanVSrcGrp,infraRsSpanVDestGrp,infraRsL2IfPol,infraRsStormctrlIfPol,infraRsQosEgressDppIfPol,infraRsQosIngressDppIfPol,infraRsQosSdIfPol,infraRsQosPfcIfPol,infraRsQosEgressDppIfPol,infraRsL2PortSecurityPol,infraRsFcIfPol,infraRsMacsecIfPol
True	384	30	apic11o.emea-sp.cisco.com class infraAttEntityP query rsp-subtree=children&rsp-subtree-class=infraProvAcc,infraRtAttEntP,infraRsDomP
True	383	324	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/qosmIfClass
```

[[Back]](./InterfacePhy.md)