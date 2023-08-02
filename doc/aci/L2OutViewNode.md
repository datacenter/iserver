# L2Out

## Node view

```
# iserver get aci l2out --apic apic21 --view node

Apic: apic21 (mode:online, cache:off)

L2Out - Nodes [#2]
------------------

+---------+----------------+----------------+------------+
| Faults  | L2Out          | Node           | Interfaces |
+---------+----------------+----------------+------------+
| 0 0 0 0 | common/default |                |            | 
+---------+----------------+----------------+------------+
| 0 0 3 0 | k8s/Test       | cl2207-eu-spdc | 3          | 
|         |                | cl2208-eu-spdc | 2          | 
+---------+----------------+----------------+------------+
```

Developer

```
# iserver get aci l2out --apic apic21 --view node

{
    "duration": 2206,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 431,
        "disconnect_time": 0,
        "mo_time": 1651,
        "total_time": 2082
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

True	431	-	connect apic21o.emea-sp.cisco.com:443
True	325	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	318	2	apic21o.emea-sp.cisco.com:443 class l2extRsPathL2OutAtt
True	361	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-common/l2out-default query rsp-subtree-include=full-deployment&target-node=all&target-path=L2ExtOutToNwIf
True	319	1	apic21o.emea-sp.cisco.com:443 mo uni/tn-k8s/l2out-Test query rsp-subtree-include=full-deployment&target-node=all&target-path=L2ExtOutToNwIf
True	328	15	apic21o.emea-sp.cisco.com:443 class fabricNode
```

[[Back]](./L2Out.md)