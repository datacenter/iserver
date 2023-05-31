# Policy - CDP

## Get all policies

```
# iserver get aci policy cdp --apic apic11

Apic: apic11

+---------------------+----+-------------+------------+--------------+
| Policy Name         | TF | Admin State | Interfaces | Ref Policies |
+---------------------+----+-------------+------------+--------------+
| cdp-disabled        |    | disabled    | 0          | 0            | 
| cdp-enabled         |    | enabled     | 4          | 3            | 
| CDP_disable         |    | disabled    | 0          | 1            | 
| CDP_enable          |    | enabled     | 86         | 24           | 
| default             |    | disabled    | 278        | 67           | 
| nidemo-dummy        |    | disabled    | 2          | 1            | 
| system-cdp-disabled |    | disabled    | 0          | 0            | 
| system-cdp-enabled  |    | enabled     | 0          | 0            | 
+---------------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11

{
    "duration": 1578,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 1012,
        "total_time": 1414
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

True	402	-	connect apic11o.emea-sp.cisco.com
True	319	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	399	370	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	294	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)