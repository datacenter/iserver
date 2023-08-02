# L2Out

## Interface view

```
# iserver get aci l2out --apic apic21 --view intf

Apic: apic21 (mode:online, cache:off)

L2Out - Interfaces [#2]
-----------------------

+---------+----------------+----------------+-----------+
| Faults  | L2Out          | Node           | Interface |
+---------+----------------+----------------+-----------+
| 0 0 0 0 | common/default |                |           | 
+---------+----------------+----------------+-----------+
| 0 0 3 0 | k8s/Test       | cl2207-eu-spdc | eth1/2/3  | 
|         |                | cl2207-eu-spdc | eth1/30   | 
|         |                | cl2207-eu-spdc | po4       | 
|         |                | cl2208-eu-spdc | eth1/2/3  | 
|         |                | cl2208-eu-spdc | po8       | 
+---------+----------------+----------------+-----------+
```

Developer

```
# iserver get aci l2out --apic apic21 --view intf

{
    "duration": 2222,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 1649,
        "total_time": 2076
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

True	427	-	connect apic21o.emea-sp.cisco.com:443
True	329	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	321	2	apic21o.emea-sp.cisco.com:443 class l2extRsPathL2OutAtt
True	345	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/l2out-default query rsp-subtree-include=full-deployment&target-node=all&target-path=L2ExtOutToNwIf
True	328	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/l2out-Test query rsp-subtree-include=full-deployment&target-node=all&target-path=L2ExtOutToNwIf
True	326	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./L2Out.md)