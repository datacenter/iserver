# Node Interface - Physical

## Filter by transceiver type

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --trans *h40g*
    --view trans

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+------+---------+----------+--------+-------+-----------------+------------------+-----+---------------+
| Node                 | Interface | Oper | Present | State    | Optics | Name  | Type            | PN               | Rev | SN            |
+----------------------+-----------+------+---------+----------+--------+-------+-----------------+------------------+-----+---------------+
| pod-1/bl2205-eu-spdc | 1/11      | up   | yes     | inserted | qsfp   | CISCO | QSFP-H40G-AOC3M | FCBN410QE2C03-C1 | D   | FIW213402UA-B | 
| pod-1/bl2205-eu-spdc | 1/12      | up   | yes     | inserted | qsfp   | CISCO | QSFP-H40G-AOC3M | FCBN410QE2C03-C1 | D   | FIW2134024Q-B | 
| pod-1/bl2205-eu-spdc | 1/19      | up   | yes     | inserted | qsfp   | CISCO | QSFP-H40G-AOC3M | FCBN410QE2C03-C1 | D   | FIW213402T9-B | 
+----------------------+-----------+------+---------+----------+--------+-------+-----------------+------------------+-----+---------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --trans *h40g*
    --view trans

{
    "duration": 2654,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 1910,
        "total_time": 2327
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

True	417	-	connect apic21o.emea-sp.cisco.com:443
True	303	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	978	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	340	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	289	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmFcot
```

[[Back]](./InterfacePhy.md)