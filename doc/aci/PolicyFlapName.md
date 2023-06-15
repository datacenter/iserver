# Policy - Link Flap

## Filter by name

```
# iserver get aci policy flap --apic apic11 --name default

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
# iserver get aci policy flap --apic apic11 --name default

{
    "duration": 1774,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 434,
        "disconnect_time": 0,
        "mo_time": 1066,
        "total_time": 1500
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

True	434	-	connect apic11o.emea-sp.cisco.com
True	349	1	apic11o.emea-sp.cisco.com class fabricLinkFlapPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	399	464	apic11o.emea-sp.cisco.com class l1RsLinkFlapPolCons
True	318	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyFlap.md)