# Node Protocol - ARP

## Leaf nodes adjacencies

```
# iserver get aci proto arp --apic apic11 --role leaf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
| Node                | VRF                            | MAC               | IP              | State      | Interface  | Phy Interface | Timestamp                     |
+---------------------+--------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF           | 00:A3:8E:EB:B3:3F | 192.168.254.1   | normal     | eth1/24.62 | eth1/24       | 2023-05-30T18:20:51.579+02:00 | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.66  | normal     | eth1/24.36 | eth1/24       | 2023-05-30T18:08:08.346+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.98  | normal     | eth1/24.65 | eth1/24       | 2023-05-30T18:08:05.783+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.102 | normal     | eth1/24.60 | eth1/24       | 2023-05-30T18:08:05.673+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.90  | normal     | eth1/24.64 | eth1/24       | 2023-05-30T18:08:06.103+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.94  | normal     | eth1/24.66 | eth1/24       | 2023-05-30T18:08:05.725+02:00 | 
| pod-1/bl205-eu-spdc | mgmt:inb                       | 00:A3:8E:EB:B3:3F | 192.168.254.17  | normal     | eth1/24.67 | eth1/24       | 2023-05-30T18:08:06.156+02:00 | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF             | 00:50:56:B2:80:63 | 15.2.7.1        | normal     | vlan63     | tunnel2       | 2023-05-30T18:16:41.514+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:22:BD:CD:C2:BB | 15.2.7.252      | normal     | vlan61     | tunnel2       | 2023-05-30T18:14:54.885+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:0E:D8 | 15.2.7.5        | normal     | vlan61     | po5           | 2023-05-30T18:20:32.983+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:62:BB | 15.2.7.4        | normal     | vlan61     | po5           | 2023-05-30T18:21:04.495+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:77:0B | 15.2.7.3        | normal     | vlan61     | tunnel2       | 2023-05-30T18:20:07.840+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:7E:F3 | 15.2.7.2        | normal     | vlan61     | po5           | 2023-05-30T18:17:03.624+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:8F:CB | 15.2.7.6        | normal     | vlan61     | po5           | 2023-05-30T18:20:27.742+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:D5:AB | 15.2.7.1        | normal     | vlan61     | po5           | 2023-05-30T18:17:15.702+02:00 | 
| pod-1/bl205-eu-spdc | overlay-1                      | 00:8A:96:1C:7C:B4 | 15.16.2.1       | normal     | eth1/28    | eth1/28       | 2023-05-30T18:10:03.901+02:00 | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:A3:8E:EB:B3:3F | 192.168.254.41  | normal     | eth1/24.71 | eth1/24       | 2023-05-30T18:08:06.051+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:22:BD:F8:19:FF | 10.58.24.108    | normal     | vlan35     | tunnel2       | 2023-05-30T18:19:09.001+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.104    | normal     | vlan35     | tunnel2       | 2023-05-30T18:19:52.306+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.106    | normal     | vlan35     | tunnel2       | 2023-05-30T18:19:51.464+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.99     | normal     | vlan35     | po5           | 2023-05-30T18:21:11.420+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.103    | normal     | vlan35     | po5           | 2023-05-30T18:19:07.230+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.98     | normal     | vlan35     | tunnel2       | 2023-05-30T18:21:09.762+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:A9:62 | 10.58.24.97     | normal     | vlan35     | po5           | 2023-05-30T18:21:01.486+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E3:FD | 10.58.24.102    | normal     | vlan35     | po5           | 2023-05-30T18:20:57.389+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E7:5B | 10.58.24.105    | normal     | vlan35     | po5           | 2023-05-30T18:20:28.595+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:ED:D0 | 10.58.24.101    | normal     | vlan35     | po5           | 2023-05-30T18:20:25.981+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:A3:8E:EB:B3:3F | 192.168.254.105 | normal     | eth1/24.68 | eth1/24       | 2023-05-30T18:08:06.050+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_BGP_VRF           | 00:A3:8E:EB:B3:3F | 192.168.254.5   | normal     | eth1/24.47 | eth1/24       | 2023-05-30T18:20:51.449+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_privIP_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.70  | normal     | eth1/24.38 | eth1/24       | 2023-05-30T18:09:09.700+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.96  | normal     | eth1/24.43 | eth1/24       | 2023-05-30T18:09:09.643+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.100 | normal     | eth1/24.40 | eth1/24       | 2023-05-30T18:09:08.080+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.88  | normal     | eth1/24.44 | eth1/24       | 2023-05-30T18:09:07.893+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.92  | normal     | eth1/24.45 | eth1/24       | 2023-05-30T18:09:09.757+02:00 | 
| pod-1/bl206-eu-spdc | mgmt:inb                       | 00:A3:8E:EB:B3:3F | 192.168.254.21  | normal     | eth1/24.48 | eth1/24       | 2023-05-30T18:09:08.000+02:00 | 
| pod-1/bl206-eu-spdc | MPC-F5T:F5-OUT_VRF             | 00:50:56:B2:80:63 | 15.2.7.1        | normal     | vlan42     | po4           | 2023-05-30T18:17:59.056+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:22:BD:CD:C2:BB | 15.2.7.253      | normal     | vlan41     | tunnel2       | 2023-05-30T18:14:54.757+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:0E:D8 | 15.2.7.5        | normal     | vlan41     | tunnel2       | 2023-05-30T18:20:50.801+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:62:BB | 15.2.7.4        | normal     | vlan41     | tunnel2       | 2023-05-30T18:17:29.327+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:77:0B | 15.2.7.3        | normal     | vlan41     | po4           | 2023-05-30T18:17:01.835+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:7E:F3 | 15.2.7.2        | normal     | vlan41     | tunnel2       | 2023-05-30T18:19:32.487+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:8F:CB | 15.2.7.6        | normal     | vlan41     | tunnel2       | 2023-05-30T18:18:58.239+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:D5:AB | 15.2.7.1        | normal     | vlan41     | tunnel2       | 2023-05-30T18:19:29.818+02:00 | 
| pod-1/bl206-eu-spdc | overlay-1                      | 00:8A:96:1C:7C:B0 | 15.16.2.5       | normal     | eth1/28    | eth1/28       | 2023-05-30T18:15:26.511+02:00 | 
| pod-1/bl206-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:A3:8E:EB:B3:3F | 192.168.254.45  | normal     | eth1/24.49 | eth1/24       | 2023-05-30T18:09:07.943+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:22:BD:F8:19:FF | 10.58.24.109    | normal     | vlan39     | tunnel2       | 2023-05-30T18:19:08.872+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.104    | normal     | vlan39     | po4           | 2023-05-30T18:20:52.079+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.106    | normal     | vlan39     | po4           | 2023-05-30T18:21:15.302+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.99     | normal     | vlan39     | tunnel2       | 2023-05-30T18:21:11.289+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.103    | normal     | vlan39     | tunnel2       | 2023-05-30T18:19:20.413+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.98     | normal     | vlan39     | po4           | 2023-05-30T18:21:09.632+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:A9:62 | 10.58.24.97     | normal     | vlan39     | tunnel2       | 2023-05-30T18:06:07.743+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E3:FD | 10.58.24.102    | normal     | vlan39     | tunnel2       | 2023-05-30T18:20:45.482+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E7:5B | 10.58.24.105    | normal     | vlan39     | tunnel2       | 2023-05-30T18:20:39.729+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:ED:D0 | 10.58.24.101    | normal     | vlan39     | tunnel2       | 2023-05-30T18:21:13.466+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:A3:8E:EB:B3:3F | 192.168.254.107 | normal     | eth1/24.46 | eth1/24       | 2023-05-30T18:09:08.057+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:22:BD:F8:19:FF | 15.254.104.253  | normal     | vlan470    | tunnel7       | 2023-05-30T18:18:15.549+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:70:4D:85 | 15.100.7.101    | normal     | vlan468    | po16          | 2023-05-30T18:21:05.842+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:B6:A6:15 | 15.254.103.191  | normal     | vlan469    | eth1/12       | 2023-05-30T18:11:14.056+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:BC:A6:70 | 15.100.7.41     | normal     | vlan468    | po13          | 2023-05-30T18:13:51.435+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:C4:FE:86 | 15.254.103.192  | normal     | vlan469    | eth1/15       | 2023-05-30T18:21:19.632+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | unspecified       | 15.254.103.193  | incomplete | vlan469    |               | 2023-05-30T18:21:18.400+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.107.253  | normal     | vlan474    | tunnel7       | 2023-05-30T18:04:45.134+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.106.254  | normal     | vlan473    | tunnel7       | 2023-05-30T18:07:20.097+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | FA:16:3E:B6:A6:15 | 15.254.106.191  | normal     | vlan473    | eth1/12       | 2023-05-30T18:07:17.868+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | FA:16:3E:C4:FE:86 | 15.254.106.192  | normal     | vlan473    | eth1/15       | 2023-05-30T18:19:39.508+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | unspecified       | 15.254.106.195  | incomplete | vlan473    |               | 2023-05-30T18:21:02.312+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | unspecified       | 15.254.106.193  | incomplete | vlan473    |               | 2023-05-30T18:21:02.593+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF        | FA:16:3E:A8:F7:A2 | 15.100.4.220    | normal     | vlan457    | po27          | 2023-05-30T18:21:09.244+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF        | FA:16:3E:B0:E0:5D | 15.100.4.221    | normal     | vlan457    | po16          | 2023-05-30T18:20:52.390+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:22:BD:F8:19:FF | 15.254.134.253  | normal     | vlan463    | tunnel7       | 2023-05-30T18:03:34.054+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | FA:16:3E:12:76:80 | 15.100.103.101  | normal     | vlan472    | po26          | 2023-05-30T18:20:33.507+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.254.133.194  | incomplete | vlan462    |               | 2023-05-30T18:20:54.460+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.254.133.192  | incomplete | vlan462    |               | 2023-05-30T18:21:09.832+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.137.253  | normal     | vlan461    | tunnel7       | 2023-05-30T18:17:28.410+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.136.254  | normal     | vlan460    | tunnel7       | 2023-05-30T18:16:59.360+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.136.195  | incomplete | vlan460    |               | 2023-05-30T18:21:02.257+02:00 | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:A3:8E:EB:B3:3F | 15.3.9.254      | normal     | vlan471    | po2           | 2023-05-30T18:14:43.183+02:00 | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF            | 00:A3:8E:EB:B3:3F | 15.2.25.1       | normal     | vlan455    | po2           | 2023-05-30T18:14:42.689+02:00 | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:A3:8E:EB:B3:3F | 15.2.9.254      | normal     | vlan456    | po2           | 2023-05-30T18:14:42.613+02:00 | 
| pod-1/cl201-eu-spdc | overlay-1                      | 5C:71:0D:ED:E4:0B | 10.3.0.1        | normal     | vlan9      | eth1/91       | 2023-05-30T18:05:45.684+02:00 | 
| pod-1/cl201-eu-spdc | overlay-1                      | 5C:71:0D:EE:0C:4B | 10.3.0.2        | normal     | vlan9      | eth1/92       | 2023-05-30T18:09:17.656+02:00 | 
| pod-1/cl201-eu-spdc | overlay-1                      | 5C:71:0D:EE:99:03 | 10.3.0.3        | normal     | vlan9      | eth1/93       | 2023-05-30T18:08:04.612+02:00 | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:22:BD:F8:19:FF | 10.58.29.157    | normal     | vlan452    | tunnel7       | 2023-05-30T18:13:19.617+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:22:BD:F8:19:FF | 15.254.104.254  | normal     | vlan491    | tunnel7       | 2023-05-30T18:18:16.467+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:70:4D:85 | 15.100.7.101    | normal     | vlan492    | tunnel7       | 2023-05-30T18:03:30.426+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:72:79:10 | 15.254.104.191  | normal     | vlan491    | tunnel7       | 2023-05-30T18:07:06.693+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:BC:A6:70 | 15.100.7.41     | normal     | vlan492    | tunnel7       | 2023-05-30T18:13:52.353+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:CB:11:71 | 15.254.104.192  | normal     | vlan491    | tunnel7       | 2023-05-30T18:04:23.153+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | unspecified       | 15.254.104.193  | incomplete | vlan491    |               | 2023-05-30T18:21:14.373+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | unspecified       | 15.254.104.194  | incomplete | vlan491    |               | 2023-05-30T18:21:18.181+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.106.252  | normal     | vlan495    | tunnel7       | 2023-05-30T18:07:21.015+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.107.254  | normal     | vlan494    | tunnel7       | 2023-05-30T18:04:46.054+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | FA:16:3E:72:79:10 | 15.254.107.191  | normal     | vlan494    | tunnel7       | 2023-05-30T18:04:27.605+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | FA:16:3E:CB:11:71 | 15.254.107.192  | normal     | vlan494    | tunnel7       | 2023-05-30T18:06:41.917+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | unspecified       | 15.254.107.196  | incomplete | vlan494    |               | 2023-05-30T18:20:56.101+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | unspecified       | 15.254.107.194  | incomplete | vlan494    |               | 2023-05-30T18:21:00.633+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF        | FA:16:3E:A8:F7:A2 | 15.100.4.220    | normal     | vlan482    | tunnel7       | 2023-05-30T18:04:00.641+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF        | FA:16:3E:B0:E0:5D | 15.100.4.221    | normal     | vlan482    | tunnel7       | 2023-05-30T18:07:43.457+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:22:BD:F8:19:FF | 15.254.134.254  | normal     | vlan481    | tunnel7       | 2023-05-30T18:03:34.974+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | FA:16:3E:12:76:80 | 15.100.103.101  | normal     | vlan479    | tunnel7       | 2023-05-30T18:16:39.449+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.137.254  | normal     | vlan484    | tunnel7       | 2023-05-30T18:17:29.330+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.136.252  | normal     | vlan483    | tunnel7       | 2023-05-30T18:17:00.280+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.137.195  | incomplete | vlan484    |               | 2023-05-30T18:20:53.969+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.137.192  | incomplete | vlan484    |               | 2023-05-30T18:21:08.497+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.137.191  | incomplete | vlan484    |               | 2023-05-30T18:21:16.462+02:00 | 
| pod-1/cl202-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:A3:8E:EB:B3:3F | 15.3.9.254      | normal     | vlan487    | tunnel7       | 2023-05-30T18:14:43.835+02:00 | 
| pod-1/cl202-eu-spdc | MPC:MPC-sPBR-IN_VRF            | 00:A3:8E:EB:B3:3F | 15.2.25.1       | normal     | vlan476    | tunnel7       | 2023-05-30T18:14:43.302+02:00 | 
| pod-1/cl202-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:A3:8E:EB:B3:3F | 15.2.9.254      | normal     | vlan477    | tunnel7       | 2023-05-30T18:14:42.458+02:00 | 
| pod-1/cl202-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:22:BD:F8:19:FF | 10.58.29.156    | normal     | vlan475    | tunnel7       | 2023-05-30T18:13:20.535+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 00:50:56:B2:DE:E5 | 15.3.25.100     | normal     | vlan25     | po2           | 2023-05-30T18:17:02.630+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:7C:46 | 15.3.7.3        | normal     | vlan24     | po2           | 2023-05-30T18:18:00.861+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:89:29 | 15.3.7.1        | normal     | vlan24     | po2           | 2023-05-30T18:20:19.981+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:E0:7F | 15.3.7.2        | normal     | vlan24     | tunnel8       | 2023-05-30T18:21:18.512+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 00:50:56:B2:29:73 | 15.3.21.11      | normal     | vlan23     | tunnel8       | 2023-05-30T18:15:51.257+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:48 | 192.168.31.2    | normal     | eth1/36.6  | eth1/36       | 2023-05-30T18:19:34.997+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:74 | 15.16.3.1       | normal     | eth1/29    | eth1/29       | 2023-05-30T18:12:01.921+02:00 | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 00:22:BD:F8:19:FF | 10.58.26.93     | normal     | vlan22     | tunnel8       | 2023-05-30T18:13:22.038+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 00:50:56:B2:DE:E5 | 15.3.25.100     | normal     | vlan22     | tunnel8       | 2023-05-30T18:18:11.669+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:7C:46 | 15.3.7.3        | normal     | vlan23     | tunnel8       | 2023-05-30T18:18:44.171+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:89:29 | 15.3.7.1        | normal     | vlan23     | tunnel8       | 2023-05-30T18:17:19.757+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:E0:7F | 15.3.7.2        | normal     | vlan23     | po1           | 2023-05-30T18:16:56.667+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 00:50:56:B2:29:73 | 15.3.21.11      | normal     | vlan21     | po1           | 2023-05-30T18:05:47.959+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:4C | 192.168.32.2    | normal     | eth1/36.6  | eth1/36       | 2023-05-30T18:18:26.420+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:70 | 15.16.3.5       | normal     | eth1/29    | eth1/29       | 2023-05-30T18:14:44.167+02:00 | 
| pod-1/rl302-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 00:22:BD:F8:19:FF | 10.58.26.92     | normal     | vlan40     | tunnel8       | 2023-05-30T18:13:21.862+02:00 | 
+---------------------+--------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --role leaf

{
    "duration": 4691,
    "apic": {
        "read": true,
        "success": 14,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 13,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 3961,
        "total_time": 4351
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

True	390	-	connect apic11o.emea-sp.cisco.com
True	283	11	apic11o.emea-sp.cisco.com class fabricNode
True	284	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	297	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	285	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/arpDom
True	460	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	301	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/arpDom
True	301	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	302	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/arpDom
True	280	26	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	275	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/arpDom
True	282	8	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	274	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/arpDom
True	337	8	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)