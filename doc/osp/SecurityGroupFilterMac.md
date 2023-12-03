# Security Group

## Filter by mac address

```
# iserver get osp sg --cluster pod1 --mac 9782 -v port

Cluster: pod1

Security Group - Port and Rule [#1]
-----------------------------------

+--------+--------+-------------------+---------------+-----------+-----------+----------+-------------+---------------+--------------+
| Tenant | Name   | MAC               | VM            | EtherType | Direction | Protocol | Port Range  | Remote Prefix | Remote Group |
+--------+--------+-------------------+---------------+-----------+-----------+----------+-------------+---------------+--------------+
| smi5gc | portal | fa:16:3e:cc:97:82 | smi5gc/portal | IPv4      | egress    | --       | --          | --            | --           | 
|        |        |                   |               | IPv4      | ingress   | udp      | 123-123     | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 24224-24224 | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 8010-8010   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 3142-3142   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 8280-8280   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 3000-3000   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 9095-9095   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 9191-9191   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | udp      | 5141-5141   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 9080-9080   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 5601-5601   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | udp      | 53-53       | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv4      | ingress   | tcp      | 9090-9090   | 0.0.0.0/0     | --           | 
|        |        |                   |               | IPv6      | egress    | --       | --          | --            | --           | 
+--------+--------+-------------------+---------------+-----------+-----------+----------+-------------+---------------+--------------+

Filter: name, tenant, mac, vm
View:   state (def), id, rule, port, all
```

Developer

```
# iserver get osp sg --cluster pod1 --mac 9782 -v port

{
    "duration": 6949,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 5785,
        "total_time": 5785
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

2023-11-20 18:23:58.237408	True	1764	get	security_groups
2023-11-20 18:23:58.684048	True	406	get	tenants
2023-11-20 18:23:59.102093	True	402	get	ports
2023-11-20 18:24:02.909897	True	3213	get	virtual_machines
```

[[Back]](./SecurityGroupGet.md)