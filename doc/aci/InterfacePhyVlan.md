# Node Interface - Physical

## Filter by internal vlan

Example: single vlan

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --vlan 27
    --view vlan

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans                                                               | EPG                      | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | unknown | vlan-1  | 5-8,11-12,14-15,17-19,22-31,35,37-38,43-44,46-51,53-59,61,63,69-70,72-81 | CNC_demo/CNC_ANP/CNC_bus | 27            | vlan-2001  | vxlan-11892  | up              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | unknown | vlan-1  | 5-8,11-12,14-15,17-18,22-23,26-27,30-31,37-38,43-44,46-51,53-58,61,63    | CNC_demo/CNC_ANP/CNC_bus | 27            | vlan-2001  | vxlan-11892  | up              | 
+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Example: multiple vlans

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --vlan 27,42-45
    --view vlan

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans                                                               | EPG                      | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | unknown | vlan-1  | 5-8,11-12,14-15,17-19,22-31,35,37-38,43-44,46-51,53-59,61,63,69-70,72-81 | CNC_demo/CNC_ANP/CNC_bus | 27            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt     | 44            | vlan-2173  | vxlan-12064  | up              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | unknown | vlan-1  | 5-8,11-12,14-15,17-18,22-23,26-27,30-31,37-38,43-44,46-51,53-58,61,63    | CNC_demo/CNC_ANP/CNC_bus | 27            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt     | 44            | vlan-2173  | vxlan-12064  | up              | 
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | 2-3,32-33,41-42                                                          | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | 2-3,19-20,32-33,41-43,45                                                 | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt     | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-45 | vlan-1  |                                                                          | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt     | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-45 | vlan-1  |                                                                          | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt     | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-45 | vlan-1  | 19-20,32-33,41-43,45                                                     | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
|                     |           |      |         |         |                                                                          | P5G/P5G_App/P5G-mgmt     | 45            | vlan-900   | vxlan-10292  | up              | 
+---------------------+-----------+------+---------+---------+--------------------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --vlan 27
    --view vlan

{
    "duration": 16231,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 420,
        "disconnect_time": 0,
        "mo_time": 15124,
        "total_time": 15544
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

True	420	-	connect apic11o.emea-sp.cisco.com
True	315	11	apic11o.emea-sp.cisco.com class fabricNode
True	323	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	325	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	401	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	432	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	350	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	363	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	366	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	714	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	329	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	363	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	385	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	362	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	326	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	368	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	471	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	361	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	377	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	412	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	378	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	375	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./InterfacePhy.md)