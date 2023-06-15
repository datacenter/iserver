# Policy - Link Level Flow Control

## Filter by name

```
# iserver get aci policy link-fc --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+----------------------+-------------------+------------+--------------+
| Policy Name | TF | Receive Flow Control | Send Flow Control | Interfaces | Ref Policies |
+-------------+----+----------------------+-------------------+------------+--------------+
| default     |    | off                  | off               | 398        | 82           | 
+-------------+----+----------------------+-------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy link-fc --apic apic11 --name default

{
    "duration": 1781,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 1034,
        "total_time": 1455
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
True	325	2	apic11o.emea-sp.cisco.com class qosLlfcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	391	400	apic11o.emea-sp.cisco.com class l1RsQosLlfcIfPolCons
True	318	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLinkFc.md)