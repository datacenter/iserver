# Node Interface - Virtual Port Channel (VPC)

## Filter by domain id

```
# iserver get aci intf vpc --apic apic21 --node any --id 256

Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

Interface Virtual Port Channel - State [#2]
-------------------------------------------

+----------------------+--------+---------+--------+-----------+-----------------------+---------------------------------+------------+--------------+---------------+----------------+
| Node                 | Health | Faults  | Domain | LACP Role | Oper Role             | Oper State                      | Peer State | Constistency | Local Members | Remote Members |
+----------------------+--------+---------+--------+-----------+-----------------------+---------------------------------+------------+--------------+---------------+----------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 256    | master    | cfg-master-oper-slave | configured-master,vpcs-reinited | up         | pass         | 6/6           | 6/6            | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | 256    | slave     | cfg-slave-oper-master | sticky-master,vpcs-reinited     | up         | pass         | 6/6           | 6/6            | 
+----------------------+--------+---------+--------+-----------+-----------------------+---------------------------------+------------+--------------+---------------+----------------+
```

Developer

```
# iserver get aci intf vpc --apic apic21 --node any --id 256

{
    "duration": 5644,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 359,
        "disconnect_time": 0,
        "mo_time": 4941,
        "total_time": 5300
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

True	359	-	connect apic21o.emea-sp.cisco.com:443
True	279	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	271	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	402	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	262	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	272	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	460	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	258	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	266	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	276	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	278	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	272	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	276	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	257	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	263	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	305	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	271	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceVpc.md)