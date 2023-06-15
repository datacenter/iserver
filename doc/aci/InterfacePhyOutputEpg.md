# Node Interface - Physical

## EPG focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view epg

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------------------------------------------------------+---------------+---------+
| Node                | Interface | Oper | EPG                                                     | Bridge Domain | Subnets |
+---------------------+-----------+------+---------------------------------------------------------+---------------+---------+
| pod-1/bl205-eu-spdc | 1/1       | up   | CNC_demo/CNC_ANP/CNC_bus                                |               |         | 
|                     |           |      | DT-EPNM/DT-EPNM/Data                                    |               |         | 
|                     |           |      | DT-EPNM/DT-EPNM/Device                                  |               |         | 
|                     |           |      | NXOS-HandOff_Test/TEST/EPG1                             |               |         | 
|                     |           |      | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         |               |         | 
|                     |           |      | MPC-F5T/F5_ANP/F5_IN                                    |               |         | 
|                     |           |      | MPC-F5T/F5_ANP/F5_OUT                                   |               |         | 
|                     |           |      | DT-EPNM/DT-EPNM/MGMT                                    |               |         | 
|                     |           |      | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    |               |         | 
|                     |           |      | common/Infra_ANP/PrivateIP-MGMT                         |               |         | 
|                     |           |      | TESTING_BRUNO/UntitledAP1/SITE1                         |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     |               |         | 
|                     |           |      | SPN_IntraLab/SPN_Connect_ANP/TEST1                      |               |         | 
|                     |           |      | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd |               |         | 
| pod-1/bl205-eu-spdc | 1/2       | up   | CNC_demo/CNC_ANP/CNC_bus                                |               |         | 
|                     |           |      | NXOS-HandOff_Test/TEST/EPG1                             |               |         | 
|                     |           |      | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         |               |         | 
|                     |           |      | MPC-F5T/F5_ANP/F5_IN                                    |               |         | 
|                     |           |      | MPC-F5T/F5_ANP/F5_OUT                                   |               |         | 
|                     |           |      | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    |               |         | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    |               |         | 
|                     |           |      | common/Infra_ANP/PrivateIP-MGMT                         |               |         | 
|                     |           |      | TESTING_BRUNO/UntitledAP1/SITE1                         |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  |               |         | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     |               |         | 
|                     |           |      | SPN_IntraLab/SPN_Connect_ANP/TEST1                      |               |         | 
|                     |           |      | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd |               |         | 
| pod-1/bl205-eu-spdc | 1/3       | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/4       | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/5       | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/6       | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/7       | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/8       | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/9       | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/10      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/11      | up   |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/12      | up   |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/13      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/14      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/15      | up   | P5G/P5G_App/P5G-Edge-Int                                |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-N6-NAT                                  |               |         | 
| pod-1/bl205-eu-spdc | 1/16      | up   | P5G/P5G_App/P5G-Edge-Int                                |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    |               |         | 
|                     |           |      | P5G/P5G_App/P5G-N6-NAT                                  |               |         | 
| pod-1/bl205-eu-spdc | 1/17      | down | P5G/P5G_App/P5G-Edge-Int                                |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    |               |         | 
|                     |           |      | P5G/P5G_App/P5G-N6-NAT                                  |               |         | 
| pod-1/bl205-eu-spdc | 1/18      | down | P5G/P5G_App/P5G-Edge-Int                                |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    |               |         | 
|                     |           |      | P5G/P5G_App/P5G-N6-NAT                                  |               |         | 
| pod-1/bl205-eu-spdc | 1/19      | up   | P5G/P5G_App/P5G-Edge-Int                                |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              |               |         | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    |               |         | 
| pod-1/bl205-eu-spdc | 1/20      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/21      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/22      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/23      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/24      | up   |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/25      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/26      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/27      | up   | SPN_IntraLab/SPN_Connect_ANP/TEST1                      |               |         | 
| pod-1/bl205-eu-spdc | 1/28      | up   |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/29      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/30      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/31      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/32      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/33      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/34      | down |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/35      | up   |                                                         |               |         | 
| pod-1/bl205-eu-spdc | 1/36      | up   |                                                         |               |         | 
+---------------------+-----------+------+---------------------------------------------------------+---------------+---------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view epg

{
    "duration": 15033,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 388,
        "disconnect_time": 0,
        "mo_time": 14050,
        "total_time": 14438
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

True	388	-	connect apic11o.emea-sp.cisco.com
True	297	13	apic11o.emea-sp.cisco.com class fabricNode
True	326	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	326	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	321	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	588	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	311	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	360	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	377	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	384	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	330	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	316	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	343	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./InterfacePhy.md)