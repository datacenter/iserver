# Node Protocol - ARP

## Leaf nodes adjacencies

```
# iserver get aci proto arp --apic apic11 --role leaf

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+-------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
| Node                | VRF                           | MAC               | IP              | State      | Interface  | Phy Interface | Timestamp                     |
+---------------------+-------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
| pod-1/bl205-eu-spdc | common:Infra_BGP_VRF          | 00:A3:8E:EB:B3:3F | 192.168.254.1   | normal     | eth1/24.48 | eth1/24       | 2023-06-14T07:59:40.468+02:00 | 
| pod-1/bl205-eu-spdc | common:Infra_privIP_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.66  | normal     | eth1/24.47 | eth1/24       | 2023-06-14T07:55:52.820+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.98  | normal     | eth1/24.51 | eth1/24       | 2023-06-14T07:55:55.983+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim1_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.102 | normal     | eth1/24.46 | eth1/24       | 2023-06-14T07:55:56.446+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.90  | normal     | eth1/24.52 | eth1/24       | 2023-06-14T07:55:57.429+02:00 | 
| pod-1/bl205-eu-spdc | common:smi5Gc-cvim4_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.94  | normal     | eth1/24.55 | eth1/24       | 2023-06-14T07:55:56.393+02:00 | 
| pod-1/bl205-eu-spdc | mgmt:inb                      | 00:A3:8E:EB:B3:3F | 192.168.254.17  | normal     | eth1/24.54 | eth1/24       | 2023-06-14T07:55:56.033+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.2        | incomplete | vlan67     |               | 2023-06-14T08:05:53.125+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.5        | incomplete | vlan67     |               | 2023-06-14T08:06:08.897+02:00 | 
| pod-1/bl205-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.4        | incomplete | vlan67     |               | 2023-06-14T08:06:17.641+02:00 | 
| pod-1/bl205-eu-spdc | overlay-1                     | 00:8A:96:1C:7C:B4 | 15.16.2.1       | normal     | eth1/28    | eth1/28       | 2023-06-14T07:49:18.345+02:00 | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 00:A3:8E:EB:B3:3F | 192.168.254.41  | normal     | eth1/24.50 | eth1/24       | 2023-06-14T07:55:52.876+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:A3:8E:EB:B3:3F | 192.168.254.105 | normal     | eth1/24.53 | eth1/24       | 2023-06-14T07:55:52.923+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_BGP_VRF          | 00:A3:8E:EB:B3:3F | 192.168.254.5   | normal     | eth1/24.55 | eth1/24       | 2023-06-14T07:59:40.927+02:00 | 
| pod-1/bl206-eu-spdc | common:Infra_privIP_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.70  | normal     | eth1/24.54 | eth1/24       | 2023-06-14T07:55:53.088+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.96  | normal     | eth1/24.62 | eth1/24       | 2023-06-14T07:55:50.648+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim1_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.100 | normal     | eth1/24.56 | eth1/24       | 2023-06-14T07:55:50.011+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.88  | normal     | eth1/24.61 | eth1/24       | 2023-06-14T07:55:50.051+02:00 | 
| pod-1/bl206-eu-spdc | common:smi5Gc-cvim4_VRF       | 00:A3:8E:EB:B3:3F | 192.168.254.92  | normal     | eth1/24.64 | eth1/24       | 2023-06-14T07:55:50.071+02:00 | 
| pod-1/bl206-eu-spdc | mgmt:inb                      | 00:A3:8E:EB:B3:3F | 192.168.254.21  | normal     | eth1/24.59 | eth1/24       | 2023-06-14T07:55:50.838+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.1        | incomplete | vlan58     |               | 2023-06-14T08:05:52.499+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.5        | incomplete | vlan58     |               | 2023-06-14T08:06:05.819+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.4        | incomplete | vlan58     |               | 2023-06-14T08:06:07.843+02:00 | 
| pod-1/bl206-eu-spdc | MPC:MPC-sPBR-OUT_VRF          | unspecified       | 15.2.7.6        | incomplete | vlan58     |               | 2023-06-14T08:06:14.259+02:00 | 
| pod-1/bl206-eu-spdc | overlay-1                     | 00:8A:96:1C:7C:B0 | 15.16.2.5       | normal     | eth1/28    | eth1/28       | 2023-06-14T07:50:52.807+02:00 | 
| pod-1/bl206-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 00:A3:8E:EB:B3:3F | 192.168.254.45  | normal     | eth1/24.60 | eth1/24       | 2023-06-14T07:55:50.065+02:00 | 
| pod-1/bl206-eu-spdc | UC3-CL2023-Demo:default       | 00:A3:8E:EB:B3:3F | 192.168.254.107 | normal     | eth1/24.63 | eth1/24       | 2023-06-14T07:55:53.551+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | unspecified       | 15.254.103.195  | incomplete | vlan496    |               | 2023-06-14T08:05:59.858+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | unspecified       | 15.254.106.195  | incomplete | vlan492    |               | 2023-06-14T08:06:15.382+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | unspecified       | 15.254.106.192  | incomplete | vlan492    |               | 2023-06-14T08:06:21.386+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | unspecified       | 15.100.103.101  | incomplete | vlan471    |               | 2023-06-14T08:05:55.542+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | unspecified       | 15.254.133.196  | incomplete | vlan473    |               | 2023-06-14T08:06:06.550+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | unspecified       | 15.254.133.194  | incomplete | vlan473    |               | 2023-06-14T08:06:11.742+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | unspecified       | 15.254.133.195  | incomplete | vlan473    |               | 2023-06-14T08:06:12.754+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | unspecified       | 15.254.133.192  | incomplete | vlan473    |               | 2023-06-14T08:06:13.385+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | unspecified       | 15.254.136.196  | incomplete | vlan494    |               | 2023-06-14T08:06:07.958+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | unspecified       | 15.254.136.191  | incomplete | vlan494    |               | 2023-06-14T08:06:14.130+02:00 | 
| pod-1/cl201-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | unspecified       | 15.254.136.193  | incomplete | vlan494    |               | 2023-06-14T08:06:15.826+02:00 | 
| pod-1/cl201-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 00:A3:8E:EB:B3:3F | 15.3.9.254      | normal     | vlan499    | po26          | 2023-06-14T07:56:50.980+02:00 | 
| pod-1/cl201-eu-spdc | overlay-1                     | 5C:71:0D:EE:0C:4B | 10.3.0.2        | normal     | vlan9      | eth1/92       | 2023-06-14T07:47:46.246+02:00 | 
| pod-1/cl201-eu-spdc | overlay-1                     | 5C:71:0D:EE:99:03 | 10.3.0.3        | normal     | vlan9      | eth1/93       | 2023-06-14T07:52:48.501+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N3-N4_VRF | unspecified       | 15.254.104.191  | incomplete | vlan488    |               | 2023-06-14T08:06:02.113+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim1-N6_VRF    | unspecified       | 15.254.107.193  | incomplete | vlan472    |               | 2023-06-14T08:06:11.277+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N3-N4_VRF | unspecified       | 15.100.103.41   | incomplete | vlan471    |               | 2023-06-14T08:06:00.117+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | unspecified       | 15.254.137.191  | incomplete | vlan490    |               | 2023-06-14T08:06:09.137+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | unspecified       | 15.254.137.194  | incomplete | vlan490    |               | 2023-06-14T08:06:11.341+02:00 | 
| pod-1/cl202-eu-spdc | common:smi5Gc-cvim4-N6_VRF    | unspecified       | 15.254.137.195  | incomplete | vlan490    |               | 2023-06-14T08:06:15.777+02:00 | 
| pod-1/cl202-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 00:A3:8E:EB:B3:3F | 15.3.9.254      | normal     | vlan483    | tunnel3       | 2023-06-14T07:57:22.236+02:00 | 
| pod-1/cl202-eu-spdc | overlay-1                     | 5C:71:0D:ED:E4:0B | 10.3.0.1        | normal     | vlan9      | eth1/91       | 2023-06-14T07:52:48.093+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 00:50:56:B2:7C:46 | 15.3.7.3        | normal     | vlan25     | tunnel7       | 2023-06-14T08:05:12.722+02:00 | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | unspecified       | 15.3.7.1        | incomplete | vlan25     |               | 2023-06-14T08:06:15.762+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                     | 00:8A:96:9A:C0:48 | 192.168.31.2    | normal     | eth1/36.6  | eth1/36       | 2023-06-14T07:48:38.602+02:00 | 
| pod-1/rl301-eu-spdc | overlay-1                     | 00:8A:96:9A:C0:74 | 15.16.3.1       | normal     | eth1/29    | eth1/29       | 2023-06-14T07:50:49.210+02:00 | 
| pod-1/rl302-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF      | 00:50:56:B2:7C:46 | 15.3.7.3        | normal     | vlan24     | po1           | 2023-06-14T08:05:43.068+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                     | 00:8A:96:9A:C0:4C | 192.168.32.2    | normal     | eth1/36.6  | eth1/36       | 2023-06-14T07:48:56.121+02:00 | 
| pod-1/rl302-eu-spdc | overlay-1                     | 00:8A:96:9A:C0:70 | 15.16.3.5       | normal     | eth1/29    | eth1/29       | 2023-06-14T07:51:13.344+02:00 | 
+---------------------+-------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --role leaf

{
    "duration": 6915,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 445,
        "disconnect_time": 0,
        "mo_time": 5721,
        "total_time": 6166
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

True	445	-	connect apic11o.emea-sp.cisco.com
True	322	13	apic11o.emea-sp.cisco.com class fabricNode
True	299	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	319	13	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	332	27	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/arpDom
True	331	14	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	333	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/arpDom
True	336	14	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	352	31	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/arpDom
True	365	8	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	363	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/arpDom
True	329	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	332	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/arpDom
True	357	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	347	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/arpDom
True	360	4	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	313	19	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/arpDom
True	331	3	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)