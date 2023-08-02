# L2 Domain

## Interface view

```
# iserver get aci domain l2 --apic apic21 --view intf

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call

L2 Domain - Interfaces [#2]
---------------------------

+---------+-------------+------------+------------------+----------------+-----------+
| Faults  | Domain      | AAEP       | VLAN Pool        | Node           | Interface |
+---------+-------------+------------+------------------+----------------+-----------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool   | bl2205-eu-spdc | eth1/25   | 
|         |             |            |                  | bl2206-eu-spdc | eth1/25   | 
|         |             |            |                  | cl2201-eu-spdc | eth1/25   | 
|         |             |            |                  | cl2201-eu-spdc | eth1/96   | 
|         |             |            |                  | cl2202-eu-spdc | eth1/25   | 
|         |             |            |                  | cl2202-eu-spdc | eth1/96   | 
+---------+-------------+------------+------------------+----------------+-----------+
| 0 0 0 0 | test        | nidemo     | nidemo-3000-3001 | rl2701-eu-spdc | eth1/19   | 
|         |             |            |                  | rl2701-eu-spdc | eth1/20   | 
|         |             |            |                  | rl2702-eu-spdc | eth1/19   | 
|         |             |            |                  | rl2702-eu-spdc | eth1/20   | 
+---------+-------------+------------+------------------+----------------+-----------+
```

Developer

```
# iserver get aci domain l2 --apic apic21 --view intf

{
    "duration": 2861,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 470,
        "disconnect_time": 0,
        "mo_time": 2077,
        "total_time": 2547
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

True	470	-	connect apic21o.emea-sp.cisco.com:443
True	389	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	701	1	apic21o.emea-sp.cisco.com:443 mo uni/l2dom-Infra_L2dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	370	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	617	1	apic21o.emea-sp.cisco.com:443 mo uni/l2dom-test query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
```

[[Back]](./DomainL2.md)