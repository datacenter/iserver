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
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF           | 00:A3:8E:EB:B3:3F | 192.168.254.1   | normal     | eth1/24.62 | eth1/24       | 2023-05-24T11:01:02.001+02:00 | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.66  | normal     | eth1/24.36 | eth1/24       | 2023-05-24T10:53:02.380+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.98  | normal     | eth1/24.65 | eth1/24       | 2023-05-24T10:52:59.780+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.102 | normal     | eth1/24.60 | eth1/24       | 2023-05-24T10:52:59.677+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.90  | normal     | eth1/24.64 | eth1/24       | 2023-05-24T10:53:00.330+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.94  | normal     | eth1/24.66 | eth1/24       | 2023-05-24T10:52:59.734+02:00 | 
| pod-1/bl205-eu-spdc | mgmt:inb                       | 00:A3:8E:EB:B3:3F | 192.168.254.17  | normal     | eth1/24.67 | eth1/24       | 2023-05-24T10:53:00.387+02:00 | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF             | 00:50:56:B2:80:63 | 15.2.7.1        | normal     | vlan63     | tunnel2       | 2023-05-24T11:06:53.392+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:22:BD:CD:C2:BB | 15.2.7.252      | normal     | vlan61     | tunnel2       | 2023-05-24T11:07:22.060+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:0E:D8 | 15.2.7.5        | normal     | vlan61     | po5           | 2023-05-24T11:07:33.075+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:62:BB | 15.2.7.4        | normal     | vlan61     | po5           | 2023-05-24T11:07:04.839+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:77:0B | 15.2.7.3        | normal     | vlan61     | tunnel2       | 2023-05-24T11:08:30.733+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:7E:F3 | 15.2.7.2        | normal     | vlan61     | po5           | 2023-05-24T11:04:36.971+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:8F:CB | 15.2.7.6        | normal     | vlan61     | po5           | 2023-05-24T11:08:50.366+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:D5:AB | 15.2.7.1        | normal     | vlan61     | po5           | 2023-05-24T11:04:48.961+02:00 | 
| pod-1/bl205-eu-spdc | overlay-1                      | 00:8A:96:1C:7C:B4 | 15.16.2.1       | normal     | eth1/28    | eth1/28       | 2023-05-24T11:05:31.667+02:00 | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:A3:8E:EB:B3:3F | 192.168.254.41  | normal     | eth1/24.71 | eth1/24       | 2023-05-24T10:53:00.274+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:22:BD:F8:19:FF | 10.58.24.108    | normal     | vlan35     | tunnel2       | 2023-05-24T10:51:13.840+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.104    | normal     | vlan35     | tunnel2       | 2023-05-24T11:08:46.896+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.99     | normal     | vlan35     | po5           | 2023-05-24T11:08:24.036+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.106    | normal     | vlan35     | tunnel2       | 2023-05-24T11:08:25.488+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.103    | normal     | vlan35     | po5           | 2023-05-24T11:08:25.567+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.98     | normal     | vlan35     | tunnel2       | 2023-05-24T11:08:48.915+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:A9:62 | 10.58.24.97     | normal     | vlan35     | po5           | 2023-05-24T11:08:33.320+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E3:FD | 10.58.24.102    | normal     | vlan35     | po5           | 2023-05-24T11:08:25.126+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E7:5B | 10.58.24.105    | normal     | vlan35     | po5           | 2023-05-24T11:09:02.373+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:ED:D0 | 10.58.24.101    | normal     | vlan35     | po5           | 2023-05-24T11:06:51.262+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default        | 00:A3:8E:EB:B3:3F | 192.168.254.105 | normal     | eth1/24.68 | eth1/24       | 2023-05-24T10:53:00.217+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_BGP_VRF           | 00:A3:8E:EB:B3:3F | 192.168.254.5   | normal     | eth1/24.47 | eth1/24       | 2023-05-24T11:01:01.871+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_privIP_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.70  | normal     | eth1/24.38 | eth1/24       | 2023-05-24T10:54:03.744+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.96  | normal     | eth1/24.43 | eth1/24       | 2023-05-24T10:54:03.695+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.100 | normal     | eth1/24.40 | eth1/24       | 2023-05-24T10:54:02.027+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.88  | normal     | eth1/24.44 | eth1/24       | 2023-05-24T10:54:01.930+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.92  | normal     | eth1/24.45 | eth1/24       | 2023-05-24T10:54:03.797+02:00 | 
| pod-1/bl206-eu-spdc | mgmt:inb                       | 00:A3:8E:EB:B3:3F | 192.168.254.21  | normal     | eth1/24.48 | eth1/24       | 2023-05-24T10:54:01.987+02:00 | 
| pod-1/bl206-eu-spdc | MPC-F5T:F5-OUT_VRF             | 00:50:56:B2:80:63 | 15.2.7.1        | normal     | vlan42     | po4           | 2023-05-24T11:04:54.036+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:22:BD:CD:C2:BB | 15.2.7.253      | normal     | vlan41     | tunnel2       | 2023-05-24T11:07:21.929+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:0E:D8 | 15.2.7.5        | normal     | vlan41     | tunnel2       | 2023-05-24T11:08:02.118+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:62:BB | 15.2.7.4        | normal     | vlan41     | tunnel2       | 2023-05-24T11:05:38.292+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:77:0B | 15.2.7.3        | normal     | vlan41     | po4           | 2023-05-24T11:06:34.747+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:7E:F3 | 15.2.7.2        | normal     | vlan41     | tunnel2       | 2023-05-24T11:06:35.007+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:8F:CB | 15.2.7.6        | normal     | vlan41     | tunnel2       | 2023-05-24T11:07:01.055+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:D5:AB | 15.2.7.1        | normal     | vlan41     | tunnel2       | 2023-05-24T11:07:40.629+02:00 | 
| pod-1/bl206-eu-spdc | overlay-1                      | 00:8A:96:1C:7C:B0 | 15.16.2.5       | normal     | eth1/28    | eth1/28       | 2023-05-24T10:51:55.791+02:00 | 
| pod-1/bl206-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:A3:8E:EB:B3:3F | 192.168.254.45  | normal     | eth1/24.49 | eth1/24       | 2023-05-24T10:54:01.940+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:22:BD:F8:19:FF | 10.58.24.109    | normal     | vlan39     | tunnel2       | 2023-05-24T10:51:13.708+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.104    | normal     | vlan39     | po4           | 2023-05-24T11:09:13.390+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.99     | normal     | vlan39     | tunnel2       | 2023-05-24T11:08:23.906+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.106    | normal     | vlan39     | po4           | 2023-05-24T11:08:23.310+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.103    | normal     | vlan39     | tunnel2       | 2023-05-24T11:09:11.005+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.98     | normal     | vlan39     | po4           | 2023-05-24T11:08:48.785+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:A9:62 | 10.58.24.97     | normal     | vlan39     | tunnel2       | 2023-05-24T11:03:49.683+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E3:FD | 10.58.24.102    | normal     | vlan39     | tunnel2       | 2023-05-24T11:07:03.589+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E7:5B | 10.58.24.105    | normal     | vlan39     | tunnel2       | 2023-05-24T11:08:41.763+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:ED:D0 | 10.58.24.101    | normal     | vlan39     | tunnel2       | 2023-05-24T11:08:34.557+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:A3:8E:EB:B3:3F | 192.168.254.107 | normal     | eth1/24.46 | eth1/24       | 2023-05-24T10:54:02.010+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:22:BD:F8:19:FF | 15.254.104.253  | normal     | vlan470    | tunnel7       | 2023-05-24T10:53:58.894+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:70:4D:85 | 15.100.7.101    | normal     | vlan468    | po16          | 2023-05-24T11:08:41.010+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:B6:A6:15 | 15.254.103.191  | normal     | vlan469    | eth1/12       | 2023-05-24T11:07:09.460+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:BC:A6:70 | 15.100.7.41     | normal     | vlan468    | po13          | 2023-05-24T11:07:03.243+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:C4:FE:86 | 15.254.103.192  | normal     | vlan469    | eth1/15       | 2023-05-24T10:58:25.056+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | unspecified       | 15.254.103.193  | incomplete | vlan469    |               | 2023-05-24T11:08:46.764+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | unspecified       | 15.254.103.195  | incomplete | vlan469    |               | 2023-05-24T11:08:59.956+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | unspecified       | 15.254.103.196  | incomplete | vlan469    |               | 2023-05-24T11:09:01.508+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.107.253  | normal     | vlan474    | tunnel7       | 2023-05-24T10:55:59.954+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.106.254  | normal     | vlan473    | tunnel7       | 2023-05-24T10:59:08.657+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | FA:16:3E:B6:A6:15 | 15.254.106.191  | normal     | vlan473    | eth1/12       | 2023-05-24T11:04:35.520+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | FA:16:3E:C4:FE:86 | 15.254.106.192  | normal     | vlan473    | eth1/15       | 2023-05-24T10:53:19.300+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | unspecified       | 15.254.106.194  | incomplete | vlan473    |               | 2023-05-24T11:08:52.413+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | unspecified       | 15.254.106.196  | incomplete | vlan473    |               | 2023-05-24T11:08:58.604+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF        | FA:16:3E:A8:F7:A2 | 15.100.4.220    | normal     | vlan457    | po27          | 2023-05-24T11:08:35.451+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1_VRF        | FA:16:3E:B0:E0:5D | 15.100.4.221    | normal     | vlan457    | po16          | 2023-05-24T11:08:51.618+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:22:BD:F8:19:FF | 15.254.134.253  | normal     | vlan463    | tunnel7       | 2023-05-24T10:56:09.066+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | FA:16:3E:12:76:80 | 15.100.103.101  | normal     | vlan472    | po26          | 2023-05-24T11:08:39.395+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.100.103.41   | incomplete | vlan472    |               | 2023-05-24T11:08:47.576+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.254.133.196  | incomplete | vlan462    |               | 2023-05-24T11:08:49.696+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.254.133.194  | incomplete | vlan462    |               | 2023-05-24T11:08:57.664+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.254.133.192  | incomplete | vlan462    |               | 2023-05-24T11:09:00.424+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.254.133.195  | incomplete | vlan462    |               | 2023-05-24T11:09:03.160+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.137.253  | normal     | vlan461    | tunnel7       | 2023-05-24T11:09:05.462+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.136.254  | normal     | vlan460    | tunnel7       | 2023-05-24T10:51:01.638+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.136.191  | incomplete | vlan460    |               | 2023-05-24T11:09:11.988+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.136.195  | incomplete | vlan460    |               | 2023-05-24T11:09:14.392+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.136.192  | incomplete | vlan460    |               | 2023-05-24T11:09:14.432+02:00 | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:A3:8E:EB:B3:3F | 15.3.9.254      | normal     | vlan471    | po2           | 2023-05-24T10:59:37.123+02:00 | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-IN_VRF            | 00:A3:8E:EB:B3:3F | 15.2.25.1       | normal     | vlan455    | po2           | 2023-05-24T10:59:36.593+02:00 | 
| pod-1/cl201-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:A3:8E:EB:B3:3F | 15.2.9.254      | normal     | vlan456    | po2           | 2023-05-24T10:59:36.533+02:00 | 
| pod-1/cl201-eu-spdc | overlay-1                      | 5C:71:0D:ED:E4:0B | 10.3.0.1        | normal     | vlan9      | eth1/91       | 2023-05-24T11:01:01.480+02:00 | 
| pod-1/cl201-eu-spdc | overlay-1                      | 5C:71:0D:EE:0C:4B | 10.3.0.2        | normal     | vlan9      | eth1/92       | 2023-05-24T11:04:36.692+02:00 | 
| pod-1/cl201-eu-spdc | overlay-1                      | 5C:71:0D:EE:99:03 | 10.3.0.3        | normal     | vlan9      | eth1/93       | 2023-05-24T11:03:45.449+02:00 | 
| pod-1/cl201-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:22:BD:F8:19:FF | 10.58.29.157    | normal     | vlan452    | tunnel7       | 2023-05-24T11:05:03.602+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:22:BD:F8:19:FF | 15.254.104.254  | normal     | vlan491    | tunnel7       | 2023-05-24T10:53:59.814+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:70:4D:85 | 15.100.7.101    | normal     | vlan492    | tunnel7       | 2023-05-24T10:59:27.301+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:72:79:10 | 15.254.104.191  | normal     | vlan491    | tunnel7       | 2023-05-24T11:03:49.173+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:BC:A6:70 | 15.100.7.41     | normal     | vlan492    | tunnel7       | 2023-05-24T11:07:04.161+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | FA:16:3E:CB:11:71 | 15.254.104.192  | normal     | vlan491    | tunnel7       | 2023-05-24T11:00:21.821+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.106.252  | normal     | vlan495    | tunnel7       | 2023-05-24T10:59:09.574+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.107.254  | normal     | vlan494    | tunnel7       | 2023-05-24T10:56:00.874+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | FA:16:3E:72:79:10 | 15.254.107.191  | normal     | vlan494    | tunnel7       | 2023-05-24T10:59:31.733+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF     | FA:16:3E:CB:11:71 | 15.254.107.192  | normal     | vlan494    | tunnel7       | 2023-05-24T11:06:32.881+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF        | FA:16:3E:A8:F7:A2 | 15.100.4.220    | normal     | vlan482    | tunnel7       | 2023-05-24T10:59:11.877+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1_VRF        | FA:16:3E:B0:E0:5D | 15.100.4.221    | normal     | vlan482    | tunnel7       | 2023-05-24T11:04:18.113+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:22:BD:F8:19:FF | 15.254.134.254  | normal     | vlan481    | tunnel7       | 2023-05-24T10:56:09.986+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | FA:16:3E:12:76:80 | 15.100.103.101  | normal     | vlan479    | tunnel7       | 2023-05-24T11:09:13.741+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.254.134.193  | incomplete | vlan481    |               | 2023-05-24T11:08:51.045+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | unspecified       | 15.100.103.41   | incomplete | vlan479    |               | 2023-05-24T11:08:53.453+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.137.254  | normal     | vlan484    | tunnel7       | 2023-05-24T11:09:06.382+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | 00:22:BD:F8:19:FF | 15.254.136.252  | normal     | vlan483    | tunnel7       | 2023-05-24T10:51:02.558+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.137.192  | incomplete | vlan484    |               | 2023-05-24T11:08:58.542+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.137.193  | incomplete | vlan484    |               | 2023-05-24T11:08:59.694+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.137.194  | incomplete | vlan484    |               | 2023-05-24T11:09:07.969+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF     | unspecified       | 15.254.137.191  | incomplete | vlan484    |               | 2023-05-24T11:09:14.533+02:00 | 
| pod-1/cl202-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:A3:8E:EB:B3:3F | 15.3.9.254      | normal     | vlan487    | tunnel7       | 2023-05-24T10:59:37.752+02:00 | 
| pod-1/cl202-eu-spdc | MPC:MPC-sPBR-IN_VRF            | 00:A3:8E:EB:B3:3F | 15.2.25.1       | normal     | vlan476    | tunnel7       | 2023-05-24T10:59:37.222+02:00 | 
| pod-1/cl202-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:A3:8E:EB:B3:3F | 15.2.9.254      | normal     | vlan477    | tunnel7       | 2023-05-24T10:59:36.399+02:00 | 
| pod-1/cl202-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:22:BD:F8:19:FF | 10.58.29.156    | normal     | vlan475    | tunnel7       | 2023-05-24T11:05:04.522+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 00:50:56:B2:DE:E5 | 15.3.25.100     | normal     | vlan25     | po2           | 2023-05-24T10:52:08.634+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:7C:46 | 15.3.7.3        | normal     | vlan24     | po2           | 2023-05-24T11:05:30.973+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:89:29 | 15.3.7.1        | normal     | vlan24     | po2           | 2023-05-24T11:06:33.917+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:E0:7F | 15.3.7.2        | normal     | vlan24     | tunnel8       | 2023-05-24T11:04:46.655+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 00:50:56:B2:29:73 | 15.3.21.11      | normal     | vlan23     | tunnel8       | 2023-05-24T10:52:55.602+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:48 | 192.168.31.2    | normal     | eth1/36.6  | eth1/36       | 2023-05-24T10:55:52.193+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:74 | 15.16.3.1       | normal     | eth1/29    | eth1/29       | 2023-05-24T11:07:11.885+02:00 | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 00:22:BD:F8:19:FF | 10.58.26.93     | normal     | vlan22     | tunnel8       | 2023-05-24T11:06:14.930+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 00:50:56:B2:DE:E5 | 15.3.25.100     | normal     | vlan22     | tunnel8       | 2023-05-24T10:56:11.024+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:7C:46 | 15.3.7.3        | normal     | vlan23     | tunnel8       | 2023-05-24T11:07:15.743+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:89:29 | 15.3.7.1        | normal     | vlan23     | tunnel8       | 2023-05-24T11:05:23.941+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:E0:7F | 15.3.7.2        | normal     | vlan23     | po1           | 2023-05-24T11:05:27.924+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 00:50:56:B2:29:73 | 15.3.21.11      | normal     | vlan21     | po1           | 2023-05-24T11:02:51.128+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:4C | 192.168.32.2    | normal     | eth1/36.6  | eth1/36       | 2023-05-24T10:56:47.397+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:70 | 15.16.3.5       | normal     | eth1/29    | eth1/29       | 2023-05-24T10:51:43.912+02:00 | 
| pod-1/rl302-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 00:22:BD:F8:19:FF | 10.58.26.92     | normal     | vlan40     | tunnel8       | 2023-05-24T11:06:14.752+02:00 | 
+---------------------+--------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
```

[[Back]](./ProtocolArp.md)