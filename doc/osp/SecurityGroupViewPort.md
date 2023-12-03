# Security Group

## Port view

```
# iserver get osp sg --cluster pod1 -v port

Cluster: pod1

Security Group - Port and Rule [#7]
-----------------------------------

+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| Tenant  | Name    | MAC               | VM                    | EtherType | Direction | Protocol | Port Range  | Remote Prefix | Remote Group    |
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| --      | default | fa:16:3e:5c:b7:b8 | ialonso/ORANGE-C8KV-1 | IPv4      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:3b:d5:c6 | ialonso/SDWAN-C8KV01B | IPv4      | ingress   | --       | --          | --            | --/default      | 
|         |         | fa:16:3e:67:1b:48 | ialonso/ORANGE-C8KV-2 | IPv6      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:ae:32:44 | admin/c8koncinder     | IPv6      | ingress   | --       | --          | --            | --/default      | 
|         |         | fa:16:3e:c3:6b:06 | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:38:40:30 | smi5gc/server         |           |           |          |             |               |                 | 
|         |         | fa:16:3e:22:8e:23 | smi5gc/VPC-SI-mme     |           |           |          |             |               |                 | 
|         |         | fa:16:3e:6b:57:aa | admin/my-c8kv         |           |           |          |             |               |                 | 
|         |         | fa:16:3e:a4:f5:53 | ialonso/ORANGE-C8KV-2 |           |           |          |             |               |                 | 
|         |         | fa:16:3e:22:9c:e2 | smi5gc/VPC-SI-upf1    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:01:17:1c | smi5gc/VPC-SI-upf2    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:8f:6a:55 | smi5gc/VPC-SI-upf8    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:b3:23:ae | --                    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:97:c1:38 | ialonso/ORANGE-C8KV-1 |           |           |          |             |               |                 | 
|         |         | fa:16:3e:0c:78:90 | admin/c8koncinder     |           |           |          |             |               |                 | 
|         |         | fa:16:3e:78:dd:45 | --                    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:14:7d:d0 | ialonso/SDWAN-C8KV01B |           |           |          |             |               |                 | 
|         |         | fa:16:3e:bb:2b:cd | smi5gc/esc            |           |           |          |             |               |                 | 
|         |         | fa:16:3e:15:b1:7f | smi5gc/VPC-SI-saegw1  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:57:23:38 | smi5gc/VPC-SI-saegw2  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:13:75:c2 | admin/my-cirros-img   |           |           |          |             |               |                 | 
|         |         | fa:16:3e:dd:d2:9d | smi5gc/VPC-SI-saegw1  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:18:11:ba | smi5gc/VPC-SI-saegw2  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:e8:f1:d5 | smi5gc/VPC-SI-upf1    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:48:32:31 | smi5gc/VPC-SI-upf2    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:fc:e6:60 | smi5gc/VPC-SI-upf8    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:89:e6:2b | admin/test-sriov      |           |           |          |             |               |                 | 
|         |         | fa:16:3e:c3:ad:0b | smi5gc/VPC-SI-saegw1  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:1e:c2:e6 | smi5gc/VPC-SI-saegw2  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:e7:65:c7 | smi5gc/VPC-SI-upf1    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:74:59:71 | smi5gc/VPC-SI-upf2    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:7d:a2:a1 | smi5gc/VPC-SI-upf8    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:88:5f:dd | smi5gc/VPC-SI-mme     |           |           |          |             |               |                 | 
|         |         | fa:16:3e:cf:4b:b5 | smi5gc/VPC-SI-upf1    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:d8:3b:77 | smi5gc/VPC-SI-upf2    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:8f:e0:92 | smi5gc/VPC-SI-upf8    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:2d:58:f2 | smi5gc/esc            |           |           |          |             |               |                 | 
|         |         | fa:16:3e:6f:c4:6a | smi5gc/VPC-SI-saegw1  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:92:89:86 | smi5gc/VPC-SI-saegw2  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:cc:7f:24 | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:63:7d:aa | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:fe:4d:de | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:70:4d:85 | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:7c:ff:47 | smi5gc/VPC-SI-mme     |           |           |          |             |               |                 | 
|         |         | fa:16:3e:b4:94:eb | smi5gc/server         |           |           |          |             |               |                 | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| admin   | default | fa:16:3e:ae:32:44 | admin/c8koncinder     | IPv4      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:6b:57:aa | admin/my-c8kv         | IPv4      | ingress   | --       | --          | --            | admin/default   | 
|         |         | fa:16:3e:0c:78:90 | admin/c8koncinder     | IPv6      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:13:75:c2 | admin/my-cirros-img   | IPv6      | ingress   | --       | --          | --            | admin/default   | 
|         |         | fa:16:3e:89:e6:2b | admin/test-sriov      |           |           |          |             |               |                 | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| ialonso | default | fa:16:3e:5c:b7:b8 | ialonso/ORANGE-C8KV-1 | IPv4      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:3b:d5:c6 | ialonso/SDWAN-C8KV01B | IPv4      | ingress   | --       | --          | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:67:1b:48 | ialonso/ORANGE-C8KV-2 | IPv4      | ingress   | --       | --          | --            | ialonso/default | 
|         |         | fa:16:3e:a4:f5:53 | ialonso/ORANGE-C8KV-2 | IPv6      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:97:c1:38 | ialonso/ORANGE-C8KV-1 | IPv6      | ingress   | --       | --          | --            | ialonso/default | 
|         |         | fa:16:3e:14:7d:d0 | ialonso/SDWAN-C8KV01B |           |           |          |             |               |                 | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| service | default |                   |                       | IPv4      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv4      | ingress   | --       | --          | --            | service/default | 
|         |         |                   |                       | IPv6      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv6      | ingress   | --       | --          | --            | service/default | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| smi5gc  | default | fa:16:3e:c3:6b:06 | smi5gc/lattice        | IPv4      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:38:40:30 | smi5gc/server         | IPv4      | ingress   | tcp      | 9830-9830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:22:8e:23 | smi5gc/VPC-SI-mme     | IPv4      | ingress   | tcp      | 4022-4022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:22:9c:e2 | smi5gc/VPC-SI-upf1    | IPv4      | ingress   | tcp      | 4830-4830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:01:17:1c | smi5gc/VPC-SI-upf2    | IPv4      | ingress   | tcp      | 1022-1022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:8f:6a:55 | smi5gc/VPC-SI-upf8    | IPv4      | ingress   | tcp      | 5022-5022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:b3:23:ae | --                    | IPv4      | ingress   | tcp      | 179-179     | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:78:dd:45 | --                    | IPv4      | ingress   | tcp      | 6443-6443   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:bb:2b:cd | smi5gc/esc            | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:15:b1:7f | smi5gc/VPC-SI-saegw1  | IPv4      | ingress   | tcp      | 7022-7022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:57:23:38 | smi5gc/VPC-SI-saegw2  | IPv4      | ingress   | tcp      | 6022-6022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:dd:d2:9d | smi5gc/VPC-SI-saegw1  | IPv4      | ingress   | tcp      | 8081-8081   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:18:11:ba | smi5gc/VPC-SI-saegw2  | IPv4      | ingress   | tcp      | 830-830     | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:e8:f1:d5 | smi5gc/VPC-SI-upf1    | IPv4      | ingress   | tcp      | 6830-6830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:48:32:31 | smi5gc/VPC-SI-upf2    | IPv4      | ingress   | udp      | 2123-2123   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:fc:e6:60 | smi5gc/VPC-SI-upf8    | IPv4      | ingress   | tcp      | 9022-9022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:c3:ad:0b | smi5gc/VPC-SI-saegw1  | IPv4      | ingress   | tcp      | 7830-7830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:1e:c2:e6 | smi5gc/VPC-SI-saegw2  | IPv4      | ingress   | tcp      | 2022-2022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:e7:65:c7 | smi5gc/VPC-SI-upf1    | IPv4      | ingress   | sctp     | 38412-38412 | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:74:59:71 | smi5gc/VPC-SI-upf2    | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:7d:a2:a1 | smi5gc/VPC-SI-upf8    | IPv4      | ingress   | udp      | 1812-1812   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:88:5f:dd | smi5gc/VPC-SI-mme     | IPv4      | ingress   | tcp      | 1830-1830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:cf:4b:b5 | smi5gc/VPC-SI-upf1    | IPv4      | ingress   | tcp      | 2153-2153   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:d8:3b:77 | smi5gc/VPC-SI-upf2    | IPv4      | ingress   | tcp      | 20001-20004 | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:8f:e0:92 | smi5gc/VPC-SI-upf8    | IPv4      | ingress   | tcp      | 2024-2024   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:2d:58:f2 | smi5gc/esc            | IPv4      | ingress   | --       | --          | --            | smi5gc/default  | 
|         |         | fa:16:3e:6f:c4:6a | smi5gc/VPC-SI-saegw1  | IPv4      | ingress   | tcp      | 3830-3830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:92:89:86 | smi5gc/VPC-SI-saegw2  | IPv4      | ingress   | tcp      | 2830-2830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:cc:7f:24 | smi5gc/lattice        | IPv4      | ingress   | udp      | 2152-2152   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:63:7d:aa | smi5gc/lattice        | IPv4      | ingress   | tcp      | 8022-8022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:fe:4d:de | smi5gc/lattice        | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:70:4d:85 | smi5gc/lattice        | IPv4      | ingress   | tcp      | 3868-3868   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:7c:ff:47 | smi5gc/VPC-SI-mme     | IPv4      | ingress   | tcp      | 5021-5091   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:b4:94:eb | smi5gc/server         | IPv4      | ingress   | tcp      | 8830-8830   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | udp      | 1813-1813   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 5830-5830   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 3022-3022   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv6      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv6      | ingress   | --       | --          | --            | smi5gc/default  | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| smi5gc  | esc     | fa:16:3e:bb:2b:cd | smi5gc/esc            | IPv4      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 830-830     | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 8250-8250   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv6      | egress    | --       | --          | --            | --              | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| smi5gc  | portal  | fa:16:3e:cc:97:82 | smi5gc/portal         | IPv4      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv4      | ingress   | udp      | 123-123     | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 24224-24224 | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 8010-8010   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 3142-3142   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 8280-8280   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 3000-3000   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 9095-9095   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 9191-9191   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | udp      | 5141-5141   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 9080-9080   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 5601-5601   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | udp      | 53-53       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 9090-9090   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv6      | egress    | --       | --          | --            | --              | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+

Filter: name, tenant, mac, vm
View:   state (def), id, rule, port, all
```

Developer

```
# iserver get osp sg --cluster pod1 -v port

{
    "duration": 7118,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 5070,
        "total_time": 5070
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

2023-11-20 18:22:54.373878	True	1747	get	security_groups
2023-11-20 18:22:54.689458	True	269	get	tenants
2023-11-20 18:22:55.102569	True	403	get	ports
2023-11-20 18:22:58.535023	True	2651	get	virtual_machines
```

[[Back]](./SecurityGroupGet.md)