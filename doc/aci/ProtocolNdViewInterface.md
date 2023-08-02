# Node Protocol - ND

## Intf view

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

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
```

Developer

```
# iserver get aci proto nd --apic apic11 --node bl205-eu-spdc --view intf

{
    "duration": 2291,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 403,
        "disconnect_time": 0,
        "mo_time": 1531,
        "total_time": 1934
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

True	403	-	connect apic11o.emea-sp.cisco.com:443
True	297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	300	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd query query-target=children&rsp-subtree-include=health,fault-count
True	312	25	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/ndDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	272	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/nd/inst query query-target=subtree&target-subtree-class=ndAdjEp
True	350	34	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-205/ndIf query rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolNd.md)