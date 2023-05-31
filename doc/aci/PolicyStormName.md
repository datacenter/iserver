# Policy - Storm Control

## Filter by name

```
# iserver get aci policy storm --apic apic11 --name default

Apic: apic11

+-------------+-------+-------------+------------+----------------+-------------+------------------+----------------------+------------+-----------+--------------+
| Policy Name | TF    | Packet Type | Rate [%]   | Burst Rate [%] | Rate [pps]  | Burst Rate [pps] | Storm Control Action | Storm Soak | Instances | Ref Policies |
+-------------+-------+-------------+------------+----------------+-------------+------------------+----------------------+------------+-----------+--------------+
| default     | False | all         | 100.000000 | 100.000000     | unspecified | unspecified      | drop                 | 3          | 414       | 83           | 
+-------------+-------+-------------+------------+----------------+-------------+------------------+----------------------+------------+-----------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy storm --apic apic11 --name default

{
    "duration": 1599,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 396,
        "disconnect_time": 0,
        "mo_time": 1050,
        "total_time": 1446
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

True	396	-	connect apic11o.emea-sp.cisco.com
True	319	1	apic11o.emea-sp.cisco.com class stormctrlIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	438	414	apic11o.emea-sp.cisco.com class l1RsStormctrlIfPolCons
True	293	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyStorm.md)