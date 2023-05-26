# Node Protocol - ARP

## Filter adjacencies by MAC address

```
# iserver get aci proto arp --apic apic11 --mac 56b2

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------------------+-------------------+--------------+--------+-----------+---------------+-------------------------------+
| Node                | VRF                     | MAC               | IP           | State  | Interface | Phy Interface | Timestamp                     |
+---------------------+-------------------------+-------------------+--------------+--------+-----------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF      | 00:50:56:B2:80:63 | 15.2.7.1     | normal | vlan63    | tunnel2       | 2023-05-24T11:06:53.392+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:0E:D8 | 15.2.7.5     | normal | vlan61    | po5           | 2023-05-24T11:07:33.075+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:62:BB | 15.2.7.4     | normal | vlan61    | po5           | 2023-05-24T11:07:04.839+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:77:0B | 15.2.7.3     | normal | vlan61    | tunnel2       | 2023-05-24T11:08:30.733+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:7E:F3 | 15.2.7.2     | normal | vlan61    | po5           | 2023-05-24T11:09:37.051+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:8F:CB | 15.2.7.6     | normal | vlan61    | po5           | 2023-05-24T11:08:50.366+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:D5:AB | 15.2.7.1     | normal | vlan61    | po5           | 2023-05-24T11:04:48.961+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:13:6E | 10.58.24.104 | normal | vlan35    | tunnel2       | 2023-05-24T11:09:17.105+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:13:6E | 10.58.24.99  | normal | vlan35    | po5           | 2023-05-24T11:09:24.075+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:94:45 | 10.58.24.106 | normal | vlan35    | tunnel2       | 2023-05-24T11:08:25.488+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:9F:42 | 10.58.24.103 | normal | vlan35    | po5           | 2023-05-24T11:09:25.983+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:9F:42 | 10.58.24.98  | normal | vlan35    | tunnel2       | 2023-05-24T11:08:48.915+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:A9:62 | 10.58.24.97  | normal | vlan35    | po5           | 2023-05-24T11:09:25.031+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:E3:FD | 10.58.24.102 | normal | vlan35    | po5           | 2023-05-24T11:09:25.030+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:E7:5B | 10.58.24.105 | normal | vlan35    | po5           | 2023-05-24T11:09:26.949+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:ED:D0 | 10.58.24.101 | normal | vlan35    | po5           | 2023-05-24T11:06:51.262+02:00 | 
+---------------------+-------------------------+-------------------+--------------+--------+-----------+---------------+-------------------------------+
```

[[Back]](./ProtocolArp.md)