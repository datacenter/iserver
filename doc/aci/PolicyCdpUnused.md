# Policy - CDP

## Unused

```
# iserver get aci policy cdp --apic apic11 --unused

Apic: apic11

+---------------------+----+-------------+------------+--------------+
| Policy Name         | TF | Admin State | Interfaces | Ref Policies |
+---------------------+----+-------------+------------+--------------+
| cdp-disabled        |    | disabled    | 0          | 0            | 
| system-cdp-disabled |    | disabled    | 0          | 0            | 
| system-cdp-enabled  |    | enabled     | 0          | 0            | 
+---------------------+----+-------------+------------+--------------+
```

Developer

```
# iserver get aci policy cdp --apic apic11 --unused

{
    "duration": 1541,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 1043,
        "total_time": 1445
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
True	313	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	414	370	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	316	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)