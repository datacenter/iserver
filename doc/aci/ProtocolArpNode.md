# Node Protocol - ARP

## Single node adjacencies

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
| Node                | VRF                           | MAC               | IP              | State  | Interface  | Phy Interface | Timestamp                     |
+---------------------+-------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF          | 00:A3:8E:EB:B3:3F | 192.168.254.1   | normal | eth1/24.62 | eth1/24       | 2023-05-30T18:20:51.579+02:00 | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.66  | normal | eth1/24.36 | eth1/24       | 2023-05-30T18:08:08.346+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.98  | normal | eth1/24.65 | eth1/24       | 2023-05-30T18:08:05.783+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.102 | normal | eth1/24.60 | eth1/24       | 2023-05-30T18:08:05.673+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.90  | normal | eth1/24.64 | eth1/24       | 2023-05-30T18:08:06.103+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.94  | normal | eth1/24.66 | eth1/24       | 2023-05-30T18:08:05.725+02:00 | 
| pod-1/bl205-eu-spdc | mgmt:inb                      | 00:A3:8E:EB:B3:3F | 192.168.254.17  | normal | eth1/24.67 | eth1/24       | 2023-05-30T18:08:06.156+02:00 | 
| pod-1/bl205-eu-spdc | MPC-F5T:F5-OUT_VRF            | 00:50:56:B2:80:63 | 15.2.7.1        | normal | vlan63     | tunnel2       | 2023-05-30T18:16:41.514+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:22:BD:CD:C2:BB | 15.2.7.252      | normal | vlan61     | tunnel2       | 2023-05-30T18:14:54.885+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:0E:D8 | 15.2.7.5        | normal | vlan61     | po5           | 2023-05-30T18:20:32.983+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:62:BB | 15.2.7.4        | normal | vlan61     | po5           | 2023-05-30T18:21:04.495+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:77:0B | 15.2.7.3        | normal | vlan61     | tunnel2       | 2023-05-30T18:20:07.840+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:7E:F3 | 15.2.7.2        | normal | vlan61     | po5           | 2023-05-30T18:17:03.624+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:8F:CB | 15.2.7.6        | normal | vlan61     | po5           | 2023-05-30T18:20:27.742+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | 00:50:56:B2:D5:AB | 15.2.7.1        | normal | vlan61     | po5           | 2023-05-30T18:17:15.702+02:00 | 
| pod-1/bl205-eu-spdc | overlay-1                     | 00:8A:96:1C:7C:B4 | 15.16.2.1       | normal | eth1/28    | eth1/28       | 2023-05-30T18:10:03.901+02:00 | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 00:A3:8E:EB:B3:3F | 192.168.254.41  | normal | eth1/24.71 | eth1/24       | 2023-05-30T18:08:06.051+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:22:BD:F8:19:FF | 10.58.24.108    | normal | vlan35     | tunnel2       | 2023-05-30T18:19:09.001+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:13:6E | 10.58.24.104    | normal | vlan35     | tunnel2       | 2023-05-30T18:19:52.306+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:94:45 | 10.58.24.106    | normal | vlan35     | tunnel2       | 2023-05-30T18:19:51.464+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:94:45 | 10.58.24.99     | normal | vlan35     | po5           | 2023-05-30T18:20:11.404+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:9F:42 | 10.58.24.103    | normal | vlan35     | po5           | 2023-05-30T18:19:07.230+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:9F:42 | 10.58.24.98     | normal | vlan35     | tunnel2       | 2023-05-30T18:20:09.751+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:A9:62 | 10.58.24.97     | normal | vlan35     | po5           | 2023-05-30T18:21:01.486+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:E3:FD | 10.58.24.102    | normal | vlan35     | po5           | 2023-05-30T18:20:57.389+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:E7:5B | 10.58.24.105    | normal | vlan35     | po5           | 2023-05-30T18:20:28.595+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:50:56:B2:ED:D0 | 10.58.24.101    | normal | vlan35     | po5           | 2023-05-30T18:20:25.981+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:A3:8E:EB:B3:3F | 192.168.254.105 | normal | eth1/24.68 | eth1/24       | 2023-05-30T18:08:06.050+02:00 | 
+---------------------+-------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc

{
    "duration": 1374,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 875,
        "total_time": 1264
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

True	389	-	connect apic11o.emea-sp.cisco.com
True	311	11	apic11o.emea-sp.cisco.com class fabricNode
True	276	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	288	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)