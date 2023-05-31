# Policy - Transceiver

## Filter by name

```
# iserver get aci policy transceiver --apic apic11 --name default

Apic: apic11

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
    "duration": 1511,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 1011,
        "total_time": 1406
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

True	395	-	connect apic11o.emea-sp.cisco.com
True	296	2	apic11o.emea-sp.cisco.com class xcvrOpticsIfPol
True	422	414	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	293	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyTrans.md)