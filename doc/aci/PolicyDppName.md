# Policy - DPP

## Filter by name

```
# iserver get aci policy dpp --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+-------------+------+----------------+----------------+--------------+-------------+-----------------+-------+-----------+------------+--------------+
| Policy Name | TF | Admin State | Type | Conform Action | Violate Action | Sharing Mode | Burst       | Excessive Burst | Rate  | Peak Rate | Interfaces | Ref Policies |
+-------------+----+-------------+------+----------------+----------------+--------------+-------------+-----------------+-------+-----------+------------+--------------+
| default     |    | disabled    | 1R2C | transmit       | drop           | dedicated    | unspecified | unspecified     | 0 pps | 0 pps     | 0          | 92           | 
| default     |    | disabled    | 1R2C | transmit       | drop           | dedicated    | unspecified | unspecified     | 0 pps | 0 pps     | 470        | 249          | 
+-------------+----+-------------+------+----------------+----------------+--------------+-------------+-----------------+-------+-----------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy dpp --apic apic11 --name default

{
    "duration": 2057,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 433,
        "disconnect_time": 0,
        "mo_time": 1179,
        "total_time": 1612
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

True	433	-	connect apic11o.emea-sp.cisco.com
True	380	2	apic11o.emea-sp.cisco.com class qosDppPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	413	470	apic11o.emea-sp.cisco.com class l1RsQosEgressDppIfPolCons
True	386	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyDpp.md)