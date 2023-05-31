# Node Interface - Physical

## EPG focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view vlan

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+---------------------------------------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans                                                               | EPG                                                     | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+---------------------------------------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | unknown | vlan-1  | 5-8,11-12,14-15,17-19,22-31,35,37-38,43-44,46-51,53-59,61,63,69-70,72-81 | CNC_demo/CNC_ANP/CNC_bus                                | 27            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         |                                                                          | DT-EPNM/DT-EPNM/Data                                    | 78            | vlan-2170  | vxlan-12061  | up              | 
|                     |           |      |         |         |                                                                          | DT-EPNM/DT-EPNM/Device                                  | 79            | vlan-2003  | vxlan-11894  | up              | 
|                     |           |      |         |         |                                                                          | NXOS-HandOff_Test/TEST/EPG1                             | 8             | vlan-2343  | vxlan-12234  | up              | 
|                     |           |      |         |         |                                                                          | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         | 15            | vlan-2338  | vxlan-12229  | up              | 
|                     |           |      |         |         |                                                                          | MPC-F5T/F5_ANP/F5_IN                                    | 38            | vlan-2008  | vxlan-11899  | up              | 
|                     |           |      |         |         |                                                                          | MPC-F5T/F5_ANP/F5_OUT                                   | 18            | vlan-2009  | vxlan-11900  | up              | 
|                     |           |      |         |         |                                                                          | DT-EPNM/DT-EPNM/MGMT                                    | 80            | vlan-2169  | vxlan-12060  | up              | 
|                     |           |      |         |         |                                                                          | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    | 54            | vlan-2172  | vxlan-12063  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1C-NGC-N2                              | 77            | vlan-2337  | vxlan-12228  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt                                    | 44            | vlan-2173  | vxlan-12064  | up              | 
|                     |           |      |         |         |                                                                          | common/Infra_ANP/PrivateIP-MGMT                         | 56            | vlan-2007  | vxlan-11898  | up              | 
|                     |           |      |         |         |                                                                          | TESTING_BRUNO/UntitledAP1/SITE1                         | 12            | vlan-2168  | vxlan-12059  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                | 47            | vlan-2006  | vxlan-11897  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    | 49            | vlan-2342  | vxlan-12233  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    | 6             | vlan-2002  | vxlan-11893  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  | 31            | vlan-2335  | vxlan-12226  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     | 23            | vlan-2341  | vxlan-12232  | up              | 
|                     |           |      |         |         |                                                                          | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | 51            | vlan-2339  | vxlan-12230  | up              | 
|                     |           |      |         |         |                                                                          | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd | 58            | vlan-2340  | vxlan-12231  | up              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | unknown | vlan-1  | 5-8,11-12,14-15,17-18,22-23,26-27,30-31,37-38,43-44,46-51,53-58,61,63    | CNC_demo/CNC_ANP/CNC_bus                                | 27            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         |                                                                          | NXOS-HandOff_Test/TEST/EPG1                             | 8             | vlan-2343  | vxlan-12234  | up              | 
|                     |           |      |         |         |                                                                          | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         | 15            | vlan-2338  | vxlan-12229  | up              | 
|                     |           |      |         |         |                                                                          | MPC-F5T/F5_ANP/F5_IN                                    | 38            | vlan-2008  | vxlan-11899  | up              | 
|                     |           |      |         |         |                                                                          | MPC-F5T/F5_ANP/F5_OUT                                   | 18            | vlan-2009  | vxlan-11900  | up              | 
|                     |           |      |         |         |                                                                          | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    | 54            | vlan-2172  | vxlan-12063  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt                                    | 44            | vlan-2173  | vxlan-12064  | up              | 
|                     |           |      |         |         |                                                                          | common/Infra_ANP/PrivateIP-MGMT                         | 56            | vlan-2007  | vxlan-11898  | up              | 
|                     |           |      |         |         |                                                                          | TESTING_BRUNO/UntitledAP1/SITE1                         | 12            | vlan-2168  | vxlan-12059  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                | 47            | vlan-2006  | vxlan-11897  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    | 49            | vlan-2342  | vxlan-12233  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    | 6             | vlan-2002  | vxlan-11893  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  | 31            | vlan-2335  | vxlan-12226  | up              | 
|                     |           |      |         |         |                                                                          | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     | 23            | vlan-2341  | vxlan-12232  | up              | 
|                     |           |      |         |         |                                                                          | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | 51            | vlan-2339  | vxlan-12230  | up              | 
|                     |           |      |         |         |                                                                          | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd | 58            | vlan-2340  | vxlan-12231  | up              | 
| pod-1/bl205-eu-spdc | 1/3       | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/4       | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/5       | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/6       | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/7       | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/8       | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/9       | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/10      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/11      | up   | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/12      | up   | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/13      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/14      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | 2-3,32-33,41-42                                                          | P5G/P5G_App/P5G-Edge-Int                                | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1U-NGU-N3                              | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-N6-NAT                                  | 3             | vlan-906   | vxlan-10298  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | 2-3,19-20,32-33,41-43,45                                                 | P5G/P5G_App/P5G-Edge-Int                                | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1C-NGC-N2                              | 20            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1U-NGU-N3                              | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt                                    | 45            | vlan-900   | vxlan-10292  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-N6-NAT                                  | 3             | vlan-906   | vxlan-10298  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-45 | vlan-1  |                                                                          | P5G/P5G_App/P5G-Edge-Int                                | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1C-NGC-N2                              | 20            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1U-NGU-N3                              | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt                                    | 45            | vlan-900   | vxlan-10292  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-N6-NAT                                  | 3             | vlan-906   | vxlan-10298  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-45 | vlan-1  |                                                                          | P5G/P5G_App/P5G-Edge-Int                                | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1C-NGC-N2                              | 20            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1U-NGU-N3                              | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt                                    | 45            | vlan-900   | vxlan-10292  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-N6-NAT                                  | 3             | vlan-906   | vxlan-10298  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-45 | vlan-1  | 19-20,32-33,41-43,45                                                     | P5G/P5G_App/P5G-Edge-Int                                | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1C-NGC-N2                              | 20            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-F1U-NGU-N3                              | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt                                    | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/20      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/21      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/22      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/23      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/24      | up   | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/25      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/26      | down | unknown | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/27      | up   | unknown | vlan-1  | 50,52                                                                    | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | 52            | vlan-2000  | vxlan-24492  | up              | 
| pod-1/bl205-eu-spdc | 1/28      | up   | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/29      | down | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/30      | down | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/31      | down | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/32      | down | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/33      | down | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/34      | down | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/35      | up   | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
| pod-1/bl205-eu-spdc | 1/36      | up   | vlan-1  | vlan-1  |                                                                          |                                                         |               |            |              |                 | 
+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+---------------------------------------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --view vlan

{
    "duration": 17196,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 449,
        "disconnect_time": 0,
        "mo_time": 15726,
        "total_time": 16175
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

True	449	-	connect apic11o.emea-sp.cisco.com
True	330	11	apic11o.emea-sp.cisco.com class fabricNode
True	359	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	326	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	424	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	410	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	414	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	919	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	342	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	400	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	368	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	375	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	360	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	415	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	407	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	324	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	374	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	454	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	378	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	438	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	399	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	417	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	343	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	399	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./InterfacePhy.md)