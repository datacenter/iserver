# Node Interface - Port Channel (PC)

## Filter by port channel id

```
# iserver get aci intf pc --apic apic21 --node bl2205-eu-spdc --id po1

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Port Channel - State [#1]
-----------------------------------

+----------------------+--------+---------+-----+------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
| Node                 | Health | Faults  | Id  | Name       | Protocol    | Admin | State | Reason | VPC | Members | Layer    | Mode  | Speed |
+----------------------+--------+---------+-----+------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po1 | SPN_PolGrp | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 10G   | 
+----------------------+--------+---------+-----+------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
```

Developer

```
# iserver get aci intf pc --apic apic21 --node bl2205-eu-spdc --id po1

{
    "duration": 2088,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 420,
        "disconnect_time": 0,
        "mo_time": 1357,
        "total_time": 1777
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

True	420	-	connect apic21o.emea-sp.cisco.com:443
True	302	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	455	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	307	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	293	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
```

[[Back]](./InterfacePc.md)