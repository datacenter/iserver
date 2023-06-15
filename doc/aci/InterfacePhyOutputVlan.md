# Node Interface - Physical

## EPG focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view vlan

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+------------------------------------------------------------+---------------------------------------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans                                                 | EPG                                                     | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+------------------------------------------------------------+---------------------------------------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | unknown | vlan-1  | 3-4,6-7,11-16,21-31,33-41,43-45,49,56,59,61-62,65-69,72-81 | CNC_demo/CNC_ANP/CNC_bus                                | 38            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         |                                                            | DT-EPNM/DT-EPNM/Data                                    | 77            | vlan-2170  | vxlan-12061  | up              | 
|                     |           |      |         |         |                                                            | DT-EPNM/DT-EPNM/Device                                  | 73            | vlan-2003  | vxlan-11894  | up              | 
|                     |           |      |         |         |                                                            | NXOS-HandOff_Test/TEST/EPG1                             | 69            | vlan-2343  | vxlan-12234  | up              | 
|                     |           |      |         |         |                                                            | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         | 36            | vlan-2338  | vxlan-12229  | up              | 
|                     |           |      |         |         |                                                            | MPC-F5T/F5_ANP/F5_IN                                    | 31            | vlan-2008  | vxlan-11899  | up              | 
|                     |           |      |         |         |                                                            | MPC-F5T/F5_ANP/F5_OUT                                   | 34            | vlan-2009  | vxlan-11900  | up              | 
|                     |           |      |         |         |                                                            | DT-EPNM/DT-EPNM/MGMT                                    | 74            | vlan-2169  | vxlan-12060  | up              | 
|                     |           |      |         |         |                                                            | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    | 24            | vlan-2172  | vxlan-12063  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1C-NGC-N2                              | 78            | vlan-2337  | vxlan-12228  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-mgmt                                    | 41            | vlan-2173  | vxlan-12064  | up              | 
|                     |           |      |         |         |                                                            | common/Infra_ANP/PrivateIP-MGMT                         | 62            | vlan-2007  | vxlan-11898  | up              | 
|                     |           |      |         |         |                                                            | TESTING_BRUNO/UntitledAP1/SITE1                         | 66            | vlan-2168  | vxlan-12059  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                | 12            | vlan-2006  | vxlan-11897  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    | 14            | vlan-2342  | vxlan-12233  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    | 16            | vlan-2002  | vxlan-11893  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  | 4             | vlan-2335  | vxlan-12226  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     | 26            | vlan-2341  | vxlan-12232  | up              | 
|                     |           |      |         |         |                                                            | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | 7             | vlan-2339  | vxlan-12230  | up              | 
|                     |           |      |         |         |                                                            | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd | 28            | vlan-2340  | vxlan-12231  | up              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | unknown | vlan-1  | 3-4,6-7,11-16,23-28,30-31,33-38,40-41,56,61-62,65-69       | CNC_demo/CNC_ANP/CNC_bus                                | 38            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         |                                                            | NXOS-HandOff_Test/TEST/EPG1                             | 69            | vlan-2343  | vxlan-12234  | up              | 
|                     |           |      |         |         |                                                            | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         | 36            | vlan-2338  | vxlan-12229  | up              | 
|                     |           |      |         |         |                                                            | MPC-F5T/F5_ANP/F5_IN                                    | 31            | vlan-2008  | vxlan-11899  | up              | 
|                     |           |      |         |         |                                                            | MPC-F5T/F5_ANP/F5_OUT                                   | 34            | vlan-2009  | vxlan-11900  | up              | 
|                     |           |      |         |         |                                                            | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    | 24            | vlan-2172  | vxlan-12063  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-mgmt                                    | 41            | vlan-2173  | vxlan-12064  | up              | 
|                     |           |      |         |         |                                                            | common/Infra_ANP/PrivateIP-MGMT                         | 62            | vlan-2007  | vxlan-11898  | up              | 
|                     |           |      |         |         |                                                            | TESTING_BRUNO/UntitledAP1/SITE1                         | 66            | vlan-2168  | vxlan-12059  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                | 12            | vlan-2006  | vxlan-11897  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    | 14            | vlan-2342  | vxlan-12233  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    | 16            | vlan-2002  | vxlan-11893  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  | 4             | vlan-2335  | vxlan-12226  | up              | 
|                     |           |      |         |         |                                                            | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     | 26            | vlan-2341  | vxlan-12232  | up              | 
|                     |           |      |         |         |                                                            | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | 7             | vlan-2339  | vxlan-12230  | up              | 
|                     |           |      |         |         |                                                            | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd | 28            | vlan-2340  | vxlan-12231  | up              | 
| pod-1/bl205-eu-spdc | 1/3       | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/4       | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/5       | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/6       | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/7       | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/8       | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/9       | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/10      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/11      | up   | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/12      | up   | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/13      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/14      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | 57-58,63-64,70-71                                          | P5G/P5G_App/P5G-Edge-Int                                | 58            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1U-NGU-N3                              | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-N6-NAT                                  | 64            | vlan-906   | vxlan-10298  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | 40,42,57-60,63-64,70-71                                    | P5G/P5G_App/P5G-Edge-Int                                | 58            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1C-NGC-N2                              | 60            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1U-NGU-N3                              | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-mgmt                                    | 42            | vlan-900   | vxlan-10292  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-N6-NAT                                  | 64            | vlan-906   | vxlan-10298  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-42 | vlan-1  |                                                            | P5G/P5G_App/P5G-Edge-Int                                | 58            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1C-NGC-N2                              | 60            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1U-NGU-N3                              | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-mgmt                                    | 42            | vlan-900   | vxlan-10292  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-N6-NAT                                  | 64            | vlan-906   | vxlan-10298  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-42 | vlan-1  |                                                            | P5G/P5G_App/P5G-Edge-Int                                | 58            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1C-NGC-N2                              | 60            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1U-NGU-N3                              | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-mgmt                                    | 42            | vlan-900   | vxlan-10292  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-N6-NAT                                  | 64            | vlan-906   | vxlan-10298  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-42 | vlan-1  | 40,42,57-60,70-71                                          | P5G/P5G_App/P5G-Edge-Int                                | 58            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1C-NGC-N2                              | 60            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-F1U-NGU-N3                              | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                            | P5G/P5G_App/P5G-mgmt                                    | 42            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/20      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/21      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/22      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/23      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/24      | up   | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/25      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/26      | down | unknown | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/27      | up   | unknown | vlan-1  | 6,8                                                        | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | 8             | vlan-2000  | vxlan-24492  | up              | 
| pod-1/bl205-eu-spdc | 1/28      | up   | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/29      | down | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/30      | down | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/31      | down | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/32      | down | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/33      | down | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/34      | down | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/35      | up   | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/36      | up   | vlan-1  | vlan-1  |                                                            |                                                         |               |            |              |                 | 
+---------------------+-----------+------+---------+---------+------------------------------------------------------------+---------------------------------------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view vlan

{
    "duration": 15355,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 14336,
        "total_time": 14731
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	313	13	apic11o.emea-sp.cisco.com class fabricNode
True	303	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	305	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	328	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	560	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	296	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	329	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	395	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	373	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	501	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	413	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./InterfacePhy.md)