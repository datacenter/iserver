# Policy - Port Channel Member

## Filter by name

```
# iserver get aci policy lacp-m --apic apic11 --name default

Apic: apic11

+-------------+----+----------+---------------+------------+--------------+
| Policy Name | TF | Priority | Transmit Rate | Interfaces | Ref Policies |
+-------------+----+----------+---------------+------------+--------------+
| default     |    | 32768    | normal        | 70         | 1            | 
+-------------+----+----------+---------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy lacp-m --apic apic11 --name default

{
    "duration": 1462,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 394,
        "disconnect_time": 0,
        "mo_time": 954,
        "total_time": 1348
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

True	394	-	connect apic11o.emea-sp.cisco.com
True	294	1	apic11o.emea-sp.cisco.com class lacpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	338	70	apic11o.emea-sp.cisco.com class l1RsLacpIfPolCons
True	322	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacpm.md)