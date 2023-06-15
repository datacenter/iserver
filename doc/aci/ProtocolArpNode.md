# Node Protocol - ARP

## Single node adjacencies

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

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
| pod-1/bl205-eu-spdc | overlay-1                     | 00:8A:96:1C:7C:B4 | 15.16.2.1       | normal     | eth1/28    | eth1/28       | 2023-06-14T07:49:18.345+02:00 | 
| pod-1/bl205-eu-spdc | SPIN_InnoLab:SPIN_VRF1        | 00:A3:8E:EB:B3:3F | 192.168.254.41  | normal     | eth1/24.50 | eth1/24       | 2023-06-14T07:55:52.876+02:00 | 
| pod-1/bl205-eu-spdc | UC3-CL2023-Demo:default       | 00:A3:8E:EB:B3:3F | 192.168.254.105 | normal     | eth1/24.53 | eth1/24       | 2023-06-14T07:55:52.923+02:00 | 
+---------------------+-------------------------------+-------------------+-----------------+------------+------------+---------------+-------------------------------+
```

Developer

```
# iserver get aci proto arp --apic apic11 --node bl205-eu-spdc

{
    "duration": 1685,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 454,
        "disconnect_time": 0,
        "mo_time": 1008,
        "total_time": 1462
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

True	454	-	connect apic11o.emea-sp.cisco.com
True	363	13	apic11o.emea-sp.cisco.com class fabricNode
True	325	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom
True	320	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
```

[[Back]](./ProtocolArp.md)