# Node Interface - Encapsulated Routed

## Filter by interface id

```
# iserver get aci intf l3e --apic apic21 --node bl2205-eu-spdc --id eth1/35*

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+--------+---------+-----------+-------+------+--------+---------+------+--------------------+-------+-------------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Encap  | SR-MPLS | MTU  | IP Unnumbered Intf | Delay | Router MAC        |
+----------------------+--------+---------+-----------+-------+------+--------+---------+------+--------------------+-------+-------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | eth1/35.9 | up    | up   | vlan-2 | no      | 9366 | lo0                | 1     | 00:00:00:00:00:00 | 
+----------------------+--------+---------+-----------+-------+------+--------+---------+------+--------------------+-------+-------------------+
```

Developer

```
# iserver get aci intf l3e --apic apic21 --node bl2205-eu-spdc --id eth1/35*

{
    "duration": 2441,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 663,
        "disconnect_time": 0,
        "mo_time": 1435,
        "total_time": 2098
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

True	663	-	connect apic21o.emea-sp.cisco.com:443
True	493	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	483	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required
True	459	33	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4If
```

[[Back]](./InterfaceL3e.md)