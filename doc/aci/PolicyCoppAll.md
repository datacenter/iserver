# Policy - CoPP

## Get all policies

```
# iserver get aci policy copp --apic apic11

Apic: apic11

+-------------+----+-----------+------------+--------------+
| Policy Name | TF | Protocols | Interfaces | Ref Policies |
+-------------+----+-----------+------------+--------------+
| default     |    | 0         | 408        | 86           | 
+-------------+----+-----------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy copp --apic apic11

{
    "duration": 1866,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 434,
        "disconnect_time": 0,
        "mo_time": 1320,
        "total_time": 1754
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

True	434	-	connect apic11o.emea-sp.cisco.com
True	302	1	apic11o.emea-sp.cisco.com class coppIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	311	0	apic11o.emea-sp.cisco.com class coppProtoClassP
True	414	408	apic11o.emea-sp.cisco.com class l1RsCoppIfPolCons
True	293	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCopp.md)