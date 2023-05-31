# Node Interface - Physical

## Filter by encapsulation vlan

Example: single vlan

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --evlan 908
    --view vlan

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+--------------------------+--------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans               | EPG                      | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+--------------------------+--------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | 2-3,32-33,41-42          | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | 2-3,19-20,32-33,41-43,45 | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-45 | vlan-1  |                          | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-45 | vlan-1  |                          | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-45 | vlan-1  | 19-20,32-33,41-43,45     | P5G/P5G_App/P5G-Edge-Int | 42            | vlan-908   | vxlan-10300  | up              | 
+---------------------+-----------+------+---------+---------+--------------------------+--------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Example: multiple vlans

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --evlan 900,904-905
    --view vlan

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+--------------------------+----------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans               | EPG                        | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+--------------------------+----------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | 2-3,32-33,41-42          | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | 2-3,19-20,32-33,41-43,45 | P5G/P5G_App/P5G-F1C-NGC-N2 | 20            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                          | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                          | P5G/P5G_App/P5G-mgmt       | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-45 | vlan-1  |                          | P5G/P5G_App/P5G-F1C-NGC-N2 | 20            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                          | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                          | P5G/P5G_App/P5G-mgmt       | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-45 | vlan-1  |                          | P5G/P5G_App/P5G-F1C-NGC-N2 | 20            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                          | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                          | P5G/P5G_App/P5G-mgmt       | 45            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-45 | vlan-1  | 19-20,32-33,41-43,45     | P5G/P5G_App/P5G-F1C-NGC-N2 | 20            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                          | P5G/P5G_App/P5G-F1U-NGU-N3 | 33            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                          | P5G/P5G_App/P5G-mgmt       | 45            | vlan-900   | vxlan-10292  | up              | 
+---------------------+-----------+------+---------+---------+--------------------------+----------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --evlan 908
    --view vlan

{
    "duration": 16816,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 508,
        "disconnect_time": 0,
        "mo_time": 15445,
        "total_time": 15953
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

True	508	-	connect apic11o.emea-sp.cisco.com
True	448	11	apic11o.emea-sp.cisco.com class fabricNode
True	321	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	326	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	435	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	689	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	322	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	401	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	363	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	365	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	381	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	458	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	387	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	455	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	381	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	350	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	453	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	387	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	412	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	361	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	374	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./InterfacePhy.md)