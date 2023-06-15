# Node Interface - Physical

## Filter by encapsulation vlan

Example: single vlan

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --evlan 908
    --view vlan

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+-------------------------+--------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans              | EPG                      | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+-------------------------+--------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | 57-58,63-64,70-71       | P5G/P5G_App/P5G-Edge-Int | 58            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | 40,42,57-60,63-64,70-71 | P5G/P5G_App/P5G-Edge-Int | 58            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-42 | vlan-1  |                         | P5G/P5G_App/P5G-Edge-Int | 58            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-42 | vlan-1  |                         | P5G/P5G_App/P5G-Edge-Int | 58            | vlan-908   | vxlan-10300  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-42 | vlan-1  | 40,42,57-60,70-71       | P5G/P5G_App/P5G-Edge-Int | 58            | vlan-908   | vxlan-10300  | up              | 
+---------------------+-----------+------+---------+---------+-------------------------+--------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Example: multiple vlans

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --evlan 900,904-905
    --view vlan

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+-------------------------+----------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans              | EPG                        | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+-------------------------+----------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/15      | up   | unknown | vlan-1  | 57-58,63-64,70-71       | P5G/P5G_App/P5G-F1U-NGU-N3 | 71            | vlan-905   | vxlan-10297  | up              | 
| pod-1/bl205-eu-spdc | 1/16      | up   | unknown | vlan-1  | 40,42,57-60,63-64,70-71 | P5G/P5G_App/P5G-F1C-NGC-N2 | 60            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                         | P5G/P5G_App/P5G-F1U-NGU-N3 | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                         | P5G/P5G_App/P5G-mgmt       | 42            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/17      | down | vlan-42 | vlan-1  |                         | P5G/P5G_App/P5G-F1C-NGC-N2 | 60            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                         | P5G/P5G_App/P5G-F1U-NGU-N3 | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                         | P5G/P5G_App/P5G-mgmt       | 42            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/18      | down | vlan-42 | vlan-1  |                         | P5G/P5G_App/P5G-F1C-NGC-N2 | 60            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                         | P5G/P5G_App/P5G-F1U-NGU-N3 | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                         | P5G/P5G_App/P5G-mgmt       | 42            | vlan-900   | vxlan-10292  | up              | 
| pod-1/bl205-eu-spdc | 1/19      | up   | vlan-42 | vlan-1  | 40,42,57-60,70-71       | P5G/P5G_App/P5G-F1C-NGC-N2 | 60            | vlan-904   | vxlan-10296  | up              | 
|                     |           |      |         |         |                         | P5G/P5G_App/P5G-F1U-NGU-N3 | 71            | vlan-905   | vxlan-10297  | up              | 
|                     |           |      |         |         |                         | P5G/P5G_App/P5G-mgmt       | 42            | vlan-900   | vxlan-10292  | up              | 
+---------------------+-----------+------+---------+---------+-------------------------+----------------------------+---------------+------------+--------------+-----------------+
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
    "duration": 15743,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 14532,
        "total_time": 14962
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

True	430	-	connect apic11o.emea-sp.cisco.com
True	299	13	apic11o.emea-sp.cisco.com class fabricNode
True	315	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	311	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	335	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	661	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	298	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	358	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	342	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	357	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	399	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	343	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	383	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	396	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	391	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	416	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./InterfacePhy.md)