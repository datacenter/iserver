# Policy - 802.1X

## Filter by name

```
# iserver get aci policy auth --apic apic11 --name default

Apic: apic11

+-------------+----+-------------+-------------+------------+--------------+
| Policy Name | TF | Admin State | Host Mode   | Interfaces | Ref Policies |
+-------------+----+-------------+-------------+------------+--------------+
| default     |    | disabled    | single-host | 0          | 83           | 
+-------------+----+-------------+-------------+------------+--------------+
```

Developer

```
# iserver get aci policy auth --apic apic11 --name default

{
    "duration": 1138,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 665,
        "total_time": 1059
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
    }
}

Log: apic
----------

True	394	-	connect apic11o.emea-sp.cisco.com
True	329	1	apic11o.emea-sp.cisco.com class l2PortAuthPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	336	0	apic11o.emea-sp.cisco.com class l1RsL2PortAuthCons
```

[[Back]](./PolicyAuth.md)