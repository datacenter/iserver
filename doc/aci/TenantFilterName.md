# Tenant

## Filter by name

```
# iserver get aci tenant --apic apic21 --name k8s

Apic: apic21 (mode:online, cache:off)

Tenant [#1]
-----------

+--------+------+
| Health | Name |
+--------+------+
| 95     | k8s  | 
+--------+------+
```

Developer

```
# iserver get aci tenant --apic apic21 --name k8s

{
    "duration": 1175,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 554,
        "total_time": 958
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

True	404	-	connect apic21o.emea-sp.cisco.com:443
True	554	12	apic21o.emea-sp.cisco.com:443 class fvTenant query rsp-subtree=children&rsp-subtree-include=health,fault-count
```

[[Back]](./Tenant.md)