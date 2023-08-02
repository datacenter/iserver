# Node Interface - Physical

## Filter by internal vlan

Example: single vlan

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --vlan 12
    --view vlan

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+---------+---------+----------------+-----------------------------+---------------+------------+--------------+-----------------+
| Node                 | Interface | Oper | Native  | Primary | Oper Vlans     | EPG                         | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+----------------------+-----------+------+---------+---------+----------------+-----------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl2205-eu-spdc | 1/19      | up   | unknown | vlan-1  | 1,4-5,11-16,20 | vEPC_demo/vEPG_ANP/vEPG_ACC | 12            | vlan-2700  | vxlan-9892   | up              | 
+----------------------+-----------+------+---------+---------+----------------+-----------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Example: multiple vlans

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --vlan 11-19
    --view vlan

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+---------+---------+----------------+------------------------------+---------------+------------+--------------+-----------------+
| Node                 | Interface | Oper | Native  | Primary | Oper Vlans     | EPG                          | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+----------------------+-----------+------+---------+---------+----------------+------------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl2205-eu-spdc | 1/19      | up   | unknown | vlan-1  | 1,4-5,11-16,20 | vEPC_demo/vEPG_ANP/vEPG_ACC  | 12            | vlan-2700  | vxlan-9892   | up              | 
|                      |           |      |         |         |                | vEPC_demo/vEPG_ANP/vEPG_CTRL | 14            | vlan-2701  | vxlan-9893   | up              | 
|                      |           |      |         |         |                | vEPC_demo/vEPG_ANP/vEPG_INT  | 16            | vlan-2800  | vxlan-9992   | up              | 
+----------------------+-----------+------+---------+---------+----------------+------------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --vlan 12
    --view vlan

{
    "duration": 16347,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 14735,
        "total_time": 15145
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

True	410	-	connect apic21o.emea-sp.cisco.com:443
True	295	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	876	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	315	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	308	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	316	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	381	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	293	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	376	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	418	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	328	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	320	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	393	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	334	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	329	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	387	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	349	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	345	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	376	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	300	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	374	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	316	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	292	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	320	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	334	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	341	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	311	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	360	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	452	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	333	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
```

[[Back]](./InterfacePhy.md)