# Policy - CDP

## Used

```
# iserver get aci policy cdp --apic apic11 --used

Apic: apic11 (mode:online, cache:off)

+--------------+----+-------------+------------+--------------+
| Policy Name  | TF | Admin State | Interfaces | Ref Policies |
+--------------+----+-------------+------------+--------------+
| cdp-enabled  |    | enabled     | 4          | 3            | 
| CDP_enable   |    | enabled     | 86         | 24           | 
| default      |    | disabled    | 334        | 67           | 
| nidemo-dummy |    | disabled    | 2          | 1            | 
+--------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy cdp --apic apic11 --used

{
    "duration": 1836,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 456,
        "disconnect_time": 0,
        "mo_time": 1051,
        "total_time": 1507
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

True	456	-	connect apic11o.emea-sp.cisco.com
True	323	8	apic11o.emea-sp.cisco.com class cdpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	383	426	apic11o.emea-sp.cisco.com class l1RsCdpIfPolCons
True	345	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCdp.md)