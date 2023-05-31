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
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF   | 00:50:56:B2:80:63 | 15.2.7.1   | normal | vlan63    | tunnel2       | 2023-05-30T18:22:42.541+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:22:BD:CD:C2:BB | 15.2.7.252 | normal | vlan61    | tunnel2       | 2023-05-30T18:14:54.885+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:0E:D8 | 15.2.7.5   | normal | vlan61    | po5           | 2023-05-30T18:20:32.983+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:62:BB | 15.2.7.4   | normal | vlan61    | po5           | 2023-05-30T18:21:04.495+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:77:0B | 15.2.7.3   | normal | vlan61    | tunnel2       | 2023-05-30T18:20:07.840+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:7E:F3 | 15.2.7.2   | normal | vlan61    | po5           | 2023-05-30T18:22:03.650+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:8F:CB | 15.2.7.6   | normal | vlan61    | po5           | 2023-05-30T18:20:27.742+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF | 00:50:56:B2:D5:AB | 15.2.7.1   | normal | vlan61    | po5           | 2023-05-30T18:22:15.727+02:00 | 
+---------------------+----------------------+-------------------+------------+--------+-----------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --subnet 15.2.0.0/16

{
    "duration": 79214,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 439,
        "disconnect_time": 0,
        "mo_time": 78641,
        "total_time": 79080
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

True	439	-	connect apic11o.emea-sp.cisco.com
True	78059	11	apic11o.emea-sp.cisco.com class fabricNode
True	308	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	274	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)