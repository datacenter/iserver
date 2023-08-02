# Node Interface - Port Channel (PC)

## Filter by port channel name

```
# iserver get aci intf pc --apic apic21 --node bl2205-eu-spdc --name HX*

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Port Channel - State [#2]
-----------------------------------

+----------------------+--------+---------+-----+-----------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
| Node                 | Health | Faults  | Id  | Name            | Protocol    | Admin | State | Reason | VPC | Members | Layer    | Mode  | Speed |
+----------------------+--------+---------+-----+-----------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po3 | HX1-FI-B_PolGrp | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 40G   | 
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | po4 | HX1-FI-A_PolGrp | lacp-active | up    | up    |        | 256 | 1/1     | switched | trunk | 40G   | 
+----------------------+--------+---------+-----+-----------------+-------------+-------+-------+--------+-----+---------+----------+-------+-------+
```

Developer

```
# iserver get aci intf pc --apic apic21 --node bl2205-eu-spdc --name HX*

{
    "duration": 2108,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 395,
        "disconnect_time": 0,
        "mo_time": 1362,
        "total_time": 1757
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

True	395	-	connect apic21o.emea-sp.cisco.com:443
True	295	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	439	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	311	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	317	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
```

[[Back]](./InterfacePc.md)