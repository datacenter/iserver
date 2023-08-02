# Node Interface - Physical

## EPG focused output

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view epg

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+------------------------------+---------------+---------+
| Node                 | Interface | Oper | EPG                          | Bridge Domain | Subnets |
+----------------------+-----------+------+------------------------------+---------------+---------+
| pod-1/bl2205-eu-spdc | 1/1       | up   |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/2       | up   |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/3       | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/4       | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/5       | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/6       | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/7       | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/8       | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/9       | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/10      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/11      | up   |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/12      | up   |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/13      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/14      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/15      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/16      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/17      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/18      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | vEPC_demo/vEPG_ANP/vEPG_ACC  |               |         | 
|                      |           |      | vEPC_demo/vEPG_ANP/vEPG_CTRL |               |         | 
|                      |           |      | vEPC_demo/vEPG_ANP/vEPG_INT  |               |         | 
|                      |           |      | vEPC_demo/vEPG_ANP/vEPG_MGMT |               |         | 
| pod-1/bl2205-eu-spdc | 1/20      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/21      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/22      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/23      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/24      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/25      | up   |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/26      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/27      | up   |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/28      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/29      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/30      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/31      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/32      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/33      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/34      | down |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/35      | up   |                              |               |         | 
| pod-1/bl2205-eu-spdc | 1/36      | up   |                              |               |         | 
+----------------------+-----------+------+------------------------------+---------------+---------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node bl2205-eu-spdc --view epg

{
    "duration": 17366,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 381,
        "disconnect_time": 0,
        "mo_time": 15820,
        "total_time": 16201
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

True	381	-	connect apic21o.emea-sp.cisco.com:443
True	365	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	1102	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	317	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	319	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	393	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	336	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	359	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	306	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	475	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	307	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	297	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	337	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	296	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	325	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	316	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	321	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	659	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	460	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	385	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	361	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	318	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	324	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	369	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	319	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	304	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	354	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	344	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	389	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	312	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	647	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	348	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	665	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	322	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
```

[[Back]](./InterfacePhy.md)