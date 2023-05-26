# Node Protocol - ARP

## Filter adjacencies by IP subnet

```
# iserver get aci proto arp --apic apic11 --subnet 15.2.0.0/16

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+----------------------+-------------------+------------+--------+-----------+---------------+-------------------------------+
| Node                | VRF                  | MAC               | IP         | State  | Interface | Phy Interface | Timestamp                     |
+---------------------+----------------------+-------------------+------------+--------+-----------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF   | 00:50:56:B2:80:63 | 15.2.7.1   | normal | vlan63    | tunnel2       | 2023-05-24T11:06:53.392+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:22:BD:CD:C2:BB | 15.2.7.252 | normal | vlan61    | tunnel2       | 2023-05-24T11:07:22.060+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:0E:D8 | 15.2.7.5   | normal | vlan61    | po5           | 2023-05-24T11:07:33.075+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:62:BB | 15.2.7.4   | normal | vlan61    | po5           | 2023-05-24T11:07:04.839+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:77:0B | 15.2.7.3   | normal | vlan61    | tunnel2       | 2023-05-24T11:08:30.733+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:7E:F3 | 15.2.7.2   | normal | vlan61    | po5           | 2023-05-24T11:09:37.051+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:8F:CB | 15.2.7.6   | normal | vlan61    | po5           | 2023-05-24T11:08:50.366+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:D5:AB | 15.2.7.1   | normal | vlan61    | po5           | 2023-05-24T11:09:48.974+02:00 | 
+---------------------+----------------------+-------------------+------------+--------+-----------+---------------+-------------------------------+
```

[[Back]](./ProtocolArp.md)