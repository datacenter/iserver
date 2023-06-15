# Policy - Link Flap

## Get all policies

```
# iserver get aci policy flap --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------+----+-----------+--------------------------+------------+--------------+
| Policy Name | TF | Max Flaps | Max Flaps Duration [sec] | Interfaces | Ref Policies |
+-------------+----+-----------+--------------------------+------------+--------------+
| default     |    | 30        | 420                      | 464        | 87           | 
+-------------+----+-----------+--------------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy flap --apic apic11

{
    "duration": 2041,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 522,
        "disconnect_time": 0,
        "mo_time": 1013,
        "total_time": 1535
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

True	522	-	connect apic11o.emea-sp.cisco.com
True	316	1	apic11o.emea-sp.cisco.com class fabricLinkFlapPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	377	464	apic11o.emea-sp.cisco.com class l1RsLinkFlapPolCons
True	320	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyFlap.md)