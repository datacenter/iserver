# Node Interface - Physical

## Filter by transceiver type

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --trans *h40g*
    --view trans

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+----------+--------+-------------+-----------------+------------------+-----+---------------+
| Node                | Interface | Oper | Present | State    | Optics | Name        | Type            | PN               | Rev | SN            |
+---------------------+-----------+------+---------+----------+--------+-------------+-----------------+------------------+-----+---------------+
| pod-1/bl205-eu-spdc | 1/15      | up   | yes     | inserted | qsfp   | CISCO       | QSFP-H40G-AOC7M | AFBR-7QER07Z-CS1 | 01  | AVE1828E0TW-B | 
| pod-1/bl205-eu-spdc | 1/16      | up   | yes     | inserted | qsfp   | CISCO       | QSFP-H40G-AOC7M | AFBR-7QER07Z-CS1 | 01  | AVE1828E0UF-A | 
| pod-1/bl205-eu-spdc | 1/17      | down | yes     | inserted | qsfp   | CISCO       | QSFP-H40G-AOC7M | AFBR-7QER07Z-CS1 | 01  | AVE1828E0VF-B | 
| pod-1/bl205-eu-spdc | 1/18      | down | yes     | inserted | qsfp   | CISCO       | QSFP-H40G-AOC7M | AFBR-7QER07Z-CS1 | 01  | AVE1828E0U5-A | 
| pod-1/bl205-eu-spdc | 1/19      | up   | yes     | inserted | qsfp   | CISCO-DELTA | QSFP-H40G-AOC3M | QAOC-40G4F1A03-C | A   | DTS2219A015-A | 
+---------------------+-----------+------+---------+----------+--------+-------------+-----------------+------------------+-----+---------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --trans *h40g*
    --view trans

{
    "duration": 1766,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 1205,
        "total_time": 1602
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

True	397	-	connect apic11o.emea-sp.cisco.com
True	291	13	apic11o.emea-sp.cisco.com class fabricNode
True	310	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	308	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	296	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmFcot
```

[[Back]](./InterfacePhy.md)