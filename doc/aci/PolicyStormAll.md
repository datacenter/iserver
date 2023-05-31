# Policy - Storm Control

## Get all policies

```
# iserver get aci policy storm --apic apic11

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
# iserver get aci policy storm --apic apic11

{
    "duration": 1559,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 404,
        "disconnect_time": 0,
        "mo_time": 1042,
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

True	404	-	connect apic11o.emea-sp.cisco.com
True	331	1	apic11o.emea-sp.cisco.com class stormctrlIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	401	414	apic11o.emea-sp.cisco.com class l1RsStormctrlIfPolCons
True	310	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyStorm.md)