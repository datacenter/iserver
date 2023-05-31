# Policy - Spanning Tree

## Filter by name

```
# iserver get aci policy stp --apic apic11 --name default

Apic: apic11

+-------------+----+-------------+------------+------------+--------------+
| Policy Name | TF | BPDU Filter | BPDU Guard | Interfaces | Ref Policies |
+-------------+----+-------------+------------+------------+--------------+
| default     |    | False       | False      | 406        | 84           | 
+-------------+----+-------------+------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy stp --apic apic11 --name default

{
    "duration": 1556,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 373,
        "disconnect_time": 0,
        "mo_time": 1044,
        "total_time": 1417
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

True	373	-	connect apic11o.emea-sp.cisco.com
True	331	2	apic11o.emea-sp.cisco.com class stpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	402	408	apic11o.emea-sp.cisco.com class l1RsStpIfPolCons
True	311	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyStp.md)