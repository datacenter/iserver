# Policy - CDP

## Used

```
# iserver get aci policy cdp --apic apic11 --used

Apic: apic11

+--------------+----+-------------+------------+--------------+
| Policy Name  | TF | Admin State | Interfaces | Ref Policies |
+--------------+----+-------------+------------+--------------+
| cdp-enabled  |    | enabled     | 4          | 3            | 
| CDP_enable   |    | enabled     | 86         | 24           | 
| default      |    | disabled    | 278        | 67           | 
| nidemo-dummy |    | disabled    | 2          | 1            | 
+--------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11 --used

{
    "duration": 1627,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 396,
        "disconnect_time": 0,
        "mo_time": 1085,
        "total_time": 1481
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

True	396	-	connect apic11o.emea-sp.cisco.com
True	313	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	468	370	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	304	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)