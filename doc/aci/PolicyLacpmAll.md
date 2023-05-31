# Policy - Port Channel Member

## Get all policies

```
# iserver get aci policy lacp-m --apic apic11

Apic: apic11

+-------------+----+----------+---------------+------------+--------------+
| Policy Name | TF | Priority | Transmit Rate | Interfaces | Ref Policies |
+-------------+----+----------+---------------+------------+--------------+
| default     |    | 32768    | normal        | 70         | 1            | 
+-------------+----+----------+---------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy lacp-m --apic apic11

{
    "duration": 1603,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 420,
        "disconnect_time": 0,
        "mo_time": 1107,
        "total_time": 1527
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

True	420	-	connect apic11o.emea-sp.cisco.com
True	386	1	apic11o.emea-sp.cisco.com class lacpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	437	70	apic11o.emea-sp.cisco.com class l1RsLacpIfPolCons
True	284	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacpm.md)