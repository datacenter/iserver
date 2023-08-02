# L2 Domain

## Node view

```
# iserver get aci domain l2 --apic apic21 --view node

Apic: apic21 (mode:online, cache:off)
[INFO] Requires per-domain api call

L2 Domain - Nodes [#2]
----------------------

+---------+-------------+------------+------------------+----------------+------------+
| Faults  | Domain      | AAEP       | VLAN Pool        | Node           | Interfaces |
+---------+-------------+------------+------------------+----------------+------------+
| 0 0 0 0 | Infra_L2dom | Infra_AAEP | Infra_VlanPool   | bl2205-eu-spdc | 1          | 
|         |             |            |                  | bl2206-eu-spdc | 1          | 
|         |             |            |                  | cl2201-eu-spdc | 2          | 
|         |             |            |                  | cl2202-eu-spdc | 2          | 
+---------+-------------+------------+------------------+----------------+------------+
| 0 0 0 0 | test        | nidemo     | nidemo-3000-3001 | rl2701-eu-spdc | 2          | 
|         |             |            |                  | rl2702-eu-spdc | 2          | 
+---------+-------------+------------+------------------+----------------+------------+
```

Developer

```
# iserver get aci domain l2 --apic apic21 --view node

{
    "duration": 2919,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 512,
        "disconnect_time": 0,
        "mo_time": 2036,
        "total_time": 2548
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

True	512	-	connect apic21o.emea-sp.cisco.com:443
True	364	2	apic21o.emea-sp.cisco.com:443 class l2extDomP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsVlanNs,infraRtDomP,l2extRtL2DomAtt,aaaDomainRef
True	699	1	apic21o.emea-sp.cisco.com:443 mo uni/l2dom-Infra_L2dom query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
True	342	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	631	1	apic21o.emea-sp.cisco.com:443 mo uni/l2dom-test query rsp-subtree-include=full-deployment&target-node=all&target-path=ADomPToEthIf
```

[[Back]](./DomainL2.md)