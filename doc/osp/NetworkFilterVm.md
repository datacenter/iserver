# Network

## Filter by virtual machine

```
# iserver get osp net --cluster pod1 --vm lattice -v port

Cluster: pod1

Network - Port [#5]
-------------------

+--------------------+---------------+-------------------+--------------+---------+-----------------------+------------------+
| Name               | CIDR          | MAC               | IP           | Type    | VM                    | HV               |
+--------------------+---------------+-------------------+--------------+---------+-----------------------+------------------+
| smi5gc/control-N2  | 15.100.5.0/24 | fa:16:3e:c9:c1:51 | 15.100.5.1   | DHCP    | --                    | AIO-server-3     | 
|                    |               | fa:16:3e:63:7d:aa | 15.100.5.101 | Compute | smi5gc/lattice        | compute-server-2 | 
|                    |               | fa:16:3e:8b:2c:b8 | 15.100.5.2   | DHCP    | --                    | AIO-server-2     | 
+--------------------+---------------+-------------------+--------------+---------+-----------------------+------------------+
| smi5gc/control-N4  | 15.100.6.0/24 | fa:16:3e:6b:5b:ab | 15.100.6.1   | DHCP    | --                    | AIO-server-2     | 
|                    |               | fa:16:3e:fe:4d:de | 15.100.6.101 | Compute | smi5gc/lattice        | compute-server-2 | 
|                    |               | fa:16:3e:6f:c6:b7 | 15.100.6.2   | DHCP    | --                    | AIO-server-1     | 
+--------------------+---------------+-------------------+--------------+---------+-----------------------+------------------+
| smi5gc/control-SBI | 15.100.4.0/24 | fa:16:3e:9b:b6:b0 | 15.100.4.1   | DHCP    | --                    | AIO-server-1     | 
|                    |               | fa:16:3e:cc:7f:24 | 15.100.4.101 | Compute | smi5gc/lattice        | compute-server-2 | 
|                    |               | fa:16:3e:77:f7:73 | 15.100.4.2   | DHCP    | --                    | AIO-server-3     | 
+--------------------+---------------+-------------------+--------------+---------+-----------------------+------------------+
| smi5gc/data-N3     | 15.100.7.0/24 | fa:16:3e:8b:39:88 | 15.100.7.1   | DHCP    | --                    | AIO-server-1     | 
|                    |               | fa:16:3e:70:4d:85 | 15.100.7.101 | Compute | smi5gc/lattice        | compute-server-2 | 
|                    |               | fa:16:3e:00:0b:d6 | 15.100.7.2   | DHCP    | --                    | AIO-server-3     | 
|                    |               | fa:16:3e:7c:ff:47 | 15.100.7.41  | Compute | smi5gc/VPC-SI-mme     | AIO-server-1     | 
+--------------------+---------------+-------------------+--------------+---------+-----------------------+------------------+
| smi5gc/management  | 15.100.1.0/24 | fa:16:3e:d3:81:f1 | 15.100.1.1   | DHCP    | --                    | AIO-server-1     | 
|                    |               | fa:16:3e:cc:97:82 | 15.100.1.100 | Compute | smi5gc/portal         | AIO-server-1     | 
|                    |               | fa:16:3e:c3:6b:06 | 15.100.1.101 | Compute | smi5gc/lattice        | compute-server-2 | 
|                    |               | fa:16:3e:38:40:30 | 15.100.1.102 | Compute | smi5gc/server         | compute-server-1 | 
|                    |               | fa:16:3e:22:8e:23 | 15.100.1.103 | Compute | smi5gc/VPC-SI-mme     | AIO-server-1     | 
|                    |               | fa:16:3e:6b:57:aa | 15.100.1.117 | Compute | admin/my-c8kv         | compute-server-2 | 
|                    |               | fa:16:3e:a4:f5:53 | 15.100.1.179 | Compute | ialonso/ORANGE-C8KV-2 | AIO-server-1     | 
|                    |               | fa:16:3e:22:9c:e2 | 15.100.1.191 | Compute | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                    |               | fa:16:3e:01:17:1c | 15.100.1.192 | Compute | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                    |               | fa:16:3e:8f:6a:55 | 15.100.1.198 | Compute | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
|                    |               | fa:16:3e:2e:aa:e4 | 15.100.1.2   | DHCP    | --                    | AIO-server-2     | 
|                    |               | fa:16:3e:b3:23:ae | 15.100.1.201 | None    | --                    |                  | 
|                    |               | fa:16:3e:97:c1:38 | 15.100.1.219 | Compute | ialonso/ORANGE-C8KV-1 | AIO-server-1     | 
|                    |               | fa:16:3e:0c:78:90 | 15.100.1.220 | Compute | admin/c8koncinder     | compute-server-2 | 
|                    |               | fa:16:3e:78:dd:45 | 15.100.1.254 | HA      | --                    | AIO-server-3     | 
|                    |               | fa:16:3e:14:7d:d0 | 15.100.1.30  | Compute | ialonso/SDWAN-C8KV01B | AIO-server-1     | 
|                    |               | fa:16:3e:bb:2b:cd | 15.100.1.36  | Compute | smi5gc/esc            | AIO-server-2     | 
|                    |               | fa:16:3e:15:b1:7f | 15.100.1.51  | Compute | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                    |               | fa:16:3e:57:23:38 | 15.100.1.52  | Compute | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
|                    |               | fa:16:3e:13:75:c2 | 15.100.1.69  | Compute | admin/my-cirros-img   | compute-server-2 | 
+--------------------+---------------+-------------------+--------------+---------+-----------------------+------------------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1 --vm lattice -v port

{
    "duration": 10976,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 10494,
        "total_time": 10494
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

2023-11-19 13:16:30.190042	True	3136	get	networks
2023-11-19 13:16:30.748399	True	536	get	tenants
2023-11-19 13:16:31.148178	True	396	get	subnets
2023-11-19 13:16:34.332233	True	3176	get	ports
2023-11-19 13:16:37.834319	True	3250	get	virtual_machines
```

[[Back]](./NetworkGet.md)