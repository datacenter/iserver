# Policy - Link Flap

## Filter by name

```
# iserver get aci policy flap --apic apic11 --name default

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
# iserver get aci policy flap --apic apic11 --name default

{
    "duration": 1582,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 1045,
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	323	1	apic11o.emea-sp.cisco.com class fabricLinkFlapPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	419	408	apic11o.emea-sp.cisco.com class l1RsLinkFlapPolCons
True	303	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyFlap.md)