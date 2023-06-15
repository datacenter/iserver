# Policy - Spanning Tree

## Get all policies

```
# iserver get aci policy stp --apic apic11

Apic: apic11 (mode:online, cache:off)

+--------------+----+-------------+------------+------------+--------------+
| Policy Name  | TF | BPDU Filter | BPDU Guard | Interfaces | Ref Policies |
+--------------+----+-------------+------------+------------+--------------+
| default      |    | False       | False      | 462        | 84           | 
| nidemo-dummy |    | False       | False      | 2          | 1            | 
+--------------+----+-------------+------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy stp --apic apic11

{
    "duration": 1923,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 453,
        "disconnect_time": 0,
        "mo_time": 1080,
        "total_time": 1533
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

True	453	-	connect apic11o.emea-sp.cisco.com
True	352	2	apic11o.emea-sp.cisco.com class stpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	400	464	apic11o.emea-sp.cisco.com class l1RsStpIfPolCons
True	328	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyStp.md)