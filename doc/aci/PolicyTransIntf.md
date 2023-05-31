# Policy - Transceiver

## Interface specific output

```
# iserver get aci policy transceiver --apic apic11 --name default --view intf

Apic: apic11

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
    "duration": 2544,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 2031,
        "total_time": 2446
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

True	415	-	connect apic11o.emea-sp.cisco.com
True	1313	2	apic11o.emea-sp.cisco.com class xcvrOpticsIfPol
True	422	414	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	296	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyTrans.md)