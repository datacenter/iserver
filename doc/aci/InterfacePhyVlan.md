# Node Interface - Physical

## Filter by internal vlan

Example: single vlan

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --vlan 38
    --view vlan

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans                                                 | EPG                      | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | unknown | vlan-1  | 3-4,6-7,11-16,21-31,33-41,43-45,49,56,59,61-62,65-69,72-81 | CNC_demo/CNC_ANP/CNC_bus | 38            | vlan-2001  | vxlan-11892  | up              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | unknown | vlan-1  | 3-4,6-7,11-16,23-28,30-31,33-38,40-41,56,61-62,65-69       | CNC_demo/CNC_ANP/CNC_bus | 38            | vlan-2001  | vxlan-11892  | up              | 
+---------------------+-----------+------+---------+---------+------------------------------------------------------------+--------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Example: multiple vlans

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --vlan 30-39
    --view vlan

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+---------+------------------------------------------------------------+---------------------------------+---------------+------------+--------------+-----------------+
| Node                | Interface | Oper | Native  | Primary | Oper Vlans                                                 | EPG                             | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+---------------------+-----------+------+---------+---------+------------------------------------------------------------+---------------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | unknown | vlan-1  | 3-4,6-7,11-16,21-31,33-41,43-45,49,56,59,61-62,65-69,72-81 | CNC_demo/CNC_ANP/CNC_bus        | 38            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         |                                                            | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN | 36            | vlan-2338  | vxlan-12229  | up              | 
|                     |           |      |         |         |                                                            | MPC-F5T/F5_ANP/F5_IN            | 31            | vlan-2008  | vxlan-11899  | up              | 
|                     |           |      |         |         |                                                            | MPC-F5T/F5_ANP/F5_OUT           | 34            | vlan-2009  | vxlan-11900  | up              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | unknown | vlan-1  | 3-4,6-7,11-16,23-28,30-31,33-38,40-41,56,61-62,65-69       | CNC_demo/CNC_ANP/CNC_bus        | 38            | vlan-2001  | vxlan-11892  | up              | 
|                     |           |      |         |         |                                                            | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN | 36            | vlan-2338  | vxlan-12229  | up              | 
|                     |           |      |         |         |                                                            | MPC-F5T/F5_ANP/F5_IN            | 31            | vlan-2008  | vxlan-11899  | up              | 
|                     |           |      |         |         |                                                            | MPC-F5T/F5_ANP/F5_OUT           | 34            | vlan-2009  | vxlan-11900  | up              | 
+---------------------+-----------+------+---------+---------+------------------------------------------------------------+---------------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --vlan 38
    --view vlan

{
    "duration": 17742,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 16367,
        "total_time": 16778
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

True	411	-	connect apic11o.emea-sp.cisco.com
True	309	13	apic11o.emea-sp.cisco.com class fabricNode
True	350	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	354	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	357	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	366	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	406	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	733	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	428	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	405	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	372	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	343	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	333	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	373	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	345	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	421	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	397	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	347	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	355	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	331	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	346	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	350	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	453	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	456	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	600	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	399	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	598	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	611	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	537	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	510	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./InterfacePhy.md)