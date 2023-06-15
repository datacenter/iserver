# Policy - Transceiver

## Filter by name

```
# iserver get aci policy transceiver --apic apic11 --name default

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
# iserver get aci policy transceiver --apic apic11 --name default

{
    "duration": 1663,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 1030,
        "total_time": 1438
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

True	408	-	connect apic11o.emea-sp.cisco.com
True	324	2	apic11o.emea-sp.cisco.com class xcvrOpticsIfPol
True	387	470	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	319	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyTrans.md)