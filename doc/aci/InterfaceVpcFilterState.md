# Node Interface - Virtual Port Channel (VPC)

## Filter by peer state

```
# iserver get aci intf vpc --apic apic21 --node any --state up

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

Interface Virtual Port Channel - State [#10]
--------------------------------------------

+----------------------+--------+---------+--------+-----------+------------------------+---------------------------------+------------+--------------+---------------+----------------+
| Node                 | Health | Faults  | Domain | LACP Role | Oper Role              | Oper State                      | Peer State | Constistency | Local Members | Remote Members |
+----------------------+--------+---------+--------+-----------+------------------------+---------------------------------+------------+--------------+---------------+----------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | 256    | master    | cfg-master-oper-slave  | configured-master,vpcs-reinited | up         | pass         | 6/6           | 6/6            | 
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | 256    | slave     | cfg-slave-oper-master  | sticky-master,vpcs-reinited     | up         | pass         | 6/6           | 6/6            | 
| pod-1/cl2201-eu-spdc | 20     | 0 1 0 0 | 212    | master    | cfg-master-oper-slave  | configured-master,vpcs-reinited | up         | pass         | 1/2           | 1/2            | 
| pod-1/cl2202-eu-spdc | 20     | 0 1 0 0 | 212    | slave     | cfg-slave-oper-master  | sticky-master,vpcs-reinited     | up         | pass         | 1/2           | 1/2            | 
| pod-1/cl2207-eu-spdc | 37     | 0 2 0 0 | 278    | slave     | cfg-master-oper-slave  | configured-master,vpcs-reinited | up         | pass         | 6/8           | 6/8            | 
| pod-1/cl2208-eu-spdc | 37     | 0 2 0 0 | 278    | master    | cfg-slave-oper-master  | sticky-master,vpcs-reinited     | up         | pass         | 6/8           | 6/8            | 
| pod-1/cl2209-eu-spdc | 100    | 0 0 0 0 | 291    | slave     | cfg-master-oper-master | configured-master,vpcs-reinited | up         | pass         | 0/0           | 0/0            | 
| pod-1/cl2210-eu-spdc | 100    | 0 0 0 0 | 291    | master    | cfg-slave-oper-slave   | vpcs-reinited                   | up         | pass         | 0/0           | 0/0            | 
| pod-1/rl2701-eu-spdc | 100    | 0 0 0 0 | 227    | master    | cfg-master-oper-slave  | configured-master,vpcs-reinited | up         | pass         | 2/2           | 2/2            | 
| pod-1/rl2702-eu-spdc | 100    | 0 0 0 0 | 227    | slave     | cfg-slave-oper-master  | sticky-master,vpcs-reinited     | up         | pass         | 2/2           | 2/2            | 
+----------------------+--------+---------+--------+-----------+------------------------+---------------------------------+------------+--------------+---------------+----------------+
```

Developer

```
# iserver get aci intf vpc --apic apic21 --node any --state up

{
    "duration": 8943,
    "apic": {
        "read": true,
        "success": 28,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 27,
        "connect_time": 363,
        "disconnect_time": 0,
        "mo_time": 8050,
        "total_time": 8413
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

True	363	-	connect apic21o.emea-sp.cisco.com:443
True	279	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	255	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	425	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	263	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	271	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	453	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	265	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/vlanCktEp
True	266	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	301	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	268	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/vlanCktEp
True	278	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	296	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	260	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/vlanCktEp
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	457	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	266	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/vlanCktEp
True	265	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	428	8	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	282	17	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/vlanCktEp
True	270	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	257	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	266	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	305	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	264	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	297	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	269	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	271	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
```

[[Back]](./InterfaceVpc.md)