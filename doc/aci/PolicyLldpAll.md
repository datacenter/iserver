# Policy - LLDP

## Get all policies

```
# iserver get aci policy lldp --apic apic11

Apic: apic11 (mode:online, cache:off)

+------------------------+----+---------------+----------------+------------+--------------+
| Policy Name            | TF | Receive State | Transmit State | Interfaces | Ref Policies |
+------------------------+----+---------------+----------------+------------+--------------+
| default                |    | enabled       | enabled        | 0          | 0            | 
| default                |    | enabled       | enabled        | 293        | 56           | 
| EU-SPDC-CDC_lldpIfPol  |    | enabled       | enabled        | 0          | 0            | 
| EU-SPDC-R3DC_lldpIfPol |    | enabled       | enabled        | 0          | 0            | 
| lldp-enabled           |    | enabled       | enabled        | 6          | 4            | 
| LLDP_disable           |    | disabled      | disabled       | 0          | 1            | 
| LLDP_enable            |    | enabled       | enabled        | 93         | 31           | 
| nidemo-dummy           |    | enabled       | enabled        | 2          | 1            | 
| system-lldp-disabled   |    | disabled      | disabled       | 0          | 0            | 
| system-lldp-enabled    |    | enabled       | enabled        | 0          | 0            | 
+------------------------+----+---------------+----------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy lldp --apic apic11

{
    "duration": 1910,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 467,
        "disconnect_time": 0,
        "mo_time": 1063,
        "total_time": 1530
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

True	467	-	connect apic11o.emea-sp.cisco.com
True	352	10	apic11o.emea-sp.cisco.com class lldpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	395	394	apic11o.emea-sp.cisco.com class l1RsLldpIfPolCons
True	316	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLldp.md)