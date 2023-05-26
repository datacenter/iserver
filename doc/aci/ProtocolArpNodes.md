# Node Protocol - ARP

## Multiple node adjacencies

```
# iserver get aci proto arp --apic apic11 --node bl206-eu-spdc --node rl

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl206-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
| Node                | VRF                            | MAC               | IP              | State  | Interface  | Phy Interface | Timestamp                     |
+---------------------+--------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
| pod-1/bl206-eu-spdc | common:Infra_BGP_VRF           | 00:A3:8E:EB:B3:3F | 192.168.254.5   | normal | eth1/24.47 | eth1/24       | 2023-05-24T11:01:01.871+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_privIP_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.70  | normal | eth1/24.38 | eth1/24       | 2023-05-24T10:54:03.744+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.96  | normal | eth1/24.43 | eth1/24       | 2023-05-24T10:54:03.695+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.100 | normal | eth1/24.40 | eth1/24       | 2023-05-24T10:54:02.027+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.88  | normal | eth1/24.44 | eth1/24       | 2023-05-24T10:54:01.930+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.92  | normal | eth1/24.45 | eth1/24       | 2023-05-24T10:54:03.797+02:00 | 
| pod-1/bl206-eu-spdc | mgmt:inb                       | 00:A3:8E:EB:B3:3F | 192.168.254.21  | normal | eth1/24.48 | eth1/24       | 2023-05-24T10:54:01.987+02:00 | 
| pod-1/bl206-eu-spdc | MPC-F5T:F5-OUT_VRF             | 00:50:56:B2:80:63 | 15.2.7.1        | normal | vlan42     | po4           | 2023-05-24T11:04:54.036+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:22:BD:CD:C2:BB | 15.2.7.253      | normal | vlan41     | tunnel2       | 2023-05-24T11:07:21.929+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:0E:D8 | 15.2.7.5        | normal | vlan41     | tunnel2       | 2023-05-24T11:08:02.118+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:62:BB | 15.2.7.4        | normal | vlan41     | tunnel2       | 2023-05-24T11:05:38.292+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:77:0B | 15.2.7.3        | normal | vlan41     | po4           | 2023-05-24T11:06:34.747+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:7E:F3 | 15.2.7.2        | normal | vlan41     | tunnel2       | 2023-05-24T11:06:35.007+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:8F:CB | 15.2.7.6        | normal | vlan41     | tunnel2       | 2023-05-24T11:07:01.055+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:D5:AB | 15.2.7.1        | normal | vlan41     | tunnel2       | 2023-05-24T11:07:40.629+02:00 | 
| pod-1/bl206-eu-spdc | overlay-1                      | 00:8A:96:1C:7C:B0 | 15.16.2.5       | normal | eth1/28    | eth1/28       | 2023-05-24T10:51:55.791+02:00 | 
| pod-1/bl206-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:A3:8E:EB:B3:3F | 192.168.254.45  | normal | eth1/24.49 | eth1/24       | 2023-05-24T10:54:01.940+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:22:BD:F8:19:FF | 10.58.24.109    | normal | vlan39     | tunnel2       | 2023-05-24T10:51:13.708+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.104    | normal | vlan39     | po4           | 2023-05-24T11:07:23.310+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.99     | normal | vlan39     | tunnel2       | 2023-05-24T11:08:23.906+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.106    | normal | vlan39     | po4           | 2023-05-24T11:08:23.310+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.103    | normal | vlan39     | tunnel2       | 2023-05-24T11:07:35.773+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.98     | normal | vlan39     | po4           | 2023-05-24T11:08:48.785+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:A9:62 | 10.58.24.97     | normal | vlan39     | tunnel2       | 2023-05-24T11:03:49.683+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E3:FD | 10.58.24.102    | normal | vlan39     | tunnel2       | 2023-05-24T11:07:03.589+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E7:5B | 10.58.24.105    | normal | vlan39     | tunnel2       | 2023-05-24T11:08:41.763+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:ED:D0 | 10.58.24.101    | normal | vlan39     | tunnel2       | 2023-05-24T11:08:34.557+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:A3:8E:EB:B3:3F | 192.168.254.107 | normal | eth1/24.46 | eth1/24       | 2023-05-24T10:54:02.010+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 00:50:56:B2:DE:E5 | 15.3.25.100     | normal | vlan25     | po2           | 2023-05-24T10:52:08.634+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:7C:46 | 15.3.7.3        | normal | vlan24     | po2           | 2023-05-24T11:05:30.973+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:89:29 | 15.3.7.1        | normal | vlan24     | po2           | 2023-05-24T11:06:33.917+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:E0:7F | 15.3.7.2        | normal | vlan24     | tunnel8       | 2023-05-24T11:04:46.655+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 00:50:56:B2:29:73 | 15.3.21.11      | normal | vlan23     | tunnel8       | 2023-05-24T10:52:55.602+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:48 | 192.168.31.2    | normal | eth1/36.6  | eth1/36       | 2023-05-24T10:55:52.193+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:74 | 15.16.3.1       | normal | eth1/29    | eth1/29       | 2023-05-24T11:07:11.885+02:00 | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 00:22:BD:F8:19:FF | 10.58.26.93     | normal | vlan22     | tunnel8       | 2023-05-24T11:06:14.930+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 00:50:56:B2:DE:E5 | 15.3.25.100     | normal | vlan22     | tunnel8       | 2023-05-24T10:56:11.024+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:7C:46 | 15.3.7.3        | normal | vlan23     | tunnel8       | 2023-05-24T11:07:15.743+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:89:29 | 15.3.7.1        | normal | vlan23     | tunnel8       | 2023-05-24T11:05:23.941+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:E0:7F | 15.3.7.2        | normal | vlan23     | po1           | 2023-05-24T11:05:27.924+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 00:50:56:B2:29:73 | 15.3.21.11      | normal | vlan21     | po1           | 2023-05-24T11:02:51.128+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:4C | 192.168.32.2    | normal | eth1/36.6  | eth1/36       | 2023-05-24T10:56:47.397+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:70 | 15.16.3.5       | normal | eth1/29    | eth1/29       | 2023-05-24T10:51:43.912+02:00 | 
| pod-1/rl302-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 00:22:BD:F8:19:FF | 10.58.26.92     | normal | vlan40     | tunnel8       | 2023-05-24T11:06:14.752+02:00 | 
+---------------------+--------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
```

[[Back]](./ProtocolArp.md)