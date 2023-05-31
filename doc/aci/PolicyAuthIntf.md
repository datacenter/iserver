# Policy - 802.1X

## Interface specific output

```
# iserver get aci policy auth --apic apic11 --name default --view intf

Apic: apic11

+-------------+----+-------------+-------------+------+-----------+
| Policy Name | TF | Admin State | Host Mode   | Node | Interface |
+-------------+----+-------------+-------------+------+-----------+
| default     |    | disabled    | single-host |      |           | 
+-------------+----+-------------+-------------+------+-----------+
```

Developer

```
# iserver get aci policy auth --apic apic11 --name default --view intf

{
    "duration": 1124,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 655,
        "total_time": 1070
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
True	314	1	apic11o.emea-sp.cisco.com class l2PortAuthPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	341	0	apic11o.emea-sp.cisco.com class l1RsL2PortAuthCons
```

[[Back]](./PolicyAuth.md)