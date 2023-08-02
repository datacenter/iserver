# L2Out

## Default output

```
# iserver get aci l2out --apic apic21

Apic: apic21 (mode:online, cache:off)

L2Out [#2]
----------

+---------+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| Faults  | L2 Out         | Target DSCP | Bridge Domain  | Encapsulation | Ext Phy Domain | Path                                                            |
+---------+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| 0 0 0 0 | common/default | unspecified | common/default | unknown       |                |                                                                 | 
+---------+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| 0 0 3 0 | k8s/Test       | unspecified | k8s/Test       | vlan-666      | Infra_L2dom    | topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp] | 
|         |                |             |                |               |                | topology/pod-1/paths-2207/pathep-[eth1/30]                      | 
+---------+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
```

Developer

```
# iserver get aci l2out --apic apic21

{
    "duration": 1273,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 455,
        "disconnect_time": 0,
        "mo_time": 682,
        "total_time": 1137
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

True	455	-	connect apic21o.emea-sp.cisco.com:443
True	354	2	apic21o.emea-sp.cisco.com:443 class l2extOut query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	328	2	apic21o.emea-sp.cisco.com:443 class l2extRsPathL2OutAtt
```

[[Back]](./L2Out.md)