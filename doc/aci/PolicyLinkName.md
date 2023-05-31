# Policy - Link Level

## Filter by name

```
# iserver get aci policy link --apic apic11 --name default

Apic: apic11

+-------------+----+----------+----------+---------+--------------+----------------------+----------+-------------+------------+--------------+
| Policy Name | TF | PHY Type | Auto Neg | Speed   | Delay [msec] | Link Debounce [msec] | FEC Mode | EMI Retrain | Interfaces | Ref Policies |
+-------------+----+----------+----------+---------+--------------+----------------------+----------+-------------+------------+--------------+
| default     |    | auto     | on       | inherit | 0            | 100                  | inherit  | disable     | 339        | 54           | 
+-------------+----+----------+----------+---------+--------------+----------------------+----------+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy link --apic apic11 --name default

{
    "duration": 1557,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 1039,
        "total_time": 1434
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	343	29	apic11o.emea-sp.cisco.com class fabricHIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	403	408	apic11o.emea-sp.cisco.com class l1RsHIfPolCons
True	293	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLink.md)