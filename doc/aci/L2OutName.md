# L2 Out

## Filter by l2 out's name

Example: name

```
# iserver get aci l2out --apic apic21 --name Test

Apic: apic21 (mode:online, cache:off)

+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
| L2 Out   | Target DSCP | Bridge Domain | Encapsulation | Ext Phy Domain | Path                                                            |
+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
| k8s/Test | unspecified | k8s/Test      | vlan-666      | Infra_L2dom    | topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp] | 
|          |             |               |               |                | topology/pod-1/paths-2207/pathep-[eth1/30]                      | 
+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
```

Example: tenant and name

```
# iserver get aci l2out --apic apic21 --name k8s/Test

Apic: apic21 (mode:online, cache:off)

+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
| L2 Out   | Target DSCP | Bridge Domain | Encapsulation | Ext Phy Domain | Path                                                            |
+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
| k8s/Test | unspecified | k8s/Test      | vlan-666      | Infra_L2dom    | topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp] | 
|          |             |               |               |                | topology/pod-1/paths-2207/pathep-[eth1/30]                      | 
+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
```

Developer

```
# iserver get aci l2out --apic apic21 --name Test

{
    "duration": 1605,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 438,
        "disconnect_time": 0,
        "mo_time": 1032,
        "total_time": 1470
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

True	438	-	connect apic21o.emea-sp.cisco.com
True	431	2	apic21o.emea-sp.cisco.com class l2extOut query rsp-subtree=children&rsp-subtree-class=l2extLNodeP,l2extInstP,l2extRsEBd,l2extRsL2DomAtt
True	601	2	apic21o.emea-sp.cisco.com class l2extRsPathL2OutAtt
```

[[Back]](./L2Out.md)