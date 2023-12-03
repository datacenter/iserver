# Subnet

## Filter by hypervisor (hv)

```
# iserver get osp sub --cluster pod1 --hv compute-server-1 -v port

Cluster: pod1

Subnet - Port [#4]
------------------

+-----------------------------+-----------------+-------------------+----------------+---------+-----------------------+------------------+
| Name                        | CIDR            | MAC               | IP             | Type    | VM                    | HV               |
+-----------------------------+-----------------+-------------------+----------------+---------+-----------------------+------------------+
| smi5gc/management-subnet    | 15.100.1.0/24   | fa:16:3e:d3:81:f1 | 15.100.1.1     | DHCP    | --                    | AIO-server-1     | 
|                             |                 | fa:16:3e:cc:97:82 | 15.100.1.100   | Compute | smi5gc/portal         | AIO-server-1     | 
|                             |                 | fa:16:3e:c3:6b:06 | 15.100.1.101   | Compute | smi5gc/lattice        | compute-server-2 | 
|                             |                 | fa:16:3e:38:40:30 | 15.100.1.102   | Compute | smi5gc/server         | compute-server-1 | 
|                             |                 | fa:16:3e:22:8e:23 | 15.100.1.103   | Compute | smi5gc/VPC-SI-mme     | AIO-server-1     | 
|                             |                 | fa:16:3e:6b:57:aa | 15.100.1.117   | Compute | admin/my-c8kv         | compute-server-2 | 
|                             |                 | fa:16:3e:a4:f5:53 | 15.100.1.179   | Compute | ialonso/ORANGE-C8KV-2 | AIO-server-1     | 
|                             |                 | fa:16:3e:22:9c:e2 | 15.100.1.191   | Compute | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                             |                 | fa:16:3e:01:17:1c | 15.100.1.192   | Compute | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                             |                 | fa:16:3e:8f:6a:55 | 15.100.1.198   | Compute | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
|                             |                 | fa:16:3e:2e:aa:e4 | 15.100.1.2     | DHCP    | --                    | AIO-server-2     | 
|                             |                 | fa:16:3e:b3:23:ae | 15.100.1.201   | None    | --                    |                  | 
|                             |                 | fa:16:3e:97:c1:38 | 15.100.1.219   | Compute | ialonso/ORANGE-C8KV-1 | AIO-server-1     | 
|                             |                 | fa:16:3e:0c:78:90 | 15.100.1.220   | Compute | admin/c8koncinder     | compute-server-2 | 
|                             |                 | fa:16:3e:78:dd:45 | 15.100.1.254   | HA      | --                    | AIO-server-3     | 
|                             |                 | fa:16:3e:14:7d:d0 | 15.100.1.30    | Compute | ialonso/SDWAN-C8KV01B | AIO-server-1     | 
|                             |                 | fa:16:3e:bb:2b:cd | 15.100.1.36    | Compute | smi5gc/esc            | AIO-server-2     | 
|                             |                 | fa:16:3e:15:b1:7f | 15.100.1.51    | Compute | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                             |                 | fa:16:3e:57:23:38 | 15.100.1.52    | Compute | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
|                             |                 | fa:16:3e:13:75:c2 | 15.100.1.69    | Compute | admin/my-cirros-img   | compute-server-2 | 
+-----------------------------+-----------------+-------------------+----------------+---------+-----------------------+------------------+
| smi5gc/sriov0-subnet        | 15.100.105.0/24 | fa:16:3e:51:c2:e3 | 15.100.105.1   | DHCP    | --                    | AIO-server-2     | 
|                             |                 | fa:16:3e:dd:d2:9d | 15.100.105.151 | Compute | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                             |                 | fa:16:3e:18:11:ba | 15.100.105.152 | Compute | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
|                             |                 | fa:16:3e:e8:f1:d5 | 15.100.105.191 | Compute | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                             |                 | fa:16:3e:48:32:31 | 15.100.105.192 | Compute | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                             |                 | fa:16:3e:fc:e6:60 | 15.100.105.198 | Compute | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
|                             |                 | fa:16:3e:15:37:ec | 15.100.105.2   | DHCP    | --                    | AIO-server-1     | 
|                             |                 | fa:16:3e:89:e6:2b | 15.100.105.245 | Compute | admin/test-sriov      | compute-server-1 | 
|                             |                 | fa:16:3e:c3:ad:0b | 15.100.105.51  | Compute | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                             |                 | fa:16:3e:1e:c2:e6 | 15.100.105.52  | Compute | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
|                             |                 | fa:16:3e:e7:65:c7 | 15.100.105.91  | Compute | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                             |                 | fa:16:3e:74:59:71 | 15.100.105.92  | Compute | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                             |                 | fa:16:3e:7d:a2:a1 | 15.100.105.98  | Compute | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
+-----------------------------+-----------------+-------------------+----------------+---------+-----------------------+------------------+
| smi5gc/orchestration-subnet | 15.100.2.0/24   | fa:16:3e:e2:ff:72 | 15.100.2.1     | DHCP    | --                    | AIO-server-2     | 
|                             |                 | fa:16:3e:88:5f:dd | 15.100.2.103   | Compute | smi5gc/VPC-SI-mme     | AIO-server-1     | 
|                             |                 | fa:16:3e:cf:4b:b5 | 15.100.2.191   | Compute | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                             |                 | fa:16:3e:d8:3b:77 | 15.100.2.192   | Compute | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                             |                 | fa:16:3e:8f:e0:92 | 15.100.2.198   | Compute | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
|                             |                 | fa:16:3e:9e:96:65 | 15.100.2.2     | DHCP    | --                    | AIO-server-3     | 
|                             |                 | fa:16:3e:2d:58:f2 | 15.100.2.36    | Compute | smi5gc/esc            | AIO-server-2     | 
|                             |                 | fa:16:3e:6f:c4:6a | 15.100.2.51    | Compute | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                             |                 | fa:16:3e:92:89:86 | 15.100.2.52    | Compute | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
+-----------------------------+-----------------+-------------------+----------------+---------+-----------------------+------------------+
| smi5gc/data-N6-subnet       | 15.100.8.0/24   | fa:16:3e:1e:37:ac | 15.100.8.1     | DHCP    | --                    | AIO-server-3     | 
|                             |                 | fa:16:3e:b4:94:eb | 15.100.8.102   | Compute | smi5gc/server         | compute-server-1 | 
|                             |                 | fa:16:3e:46:ab:b0 | 15.100.8.2     | DHCP    | --                    | AIO-server-2     | 
+-----------------------------+-----------------+-------------------+----------------+---------+-----------------------+------------------+

Filter: name, tenant, address, mac, vm, hv
View:   state (def), id, port, all
```

Developer

```
# iserver get osp sub --cluster pod1 --hv compute-server-1 -v port

{
    "duration": 6342,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 5147,
        "total_time": 5147
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
        "read": true,
        "lines": 4
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 18:10:45.187671	True	1759	get	subnets
2023-11-20 18:10:45.589080	True	365	get	tenants
2023-11-20 18:10:46.000472	True	398	get	networks
2023-11-20 18:10:46.416704	True	396	get	ports
2023-11-20 18:10:49.365446	True	2229	get	virtual_machines
```

[[Back]](./SubnetGet.md)