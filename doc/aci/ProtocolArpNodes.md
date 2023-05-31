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
| pod-1/bl206-eu-spdc | common:Infra_BGP_VRF           | 00:A3:8E:EB:B3:3F | 192.168.254.5   | normal | eth1/24.47 | eth1/24       | 2023-05-30T18:20:51.449+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_privIP_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.70  | normal | eth1/24.38 | eth1/24       | 2023-05-30T18:09:09.700+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.96  | normal | eth1/24.43 | eth1/24       | 2023-05-30T18:09:09.643+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.100 | normal | eth1/24.40 | eth1/24       | 2023-05-30T18:09:08.080+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF  | 00:A3:8E:EB:B3:3F | 192.168.254.88  | normal | eth1/24.44 | eth1/24       | 2023-05-30T18:09:07.893+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.92  | normal | eth1/24.45 | eth1/24       | 2023-05-30T18:09:09.757+02:00 | 
| pod-1/bl206-eu-spdc | mgmt:inb                       | 00:A3:8E:EB:B3:3F | 192.168.254.21  | normal | eth1/24.48 | eth1/24       | 2023-05-30T18:09:08.000+02:00 | 
| pod-1/bl206-eu-spdc | MPC-F5T:F5-OUT_VRF             | 00:50:56:B2:80:63 | 15.2.7.1        | normal | vlan42     | po4           | 2023-05-30T18:17:59.056+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:22:BD:CD:C2:BB | 15.2.7.253      | normal | vlan41     | tunnel2       | 2023-05-30T18:14:54.757+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:0E:D8 | 15.2.7.5        | normal | vlan41     | tunnel2       | 2023-05-30T18:20:50.801+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:62:BB | 15.2.7.4        | normal | vlan41     | tunnel2       | 2023-05-30T18:17:29.327+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:77:0B | 15.2.7.3        | normal | vlan41     | po4           | 2023-05-30T18:17:01.835+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:7E:F3 | 15.2.7.2        | normal | vlan41     | tunnel2       | 2023-05-30T18:19:32.487+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:8F:CB | 15.2.7.6        | normal | vlan41     | tunnel2       | 2023-05-30T18:18:58.239+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF           | 00:50:56:B2:D5:AB | 15.2.7.1        | normal | vlan41     | tunnel2       | 2023-05-30T18:19:29.818+02:00 | 
| pod-1/bl206-eu-spdc | overlay-1                      | 00:8A:96:1C:7C:B0 | 15.16.2.5       | normal | eth1/28    | eth1/28       | 2023-05-30T18:15:26.511+02:00 | 
| pod-1/bl206-eu-spdc | SPIN_InnoLab:SPIN_VRF1         | 00:A3:8E:EB:B3:3F | 192.168.254.45  | normal | eth1/24.49 | eth1/24       | 2023-05-30T18:09:07.943+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:22:BD:F8:19:FF | 10.58.24.109    | normal | vlan39     | tunnel2       | 2023-05-30T18:19:08.872+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:13:6E | 10.58.24.104    | normal | vlan39     | po4           | 2023-05-30T18:20:52.079+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.106    | normal | vlan39     | po4           | 2023-05-30T18:18:22.245+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:94:45 | 10.58.24.99     | normal | vlan39     | tunnel2       | 2023-05-30T18:21:11.289+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.103    | normal | vlan39     | tunnel2       | 2023-05-30T18:19:20.413+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:9F:42 | 10.58.24.98     | normal | vlan39     | po4           | 2023-05-30T18:21:09.632+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:A9:62 | 10.58.24.97     | normal | vlan39     | tunnel2       | 2023-05-30T18:06:07.743+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E3:FD | 10.58.24.102    | normal | vlan39     | tunnel2       | 2023-05-30T18:20:45.482+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:E7:5B | 10.58.24.105    | normal | vlan39     | tunnel2       | 2023-05-30T18:20:39.729+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:50:56:B2:ED:D0 | 10.58.24.101    | normal | vlan39     | tunnel2       | 2023-05-30T18:19:23.386+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default        | 00:A3:8E:EB:B3:3F | 192.168.254.107 | normal | eth1/24.46 | eth1/24       | 2023-05-30T18:09:08.057+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 00:50:56:B2:DE:E5 | 15.3.25.100     | normal | vlan25     | po2           | 2023-05-30T18:17:02.630+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:7C:46 | 15.3.7.3        | normal | vlan24     | po2           | 2023-05-30T18:18:00.861+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:89:29 | 15.3.7.1        | normal | vlan24     | po2           | 2023-05-30T18:20:19.981+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:E0:7F | 15.3.7.2        | normal | vlan24     | tunnel8       | 2023-05-30T18:16:18.509+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 00:50:56:B2:29:73 | 15.3.21.11      | normal | vlan23     | tunnel8       | 2023-05-30T18:15:51.257+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:48 | 192.168.31.2    | normal | eth1/36.6  | eth1/36       | 2023-05-30T18:19:34.997+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:74 | 15.16.3.1       | normal | eth1/29    | eth1/29       | 2023-05-30T18:12:01.921+02:00 | 
| pod-1/rl301-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 00:22:BD:F8:19:FF | 10.58.26.93     | normal | vlan22     | tunnel8       | 2023-05-30T18:13:22.038+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-IN_VRF        | 00:50:56:B2:DE:E5 | 15.3.25.100     | normal | vlan22     | tunnel8       | 2023-05-30T18:18:11.669+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:7C:46 | 15.3.7.3        | normal | vlan23     | tunnel8       | 2023-05-30T18:18:44.171+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:89:29 | 15.3.7.1        | normal | vlan23     | tunnel8       | 2023-05-30T18:17:19.757+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF       | 00:50:56:B2:E0:7F | 15.3.7.2        | normal | vlan23     | po1           | 2023-05-30T18:16:56.667+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-Residential-R3DC_VRF | 00:50:56:B2:29:73 | 15.3.21.11      | normal | vlan21     | po1           | 2023-05-30T18:05:47.959+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:4C | 192.168.32.2    | normal | eth1/36.6  | eth1/36       | 2023-05-30T18:18:26.420+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                      | 00:8A:96:9A:C0:70 | 15.16.3.5       | normal | eth1/29    | eth1/29       | 2023-05-30T18:14:44.167+02:00 | 
| pod-1/rl302-eu-spdc | SPIN_InnoLab:SPIN_RDC3_VRF     | 00:22:BD:F8:19:FF | 10.58.26.92     | normal | vlan40     | tunnel8       | 2023-05-30T18:13:21.862+02:00 | 
+---------------------+--------------------------------+-------------------+-----------------+--------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --node bl206-eu-spdc --node rl

{
    "duration": 2859,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 373,
        "disconnect_time": 0,
        "mo_time": 2231,
        "total_time": 2604
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

True	373	-	connect apic11o.emea-sp.cisco.com
True	315	11	apic11o.emea-sp.cisco.com class fabricNode
True	294	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/arpDom
True	280	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	311	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/arpDom
True	433	8	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	301	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/arpDom
True	297	8	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)