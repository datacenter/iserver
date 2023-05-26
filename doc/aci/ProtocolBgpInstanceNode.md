# Node Protocol - BGP

## Show BGP VRF domains for selected node

```
# iserver get aci proto bgp --apic apic11 --node cl201-eu-spdc -o vrf

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: cl201-eu-spdc

+---------------------+-------------------------------+-----------+--------+-----------------+------------------------+-----------+-------------+
| Node                | VRF                           | BGP State | Mode   | Router ID       | RD                     | Neighbors | Established |
+---------------------+-------------------------------+-----------+--------+-----------------+------------------------+-----------+-------------+
| pod-1/cl201-eu-spdc | common:Infra_BGP_VRF          | up        | fabric | 10.58.24.158    | rd:as2-nn4:201:2424848 | 0         | 0           | 
| pod-1/cl201-eu-spdc | common:Infra_privIP_VRF       | up        | fabric | 15.100.161.126  | rd:as2-nn4:201:2097161 | 0         | 0           | 
| pod-1/cl201-eu-spdc | common:Infra_VRF              | up        | fabric | 15.254.254.254  | rd:as2-nn4:201:2686976 | 0         | 0           | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | up        | fabric | 201.201.201.201 | rd:as2-nn4:201:2261001 | 8         | 4           | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | up        | fabric | 201.201.201.201 | rd:as2-nn4:201:2392070 | 6         | 2           | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF       | up        | fabric | 201.201.201.201 | rd:as2-nn4:201:2883586 | 3         | 0           | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | up        | fabric | 201.201.201.201 | rd:as2-nn4:201:2523141 | 8         | 1           | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | up        | fabric | 201.201.201.201 | rd:as2-nn4:201:2850822 | 6         | 0           | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4_VRF       | up        | fabric | 15.100.100.254  | rd:as2-nn4:201:2621441 | 0         | 0           | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a-tenant_VRF      | up        | fabric | 0.0.0.0         | rd:as2-nn4:201:2129925 | 0         | 0           | 
| pod-1/cl201-eu-spdc | cvim1a:cvim1a_VRF             | up        | fabric | 192.168.151.254 | rd:as2-nn4:201:2818052 | 0         | 0           | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a-tenant_VRF      | up        | fabric | 0.0.0.0         | rd:as2-nn4:201:3047432 | 0         | 0           | 
| pod-1/cl201-eu-spdc | cvim4a:cvim4a_VRF             | up        | fabric | 192.168.152.254 | rd:as2-nn4:201:2228224 | 0         | 0           | 
| pod-1/cl201-eu-spdc | ECMP-demo:ACC-ext_VRF         | up        | fabric | 121.121.121.121 | rd:as2-nn4:201:3047433 | 0         | 0           | 
| pod-1/cl201-eu-spdc | ECMP-demo:MPC-CDC-2_VRF       | up        | fabric | 15.2.203.254    | rd:as2-nn4:201:3047429 | 0         | 0           | 
| pod-1/cl201-eu-spdc | iks-monitoring:iks-mon_VRF    | up        | fabric | 0.0.0.0         | rd:as2-nn4:201:2228231 | 0         | 0           | 
| pod-1/cl201-eu-spdc | management                    | up        | fabric | 0.0.0.0         | rd:as2-nn4:201:2752512 | 0         | 0           | 
| pod-1/cl201-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF       | up        | fabric | 99.99.99.254    | rd:as2-nn4:201:2555904 | 0         | 0           | 
| pod-1/cl201-eu-spdc | mgmt:inb                      | up        | fabric | 10.58.28.190    | rd:as2-nn4:201:2818048 | 0         | 0           | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | up        | fabric | 121.121.121.121 | rd:as2-nn4:201:2981888 | 0         | 0           | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-IN_VRF             | up        | fabric | 15.2.64.254     | rd:as2-nn4:201:2162693 | 0         | 0           | 
| pod-1/cl201-eu-spdc | MPC-F5T:F5-OUT_VRF            | up        | fabric | 15.2.10.254     | rd:as2-nn4:201:2523139 | 0         | 0           | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF           | up        | fabric | 201.201.201.201 | rd:as2-nn4:201:2490372 | 0         | 0           | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | up        | fabric | 201.201.201.201 | rd:as2-nn4:201:2097154 | 0         | 0           | 
| pod-1/cl201-eu-spdc | NXOS-HandOff_Test:default     | up        | fabric | 192.168.1.1     | rd:as2-nn4:201:2129927 | 0         | 0           | 
| pod-1/cl201-eu-spdc | overlay-1                     | up        | fabric | 10.3.192.67     | unknown:unknown:0:0    | 2         | 2           | 
| pod-1/cl201-eu-spdc | P5G:P5G_VRF                   | up        | fabric | 0.0.0.0         | rd:as2-nn4:201:2883584 | 0         | 0           | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | up        | fabric | 1.1.1.1         | rd:as2-nn4:201:2195458 | 0         | 0           | 
| pod-1/cl201-eu-spdc | SPN_IntraLab:SPN_VRF1         | up        | fabric | 192.168.0.254   | rd:as2-nn4:201:2883591 | 0         | 0           | 
| pod-1/cl201-eu-spdc | TESTING_BRUNO:default         | up        | fabric | 192.168.1.1     | rd:as2-nn4:201:2457600 | 0         | 0           | 
+---------------------+-------------------------------+-----------+--------+-----------------+------------------------+-----------+-------------+
```

[[Back]](./ProtocolBgp.md)