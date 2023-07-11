# Node Interface - SVI

## Statistics (counters) focused output

```
# iserver get aci intf svi --apic apic21 --node cl2208-eu-spdc --view stats

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: cl2208-eu-spdc

Interface SVI Counters [#20]
----------------------------

+----------------------+--------+---------+-----------+-------+------+----------+-----------+----------+-----------+---------+----------+--------+---------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Pkts In  | Pkts Out  | Mcast In | Mcast Out | Disc In | Disc Out | Err In | Err Out |
+----------------------+--------+---------+-----------+-------+------+----------+-----------+----------+-----------+---------+----------+--------+---------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan2     | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan4     | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan6     | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan9     | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan11    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan13    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan15    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan24    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan25    | up    | up   | 3809960  | 5080524   | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan26    | up    | up   | 3810033  | 5080597   | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 99     | 0 0 0 1 | vlan27    | up    | up   | 46264595 | 104487131 | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan28    | up    | up   | 11822    | 164506    | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan29    | up    | up   | 11822    | 164509    | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 99     | 0 0 0 1 | vlan30    | up    | up   | 46264719 | 104487260 | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan31    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan33    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan35    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan37    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan40    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan50    | up    | up   | 0        | 0         | 0        | 0         | 0       | 0        | 0      | 0       | 
+----------------------+--------+---------+-----------+-------+------+----------+-----------+----------+-----------+---------+----------+--------+---------+
```

Developer

```
# iserver get aci intf svi --apic apic21 --node cl2208-eu-spdc --view stats

{
    "duration": 1881,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 1071,
        "total_time": 1473
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

True	402	-	connect apic21o.emea-sp.cisco.com:443
True	366	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	411	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	294	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
```

[[Back]](./InterfaceSvi.md)