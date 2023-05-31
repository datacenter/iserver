# Policy - Link Level Flow Control

## Get all policies

```
# iserver get aci policy link-fc --apic apic11

Apic: apic11

+--------------+----+----------------------+-------------------+------------+--------------+
| Policy Name  | TF | Receive Flow Control | Send Flow Control | Interfaces | Ref Policies |
+--------------+----+----------------------+-------------------+------------+--------------+
| default      |    | off                  | off               | 342        | 82           | 
| nidemo-dummy |    | off                  | off               | 2          | 1            | 
+--------------+----+----------------------+-------------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy link-fc --apic apic11

{
    "duration": 1532,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 1005,
        "total_time": 1395
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

True	390	-	connect apic11o.emea-sp.cisco.com
True	311	2	apic11o.emea-sp.cisco.com class qosLlfcIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	399	344	apic11o.emea-sp.cisco.com class l1RsQosLlfcIfPolCons
True	295	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLinkFc.md)