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
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF      | 00:50:56:B2:80:63 | 15.2.7.1     | normal | vlan63    | tunnel2       | 2023-05-30T18:16:41.514+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:0E:D8 | 15.2.7.5     | normal | vlan61    | po5           | 2023-05-30T18:20:32.983+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:62:BB | 15.2.7.4     | normal | vlan61    | po5           | 2023-05-30T18:21:04.495+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:77:0B | 15.2.7.3     | normal | vlan61    | tunnel2       | 2023-05-30T18:20:07.840+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:7E:F3 | 15.2.7.2     | normal | vlan61    | po5           | 2023-05-30T18:22:03.650+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:8F:CB | 15.2.7.6     | normal | vlan61    | po5           | 2023-05-30T18:20:27.742+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF    | 00:50:56:B2:D5:AB | 15.2.7.1     | normal | vlan61    | po5           | 2023-05-30T18:22:15.727+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:13:6E | 10.58.24.104 | normal | vlan35    | tunnel2       | 2023-05-30T18:21:54.162+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:94:45 | 10.58.24.106 | normal | vlan35    | tunnel2       | 2023-05-30T18:22:22.504+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:94:45 | 10.58.24.99  | normal | vlan35    | po5           | 2023-05-30T18:22:11.434+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:9F:42 | 10.58.24.103 | normal | vlan35    | po5           | 2023-05-30T18:19:07.230+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:9F:42 | 10.58.24.98  | normal | vlan35    | tunnel2       | 2023-05-30T18:22:09.768+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:A9:62 | 10.58.24.97  | normal | vlan35    | po5           | 2023-05-30T18:21:52.174+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:E3:FD | 10.58.24.102 | normal | vlan35    | po5           | 2023-05-30T18:21:57.293+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:E7:5B | 10.58.24.105 | normal | vlan35    | po5           | 2023-05-30T18:22:29.427+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default | 00:50:56:B2:ED:D0 | 10.58.24.101 | normal | vlan35    | po5           | 2023-05-30T18:22:21.180+02:00 | 
+---------------------+-------------------------+-------------------+--------------+--------+-----------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --mac 56b2

{
    "duration": 8027,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 2936,
        "disconnect_time": 0,
        "mo_time": 4934,
        "total_time": 7870
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

True	2936	-	connect apic11o.emea-sp.cisco.com
True	859	11	apic11o.emea-sp.cisco.com class fabricNode
True	3748	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	327	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)