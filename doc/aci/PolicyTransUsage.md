# Policy - Transceiver

## Usage specific output

```
# iserver get aci policy transceiver --apic apic11 --name default --view usage

Apic: apic11

+-------------+------+------+-----------------+
| Policy Name | Type | Node | Interface Count |
+-------------+------+------+-----------------+
| default     | ZR   |      |                 | 
| default     | ZR   |      |                 | 
| default     | ZRP  |      |                 | 
| default     | ZRP  |      |                 | 
+-------------+------+------+-----------------+
```

Developer

```
# iserver get aci policy transceiver --apic apic11 --name default --view usage

{
    "duration": 1517,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 1033,
        "total_time": 1432
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

True	399	-	connect apic11o.emea-sp.cisco.com
True	317	2	apic11o.emea-sp.cisco.com class xcvrOpticsIfPol
True	425	414	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	291	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyTrans.md)