# Policy - CoPP

## Filter by name

```
# iserver get aci policy copp --apic apic11 --name default

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
# iserver get aci policy copp --apic apic11 --name default

{
    "duration": 1958,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 1387,
        "total_time": 1795
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

True	408	-	connect apic11o.emea-sp.cisco.com
True	323	1	apic11o.emea-sp.cisco.com class coppIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	316	0	apic11o.emea-sp.cisco.com class coppProtoClassP
True	439	408	apic11o.emea-sp.cisco.com class l1RsCoppIfPolCons
True	309	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyCopp.md)