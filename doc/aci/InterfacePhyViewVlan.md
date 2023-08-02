# Node Interface - Physical

## EPG focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view vlan

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+---------+---------+----------------+------------------------------+---------------+------------+--------------+-----------------+
| Node                 | Interface | Oper | Native  | Primary | Oper Vlans     | EPG                          | Internal VLAN | Encap VLAN | Fabric VxLAN | VLAN Oper State |
+----------------------+-----------+------+---------+---------+----------------+------------------------------+---------------+------------+--------------+-----------------+
| pod-1/bl2205-eu-spdc | 1/1       | up   | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/2       | up   | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/3       | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/4       | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/5       | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/6       | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/7       | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/8       | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/9       | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/10      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/11      | up   | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/13      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/14      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/15      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/16      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/17      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/18      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | unknown | vlan-1  | 1,4-5,11-16,20 | vEPC_demo/vEPG_ANP/vEPG_ACC  | 12            | vlan-2700  | vxlan-9892   | up              | 
|                      |           |      |         |         |                | vEPC_demo/vEPG_ANP/vEPG_CTRL | 14            | vlan-2701  | vxlan-9893   | up              | 
|                      |           |      |         |         |                | vEPC_demo/vEPG_ANP/vEPG_INT  | 16            | vlan-2800  | vxlan-9992   | up              | 
|                      |           |      |         |         |                | vEPC_demo/vEPG_ANP/vEPG_MGMT | 5             | vlan-2900  | vxlan-10092  | up              | 
| pod-1/bl2205-eu-spdc | 1/20      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/21      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/22      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/23      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/24      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/25      | up   | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/26      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/27      | up   | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/28      | down | unknown | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/29      | down | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/30      | down | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/31      | down | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/32      | down | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/33      | down | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/34      | down | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/35      | up   | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
| pod-1/bl2205-eu-spdc | 1/36      | up   | vlan-1  | vlan-1  |                |                              |               |            |              |                 | 
+----------------------+-----------+------+---------+---------+----------------+------------------------------+---------------+------------+--------------+-----------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view vlan

{
    "duration": 18264,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 15449,
        "total_time": 15860
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

True	411	-	connect apic21o.emea-sp.cisco.com:443
True	288	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	993	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	308	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	340	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	361	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	310	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	312	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	366	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	292	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	351	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	379	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	334	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	380	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	312	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	362	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	286	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	328	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	375	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	350	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	299	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	308	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	413	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	307	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	330	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	317	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	324	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	350	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	337	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	913	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	412	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	456	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	414	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	391	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	402	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	450	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	280	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
```

[[Back]](./InterfacePhy.md)