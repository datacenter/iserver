# Node Protocol - ARP

## Verbose output

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------------------------+-----------+
| Node                | VRF                           | Adjacency |
+---------------------+-------------------------------+-----------+
| pod-1/bl205-eu-spdc | black-hole                    | 0         | 
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF          | 1         | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF       | 1         | 
| pod-1/bl205-eu-spdc | common:Infra_VRF              | 0         | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 1         | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1_VRF       | 1         | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 1         | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4_VRF       | 1         | 
| pod-1/bl205-eu-spdc | ECMP-demo:ACC_VRF             | 0         | 
| pod-1/bl205-eu-spdc | ECMP-demo:INT-ext_VRF         | 0         | 
| pod-1/bl205-eu-spdc | ECMP-demo:MPC-CDC-2_VRF       | 0         | 
| pod-1/bl205-eu-spdc | iks-monitoring:iks-mon_VRF    | 0         | 
| pod-1/bl205-eu-spdc | management                    | 0         | 
| pod-1/bl205-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF       | 0         | 
| pod-1/bl205-eu-spdc | mgmt:inb                      | 1         | 
| pod-1/bl205-eu-spdc | MPC-E:CU-DU-Infra_VRF         | 0         | 
| pod-1/bl205-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF       | 0         | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-IN_VRF             | 0         | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF            | 0         | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 0         | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 2         | 
| pod-1/bl205-eu-spdc | NXOS-HandOff_Test:default     | 0         | 
| pod-1/bl205-eu-spdc | overlay-1                     | 1         | 
| pod-1/bl205-eu-spdc | P5G:P5G_VRF                   | 0         | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 1         | 
| pod-1/bl205-eu-spdc | SPN_IntraLab:SPN_VRF1         | 0         | 
| pod-1/bl205-eu-spdc | TESTING_BRUNO:default         | 0         | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 1         | 
+---------------------+-------------------------------+-----------+

+---------------------+------------+-----------+
| Node                | Interface  | Adjacency |
+---------------------+------------+-----------+
| pod-1/bl205-eu-spdc | eth1/24.46 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.47 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.48 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.50 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.51 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.52 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.53 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.54 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.55 | 1         | 
| pod-1/bl205-eu-spdc | eth1/28    | 1         | 
| pod-1/bl205-eu-spdc | vlan67     | 2         | 
+---------------------+------------+-----------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc --view verbose

{
    "duration": 1639,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 437,
        "disconnect_time": 0,
        "mo_time": 954,
        "total_time": 1391
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

True	437	-	connect apic11o.emea-sp.cisco.com
True	350	13	apic11o.emea-sp.cisco.com class fabricNode
True	309	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	295	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)