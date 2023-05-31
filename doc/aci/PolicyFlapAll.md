# Policy - Link Flap

## Get all policies

```
# iserver get aci policy flap --apic apic11

Apic: apic11

+-------------+----+-----------+--------------------------+------------+--------------+
| Policy Name | TF | Max Flaps | Max Flaps Duration [sec] | Interfaces | Ref Policies |
+-------------+----+-----------+--------------------------+------------+--------------+
| default     |    | 30        | 420                      | 408        | 87           | 
+-------------+----+-----------+--------------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy flap --apic apic11

{
    "duration": 1536,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 1025,
        "total_time": 1424
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

True	399	-	connect apic11o.emea-sp.cisco.com
True	324	1	apic11o.emea-sp.cisco.com class fabricLinkFlapPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	408	408	apic11o.emea-sp.cisco.com class l1RsLinkFlapPolCons
True	293	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyFlap.md)