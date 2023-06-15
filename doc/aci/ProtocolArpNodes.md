# Node Protocol - ARP

## Multiple node adjacencies

```
# iserver get aci proto arp --apic apic11 --node bl206-eu-spdc --node rl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl206-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
| Node                | VRF                           | MAC               | IP              | State      | Interface  | Phy Interface | Timestamp                     |
+---------------------+-------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
| pod-1/bl206-eu-spdc | common:Infra_BGP_VRF          | 00:A3:8E:EB:B3:3F | 192.168.254.5   | normal     | eth1/24.55 | eth1/24       | 2023-06-14T07:59:40.927+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_privIP_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.70  | normal     | eth1/24.54 | eth1/24       | 2023-06-14T07:55:53.088+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.96  | normal     | eth1/24.62 | eth1/24       | 2023-06-14T07:55:50.648+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.100 | normal     | eth1/24.56 | eth1/24       | 2023-06-14T07:55:50.011+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.88  | normal     | eth1/24.61 | eth1/24       | 2023-06-14T07:55:50.051+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.92  | normal     | eth1/24.64 | eth1/24       | 2023-06-14T07:55:50.071+02:00 | 
| pod-1/bl206-eu-spdc | mgmt:inb                      | 00:A3:8E:EB:B3:3F | 192.168.254.21  | normal     | eth1/24.59 | eth1/24       | 2023-06-14T07:55:50.838+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.3        | incomplete | vlan58     |               | 2023-06-14T08:05:42.675+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.1        | incomplete | vlan58     |               | 2023-06-14T08:05:52.499+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.5        | incomplete | vlan58     |               | 2023-06-14T08:06:05.819+02:00 | 
| pod-1/bl206-eu-spdc | overlay-1                     | 00:8A:96:1C:7C:B0 | 15.16.2.5       | normal     | eth1/28    | eth1/28       | 2023-06-14T07:50:52.807+02:00 | 
| pod-1/bl206-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 00:A3:8E:EB:B3:3F | 192.168.254.45  | normal     | eth1/24.60 | eth1/24       | 2023-06-14T07:55:50.065+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 00:A3:8E:EB:B3:3F | 192.168.254.107 | normal     | eth1/24.63 | eth1/24       | 2023-06-14T07:55:53.551+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 00:50:56:B2:7C:46 | 15.3.7.3        | normal     | vlan25     | tunnel7       | 2023-06-14T08:05:12.722+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                     | 00:8A:96:9A:C0:48 | 192.168.31.2    | normal     | eth1/36.6  | eth1/36       | 2023-06-14T07:48:38.602+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                     | 00:8A:96:9A:C0:74 | 15.16.3.1       | normal     | eth1/29    | eth1/29       | 2023-06-14T07:50:49.210+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 00:50:56:B2:7C:46 | 15.3.7.3        | normal     | vlan24     | po1           | 2023-06-14T08:05:43.068+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | unspecified       | 15.3.7.1        | incomplete | vlan24     |               | 2023-06-14T08:05:45.228+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | unspecified       | 15.3.7.2        | incomplete | vlan24     |               | 2023-06-14T08:05:49.604+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                     | 00:8A:96:9A:C0:4C | 192.168.32.2    | normal     | eth1/36.6  | eth1/36       | 2023-06-14T07:48:56.121+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                     | 00:8A:96:9A:C0:70 | 15.16.3.5       | normal     | eth1/29    | eth1/29       | 2023-06-14T07:51:13.344+02:00 | 
+---------------------+-------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --node bl206-eu-spdc --node rl

{
    "duration": 3192,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 471,
        "disconnect_time": 0,
        "mo_time": 2337,
        "total_time": 2808
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
    },
    "cache_hits": 0
}

Log: apic
----------

True	471	-	connect apic11o.emea-sp.cisco.com
True	354	13	apic11o.emea-sp.cisco.com class fabricNode
True	302	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/arpDom
True	302	13	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	382	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/arpDom
True	313	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	340	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/arpDom
True	344	5	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)