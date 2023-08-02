# Node Protocol - IPv4

## Filter by ip

```
# iserver get aci proto ipv4
    --apic apic11
    --node cl201-eu-spdc
    --address 15.100.100.254
    --view route

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol IPv4 - Route [#16]
---------------------------

+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| Node                | VRF                           | Prefix            | Health | Faults  | Next Hop          | Type   | Source    | Interface | NH VRF                   | MPLS Label | Active | Preference |
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | 15.100.100.0/24   | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:Infra_VRF              | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 15.100.100.0/24   | 100    | 0 0 0 0 | 10.3.40.64/32     | static | static    |           | overlay-1                | 0          | yes    | 1          | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | 15.100.100.254/32 | 100    | 0 0 0 0 | 15.100.100.254/32 | local  | local     | vlan276   | common:smi5Gc-cvim4_VRF  | 0          | yes    | 0          | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | mgmt:inb                      | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 0.0.0.0/0         | 100    | 0 0 0 0 | 15.3.9.254/32     | static | static    | vlan510   | MPC-E:MPC-E-sPBR-OUT_VRF | 0          | yes    | 1          | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 1          | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 1          | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 0.0.0.0/0         | 100    | 0 0 0 0 | 15.2.9.254/32     | ebgp   | bgp-50000 | vlan507   | MPC:MPC-sPBR-OUT_VRF     | 0          | yes    | 20         | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 0.0.0.0/0         | 100    | 0 0 0 0 | 15.2.9.254/32     | static | static    | vlan507   | MPC:MPC-sPBR-OUT_VRF     | 0          | yes    | 1          | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 0.0.0.0/0         | 100    | 0 0 0 0 | 10.3.32.64/32     | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
|                     |                               |                   |        |         | 10.3.192.64/32    | ibgp   | bgp-50000 |           | overlay-1                | 0          | yes    | 200        | 
+---------------------+-------------------------------+-------------------+--------+---------+-------------------+--------+-----------+-----------+--------------------------+------------+--------+------------+
```

Developer

```
# iserver get aci proto ipv4
    --apic apic11
    --node cl201-eu-spdc
    --address 15.100.100.254
    --view route

{
    "duration": 12199,
    "apic": {
        "read": true,
        "success": 33,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 32,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 10760,
        "total_time": 11154
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

True	394	-	connect apic11o.emea-sp.cisco.com:443
True	306	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	286	30	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4 query query-target=children&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Dom
True	286	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-black-hole query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	360	145	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_BGP_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	386	304	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_privIP_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	382	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:Infra_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	506	116	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N3-N4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	375	50	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1-N6_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	319	33	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim1_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	337	150	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N3-N4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	309	80	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4-N6_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	294	17	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-common:smi5Gc-cvim4_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	336	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a-tenant_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	299	8	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim1a:cvim1a_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	285	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a-tenant_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	312	8	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-cvim4a:cvim4a_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	323	20	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:ACC-ext_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	314	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-ECMP-demo:MPC-CDC-2_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	286	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-iks-monitoring:iks-mon_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	283	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-management query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	279	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:EU-SPDC-ERSPAN-VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	316	77	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-mgmt:inb query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	305	45	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-E:MPC-E-sPBR-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	299	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-IN_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	294	17	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC-F5T:F5-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	313	34	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-IN_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	383	65	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-MPC:MPC-sPBR-OUT_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	767	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-NXOS-HandOff_Test:default query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	345	156	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-overlay-1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	276	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-P5G:P5G_VRF query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	316	84	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-SPIN_InnoLab:SPIN_VRF1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
True	283	4	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4/dom-SPN_IntraLab:SPN_VRF1 query query-target=subtree&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Route&target-subtree-class=uribv4Nexthop
```

[[Back]](./ProtocolIpv4.md)