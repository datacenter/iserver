# L2 Out

## Filter by l2 out's name

Example: name

```
# iserver get aci l2out --apic apic21 --name Test

Apic: apic21

+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
| L2 Out   | Target DSCP | Bridge Domain | Encapsulation | Ext Phy Domain | Path                                                            |
+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
| k8s/Test | unspecified | k8s/Test      | vlan-666      | Infra_L2dom    | topology/pod-1/paths-2207/pathep-[eth1/30]                      | 
|          |             |               |               |                | topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp] | 
+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
```

Example: tenant and name

```
# iserver get aci l2out --apic apic21 --name k8s/Test

Apic: apic21

+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
| L2 Out   | Target DSCP | Bridge Domain | Encapsulation | Ext Phy Domain | Path                                                            |
+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
| k8s/Test | unspecified | k8s/Test      | vlan-666      | Infra_L2dom    | topology/pod-1/paths-2207/pathep-[eth1/30]                      | 
|          |             |               |               |                | topology/pod-1/protpaths-2207-2208/pathep-[k8s_ocp_bm_5_PolGrp] | 
+----------+-------------+---------------+---------------+----------------+-----------------------------------------------------------------+
```

[[Back]](./L2Out.md)