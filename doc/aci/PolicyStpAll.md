# Policy - Spanning Tree

## Get all policies

```
# iserver get aci policy stp --apic apic11

Apic: apic11

+--------------+----+-------------+------------+------------+--------------+
| Policy Name  | TF | BPDU Filter | BPDU Guard | Interfaces | Ref Policies |
+--------------+----+-------------+------------+------------+--------------+
| default      |    | False       | False      | 406        | 84           | 
| nidemo-dummy |    | False       | False      | 2          | 1            | 
+--------------+----+-------------+------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy stp --apic apic11

{
    "duration": 1545,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 403,
        "disconnect_time": 0,
        "mo_time": 1007,
        "total_time": 1410
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

True	403	-	connect apic11o.emea-sp.cisco.com
True	312	2	apic11o.emea-sp.cisco.com class stpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	407	408	apic11o.emea-sp.cisco.com class l1RsStpIfPolCons
True	288	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyStp.md)