# Policy - LLDP

## Filter by name

```
# iserver get aci policy lldp --apic apic11 --name default

Apic: apic11

+-------------+----+---------------+----------------+------------+--------------+
| Policy Name | TF | Receive State | Transmit State | Interfaces | Ref Policies |
+-------------+----+---------------+----------------+------------+--------------+
| default     |    | enabled       | enabled        | 0          | 0            | 
| default     |    | enabled       | enabled        | 237        | 56           | 
+-------------+----+---------------+----------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy lldp --apic apic11 --name default

{
    "duration": 2520,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 1998,
        "total_time": 2400
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

True	402	-	connect apic11o.emea-sp.cisco.com
True	328	10	apic11o.emea-sp.cisco.com class lldpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	1380	338	apic11o.emea-sp.cisco.com class l1RsLldpIfPolCons
True	290	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLldp.md)