# Node Protocol - IPv4

## Inst view

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --view dom

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol IPv4 - Domain (VRF) [#30]
----------------------------------

+---------------------+-------------------------------+--------+---------+--------+-------+---------+--------+-------+-----+------+------+
| Node                | VRF                           | Health | Faults  | OperSt | Route | Default | Direct | Local | BGP | iBGP | eBGP |
+---------------------+-------------------------------+--------+---------+--------+-------+---------+--------+-------+-----+------+------+
| pod-1/cl201-eu-spdc | black-hole                    | 100    | 0 0 0 0 | up     | 0     | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 100    | 0 0 0 0 | up     | 57    | True    | 0      | 11    | 35  | 35   | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 100    | 0 0 0 0 | up     | 104   | True    | 0      | 2     | 100 | 100  | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 100    | 0 0 0 0 | up     | 5     | True    | 0      | 2     | 1   | 1    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 100    | 0 0 0 0 | up     | 56    | True    | 7      | 12    | 37  | 7    | 30   | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | 100    | 0 0 0 0 | up     | 23    | False   | 7      | 11    | 8   | 3    | 5    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 100    | 0 0 0 0 | up     | 15    | True    | 3      | 6     | 5   | 5    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 100    | 0 0 0 0 | up     | 73    | True    | 7      | 12    | 51  | 7    | 44   | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | 100    | 0 0 0 0 | up     | 37    | False   | 10     | 16    | 14  | 4    | 10   | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 100    | 0 0 0 0 | up     | 8     | True    | 0      | 2     | 4   | 4    | 0    | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a-tenant_VRF      | 100    | 0 0 0 0 | up     | 0     | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a_VRF             | 100    | 0 0 0 0 | up     | 4     | False   | 0      | 2     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a-tenant_VRF      | 100    | 0 0 0 0 | up     | 0     | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a_VRF             | 100    | 0 0 0 0 | up     | 4     | False   | 0      | 2     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | 100    | 0 0 0 0 | up     | 9     | False   | 3      | 5     | 1   | 1    | 0    | 
| pod-1/cl201-eu-spdc | ECMP-demo:MPC-CDC-2_VRF       | 100    | 0 0 0 0 | up     | 2     | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | iks-monitoring:iks-mon_VRF    | 100    | 0 0 0 0 | up     | 0     | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | management                    | 100    | 0 0 0 0 | up     | 0     | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF       | 100    | 0 0 0 0 | up     | 2     | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | 100    | 0 0 0 0 | up     | 38    | True    | 0      | 2     | 35  | 35   | 0    | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 100    | 0 0 0 0 | up     | 18    | True    | 3      | 5     | 10  | 10   | 0    | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-IN_VRF             | 100    | 0 0 0 0 | up     | 2     | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 100    | 0 0 0 0 | up     | 7     | True    | 0      | 1     | 5   | 5    | 0    | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 100    | 0 0 0 0 | up     | 15    | True    | 3      | 5     | 4   | 3    | 1    | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 100    | 0 0 0 0 | up     | 25    | True    | 3      | 5     | 16  | 16   | 0    | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | 100    | 0 0 0 0 | up     | 4     | False   | 0      | 1     | 2   | 2    | 0    | 
| pod-1/cl201-eu-spdc | overlay-1                     | 100    | 0 0 0 0 | up     | 59    | False   | 6      | 7     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | P5G:P5G_VRF                   | 100    | 0 0 0 0 | up     | 0     | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 100    | 0 0 0 0 | up     | 40    | True    | 3      | 5     | 33  | 33   | 0    | 
| pod-1/cl201-eu-spdc | SPN_IntraLab:SPN_VRF1         | 100    | 0 0 0 0 | up     | 2     | False   | 0      | 1     | 0   | 0    | 0    | 
+---------------------+-------------------------------+--------+---------+--------+-------+---------+--------+-------+-----+------+------+
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --view dom

{
    "duration": 12473,
    "apic": {
        "read": true,
        "success": 33,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 32,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 10489,
        "total_time": 10891
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

True	402	-	connect apic11o.emea-sp.cisco.com:443
True	539	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	325	30	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4 query query-target=children&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Dom
True	313	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-black-hole query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	354	145	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	409	304	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	326	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	338	116	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N3-N4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	524	50	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N6_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	367	33	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	398	150	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N3-N4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	380	80	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N6_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	280	17	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	278	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a-tenant_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	279	8	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	279	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a-tenant_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	281	8	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	289	20	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:ACC-ext_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	286	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:MPC-CDC-2_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	301	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-iks-monitoring:iks-mon_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	299	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-management query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	276	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	312	77	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:inb query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	292	45	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	274	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	284	17	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	294	34	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	334	65	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	276	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-NXOS-HandOff_Test:default query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	346	156	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-overlay-1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	304	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-P5G:P5G_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	346	84	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-SPIN_InnoLab:SPIN_VRF1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	306	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolIpv4.md)