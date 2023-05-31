# Node Protocol - IPv6

## Show IPv6 route table summary for selected node

```
# iserver get aci proto ipv6 --apic apic11 --node cl201-eu-spdc --view summary

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| VRF                           | State | Routes | Default | Direct | Local | BGP | iBGP | eBGP |
+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
| black-hole                    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_BGP_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_privIP_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:Infra_VRF              | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim1-N3-N4_VRF | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim1-N6_VRF    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim1_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim4-N3-N4_VRF | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim4-N6_VRF    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| common:smi5Gc-cvim4_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| cvim1a:cvim1a-tenant_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| cvim1a:cvim1a_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| cvim4a:cvim4a-tenant_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| cvim4a:cvim4a_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:ACC-ext_VRF         | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| ECMP-demo:MPC-CDC-2_VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| iks-monitoring:iks-mon_VRF    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| management                    | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:EU-SPDC-ERSPAN-VRF       | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| mgmt:inb                      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-E:MPC-E-sPBR-OUT_VRF      | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-IN_VRF             | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC-F5T:F5-OUT_VRF            | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC:MPC-sPBR-IN_VRF           | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| MPC:MPC-sPBR-OUT_VRF          | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| NXOS-HandOff_Test:default     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| overlay-1                     | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| P5G:P5G_VRF                   | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPIN_InnoLab:SPIN_VRF1        | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| SPN_IntraLab:SPN_VRF1         | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
| TESTING_BRUNO:default         | up    | 0      | False   | 0      | 0     | 0   | 0    | 0    | 
+-------------------------------+-------+--------+---------+--------+-------+-----+------+------+
```

Developer

```
# iserver get aci proto ipv6 --apic apic11 --node cl201-eu-spdc --view summary

{
    "duration": 13485,
    "apic": {
        "read": true,
        "success": 34,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 33,
        "connect_time": 434,
        "disconnect_time": 0,
        "mo_time": 12396,
        "total_time": 12830
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

True	434	-	connect apic11o.emea-sp.cisco.com
True	294	11	apic11o.emea-sp.cisco.com class fabricNode
True	318	31	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6 query query-target=children&target-subtree-class=uribv6Dom
True	290	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-black-hole query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	290	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-overlay-1 query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	317	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-SPIN_InnoLab:SPIN_VRF1 query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	306	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-TESTING_BRUNO:default query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	393	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	383	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-cvim1a:cvim1a-tenant_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	341	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-cvim4a:cvim4a-tenant_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	381	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim4-N6_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	412	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim1-N6_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	464	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-management query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	424	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim1_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	425	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-ECMP-demo:ACC-ext_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	352	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim1-N3-N4_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	331	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	337	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:Infra_BGP_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	300	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-cvim4a:cvim4a_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	326	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-cvim1a:cvim1a_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	372	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim4-N3-N4_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	441	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	393	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-MPC:MPC-sPBR-OUT_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	380	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	582	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:smi5Gc-cvim4_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	527	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-ECMP-demo:MPC-CDC-2_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	428	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:Infra_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	357	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-common:Infra_privIP_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	417	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-iks-monitoring:iks-mon_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	402	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-P5G:P5G_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	350	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	400	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	335	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-mgmt:inb query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
True	328	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/uribv6/dom-NXOS-HandOff_Test:default query query-target=subtree&target-subtree-class=uribv6Route&target-subtree-class=uribv6Nexthop
```

[[Back]](./ProtocolIpv6.md)