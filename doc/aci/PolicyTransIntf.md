# Policy - Transceiver

## Interface specific output

```
# iserver get aci policy transceiver --apic apic11 --name default --view intf

Apic: apic11 (mode:online, cache:off)

+-------------+------+------+-----------+
| Policy Name | Type | Node | Interface |
+-------------+------+------+-----------+
| default     | ZR   |      |           | 
| default     | ZR   |      |           | 
| default     | ZRP  |      |           | 
| default     | ZRP  |      |           | 
+-------------+------+------+-----------+
```

Developer

```
# iserver get aci policy transceiver --apic apic11 --name default --view intf

{
    "duration": 1947,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 477,
        "disconnect_time": 0,
        "mo_time": 1111,
        "total_time": 1588
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

True	477	-	connect apic11o.emea-sp.cisco.com
True	338	2	apic11o.emea-sp.cisco.com class xcvrOpticsIfPol
True	428	470	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	345	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyTrans.md)