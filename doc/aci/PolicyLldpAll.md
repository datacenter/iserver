# Policy - LLDP

## Get all policies

```
# iserver get aci policy lldp --apic apic11

Apic: apic11

+------------------------+----+---------------+----------------+------------+--------------+
| Policy Name            | TF | Receive State | Transmit State | Interfaces | Ref Policies |
+------------------------+----+---------------+----------------+------------+--------------+
| default                |    | enabled       | enabled        | 0          | 0            | 
| default                |    | enabled       | enabled        | 237        | 56           | 
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
    "duration": 1562,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 1061,
        "total_time": 1447
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

True	386	-	connect apic11o.emea-sp.cisco.com
True	374	10	apic11o.emea-sp.cisco.com class lldpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	395	338	apic11o.emea-sp.cisco.com class l1RsLldpIfPolCons
True	292	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLldp.md)