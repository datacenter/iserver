# Policy - Transceiver

## Usage specific output

```
# iserver get aci policy transceiver --apic apic11 --name default --view usage

Apic: apic11 (mode:online, cache:off)

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
    "duration": 1830,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 421,
        "disconnect_time": 0,
        "mo_time": 1073,
        "total_time": 1494
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

True	421	-	connect apic11o.emea-sp.cisco.com
True	324	2	apic11o.emea-sp.cisco.com class xcvrOpticsIfPol
True	420	470	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	329	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyTrans.md)