# Security Group

## Rule view

```
# iserver get osp sg --cluster pod1 -v rule

Cluster: pod1

Security Group - Rule [#7]
--------------------------

+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| Tenant  | Name    | EtherType | Direction | Protocol | Port Range  | Remote Prefix | Remote Group    | Create | Update |
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| --      | default | IPv4      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv4      | ingress   | --       | --          | --            | --/default      | 474d   | 474d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv6      | ingress   | --       | --          | --            | --/default      | 474d   | 474d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| admin   | default | IPv4      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv4      | ingress   | --       | --          | --            | admin/default   | 474d   | 474d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv6      | ingress   | --       | --          | --            | admin/default   | 474d   | 474d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| ialonso | default | IPv4      | egress    | --       | --          | --            | --              | 35d    | 35d    | 
|         |         | IPv4      | ingress   | --       | --          | 0.0.0.0/0     | --              | 28d    | 28d    | 
|         |         | IPv4      | ingress   | --       | --          | --            | ialonso/default | 35d    | 35d    | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 35d    | 35d    | 
|         |         | IPv6      | ingress   | --       | --          | --            | ialonso/default | 35d    | 35d    | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| service | default | IPv4      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv4      | ingress   | --       | --          | --            | service/default | 474d   | 474d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv6      | ingress   | --       | --          | --            | service/default | 474d   | 474d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| smi5gc  | default | IPv4      | egress    | --       | --          | --            | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9830-9830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 4022-4022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 4830-4830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 1022-1022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 5022-5022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 179-179     | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 6443-6443   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 7022-7022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 6022-6022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8081-8081   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 830-830     | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 6830-6830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 2123-2123   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9022-9022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 7830-7830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 2022-2022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | sctp     | 38412-38412 | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 1812-1812   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 1830-1830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 2153-2153   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 20001-20004 | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 2024-2024   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | --       | --          | --            | smi5gc/default  | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3830-3830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 2830-2830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 2152-2152   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8022-8022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3868-3868   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 5021-5091   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8830-8830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 1813-1813   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 5830-5830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3022-3022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 473d   | 473d   | 
|         |         | IPv6      | ingress   | --       | --          | --            | smi5gc/default  | 473d   | 473d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| smi5gc  | esc     | IPv4      | egress    | --       | --          | --            | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 830-830     | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 8250-8250   | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 4d     | 4d     | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| smi5gc  | portal  | IPv4      | egress    | --       | --          | --            | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 123-123     | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 24224-24224 | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8010-8010   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3142-3142   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8280-8280   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3000-3000   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9095-9095   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9191-9191   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 5141-5141   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9080-9080   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 5601-5601   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 53-53       | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9090-9090   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 473d   | 473d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+

Filter: name, tenant, mac, vm
View:   state (def), id, rule, port, all
```

Developer

```
# iserver get osp sg --cluster pod1 -v rule

{
    "duration": 3079,
    "osp": {
        "read": true,
        "success": 2,
        "failed": 0,
        "mo": 2,
        "mo_time": 2333,
        "total_time": 2333
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
        "lines": 3
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-20 18:22:38.807697	True	1990	get	security_groups
2023-11-20 18:22:39.183586	True	343	get	tenants
```

[[Back]](./SecurityGroupGet.md)