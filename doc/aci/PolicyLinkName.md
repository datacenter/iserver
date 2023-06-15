# Policy - Link Level

## Filter by name

```
# iserver get aci policy link --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+----------+----------+---------+--------------+----------------------+----------+-------------+------------+--------------+
| Policy Name | TF | PHY Type | Auto Neg | Speed   | Delay [msec] | Link Debounce [msec] | FEC Mode | EMI Retrain | Interfaces | Ref Policies |
+-------------+----+----------+----------+---------+--------------+----------------------+----------+-------------+------------+--------------+
| default     |    | auto     | on       | inherit | 0            | 100                  | inherit  | disable     | 395        | 54           | 
+-------------+----+----------+----------+---------+--------------+----------------------+----------+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy link --apic apic11 --name default

{
    "duration": 1902,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 1093,
        "total_time": 1514
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

True	421	-	connect apic11o.emea-sp.cisco.com
True	352	29	apic11o.emea-sp.cisco.com class fabricHIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	427	464	apic11o.emea-sp.cisco.com class l1RsHIfPolCons
True	314	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLink.md)