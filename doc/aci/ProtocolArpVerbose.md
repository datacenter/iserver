# Node Protocol - ARP

## Verbose output

Get selected ARP adjacencies as well as
- per-VRF adjacencies count
- per-interface adjacencies count

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc -o verbose

+---------------------+-------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
| Node                | VRF                           | MAC               | IP              | State  | Interface  | Phy Interface | Timestamp                     |
+---------------------+-------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF          | 00:A3:8E:EB:B3:3F | 192.168.254.1   | normal | eth1/24.62 | eth1/24       | 2023-05-07T14:44:57.317+02:00 | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.66  | normal | eth1/24.36 | eth1/24       | 2023-05-07T14:30:16.550+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.98  | normal | eth1/24.65 | eth1/24       | 2023-05-07T14:30:13.777+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.102 | normal | eth1/24.60 | eth1/24       | 2023-05-07T14:30:13.670+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.90  | normal | eth1/24.64 | eth1/24       | 2023-05-07T14:30:14.823+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.94  | normal | eth1/24.66 | eth1/24       | 2023-05-07T14:30:13.727+02:00 | 
| pod-1/bl205-eu-spdc | mgmt:inb                      | 00:A3:8E:EB:B3:3F | 192.168.254.17  | normal | eth1/24.67 | eth1/24       | 2023-05-07T14:30:14.880+02:00 | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF            | 00:50:56:B2:80:63 | 15.2.7.1        | normal | vlan63     | tunnel2       | 2023-05-07T14:48:10.298+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:22:BD:CD:C2:BB | 15.2.7.252      | normal | vlan61     | tunnel2       | 2023-05-07T14:39:39.880+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:0E:D8 | 15.2.7.5        | normal | vlan61     | po5           | 2023-05-07T14:46:08.751+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:62:BB | 15.2.7.4        | normal | vlan61     | po5           | 2023-05-07T14:47:09.159+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:77:0B | 15.2.7.3        | normal | vlan61     | tunnel2       | 2023-05-07T14:48:40.099+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:7E:F3 | 15.2.7.2        | normal | vlan61     | po5           | 2023-05-07T14:44:19.531+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:8F:CB | 15.2.7.6        | normal | vlan61     | po5           | 2023-05-07T14:44:38.351+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:D5:AB | 15.2.7.1        | normal | vlan61     | po5           | 2023-05-07T14:47:07.824+02:00 | 
| pod-1/bl205-eu-spdc | overlay-1                     | 00:8A:96:1C:7C:B4 | 15.16.2.1       | normal | eth1/28    | eth1/28       | 2023-05-07T14:34:26.479+02:00 | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 00:A3:8E:EB:B3:3F | 192.168.254.41  | normal | eth1/24.71 | eth1/24       | 2023-05-07T14:30:14.767+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:22:BD:F8:19:FF | 10.58.24.108    | normal | vlan35     | tunnel2       | 2023-05-07T14:41:30.676+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:13:6E | 10.58.24.104    | normal | vlan35     | tunnel2       | 2023-05-07T14:48:00.691+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:94:45 | 10.58.24.106    | normal | vlan35     | tunnel2       | 2023-05-07T14:48:28.438+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:94:45 | 10.58.24.99     | normal | vlan35     | po5           | 2023-05-07T14:47:47.942+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:9F:42 | 10.58.24.103    | normal | vlan35     | po5           | 2023-05-07T14:48:12.127+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:9F:42 | 10.58.24.98     | normal | vlan35     | tunnel2       | 2023-05-07T14:48:01.984+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:A9:62 | 10.58.24.97     | normal | vlan35     | po5           | 2023-05-07T14:48:08.111+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:E3:FD | 10.58.24.102    | normal | vlan35     | po5           | 2023-05-07T14:48:27.564+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:E7:5B | 10.58.24.105    | normal | vlan35     | po5           | 2023-05-07T14:48:16.165+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:ED:D0 | 10.58.24.101    | normal | vlan35     | po5           | 2023-05-07T14:45:48.156+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:A3:8E:EB:B3:3F | 192.168.254.105 | normal | eth1/24.68 | eth1/24       | 2023-05-07T14:30:14.713+02:00 | 
+---------------------+-------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+

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
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF            | 1         | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-IN_VRF           | 0         | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 7         | 
| pod-1/bl205-eu-spdc | NXOS-HandOff_Test:default     | 0         | 
| pod-1/bl205-eu-spdc | overlay-1                     | 1         | 
| pod-1/bl205-eu-spdc | P5G:P5G_VRF                   | 0         | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 1         | 
| pod-1/bl205-eu-spdc | SPN_IntraLab:SPN_VRF1         | 0         | 
| pod-1/bl205-eu-spdc | TESTING_BRUNO:default         | 0         | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 11        | 
+---------------------+-------------------------------+-----------+

+---------------------+------------+-----------+
| Node                | Interface  | Adjacency |
+---------------------+------------+-----------+
| pod-1/bl205-eu-spdc | eth1/24.36 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.60 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.62 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.64 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.65 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.66 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.67 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.68 | 1         | 
| pod-1/bl205-eu-spdc | eth1/24.71 | 1         | 
| pod-1/bl205-eu-spdc | eth1/28    | 1         | 
| pod-1/bl205-eu-spdc | vlan35     | 10        | 
| pod-1/bl205-eu-spdc | vlan61     | 7         | 
| pod-1/bl205-eu-spdc | vlan63     | 1         | 
+---------------------+------------+-----------+
```

[[Back]](./ProtocolArp.md)