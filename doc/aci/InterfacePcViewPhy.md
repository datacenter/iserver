# Node Interface - Port Channel (PC)

## Phy view

```
# iserver get aci intf pc --apic apic21 --node bl2205-eu-spdc --view phy

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Port Channel Member - Phy State [#6]
----------------------------------------------

+----------------------+-----+--------+--------------+--------+---------+-------+------+-------+--------+-------+----------------+
| Node                 | Id  | Active | Interface Id | Health | Faults  | Admin | Oper | Mode  | Duplex | Speed | VLAN           |
+----------------------+-----+--------+--------------+--------+---------+-------+------+-------+--------+-------+----------------+
| pod-1/bl2205-eu-spdc | po1 | V      | eth1/27      | 100    | 0 0 0 0 | up    | up   | trunk | full   | 10G   |                | 
| pod-1/bl2205-eu-spdc | po2 | V      | eth1/1       | 100    | 0 0 0 0 | up    | up   | trunk | full   | 100G  |                | 
| pod-1/bl2205-eu-spdc | po3 | V      | eth1/12      | 100    | 0 0 0 0 | up    | up   | trunk | full   | 40G   |                | 
| pod-1/bl2205-eu-spdc | po4 | V      | eth1/11      | 100    | 0 0 0 0 | up    | up   | trunk | full   | 40G   |                | 
| pod-1/bl2205-eu-spdc | po5 | V      | eth1/19      | 100    | 0 0 0 0 | up    | up   | trunk | full   | 40G   | 1,4-5,11-16,20 | 
| pod-1/bl2205-eu-spdc | po6 | V      | eth1/2       | 100    | 0 0 0 0 | up    | up   | trunk | full   | 100G  |                | 
+----------------------+-----+--------+--------------+--------+---------+-------+------+-------+--------+-------+----------------+
```

Developer

```
# iserver get aci intf pc --apic apic21 --node bl2205-eu-spdc --view phy

{
    "duration": 3752,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 2915,
        "total_time": 3326
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

True	411	-	connect apic21o.emea-sp.cisco.com:443
True	349	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	614	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	975	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	314	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	335	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	328	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
```

[[Back]](./InterfacePc.md)