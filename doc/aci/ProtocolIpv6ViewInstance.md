# Node Protocol - IPv4

## Inst view

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --view inst

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol IPv4 - Instance [#1]
-----------------------------

+---------------------+-------------+--------+---------+--------+-------+---------+--------+-------+-----+------+------+
| Node                | Admin State | Health | Faults  | Domain | Route | Default | Direct | Local | BGP | iBGP | eBGP |
+---------------------+-------------+--------+---------+--------+-------+---------+--------+-------+-----+------+------+
| pod-1/cl201-eu-spdc | enabled     | 100    | 0 0 0 0 | 30     | 609   | True    | 55     | 118   | 361 | 271  | 90   | 
+---------------------+-------------+--------+---------+--------+-------+---------+--------+-------+-----+------+------+
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --view inst

{
    "duration": 12062,
    "apic": {
        "read": true,
        "success": 34,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 33,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 10265,
        "total_time": 10677
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

True	412	-	connect apic11o.emea-sp.cisco.com:443
True	310	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	287	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/ipv4 query query-target=children&rsp-subtree-include=health,fault-count
True	319	30	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4 query query-target=children&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Dom
True	296	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-black-hole query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	370	145	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	401	304	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	286	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	329	116	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N3-N4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	298	50	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N6_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	290	33	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	333	150	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N3-N4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	313	80	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N6_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	326	17	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	287	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a-tenant_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	290	8	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	287	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a-tenant_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	302	8	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	303	20	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:ACC-ext_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	287	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:MPC-CDC-2_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	289	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-iks-monitoring:iks-mon_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	288	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-management query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	305	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	319	77	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:inb query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	296	45	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	277	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	311	17	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	339	34	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	343	65	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	327	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-NXOS-HandOff_Test:default query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	353	156	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-overlay-1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	292	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-P5G:P5G_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	321	84	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-SPIN_InnoLab:SPIN_VRF1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	291	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolIpv4.md)