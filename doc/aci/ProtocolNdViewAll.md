# Node Protocol - ND

## All view

```
# iserver get aci proto nd
    --apic apic11
    --node bl205-eu-spdc
    --view all
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

Protocol ND - Instance [#1]
---------------------------

+---------------------+--------+---------+-------------+----------------+----------------+------------------------+
| Node                | Health | Faults  | Admin State | Aging Interval | Neighbor Count | Active Interface Count |
+---------------------+--------+---------+-------------+----------------+----------------+------------------------+
| pod-1/bl205-eu-spdc | 100    | 0 0 0 0 | enabled     | 1380           | 0              | 0                      | 
+---------------------+--------+---------+-------------+----------------+----------------+------------------------+

Protocol ND - Domain [#25]
--------------------------

+-------------------------------+--------+---------+------------+-----------+
| VRF                           | Health | Faults  | Interfaces | Neighbors |
+-------------------------------+--------+---------+------------+-----------+
| common:Infra_BGP_VRF          | 100    | 0 0 0 0 | 6          | 0         | 
| common:Infra_privIP_VRF       | 100    | 0 0 0 0 | 2          | 0         | 
| common:Infra_VRF              | 100    | 0 0 0 0 | 1          | 0         | 
| common:smi5Gc-cvim1-N3-N4_VRF | 100    | 0 0 0 0 | 0          | 0         | 
| common:smi5Gc-cvim1_VRF       | 100    | 0 0 0 0 | 0          | 0         | 
| common:smi5Gc-cvim4-N3-N4_VRF | 100    | 0 0 0 0 | 0          | 0         | 
| common:smi5Gc-cvim4_VRF       | 100    | 0 0 0 0 | 0          | 0         | 
| ECMP-demo:ACC_VRF             | 100    | 0 0 0 0 | 0          | 0         | 
| ECMP-demo:INT-ext_VRF         | 100    | 0 0 0 0 | 1          | 0         | 
| ECMP-demo:MPC-CDC-2_VRF       | 100    | 0 0 0 0 | 1          | 0         | 
| iks-monitoring:iks-mon_VRF    | 100    | 0 0 0 0 | 1          | 0         | 
| management                    | 100    | 0 0 0 0 | 0          | 0         | 
| mgmt:EU-SPDC-ERSPAN-VRF       | 100    | 0 0 0 0 | 1          | 0         | 
| mgmt:inb                      | 100    | 0 0 0 0 | 1          | 0         | 
| MPC-E:CU-DU-Infra_VRF         | 100    | 0 0 0 0 | 1          | 0         | 
| MPC-E:MPC-E-sPBR-IN_VRF       | 100    | 0 0 0 0 | 5          | 0         | 
| MPC-F5T:F5-IN_VRF             | 100    | 0 0 0 0 | 1          | 0         | 
| MPC-F5T:F5-OUT_VRF            | 100    | 0 0 0 0 | 1          | 0         | 
| MPC:MPC-sPBR-IN_VRF           | 100    | 0 0 0 0 | 5          | 0         | 
| MPC:MPC-sPBR-OUT_VRF          | 100    | 0 0 0 0 | 0          | 0         | 
| NXOS-HandOff_Test:default     | 100    | 0 0 0 0 | 1          | 0         | 
| P5G:P5G_VRF                   | 100    | 0 0 0 0 | 1          | 0         | 
| SPIN_InnoLab:SPIN_VRF1        | 100    | 0 0 0 0 | 4          | 0         | 
| SPN_IntraLab:SPN_VRF1         | 100    | 0 0 0 0 | 1          | 0         | 
| UC3-CL2023-Demo:default       | 100    | 0 0 0 0 | 0          | 0         | 
+-------------------------------+--------+---------+------------+-----------+

Protocol ND - Neighbor [#0]
---------------------------
None

Protocol ND - Interface [#34]
-----------------------------

+---------------------+----------------------------+-----------+---------+-----+------+----------+---------+----------+------------+---------+-----------+------------+
| Node                | VRF                        | Interface | Admin   | Hop | MTU  | NS Intvl | NS Retr | RA Intvl | RA Min Int | RA Life | Reachable | Retransmit |
+---------------------+----------------------------+-----------+---------+-----+------+----------+---------+----------+------------+---------+-----------+------------+
| pod-1/bl205-eu-spdc | ECMP-demo:INT-ext_VRF      | vlan32    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | ECMP-demo:MPC-CDC-2_VRF    | vlan23    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC-E:CU-DU-Infra_VRF      | vlan19    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan1     | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan17    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan18    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan5     | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan90    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-IN_VRF          | vlan30    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF         | vlan33    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan67    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan75    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan79    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan81    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan83    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | NXOS-HandOff_Test:default  | vlan68    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | P5G:P5G_VRF                | vlan57    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1     | vlan11    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1     | vlan13    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1     | vlan15    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1     | vlan3     | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | SPN_IntraLab:SPN_VRF1      | vlan6     | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan21    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan22    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan25    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan29    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan37    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan40    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_VRF           | vlan61    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF    | vlan59    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF    | vlan70    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | iks-monitoring:iks-mon_VRF | vlan27    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF    | vlan35    | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
| pod-1/bl205-eu-spdc | mgmt:inb                   | vlan2     | enabled | 64  | 9000 | 1000     | 3       | 600      | 200        | 1800    | 0         | 0          | 
+---------------------+----------------------------+-----------+---------+-----+------+----------+---------+----------+------------+---------+-----------+------------+

Protocol ND - Interface Stats [#34]
-----------------------------------

+---------------------+----------------------------+-----------+---------+---------+---------+---------+---------+---------+---------+---------+
| Node                | VRF                        | Interface | NS Sent | NS Rcvd | NA Sent | NA Rcvd | RS Sent | RS Rcvd | RA Sent | RA Rcvd |
+---------------------+----------------------------+-----------+---------+---------+---------+---------+---------+---------+---------+---------+
| pod-1/bl205-eu-spdc | ECMP-demo:INT-ext_VRF      | vlan32    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | ECMP-demo:MPC-CDC-2_VRF    | vlan23    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC-E:CU-DU-Infra_VRF      | vlan19    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan1     | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan17    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan18    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan5     | 0       | 0       | 0       | 15      | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF    | vlan90    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-IN_VRF          | vlan30    | 0       | 0       | 0       | 15      | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF         | vlan33    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan67    | 0       | 0       | 0       | 85      | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan75    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan79    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan81    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF        | vlan83    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | NXOS-HandOff_Test:default  | vlan68    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | P5G:P5G_VRF                | vlan57    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1     | vlan11    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1     | vlan13    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1     | vlan15    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1     | vlan3     | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | SPN_IntraLab:SPN_VRF1      | vlan6     | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan21    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan22    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan25    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan29    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan37    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF       | vlan40    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_VRF           | vlan61    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF    | vlan59    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF    | vlan70    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | iks-monitoring:iks-mon_VRF | vlan27    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF    | vlan35    | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
| pod-1/bl205-eu-spdc | mgmt:inb                   | vlan2     | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 
+---------------------+----------------------------+-----------+---------+---------+---------+---------+---------+---------+---------+---------+

Protocol ND - Faults [#0]
-------------------------
None

Protocol ND - Fault Records [#0]
--------------------------------
None

Protocol ND - Event Logs [#0]
-----------------------------
None
```

Developer

```
# iserver get aci proto nd
    --apic apic11
    --node bl205-eu-spdc
    --view all
    --when 90d

{
    "duration": 3091,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 2435,
        "total_time": 2821
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

True	386	-	connect apic11o.emea-sp.cisco.com:443
True	298	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	284	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query query-target=children&rsp-subtree-include=health,fault-count
True	311	25	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/ndDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	287	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	295	34	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
True	283	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=faults,no-scoped,subtree
True	342	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	335	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolNd.md)