# L2 Out

## Get L2 Outs properties

```
# iserver get aci l2out --apic apic21

Apic: apic21

+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| L2 Out         | Target DSCP | Bridge Domain  | Encapsulation | Ext Phy Domain | Path                                                            |
+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| common/default | unspecified | common/default | unknown       |                |                                                                 | 
+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
| k8s/Test       | unspecified | k8s/Test       | vlan-666      | Infra_L2dom    | topology/pod-1/paths-2207/pathep-[eth1/30]                      | 
|                |             |                |               |                | topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp] | 
+----------------+-------------+----------------+---------------+----------------+-----------------------------------------------------------------+
```

Developer

```
# iserver get aci l2out --apic apic21

{
    "duration": 1138,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 417,
        "disconnect_time": 0,
        "mo_time": 639,
        "total_time": 1056
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
    }
}

Log: apic
----------

True	417	-	connect apic21o.emea-sp.cisco.com
True	327	2	apic21o.emea-sp.cisco.com class l2extOut query rsp-subtree=children&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	312	2	apic21o.emea-sp.cisco.com class l2extRsPathL2OutAtt
```

[[Back]](./L2Out.md)