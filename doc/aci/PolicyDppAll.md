# Policy - DPP

## Get all policies

```
# iserver get aci policy dpp --apic apic11

Apic: apic11

+-------------+----+-------------+------+----------------+----------------+--------------+-------------+-----------------+-------+-----------+------------+--------------+
| Policy Name | TF | Admin State | Type | Conform Action | Violate Action | Sharing Mode | Burst       | Excessive Burst | Rate  | Peak Rate | Interfaces | Ref Policies |
+-------------+----+-------------+------+----------------+----------------+--------------+-------------+-----------------+-------+-----------+------------+--------------+
| default     |    | disabled    | 1R2C | transmit       | drop           | dedicated    | unspecified | unspecified     | 0 pps | 0 pps     | 0          | 92           | 
| default     |    | disabled    | 1R2C | transmit       | drop           | dedicated    | unspecified | unspecified     | 0 pps | 0 pps     | 414        | 249          | 
+-------------+----+-------------+------+----------------+----------------+--------------+-------------+-----------------+-------+-----------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy dpp --apic apic11

{
    "duration": 1703,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 1134,
        "total_time": 1532
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

True	398	-	connect apic11o.emea-sp.cisco.com
True	448	2	apic11o.emea-sp.cisco.com class qosDppPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	393	414	apic11o.emea-sp.cisco.com class l1RsQosEgressDppIfPolCons
True	293	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyDpp.md)