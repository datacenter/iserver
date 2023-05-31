# Node Interface - Physical

## Filter by deployed EPG name

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --epg *SPIN-CSR*

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason    | Type | Layer    | PC  | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
| pod-1/bl205-eu-spdc | 1/1       | up    | enabled   | up   | connected | leaf | switched | po5 | 4C:71:0D:7E:83:F1 | trunk | 40G   | full   | 9000 | disable-fec | 
| pod-1/bl205-eu-spdc | 1/2       | up    | enabled   | up   | connected | leaf | switched | po3 | 4C:71:0D:7E:83:F2 | trunk | 40G   | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-----------+------+----------+-----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --epg *SPIN-CSR*

{
    "duration": 17091,
    "apic": {
        "read": true,
        "success": 42,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 41,
        "connect_time": 487,
        "disconnect_time": 0,
        "mo_time": 15878,
        "total_time": 16365
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

True	487	-	connect apic11o.emea-sp.cisco.com
True	338	11	apic11o.emea-sp.cisco.com class fabricNode
True	490	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	418	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	494	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/33] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	372	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/34] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	380	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/35] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	372	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/36] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	371	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/1] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	685	245	apic11o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	333	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/vlanCktEp
True	415	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/2] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/3] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	382	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/4] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	397	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/5] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	370	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/6] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/7] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	363	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/8] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	408	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/9] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	372	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/10] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	386	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/11] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	367	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/12] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/13] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/14] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	476	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/15] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	448	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/16] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	352	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/17] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	376	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/18] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/19] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	381	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/20] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/21] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	377	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/22] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	327	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/23] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	334	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/24] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	443	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/25] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	392	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/26] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	350	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/27] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	410	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	356	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/29] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	360	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/30] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	339	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/31] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
True	397	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/32] query rsp-subtree-include=full-deployment&target-node=all&target-path=l1EthIfToEPg
```

[[Back]](./InterfacePhy.md)