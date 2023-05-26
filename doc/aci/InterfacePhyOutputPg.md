# Node Interface - Physical

## Policy Group focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc -o pg

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+------+--------------------------+-------------------------+-------------------+-------------------------+-------------------------+
| Node                | Interface | Oper | Type | Leaf Interface Profile   | Interface Selector      | Policy Group Type | Policy Group Name       | Attached Entity Profile |
+---------------------+-----------+------+------+--------------------------+-------------------------+-------------------+-------------------------+-------------------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | leaf | UCSB1-FI-A_IntProf       | UCSB1-FI-A_IntSel       | infraAccBndlGrp   | UCSB1-FI-A_PolGrp       | UCSB1_AAEP              | 
| pod-1/bl205-eu-spdc | 1/2       | up   | leaf | UCSB1-FI-B_IntProf       | UCSB1-FI-B_IntSel       | infraAccBndlGrp   | UCSB1-FI-B_PolGrp       | UCSB1_AAEP              | 
| pod-1/bl205-eu-spdc | 1/3       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/4       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/5       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/6       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/7       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/8       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/9       | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/10      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/11      | up   | leaf | HX1-FI-A_IntProf         | HX1-FI-A_IntSel         | infraAccBndlGrp   | HX1-FI-A_PolGrp         | HX1_AAEP                | 
| pod-1/bl205-eu-spdc | 1/12      | up   | leaf | HX1-FI-B_IntProf         | HX1-FI-B_IntSel         | infraAccBndlGrp   | HX1-FI-B_PolGrp         | HX1_AAEP                | 
| pod-1/bl205-eu-spdc | 1/13      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/14      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/15      | up   | leaf | P5G-CU-PCIe1-A_IntProf   | P5G-CU-PCIe1-A_IntSel   | infraAccPortGrp   | P5G-CU-PCIe1-A_PolGrp   | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/16      | up   | leaf | P5G-CU-PCIe2-A_IntProf   | P5G-CU-PCIe2-A_IntSel   | infraAccPortGrp   | P5G-CU-PCIe2-A_PolGrp   | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/17      | down | leaf | P5G-Core-PCIe1-A_IntProf | P5G-Core-PCIe1-A_IntSel | infraAccPortGrp   | P5G-Core-PCIe1-A_PolGrp | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/18      | down | leaf | P5G-Core-PCIe2-A_IntProf | P5G-Core-PCIe2-A_IntSel | infraAccPortGrp   | P5G-Core-PCIe2-A_PolGrp | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/19      | up   | leaf | P5G-Core-MLOM-1_IntProf  | P5G-Core-MLOM-1_IntSel  | infraAccPortGrp   | P5G-Core-MLOM-1_PolGrp  | Private5G_AAEP          | 
| pod-1/bl205-eu-spdc | 1/20      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/21      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/22      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/23      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/24      | up   | leaf | Infra-BGP_IntProf        | Infra-BGP_IntSel        | infraAccPortGrp   | Infra-BGP_PolGrp        | Infra_L3_AAEP           | 
| pod-1/bl205-eu-spdc | 1/25      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/26      | down | leaf |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/27      | up   | leaf | SPN_IntProf              | SPN_IntSel              | infraAccBndlGrp   | SPN_PolGrp              | SPN_AAEP                | 
| pod-1/bl205-eu-spdc | 1/28      | up   | leaf | SR-Demo-CDC-2            | 1-28-1-28               | infraAccPortGrp   | SR-Demo-CDC-2-vlan      | DC                      | 
| pod-1/bl205-eu-spdc | 1/29      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/30      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/31      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/32      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/33      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/34      | down | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/35      | up   | fab  |                          |                         |                   |                         |                         | 
| pod-1/bl205-eu-spdc | 1/36      | up   | fab  |                          |                         |                   |                         |                         | 
+---------------------+-----------+------+------+--------------------------+-------------------------+-------------------+-------------------------+-------------------------+
```

[[Back]](./InterfacePhy.md)