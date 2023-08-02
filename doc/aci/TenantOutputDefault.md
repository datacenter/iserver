# Tenant

## Default output

```
# iserver get aci tenant --apic apic21

Apic: apic21 (mode:online, cache:off)

Tenant [#12]
------------

+--------+------------------+
| Health | Name             |
+--------+------------------+
| 100    | common           | 
| 100    | Ericsson_PACO    | 
| 61     | hefernan_ni-demo | 
| 100    | infra            | 
| 95     | k8s              | 
| 61     | mgmt             | 
| 93     | nidemo           | 
| 79     | SPN_IntraLab     | 
| 100    | Testing_MSO      | 
| 100    | ttrabatt-test    | 
| 59     | vEPC             | 
| 87     | vEPC_demo        | 
+--------+------------------+
```

Developer

```
# iserver get aci tenant --apic apic21

{
    "duration": 1226,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 463,
        "disconnect_time": 0,
        "mo_time": 534,
        "total_time": 997
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

True	463	-	connect apic21o.emea-sp.cisco.com:443
True	534	12	apic21o.emea-sp.cisco.com:443 class fvTenant query rsp-subtree=children&rsp-subtree-include=health,fault-count
```

[[Back]](./Tenant.md)