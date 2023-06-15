# Node Protocol - IPv4

## Show IPv4 route table summary for selected node

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --view summary

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| Node                | VRF                           | State | Routes | Default | Direct | Local | BGP | iBGP | eBGP |
+---------------------+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| pod-1/cl201-eu-spdc | black-hole                    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | up    | 57     | True    | 0      | 11    | 35  | 35   | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | up    | 30     | True    | 0      | 2     | 26  | 26   | 0    | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | up    | 5      | True    | 0      | 2     | 1   | 1    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | up    | 21     | True    | 7      | 12    | 7   | 7    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | up    | 15     | False   | 7      | 11    | 3   | 3    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | up    | 13     | True    | 3      | 6     | 5   | 5    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | up    | 21     | True    | 7      | 12    | 7   | 7    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | up    | 22     | False   | 10     | 16    | 4   | 4    | 0    | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | up    | 8      | True    | 0      | 2     | 4   | 4    | 0    | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a-tenant_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a_VRF             | up    | 4      | False   | 0      | 2     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a-tenant_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a_VRF             | up    | 4      | False   | 0      | 2     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | up    | 9      | False   | 3      | 5     | 1   | 1    | 0    | 
| pod-1/cl201-eu-spdc | ECMP-demo:MPC-CDC-2_VRF       | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | iks-monitoring:iks-mon_VRF    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | management                    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF       | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | up    | 38     | True    | 0      | 2     | 35  | 35   | 0    | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | up    | 16     | True    | 3      | 5     | 8   | 8    | 0    | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-IN_VRF             | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | up    | 7      | True    | 0      | 1     | 5   | 5    | 0    | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | up    | 14     | True    | 3      | 5     | 4   | 3    | 1    | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | up    | 18     | True    | 3      | 5     | 10  | 10   | 0    | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | up    | 4      | False   | 0      | 1     | 2   | 2    | 0    | 
| pod-1/cl201-eu-spdc | overlay-1                     | up    | 65     | False   | 6      | 7     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | P5G:P5G_VRF                   | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | up    | 39     | True    | 3      | 5     | 33  | 33   | 0    | 
| pod-1/cl201-eu-spdc | SPN_IntraLab:SPN_VRF1         | up    | 2      | False   | 0      | 1     | 0   | 0    | 0    | 
| pod-1/cl201-eu-spdc | TESTING_BRUNO:default         | up    | 3      | False   | 0      | 1     | 0   | 0    | 0    | 
+---------------------+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
```

Developer

```
# iserver get aci proto ipv4 --apic apic11 --node cl201-eu-spdc --view summary

{
    "duration": 12273,
    "apic": {
        "read": true,
        "success": 34,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 33,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 10793,
        "total_time": 11203
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

True	410	-	connect apic11o.emea-sp.cisco.com
True	314	13	apic11o.emea-sp.cisco.com class fabricNode
True	306	31	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4 query query-target=children&target-subtree-class=uribv4Dom
True	298	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-black-hole query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	347	175	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	322	82	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-SPIN_InnoLab:SPIN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	329	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a-tenant_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	334	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	330	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a-tenant_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	314	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-management query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	300	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	361	49	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N6_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	335	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	335	39	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	378	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-iks-monitoring:iks-mon_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	330	45	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	300	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:MPC-CDC-2_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	374	145	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	311	29	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	315	33	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N6_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	325	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	367	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	325	46	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N3-N4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	316	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	307	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	345	82	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	325	46	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N3-N4_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	342	32	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	309	77	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	314	20	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:ACC-ext_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	316	11	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	292	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-NXOS-HandOff_Test:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	364	6	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-TESTING_BRUNO:default query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	313	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv4/dom-P5G:P5G_VRF query query-target=subtree&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolIpv4.md)