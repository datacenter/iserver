# Node Protocol - IPv4

## Fault history view

```
# iserver get aci proto ipv4
    --apic apic11
    --node cl201-eu-spdc
    --view hfault
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol IPv4 - Fault Records [#9]
----------------------------------

+---------------------+-----+-------+------------------------+-------------------------------+------------------+---------------------+-----------+--------------------+----------------------------------------------------------------------------------+
| Node                | Sev | Code  | Cause                  | Created Time                  | Lifecycle        | Domain              | Interface | Address            | Description                                                                      |
+---------------------+-----+-------+------------------------+-------------------------------+------------------+---------------------+-----------+--------------------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | --  | F1425 | ip-provisioning-failed | 2023-06-12T10:39:23.104+02:00 | retaining        | MPC:MPC-sPBR-IN_VRF | vlan461   | 15.2.25.254/24     | IPv4 address(15.2.25.254/24) is operationally down, reason:Interface down on     | 
|                     |     |       |                        |                               |                  |                     |           |                    | node 201 fabric hostname cl201-eu-spdc                                           | 
| pod-1/cl201-eu-spdc | --  | F1425 | ip-provisioning-failed | 2023-06-12T10:39:23.103+02:00 | retaining        | MPC:MPC-sPBR-IN_VRF | vlan461   | 15.2.25.253/24     | IPv4 address(15.2.25.253/24) is operationally down, reason:Interface down on     | 
|                     |     |       |                        |                               |                  |                     |           |                    | node 201 fabric hostname cl201-eu-spdc                                           | 
| pod-1/cl201-eu-spdc | --  | F1425 | ip-provisioning-failed | 2023-06-12T11:17:53.572+02:00 |                  | overlay-1           | vlan9     | 10.3.0.30/27       | IPv4 address(10.3.0.30/27) is operationally down, reason:Interface down on node  | 
|                     |     |       |                        |                               |                  |                     |           |                    | 0 fabric hostname                                                                | 
| pod-1/cl201-eu-spdc | --  | F1425 | ip-provisioning-failed | 2023-06-12T11:39:23.794+02:00 |                  | MPC:MPC-sPBR-IN_VRF | vlan461   | 15.2.25.253/24     | IPv4 address(15.2.25.253/24) is operationally down, reason:Interface down on     | 
|                     |     |       |                        |                               |                  |                     |           |                    | node 201 fabric hostname cl201-eu-spdc                                           | 
| pod-1/cl201-eu-spdc | --  | F1425 | ip-provisioning-failed | 2023-06-12T11:39:23.794+02:00 |                  | MPC:MPC-sPBR-IN_VRF | vlan461   | 15.2.25.254/24     | IPv4 address(15.2.25.254/24) is operationally down, reason:Interface down on     | 
|                     |     |       |                        |                               |                  |                     |           |                    | node 201 fabric hostname cl201-eu-spdc                                           | 
| pod-1/cl201-eu-spdc | Maj | F1425 | ip-provisioning-failed | 2023-07-10T16:42:57.327+02:00 | soaking-clearing | MPC:MPC-sPBR-IN_VRF | lo19      | 201.201.201.201/32 | IPv4 address(201.201.201.201/32) is operationally down, reason:Interface down    | 
|                     |     |       |                        |                               |                  |                     |           |                    | on node 201 fabric hostname cl201-eu-spdc                                        | 
| pod-1/cl201-eu-spdc | Maj | F1425 | ip-provisioning-failed | 2023-07-10T16:42:57.228+02:00 | soaking          | MPC:MPC-sPBR-IN_VRF | lo19      | 201.201.201.201/32 | IPv4 address(201.201.201.201/32) is operationally down, reason:Interface down    | 
|                     |     |       |                        |                               |                  |                     |           |                    | on node 201 fabric hostname cl201-eu-spdc                                        | 
| pod-1/cl201-eu-spdc | --  | F1425 | ip-provisioning-failed | 2023-07-10T16:45:01.486+02:00 | retaining        | MPC:MPC-sPBR-IN_VRF | lo19      | 201.201.201.201/32 | IPv4 address(201.201.201.201/32) is operationally down, reason:Interface down    | 
|                     |     |       |                        |                               |                  |                     |           |                    | on node 201 fabric hostname cl201-eu-spdc                                        | 
| pod-1/cl201-eu-spdc | --  | F1425 | ip-provisioning-failed | 2023-07-10T17:45:02.176+02:00 |                  | MPC:MPC-sPBR-IN_VRF | lo19      | 201.201.201.201/32 | IPv4 address(201.201.201.201/32) is operationally down, reason:Interface down    | 
|                     |     |       |                        |                               |                  |                     |           |                    | on node 201 fabric hostname cl201-eu-spdc                                        | 
+---------------------+-----+-------+------------------------+-------------------------------+------------------+---------------------+-----------+--------------------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci proto ipv4
    --apic apic11
    --node cl201-eu-spdc
    --view hfault
    --when 90d

{
    "duration": 2867,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 473,
        "disconnect_time": 0,
        "mo_time": 1877,
        "total_time": 2350
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

True	473	-	connect apic11o.emea-sp.cisco.com:443
True	412	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	388	30	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/uribv4 query query-target=children&rsp-subtree-include=health,fault-count&target-subtree-class=uribv4Dom
True	1077	569	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/ipv4 query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolIpv4.md)