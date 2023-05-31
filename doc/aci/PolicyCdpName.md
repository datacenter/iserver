# Policy - CDP

## Filter by name

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled

Apic: apic11

+-------------+----+-------------+------------+--------------+
| Policy Name | TF | Admin State | Interfaces | Ref Policies |
+-------------+----+-------------+------------+--------------+
| cdp-enabled |    | enabled     | 4          | 3            | 
+-------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11 --name cdp-enabled

{
    "duration": 1548,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 1002,
        "total_time": 1402
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	313	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	402	370	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	287	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)