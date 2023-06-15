# Policy - Transceiver

## Get all policies

```
# iserver get aci policy transceiver --apic apic11

Apic: apic11 (mode:online, cache:off)

+-------------+----+-------------+------+------------+
| Policy Name | TF | Admin State | Type | Interfaces |
+-------------+----+-------------+------+------------+
| default     |    | disabled    | ZR   | 0          | 
| default     |    | disabled    | ZR   | 0          | 
| default     |    | disabled    | ZRP  | 0          | 
| default     |    | disabled    | ZRP  | 0          | 
+-------------+----+-------------+------+------------+
```

Developer

```
# iserver get aci policy transceiver --apic apic11

{
    "duration": 1806,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 455,
        "disconnect_time": 0,
        "mo_time": 1063,
        "total_time": 1518
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

True	455	-	connect apic11o.emea-sp.cisco.com
True	340	2	apic11o.emea-sp.cisco.com class xcvrOpticsIfPol
True	397	470	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	326	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyTrans.md)