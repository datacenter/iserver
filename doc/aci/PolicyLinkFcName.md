# Policy - Link Level Flow Control

## Filter by name

```
# iserver get aci policy link-fc --apic apic11 --name default

Apic: apic11

+-------------+----+----------------------+-------------------+------------+--------------+
| Policy Name | TF | Receive Flow Control | Send Flow Control | Interfaces | Ref Policies |
+-------------+----+----------------------+-------------------+------------+--------------+
| default     |    | off                  | off               | 342        | 82           | 
+-------------+----+----------------------+-------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy link-fc --apic apic11 --name default

{
    "duration": 1575,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 406,
        "disconnect_time": 0,
        "mo_time": 1059,
        "total_time": 1465
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

True	406	-	connect apic11o.emea-sp.cisco.com
True	321	2	apic11o.emea-sp.cisco.com class qosLlfcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	437	344	apic11o.emea-sp.cisco.com class l1RsQosLlfcIfPolCons
True	301	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLinkFc.md)